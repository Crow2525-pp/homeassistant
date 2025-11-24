# Climate Helper Scripts - Quick Reference

## Quick Usage Examples

### Start Heating
```yaml
- action: script.activate_heating
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: comfort  # or: eco, frost
```

### Start Cooling
```yaml
- action: script.activate_cooling
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: comfort  # or: eco, boost
```

### Dehumidify (Dry Mode)
```yaml
- action: script.activate_dry_mode
  data:
    climate_entity: climate.living_room_versatile_thermastat
```

### Fan Only (No Heating/Cooling)
```yaml
- action: script.activate_fan_only
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: eco  # optional, default: eco
```

### Turn Off
```yaml
- action: script.deactivate_climate
  data:
    climate_entity: climate.living_room_versatile_thermastat
```

---

## All Available Scripts

### 1. `set_climate_mode`
**Purpose:** Set HVAC mode only (heat/cool/dry/fan_only/off)

**Parameters:**
- `climate_entity` (required): Entity ID of climate device
- `hvac_mode` (required): One of: heat, cool, dry, fan_only, off

**Example:**
```yaml
- action: script.set_climate_mode
  data:
    climate_entity: climate.living_room_versatile_thermastat
    hvac_mode: heat
```

---

### 2. `set_climate_preset`
**Purpose:** Set preset mode only (comfort/eco/boost/frost/none)

**Parameters:**
- `climate_entity` (required): Entity ID of climate device
- `preset_mode` (required): One of: comfort, eco, boost, frost, none

**Example:**
```yaml
- action: script.set_climate_preset
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: comfort
```

---

### 3. `set_climate_mode_and_preset`
**Purpose:** Set both HVAC mode and preset mode in one call

**Parameters:**
- `climate_entity` (required): Entity ID of climate device
- `hvac_mode` (required): One of: heat, cool, dry, fan_only, off
- `preset_mode` (required): One of: comfort, eco, boost, frost, none

**Example:**
```yaml
- action: script.set_climate_mode_and_preset
  data:
    climate_entity: climate.living_room_versatile_thermastat
    hvac_mode: cool
    preset_mode: comfort
```

---

### 4. `activate_heating`
**Purpose:** Start heating with specified preset (convenience wrapper)

**Parameters:**
- `climate_entity` (required): Entity ID of climate device
- `preset_mode` (optional, default: comfort): One of: comfort, eco, frost

**Example:**
```yaml
- action: script.activate_heating
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: eco
```

**Internally calls:**
```yaml
set_climate_mode_and_preset with hvac_mode: heat
```

---

### 5. `activate_cooling`
**Purpose:** Start cooling with specified preset (convenience wrapper)

**Parameters:**
- `climate_entity` (required): Entity ID of climate device
- `preset_mode` (optional, default: comfort): One of: comfort, eco, boost

**Example:**
```yaml
- action: script.activate_cooling
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: boost
```

**Internally calls:**
```yaml
set_climate_mode_and_preset with hvac_mode: cool
```

---

### 6. `activate_dry_mode`
**Purpose:** Activate dehumidification mode

**Parameters:**
- `climate_entity` (required): Entity ID of climate device

**Example:**
```yaml
- action: script.activate_dry_mode
  data:
    climate_entity: climate.living_room_versatile_thermastat
```

**Internally calls:**
```yaml
set_climate_mode_and_preset with hvac_mode: dry, preset_mode: comfort
```

---

### 7. `activate_fan_only`
**Purpose:** Activate fan-only mode (circulation without heating/cooling)

**Parameters:**
- `climate_entity` (required): Entity ID of climate device
- `preset_mode` (optional, default: eco): One of: comfort, eco

**Example:**
```yaml
- action: script.activate_fan_only
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: comfort
```

**Internally calls:**
```yaml
set_climate_mode_and_preset with hvac_mode: fan_only
```

---

### 8. `deactivate_climate`
**Purpose:** Turn off HVAC device safely

**Parameters:**
- `climate_entity` (required): Entity ID of climate device

**Example:**
```yaml
- action: script.deactivate_climate
  data:
    climate_entity: climate.living_room_versatile_thermastat
```

**Internally calls:**
```yaml
set_climate_mode with hvac_mode: off
```

---

### 9. `record_climate_trigger`
**Purpose:** Record that a climate automation was triggered (for analytics/tracking)

**Parameters:**
- `counter_entity` (required): Counter entity to increment (e.g., input_number)
- `datetime_entity` (required): Datetime entity to update with trigger time

