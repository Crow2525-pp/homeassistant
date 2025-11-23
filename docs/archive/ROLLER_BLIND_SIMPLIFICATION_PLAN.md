# Roller Blind Simplification Plan - Three-State System

## Current Problem

**Issue:** Roller blind position tracking is inaccurate and drifts over time.

**Root Cause:** Blinds don't have position feedback sensors. Current system estimates position by:
- Starting a timer when blind moves (18-minute full travel time)
- Polling every 30 seconds
- Incrementing/decrementing position by 2.78% per interval
- Calculating based on time elapsed vs total travel time

**Problems with Current Approach:**
- Accumulates error over time (drift)
- If HA restarts mid-movement, position is lost
- Complex automation logic (5 automations + 3 input helpers)
- Requires manual correction
- Doesn't work well with partial positions

---

## Proposed Solution: Three-State System

### Simplified State Model

Instead of tracking exact position (0-100%), use just 3 states:

| State | Meaning | Position Range |
|-------|---------|----------------|
| **Closed** | Blinds fully down | 0% |
| **Partial** | Blinds partially open | 1-99% |
| **Open** | Blinds fully up | 100% |

### Benefits

✅ **Much simpler logic** - No timer calculations needed
✅ **No drift** - State is deterministic based on last command
✅ **Reliable** - Survives HA restarts
✅ **Easier to understand** - Clear states vs percentage estimates
✅ **Works with automation** - All current automations can be adapted

### How It Works

**State Transitions:**

```
CLOSED ─── open command ──→ PARTIAL ─── open command ──→ OPEN
  ↑                            ↕                            ↓
  └────── close command ←─── PARTIAL ←──── close command ──┘
```

**Rules:**
1. **From OPEN:**
   - Close command → PARTIAL (after 5 seconds)
   - Close command again → CLOSED (after full travel time)

2. **From CLOSED:**
   - Open command → PARTIAL (after 5 seconds)
   - Open command again → OPEN (after full travel time)

3. **From PARTIAL:**
   - Open command → OPEN
   - Close command → CLOSED
   - Stop command → stay PARTIAL

---

## Implementation Details

### New Input Helpers

**Replace current helpers with:**

```yaml
# configuration.yaml

input_select:
  roller_blind_state_simple:
    name: Roller Blind State
    options:
      - closed
      - partial
      - open
    initial: closed
    icon: mdi:blinds
```

**Remove these (no longer needed):**
- `input_number.roller_blind_position` (0-100%)
- `input_number.roller_blind_target_position`
- `input_select.roller_blind_state` (opening/closing/open/closed)
- `timer.roller_blind_timer`

### New Cover Template

```yaml
# config/domains/templates.yaml

cover:
  - platform: template
    covers:
      roller_blinds_simple:
        friendly_name: "Roller Blinds"
        device_class: blind
        value_template: >-
          {% if is_state('input_select.roller_blind_state_simple', 'closed') %}
            closed
          {% elif is_state('input_select.roller_blind_state_simple', 'open') %}
            open
          {% else %}
            open
          {% endif %}
        position_template: >-
          {% if is_state('input_select.roller_blind_state_simple', 'closed') %}
            0
          {% elif is_state('input_select.roller_blind_state_simple', 'open') %}
            100
          {% else %}
            50
          {% endif %}
        open_cover:
          service: script.roller_blinds_open_simple
        close_cover:
          service: script.roller_blinds_close_simple
        stop_cover:
          service: script.roller_blinds_stop
        set_cover_position:
          service: script.roller_blinds_set_position_simple
          data:
            position: "{{ position }}"
```

### New Scripts

