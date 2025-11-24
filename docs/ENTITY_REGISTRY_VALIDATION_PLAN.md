# Entity Registry & Validation System Design Plan

**Status:** 📋 Planning Document
**Purpose:** Define how the LLM can validate entities, lookup correct ones, and understand entity relationships and priorities
**Created:** 2025-11-24

---

## Problem Statement

**Current Issues:**
1. 236 KB entity list (ENTITY_LIST.md) is a flat list - hard to validate or search
2. Multiple versions of similar entities exist (e.g., base climate vs Versatile Climate)
3. LLM doesn't know which entity to prefer in different contexts
4. No way to validate if an entity actually exists or is "correct"
5. Entity relationships unclear (e.g., which climate entity controls which room)

**Example Problem:**
```yaml
# Which climate entity should be used?
climate.living_room_ac             # OLD - base climate entity
climate.living_room_versatile_thermostat  # NEW - Versatile Thermostat
```

Without knowing priorities, the LLM might use the wrong one.

---

## Proposed Solution: Tiered Entity Registry with Priority System

### 1. Registry Structure

Create a YAML-based entity registry organized by **domain** and **priority level**.

**File Structure:**
```
docs/
├── system/
│   ├── ENTITY_LIST.md                    (existing - comprehensive list)
│   ├── ENTITY_REGISTRY.yaml              (NEW - structured registry with metadata)
│   └── ENTITY_ALIASES.yaml               (NEW - entity aliases and deprecations)
├── reference/
│   ├── orphaned_entities.txt
│   ├── disabled_entities.txt
│   └── empty_devices.txt
└── ENTITY_REGISTRY_VALIDATION_PLAN.md    (this file)
```

### 2. ENTITY_REGISTRY.yaml Format

```yaml
# ENTITY_REGISTRY.yaml - Structured entity metadata with priorities
# Purpose: Enable LLM to validate entities and understand which to prefer

version: "1.0"
last_updated: 2025-11-24

# Domain: Climate Control
climate:
  description: HVAC systems and thermostats
  priority_guidance: |
    ALWAYS prefer Versatile Climate entities over base climate entities.
    Versatile Thermostat provides better control and presets.

  entities:
    # TIER 1 (PRIMARY - Always prefer these)
    living_room_versatile_thermostat:
      type: climate
      device: Living Room Versatile Thermostat
      room: living_room
      status: active
      priority: 1
      description: Living room climate control (Versatile Thermostat)
      capabilities:
        - set_temperature
        - set_hvac_mode: [heat, cool, dry, fan_only, off]
        - set_preset_mode: [comfort, eco, boost, frost, frost_protection]
      aliases: [living_room_vc, lr_thermostat]
      notes: Preferred over climate.living_room_ac

    # TIER 2 (SECONDARY - Use if Tier 1 not available)
    living_room_ac:
      type: climate
      device: Living Room AC
      room: living_room
      status: deprecated
      priority: 2
      description: Living room climate control (base entity, deprecated)
      reason_deprecated: "Superseded by Versatile Thermostat"
      replacement: living_room_versatile_thermostat
      notes: Keep for backward compatibility only

    # (More entities follow this pattern...)

# Domain: Lighting
light:
  description: Lights and lighting groups
  priority_guidance: |
    1. Prefer light groups over individual lights
    2. Use socket lights for power control
    3. Use brightness on named light entities

  entities:
    living_room_light_socket_1:
      type: light
      device: Living Room Light Socket
      room: living_room
      status: active
      priority: 1
      description: Living room main light
      capabilities:
        - on_off
        - brightness
      entity_id: light.living_room_light_socket_1

    computer_desk_light_socket_1:
      type: light
      device: Computer Desk Light Socket
      room: study
      status: active
      priority: 1
      description: Computer desk task lighting
      capabilities:
        - on_off
        - brightness
      entity_id: light.computer_desk_light_socket_1

# Domain: Binary Sensors
binary_sensor:
  description: Motion sensors, switches, door sensors, etc.
  priority_guidance: |
    Prefer Frigate motion detection over other sources.
    Use debounce for motion to avoid false positives.

  entities:
    frigate_person_detected:
      type: binary_sensor
      device: Frigate Camera System
      room: exterior
      status: active
      priority: 1
      description: Person detected by Frigate AI
      trigger_type: motion_with_ai_detection
      debounce_recommended: 2_seconds

    aqara_motion_and_light_sensor_p2_occupancy:
      type: binary_sensor
      device: Aqara Motion Sensor P2
      room: kitchen
      status: active
      priority: 1
      description: Kitchen motion sensor
      trigger_type: motion
      debounce_recommended: 2_seconds

# Domain: Input Helpers
input_boolean:
  description: Boolean input helpers (toggles)
  priority_guidance: |
    Use input helpers for control gates and mode switches.
    Always check helper exists before using in automations.

  entities:
    morning_routine_disabled:
      type: input_boolean
      status: active
      priority: 1
      description: Toggle to disable morning routine
      used_in: [morning_lights, morning_preheat]
      required: true

    morning_routine_triggered_today:
      type: input_boolean
      status: active
      priority: 1
      description: Gate to prevent duplicate morning routine triggers
      used_in: [motion_morning_routine]
      required: true
      reset_at: "00:00:00"

input_select:
  description: Select input helpers (dropdown)
  entities:
    occupancy:
      type: input_select
      status: active
      priority: 1
      description: Current occupancy state
      options: [Home, Away, Sleeping, Holiday]
      used_in: [climate_automations, lighting_automations]
      required: true

input_datetime:
  description: Date/time input helpers
  entities:
    ac_filter_downstairs:
      type: input_datetime
      status: active
      priority: 1
      description: AC filter last changed date
      used_in: [rfid_ac_filter_automation]
      required: true

# Domain: Sensor
sensor:
  description: Various sensors
  priority_guidance: |
    Temperature sensors: Prefer Versatile Thermostat internal sensor
    Weather: Use external API for accuracy

  entities:
    essendon_airport_temp:
      type: sensor
      device: Weather Integration
      room: external
      status: active
      priority: 1
      description: Outside temperature from Essendon Airport
      unit: celsius
      used_in: [morning_preheat]
      required: true

# Domain: Scripts
script:
  description: Home Assistant scripts (custom actions)
  priority_guidance: |
    Use climate helper scripts for all HVAC actions.
    Prefer named scripts over inline service calls.

  entities:
    activate_heating:
      type: script
      status: active
      priority: 1
      description: Activate heating with specified preset
      parameters:
        - name: climate_entity
          type: string
          required: true
        - name: preset_mode
          type: string
          required: true
          options: [comfort, eco, boost, frost, frost_protection]
      used_in: [morning_preheat, climate_automations]
      file: config/domains/climate_scripts.yaml

    activate_cooling:
      type: script
      status: active
      priority: 1
      description: Activate cooling
      parameters:
        - name: climate_entity
          type: string
          required: true
        - name: preset_mode
          type: string
          required: true
      file: config/domains/climate_scripts.yaml

    deactivate_climate:
      type: script
      status: active
      priority: 1
      description: Turn off HVAC
      parameters:
        - name: climate_entity
          type: string
          required: true
      file: config/domains/climate_scripts.yaml
```