**Example:**
```yaml
- action: script.record_climate_trigger
  data:
    counter_entity: input_number.living_room_heat_triggers_today
    datetime_entity: input_datetime.last_trigger_living_room_heat
```

**Use Case:** Track how many times heating activated per day, and when the last trigger occurred

---

## Preset Modes Explained

### comfort
- **Use:** Normal comfortable operation
- **Typical setpoint:** 20-22°C
- **Best for:** Active occupancy hours

### eco
- **Use:** Energy-saving mode
- **Typical setpoint:** 18-20°C (heating) or 24-26°C (cooling)
- **Best for:** Away mode, shoulder seasons, nighttime

### boost / frost
- **boost:** Maximum cooling/dehumidifying
- **frost:** Minimum heating (freeze protection)
- **Best for:** Extreme weather, emergency conditions

### none
- **Use:** Default thermostat behavior
- **No preset applied**

---

## HVAC Modes Explained

| Mode | Purpose | When to Use |
|------|---------|------------|
| **heat** | Heating only | Winter, cold days |
| **cool** | Cooling only | Summer, hot days |
| **dry** | Dehumidification | High humidity, no temperature change |
| **fan_only** | Circulation only | Mild weather, air mixing needed |
| **off** | Complete shutdown | Away mode, no comfort required |

---

## Common Patterns

### Pattern 1: Morning Wake-Up Heating
```yaml
- trigger: time
  at: "06:00:00"
- action: script.activate_heating
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: comfort
```

### Pattern 2: Hot Day Cooling
```yaml
- trigger: state
  entity_id: sensor.temperature
  above: 25
- action: script.activate_cooling
  data:
    climate_entity: climate.living_room_versatile_thermastat
    preset_mode: comfort
```

### Pattern 3: High Humidity Dehumidify
```yaml
- trigger: state
  entity_id: sensor.humidity
  above: 75
- action: script.activate_dry_mode
  data:
    climate_entity: climate.living_room_versatile_thermastat
```

### Pattern 4: Shutdown When Away
```yaml
- trigger: state
  entity_id: input_select.occupancy
  to: Away
- action: script.deactivate_climate
  data:
    climate_entity: climate.living_room_versatile_thermastat
```

### Pattern 5: Cool-Down Before Bed
```yaml
- trigger: state
  entity_id: input_select.occupancy
  to: Sleeping
- action: script.activate_cooling
  data:
    climate_entity: climate.master_bedroom_versatile_thermastat
    preset_mode: eco
```

### Pattern 6: Track Trigger Count
```yaml
- trigger: state
  entity_id: climate.living_room_versatile_thermastat
  to: heat
- action: script.record_climate_trigger
  data:
    counter_entity: input_number.living_room_heat_triggers_today
    datetime_entity: input_datetime.last_trigger_living_room_heat
```

---

## Multi-Room Example

Control multiple rooms in sequence:

```yaml
- id: activate_all_bedrooms_cooling
  alias: "Bedrooms - Activate Cooling"
  triggers:
    - trigger: state
      entity_id: input_boolean.super_hot_today
      to: "on"
  actions:
    # Master Bedroom
    - action: script.activate_cooling
      data:
        climate_entity: climate.masterbed_versatile_thermostat
        preset_mode: comfort
    # Henry's Room
    - action: script.activate_cooling
      data:
        climate_entity: climate.henry_s_room_versatile_thermostat
        preset_mode: comfort
    # Otto's Room
    - action: script.activate_cooling
      data:
        climate_entity: climate.otto_s_room
        preset_mode: comfort
```

---

## Troubleshooting

### Script Not Found Error
**Solution:** Make sure `climate_scripts.yaml` is included in your `scripts.yaml` config

### Climate Device Not Responding
**Solution:** Check device is online first:
```yaml
- condition: state
  entity_id: climate.living_room_versatile_thermastat
  state_not: unavailable
```

### Preset Not Supported by Device
**Solution:** Check your thermostat supports that preset. Fall back to mode-only:
```yaml
- action: script.set_climate_mode
  data:
    climate_entity: climate.living_room_versatile_thermastat
    hvac_mode: heat
```

### Multiple Automations Conflicting
**Solution:** Add conditions to prevent conflicts:
```yaml
conditions:
  - condition: state
    entity_id: input_boolean.climate_manual_control_living
    state: "off"  # Don't run if manually overridden
```

---

## File Location

Scripts are defined in: `config/domains/climate_scripts.yaml`

Included via: `config/domains/scripts.yaml` (via `!include climate_scripts.yaml`)

---

**Last Updated:** 2025-11-05