```yaml
# config/domains/scripts.yaml

roller_blinds_open_simple:
  alias: Roller Blinds Open (Simple)
  sequence:
    # Send IR open command
    - service: remote.send_command
      data:
        device: Roller Blinds
        command: Up
      target:
        device_id: 3d7542325305f19a1d70e5b14947b2a9

    # Update state based on current position
    - choose:
        # From CLOSED → PARTIAL (stop after 5 seconds)
        - conditions:
            - condition: state
              entity_id: input_select.roller_blind_state_simple
              state: 'closed'
          sequence:
            - delay:
                seconds: 5
            - service: script.roller_blinds_stop
            - service: input_select.select_option
              target:
                entity_id: input_select.roller_blind_state_simple
              data:
                option: 'partial'

        # From PARTIAL → OPEN (let it run full 18 minutes)
        - conditions:
            - condition: state
              entity_id: input_select.roller_blind_state_simple
              state: 'partial'
          sequence:
            - delay:
                seconds: 1080  # 18 minutes
            - service: input_select.select_option
              target:
                entity_id: input_select.roller_blind_state_simple
              data:
                option: 'open'

      # Already OPEN → Do nothing
      default: []
  mode: restart

roller_blinds_close_simple:
  alias: Roller Blinds Close (Simple)
  sequence:
    # Send IR close command
    - service: remote.send_command
      data:
        device: Roller Blinds
        command: Down
      target:
        device_id: 3d7542325305f19a1d70e5b14947b2a9

    # Update state based on current position
    - choose:
        # From OPEN → PARTIAL (stop after 5 seconds)
        - conditions:
            - condition: state
              entity_id: input_select.roller_blind_state_simple
              state: 'open'
          sequence:
            - delay:
                seconds: 5
            - service: script.roller_blinds_stop
            - service: input_select.select_option
              target:
                entity_id: input_select.roller_blind_state_simple
              data:
                option: 'partial'

        # From PARTIAL → CLOSED (let it run full 18 minutes)
        - conditions:
            - condition: state
              entity_id: input_select.roller_blind_state_simple
              state: 'partial'
          sequence:
            - delay:
                seconds: 1080  # 18 minutes
            - service: input_select.select_option
              target:
                entity_id: input_select.roller_blind_state_simple
              data:
                option: 'closed'

      # Already CLOSED → Do nothing
      default: []
  mode: restart

roller_blinds_set_position_simple:
  alias: Roller Blinds Set Position (Simple)
  fields:
    position:
      description: Target position (0=closed, 50=partial, 100=open)
      example: 50
  sequence:
    - choose:
        # Position 0-20 = CLOSED
        - conditions:
            - condition: template
              value_template: "{{ position <= 20 }}"
          sequence:
            - service: script.roller_blinds_close_simple

        # Position 21-79 = PARTIAL
        - conditions:
            - condition: template
              value_template: "{{ position > 20 and position < 80 }}"
          sequence:
            # Determine if we need to open or close to get to partial
            - choose:
                # Currently CLOSED → Open to partial
                - conditions:
                    - condition: state
                      entity_id: input_select.roller_blind_state_simple
                      state: 'closed'
                  sequence:
                    - service: script.roller_blinds_open_simple

                # Currently OPEN → Close to partial
                - conditions:
                    - condition: state
                      entity_id: input_select.roller_blind_state_simple
                      state: 'open'
                  sequence:
                    - service: script.roller_blinds_close_simple

              # Already PARTIAL → Do nothing
              default: []

        # Position 80-100 = OPEN
        - conditions:
            - condition: template
              value_template: "{{ position >= 80 }}"
          sequence:
            - service: script.roller_blinds_open_simple
            # If currently CLOSED, need to open twice
            - condition: state
              entity_id: input_select.roller_blind_state_simple
              state: 'closed'
            - delay:
                seconds: 6
            - service: script.roller_blinds_open_simple
  mode: restart
```

---

## Automation Updates

### Automations to Remove

**Delete these (no longer needed):**
1. `covers_refresh_roller_blind_positions` - No more polling
2. `covers_roller_blind_timer_finished_full_open` - No more timer
3. `covers_roller_blind_timer_finished_full_close` - No more timer
4. `covers_roller_blind_partial_position_stop` - No more partial position calculation
5. `covers_roller_blind_position_debug_logger` - No more position tracking

**Keep but update:**
- All blinds automation (morning open, evening close, etc.)
- Just replace position values with state names

### Example Automation Update

**Before:**
```yaml
action:
  - service: cover.set_cover_position
    target:
      entity_id: cover.roller_blinds_chan1
    data:
      position: 50  # Half open
```

**After:**
```yaml
action:
  - service: input_select.select_option
    target:
      entity_id: input_select.roller_blind_state_simple
    data:
      option: 'partial'

  # Then trigger the appropriate script
  - choose:
      - conditions:
          - condition: state
            entity_id: input_select.roller_blind_state_simple
            state: 'closed'
        sequence:
          - service: script.roller_blinds_open_simple
      - conditions:
          - condition: state
            entity_id: input_select.roller_blind_state_simple
            state: 'open'
        sequence:
          - service: script.roller_blinds_close_simple
```

**OR simpler:**
```yaml
action:
  - service: cover.set_cover_position
    target:
      entity_id: cover.roller_blinds_simple
    data:
      position: 50  # Maps to 'partial' state
```

---

## UI Updates

### Dashboard Card

**Before (complex position slider):**
```yaml
features:
  - type: cover-open-close
  - type: cover-position  # Position slider 0-100%
type: tile
entity: cover.roller_blinds_chan1
```