### 3. ENTITY_ALIASES.yaml - Deprecated/Alternative Names

```yaml
# Entity aliases and deprecations
# Use this to redirect old names to new ones

aliases:
  # Climate
  living_room_ac: living_room_versatile_thermostat
  lr_ac: living_room_versatile_thermostat
  living_room_climate: living_room_versatile_thermostat

  # Lighting
  lr_light: living_room_light_socket_1
  desk_light: computer_desk_light_socket_1

deprecations:
  living_room_ac:
    status: deprecated
    reason: "Superseded by Versatile Thermostat"
    replacement: living_room_versatile_thermostat
    deprecated_since: "2025-10-15"
    removal_planned: "2025-12-31"
    migration_guide: "Use living_room_versatile_thermostat instead"
```

---

## 3. Priority System Explanation

### Priority Levels

| Level | Name | When to Use | Example |
|-------|------|-------------|---------|
| **1** | Primary/Active | Prefer in new automations | `living_room_versatile_thermostat` |
| **2** | Secondary | Only if Primary unavailable | `living_room_ac` (deprecated) |
| **3** | Fallback | Legacy/backup only | old base climate entities |
| **4** | Disabled | Don't use | broken/unused entities |

### Priority Decision Rules

**For LLM Automation Creation:**

```
IF domain == "climate" THEN
  1. Filter for status="active"
  2. Filter for priority <= 2
  3. Prefer priority=1 entities
  4. Check compatibility with automation type
  ELSE IF domain == "light" THEN
  1. Prefer light groups (if exist)
  2. Then socket entities
  3. Check brightness_support for dimming automations
  ELSE IF domain == "binary_sensor" THEN
  1. Filter by room
  2. Prefer AI-based (Frigate) over simple motion
  3. Apply debounce if motion-based
END
```

---

## 4. Entity Validation System

### 4.1 Validation Checklist

When using an entity, validate:

```yaml
entity_validation_checklist:
  - [ ] Entity exists in ENTITY_REGISTRY.yaml
  - [ ] Status is "active" (not deprecated/disabled)
  - [ ] Priority is 1-2 (not fallback/disabled)
  - [ ] Has required_configuration completed
  - [ ] All required input helpers exist (if automation)
  - [ ] Room/location makes sense for automation
  - [ ] Entity has required capabilities
```

### 4.2 Validation Query Examples

**Query 1: "Get the best climate entity for living room"**
```yaml
domain: climate
room: living_room
priority: [1, 2]
status: active
result: living_room_versatile_thermostat
```

**Query 2: "Get all motion sensors with debounce capability"**
```yaml
domain: binary_sensor
trigger_type: motion
debounce_recommended: exists
result: [aqara_motion_and_light_sensor_p2_occupancy, ...]
```

**Query 3: "Is entity.xyz valid for use?"**
```yaml
check:
  entity: climate.living_room_ac
  purpose: new_automation
result:
  exists: true
  status: deprecated
  priority: 2
  recommendation: "Use living_room_versatile_thermostat instead"
  valid_for_new: false
  valid_for_legacy: true
```

---

## 5. Integration with LLM Automation Creation

### 5.1 Before Writing Automation Code

1. **Entity Selection Phase**
   - Query ENTITY_REGISTRY.yaml for needed domain
   - Filter by: `status=active AND priority<=2`
   - Match by room/location
   - Validate all required helpers exist

2. **Dependency Resolution**
   - Check `used_in` field for conflicts
   - Verify all input helpers are available
   - Confirm capabilities match automation needs

3. **Documentation Phase**
   - Include entity ID with human name
   - Add comment why this entity was chosen
   - Note any deprecated alternatives

### 5.2 Example: Creating Morning Light Automation

```yaml
# PROCESS:

# 1. QUERY ENTITY REGISTRY
Query: "Get light entity for wake-up in study"
Result:
  - computer_desk_light_socket_1 (priority=1, active)
  - reading_light_socket_1 (priority=1, active)

# 2. CHECK CAPABILITIES
Selected: computer_desk_light_socket_1
- Supports: on_off, brightness ✓
- Needed for automation: on_off, brightness ✓
- Status: active ✓

# 3. CHECK HELPERS
Need:
  - input_boolean.morning_routine_disabled ✓ exists
  - input_select.occupancy ✓ exists

# 4. WRITE AUTOMATION with metadata
- id: morning_lights_computer_room
  alias: "Morning Routine - Lights"
  description: "Turn on computer room light at 5:00 AM"

  # Entity selection notes:
  # - Entity: computer_desk_light_socket_1 (Priority 1, Active)
  # - Why: Best light for morning wake-up in study
  # - Alternative: reading_light_socket_1 (if desk light unavailable)

  action:
    - service: light.turn_on
      target:
        entity_id: light.computer_desk_light_socket_1  # Priority 1
      data:
        brightness_pct: 30
```

---

## 6. Maintenance Strategy

### 6.1 Registry Updates

**When to update ENTITY_REGISTRY.yaml:**
- ✅ New entity is added to system
- ✅ Entity status changes (active → deprecated)
- ✅ Entity renamed or replaced
- ✅ New priority discovered
- ✅ Capabilities change

**When NOT to update:**
- ❌ Temporary state changes (entity unavailable)
- ❌ Attribute value changes (temperature readings)

### 6.2 Automated Validation Script (Future)

```python
# Pseudo-code for registry validator
validate_entity_registry():
  registry = load('ENTITY_REGISTRY.yaml')
  ha_entities = query_home_assistant()

  for each_registry_entry:
    # Check entity actually exists
    if entry.entity_id not in ha_entities:
      warn(f"Registry entity missing: {entry.entity_id}")

    # Check active entities aren't deprecated
    if entry.status=="active" and entry.priority==2:
      warn(f"Priority 2 marked active: {entry.entity_id}")

    # Check required helpers exist
    for helper in entry.required_helpers:
      if helper not in ha_entities:
        error(f"Required helper missing: {helper}")

    # Check aliases point to valid entities
    for alias in entry.aliases:
      if alias in ha_entities:
        error(f"Alias conflict: {alias}")

  return validation_report
```

---

## 7. Usage Examples for LLM

### Example 1: "Create automation to turn on kitchen light at sunset"

