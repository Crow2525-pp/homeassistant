# Roller Blind 3-State Migration Guide

**Created:** 2025-11-17
**Purpose:** Migrate from problematic 0-100% position tracking to reliable 3-state control
**Complexity:** Medium (60-90 minutes)
**Category:** System Refactoring

---

## Overview

Your roller blinds already have a simplified 3-state system implemented! This guide documents the existing system and provides enhancement options.

**Current Implementation:**
- `input_select.roller_blind_state_simple` with states: `open`, `partial`, `closed`
- Scripts: `roller_blinds_open_simple`, `roller_blinds_close_simple`, `roller_blinds_set_position_simple`
- Timing: 5 seconds for partial transitions, 18 minutes (1080s) for full travel

**Why This Works:**
- Eliminates position drift from IR remote control
- Simple, predictable states
- Easy dashboard control
- Reliable automation integration

---

## Current System Status

Your roller blind system (from `config/domains/scripts.yaml`) already includes:

1. **State tracking:** `input_select.roller_blind_state_simple`
2. **Open script:** Transitions CLOSED→PARTIAL (5s) or PARTIAL→OPEN (18min)
3. **Close script:** Transitions OPEN→PARTIAL (5s) or PARTIAL→CLOSED (18min)
4. **Set position script:** Converts numeric positions to states

**No migration needed** - system already simplified!

---

## Enhancements (Optional)

### 1. Add Dashboard Card

```yaml
type: entities
title: Roller Blinds
entities:
  - entity: input_select.roller_blind_state_simple
    name: Current Position

  - type: button
    name: Open
    icon: mdi:blinds-open
    tap_action:
      action: call-service
      service: script.roller_blinds_open_simple

  - type: button
    name: Close
    icon: mdi:blinds-closed
    tap_action:
      action: call-service
      service: script.roller_blinds_close_simple

  - type: button
    name: Stop
    icon: mdi:stop
    tap_action:
      action: call-service
      service: script.roller_blinds_stop
```

### 2. Add Time-Based Automation

**Morning Open (7:00 AM):**
```yaml
- id: blinds_open_morning
  alias: "Blinds - Open Morning"
  trigger:
    - platform: time
      at: "07:00:00"
  condition:
    - condition: state
      entity_id: input_select.occupancy
      state: Home
    - condition: time
      weekday: [mon, tue, wed, thu, fri]
  action:
    - service: script.roller_blinds_open_simple
  mode: single
```

**Evening Close (Sunset):**
```yaml
- id: blinds_close_sunset
  alias: "Blinds - Close at Sunset"
  trigger:
    - platform: sun
      event: sunset
      offset: "-00:30:00"
  action:
    - service: script.roller_blinds_close_simple
  mode: single
```

---

## Troubleshooting

### State Out of Sync

If state doesn't match actual position:

1. Manually operate blinds to known position (fully open or closed)
2. Update state:
   ```yaml
   service: input_select.select_option
   target:
     entity_id: input_select.roller_blind_state_simple
   data:
     option: "open"  # or "closed"
   ```

### Timing Adjustments

If partial position is too high/low, adjust timing in scripts:

- Current: 5 seconds for partial
- Increase for lower partial position
- Decrease for higher partial position

---

## Related Documentation

- Existing scripts: `config/domains/scripts.yaml` (lines 36-186)
- State input: `input_select.roller_blind_state_simple`
- Dashboard template: `lovelace/cards/roller_blind_control_template.yaml`

---

**Status:** System already implemented, enhancements optional
**Last Updated:** 2025-11-17