**After (simple three buttons):**
```yaml
type: entities
entities:
  - entity: input_select.roller_blind_state_simple
    name: Roller Blinds

# OR use buttons:
type: horizontal-stack
cards:
  - type: button
    name: Open
    icon: mdi:blinds-open
    tap_action:
      action: call-service
      service: script.roller_blinds_open_simple
  - type: button
    name: Partial
    icon: mdi:blinds
    tap_action:
      action: call-service
      service: cover.set_cover_position
      service_data:
        entity_id: cover.roller_blinds_simple
        position: 50
  - type: button
    name: Close
    icon: mdi:blinds-closed
    tap_action:
      action: call-service
      service: script.roller_blinds_close_simple
```

---

## Migration Steps

### Step 1: Backup Current Setup

```bash
# Backup automation file
cp automations/05b_blinds_shades.yaml automations/05b_blinds_shades.yaml.backup

# Backup configuration
cp configuration.yaml configuration.yaml.backup

# Commit to git
git add -A
git commit -m "Backup before roller blind simplification"
```

### Step 2: Add New Helpers (Parallel)

Add `input_select.roller_blind_state_simple` to configuration.yaml

**Don't remove old helpers yet!** Test in parallel first.

### Step 3: Create New Scripts

Add the three new scripts to `config/domains/scripts.yaml`

Test manually:
- Call `script.roller_blinds_open_simple` and verify state changes
- Call `script.roller_blinds_close_simple` and verify state changes

### Step 4: Create New Cover Template

Add `cover.roller_blinds_simple` to `config/domains/templates.yaml`

Test in UI:
- Open Developer Tools → States
- Find `cover.roller_blinds_simple`
- Test open/close/set_position services

### Step 5: Update Automations

**One at a time:**
1. Disable old automation
2. Create new automation using simple state
3. Test thoroughly
4. Delete old automation

### Step 6: Update Dashboard Cards

Replace old cover entity with new simple cover

### Step 7: Clean Up

**Remove old helpers:**
- `input_number.roller_blind_position`
- `input_number.roller_blind_target_position`
- `input_select.roller_blind_state`
- `timer.roller_blind_timer`

**Delete old automations:**
- All 5 position-tracking automations

---

## Testing Checklist

### Manual Testing

- [ ] Open blind from fully closed
  - [ ] State changes: closed → partial → open
- [ ] Close blind from fully open
  - [ ] State changes: open → partial → closed
- [ ] Stop blind mid-movement
  - [ ] State changes to partial
- [ ] Set position to 0%
  - [ ] Blind closes fully, state = closed
- [ ] Set position to 50%
  - [ ] Blind moves to partial, state = partial
- [ ] Set position to 100%
  - [ ] Blind opens fully, state = open

### Automation Testing

- [ ] Morning automation triggers
  - [ ] Blinds open correctly
  - [ ] State reflects correctly in UI
- [ ] Evening automation triggers
  - [ ] Blinds close correctly
  - [ ] State reflects correctly in UI
- [ ] Restart Home Assistant mid-movement
  - [ ] State persists correctly
  - [ ] No errors in logs

---

## Rollback Plan

If new system doesn't work:

1. **Disable new automations**
2. **Re-enable old automations:**
   ```bash
   cp automations/05b_blinds_shades.yaml.backup automations/05b_blinds_shades.yaml
   ```
3. **Restore old helpers** in configuration.yaml
4. **Restart Home Assistant**
5. **Delete new scripts and cover template**

---

## Expected Outcomes

### Before Simplification
- 8 input helpers (position, target, state, timer)
- 5 complex position-tracking automations
- ~150 lines of automation code
- Drift/accuracy issues
- Difficult to debug

### After Simplification
- 1 simple input_select (3 states)
- 3 simple scripts (open/close/set_position)
- ~100 lines of script code
- No drift (deterministic states)
- Easy to understand and debug

---

## Alternative: Hardware Upgrade

If the three-state system isn't sufficient, consider:

### Option 1: Zigbee Motor Replacement

**Products:**
- Zemismart Zigbee roller blind motor (~$50-80)
- Yoolax Zigbee motor (~$60-100)

**Benefits:**
- Native position feedback
- Battery powered (no wiring)
- Direct Home Assistant integration
- Accurate position (reported from motor encoder)

### Option 2: Add Position Sensors

**Products:**
- Aqara door/window sensor on blind track (~$20)
- ESP32 with ToF sensor (~$15)

**Benefits:**
- Keep existing motor
- Add position feedback
- Cheaper than motor replacement

---

## Recommendation

**Start with three-state simplification:**
- Low cost (free)
- Low risk (easy rollback)
- Solves most use cases
- Test for 2-4 weeks

**If still not satisfied:**
- Consider hardware upgrade
- Zigbee motor provides best experience
- Cost: ~$50-100 per blind

---

**Generated:** 2025-11-16
**Status:** Ready for implementation (when desired)
**Estimated Time:** 2-3 hours for full migration