```yaml
# LLM PROCESS:

# 1. Query registry
Query: "Get light for kitchen, status=active, priority<=2"
Result: [light.kitchen_light_socket_1 (priority=1)]

# 2. Check sunset trigger availability
Query: "Can I use time-of-day: sunset?"
Result: Yes, sun integration available

# 3. Check for gate/condition helpers
Query: "Is there a disable_automations helper?"
Result: No, use individual automation_disabled helpers

# 4. Generate automation with metadata
- id: kitchen_sunset_light
  alias: "Kitchen - Sunset Light"
  description: "Turn on kitchen light at sunset"

  trigger:
    - platform: sun
      event: sunset

  condition:
    - condition: state
      entity_id: input_select.occupancy
      state: Home

  action:
    - service: light.turn_on
      target:
        entity_id: light.kitchen_light_socket_1  # From registry: Priority 1
      data:
        brightness_pct: 80

  # NOTES FROM REGISTRY:
  # Entity: kitchen_light_socket_1 (Priority 1, Active)
  # Capabilities: on_off, brightness
  # No known conflicts
```

### Example 2: "I need the climate entity for the living room"

```yaml
# LLM PROCESS:

# Query registry with room filter
Query: climate domain, room=living_room, status=active
Result: living_room_versatile_thermostat (Priority 1)

# Check for deprecated alternatives
Query: Are there other climate entities for living_room?
Result:
  - living_room_ac (Priority 2, status=deprecated)
  - living_room_climate (Priority 3, status=disabled)

# Response to user:
{
  "recommended": "climate.living_room_versatile_thermostat",
  "priority": 1,
  "status": "active",
  "why": "Versatile Thermostat provides better control and presets",
  "alternatives": [
    {
      "entity": "climate.living_room_ac",
      "priority": 2,
      "status": "deprecated",
      "notes": "Only use if Versatile Thermostat unavailable"
    }
  ]
}
```

---

## 8. Implementation Roadmap

### Phase 1: Foundation (Now)
- [ ] Create ENTITY_REGISTRY.yaml structure (this document)
- [ ] Populate with primary entities (Tier 1 & 2)
- [ ] Create ENTITY_ALIASES.yaml for deprecated names
- [ ] Document in this plan

### Phase 2: Integration (Week 2)
- [ ] Update existing automations with entity metadata comments
- [ ] Create LLM query examples
- [ ] Test entity lookups with sample automations

### Phase 3: Validation (Week 3)
- [ ] Create validation script (check entities exist)
- [ ] Add checks to GitHub Actions CI/CD
- [ ] Create dashboard for registry status

### Phase 4: Automation (Week 4+)
- [ ] Build entity lookup API in Python
- [ ] Integration with Home Assistant REST API
- [ ] LLM query interface (ask "which entity for X?")

---

## 9. Registry Data Fields Reference

```yaml
entity_metadata:
  type: <domain type>                 # climate, light, binary_sensor, etc.
  device: <physical device name>      # What real device this represents
  room: <room name>                   # Physical location
  status: [active, deprecated, disabled, unavailable]
  priority: <1-4>                     # Priority tier
  description: <human readable>       # What it does
  capabilities: [list]                # What it can do
  entity_id: <full entity id>        # Actual entity ID (if different)
  aliases: [list]                     # Alternative names
  used_in: [automations]             # Where it's actively used
  required: true/false                # Must exist for system to work
  reset_at: <time>                   # Auto-reset time (for gate helpers)
  debounce_recommended: <seconds>    # If motion/sensor
  unit: <unit of measurement>         # For sensors
  parameters: [list]                  # For scripts
  replacement: <entity>               # If deprecated, what to use
  migration_guide: <text>             # How to migrate
  deprecated_since: <date>            # When deprecated
  removal_planned: <date>             # When will be removed
```

---

## 10. Benefits of This System

✅ **For LLM:**
- Know which entity to use in different contexts
- Understand entity priorities and preferences
- Validate entities before creating automations
- Get clear deprecation warnings

✅ **For Maintenance:**
- Single source of truth for all entities
- Clear migration path for deprecated entities
- Easy to track what each entity is used for
- Automated validation possible

✅ **For Automations:**
- Self-documenting entity choices
- Easy to identify wrong entity being used
- Clear upgrade paths

✅ **For Future Development:**
- Foundation for entity API
- Basis for dashboards showing entity status
- Integration point for Home Assistant discovery

---

## Next Steps

1. **Approve Structure:** Review and approve registry format
2. **Populate Registry:** Add all active entities from current system
3. **Test Lookups:** Create query examples and test with sample automations
4. **Implement Validation:** Build checking system for registry integrity
5. **Document Integration:** Add to LLM automation creation workflow

---

*Plan created: 2025-11-24*
*Status: Ready for implementation*
