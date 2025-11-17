# Morning Wake-up & Preheat Routine Setup Guide

**Created:** 2025-11-17
**Purpose:** Automated morning heating and lighting for comfortable wake-up
**Complexity:** Medium (30-45 minutes)
**Category:** Automation Template

---

## Overview

This guide sets up comprehensive morning routines including:
- 5:00 AM lighting automation (computer room only, NOT bedroom)
- 5:30 AM downstairs preheat with intelligent preset selection
- Motion-based kitchen routine (5:30-7:00 AM)
- Dashboard controls for easy customization

**Key Features:**
- **Intelligent preset selection:** Chooses eco/comfort/boost based on outside temperature, time of day, WFH status, and home presence
- **No hard-coded temperatures:** Uses versatile climate presets only
- **One-time morning trigger:** Prevents repeated triggering throughout morning
- **Easy customization:** Input helpers for all settings

---

## Architecture Overview

### Preset Selection Logic

The system selects climate presets based on multiple factors:

**Primary Factor: Outside Temperature**
- Below 5°C: `boost` preset (maximum warmth)
- 5-10°C: `comfort` preset (normal heating)
- Above 10°C: `eco` preset (minimal heating)

**Secondary Factors:**
- **WFH (Work From Home):** If WFH toggle is on, prefer `comfort` over `eco`
- **Home Presence:** If no one home, use `frost` preset
- **Time of Day:** 5:30-6:30 AM prioritizes comfort for wake-up
- **Heating State:** If heating already on, maintain current preset

**User Override:**
- Manual preset selector can force a specific preset
- Disable toggle can turn off all morning automation

---

## Prerequisites

- Versatile climate entity configured (e.g., `climate.living_room_versatile_thermastat`)
- Outside temperature sensor (e.g., `sensor.essendon_airport_temp`)
- Motion sensors for kitchen (optional)
- Light entities properly configured

**Estimated Time:** 30-45 minutes

---

## Step 1: Create Input Helpers

### Via Home Assistant UI

Navigate to **Settings** > **Devices & Services** > **Helpers**

**Helper 1: Morning Routine Disable Toggle**
- Type: **Toggle**
- Name: `Morning Routine Disabled`
- Entity ID: `input_boolean.morning_routine_disabled`
- Icon: `mdi:power`

**Helper 2: Work From Home Indicator**
- Type: **Toggle**
- Name: `Work From Home Today`
- Entity ID: `input_boolean.wfh_today`
- Icon: `mdi:home-account`

**Helper 3: Morning Preset Selector (Override)**
- Type: **Dropdown**
- Name: `Morning Preset Override`
- Entity ID: `input_select.morning_preset_override`
- Options:
  - `auto` (default - use intelligent selection)
  - `eco`
  - `comfort`
  - `boost`
  - `off`
- Icon: `mdi:thermostat`

**Helper 4: Morning Lighting Room Selector**
- Type: **Dropdown**
- Name: `Morning Lights - Rooms`
- Entity ID: `input_select.morning_lights_rooms`
- Options:
  - `Computer Room Only` (default)
  - `Kitchen Only`
  - `Both`
  - `None`
- Icon: `mdi:lightbulb-group`

**Helper 5: Morning Routine Triggered (Gate)**
- Type: **Toggle**
- Name: `Morning Routine Triggered Today`
- Entity ID: `input_boolean.morning_routine_triggered_today`
- Icon: `mdi:gate`
- **Note:** This automatically resets daily, used to prevent duplicate triggers

---

## Step 2: Create Morning Preheat Automation

Copy from `automations/99_morning_preheat_template.yaml` or create via UI:

### Key Logic

**Trigger:** 5:30 AM weekdays (Monday-Friday)

**Conditions:**
- Morning routine not disabled
- Home occupied (not Away/Holiday)
- Winter season (optional - can remove if heating year-round)

**Actions:**
1. Calculate desired preset based on outside temp, WFH, time, presence
2. Set climate to heat mode with calculated preset
3. (Optional) Send notification

**Preset Selection Template:**
```yaml
{% set outside_temp = states('sensor.essendon_airport_temp') | float(15) %}
{% set wfh = is_state('input_boolean.wfh_today', 'on') %}
{% set home = is_state('input_select.occupancy', 'Home') %}
{% set override = states('input_select.morning_preset_override') %}

{% if override != 'auto' %}
  {{ override }}
{% elif not home %}
  frost
{% elif outside_temp < 5 %}
  boost
{% elif outside_temp < 10 %}
  comfort
{% elif wfh %}
  comfort
{% else %}
  eco
{% endif %}
```

---

## Step 3: Create Morning Lighting Automation

Copy from `automations/99_morning_lights_template.yaml` or create via UI:

### Key Logic

**Trigger:** 5:00 AM weekdays

**Conditions:**
- Morning routine not disabled
- Selected room(s) configured
- Lights not already on

**Actions:**
1. Turn on computer room light to 30% (gradual warm-up)
2. **DOES NOT turn on bedroom light** (as specified in requirements)
3. (Optional) Turn on kitchen light if selected

**Entity References:**
- Computer room: `light.computer_desk_light_socket_1`
- Kitchen: `light.living_room_light_socket_1` (or your kitchen light)
- Lounge group: `light.lounge` (general lighting)

---

## Step 4: Create Motion-Based Morning Routine

Copy from `automations/99_motion_morning_routine_template.yaml` or create via UI:

### Key Logic

**Trigger:** Motion detected in kitchen between 5:30-7:00 AM

**Conditions:**
- Morning routine not already triggered today
- Morning routine not disabled
- Time between 5:30-7:00 AM

**Actions:**
1. Set gate: `input_boolean.morning_routine_triggered_today` to ON
2. Turn on kitchen lights to 50%
3. (Optional) Start coffee maker or other appliances
4. (Optional) Play morning news briefing

**Gate Reset:**
- Automatically resets at midnight via separate automation
- Prevents kitchen motion from re-triggering routine multiple times

---

## Step 5: Create Gate Reset Automation

This automation resets the morning trigger gate daily at midnight:

```yaml
- id: morning_routine_gate_reset
  alias: "Morning Routine - Reset Gate Daily"
  description: "Reset morning trigger gate at midnight for next day"

  trigger:
    - platform: time
      at: "00:00:00"

  action:
    - service: input_boolean.turn_off
      target:
        entity_id: input_boolean.morning_routine_triggered_today

  mode: single
```

---

## Step 6: Add Dashboard Control Card

Add to your Lovelace dashboard:

```yaml
type: entities
title: Morning Routine Controls
entities:
  - entity: input_boolean.morning_routine_disabled
    name: Disable Morning Routine
    icon: mdi:power

  - entity: input_boolean.wfh_today
    name: Working From Home Today
    icon: mdi:home-account

  - entity: input_select.morning_preset_override
    name: Heating Preset Override
    icon: mdi:thermostat

  - entity: input_select.morning_lights_rooms
    name: Morning Lights
    icon: mdi:lightbulb-group

  - type: section

  - entity: sensor.essendon_airport_temp
    name: Outside Temperature
    icon: mdi:thermometer

  - entity: input_boolean.morning_routine_triggered_today
    name: Routine Triggered Today
    icon: mdi:gate
    tap_action:
      action: none

  - type: button
    name: Test Preheat Now
    icon: mdi:play
    tap_action:
      action: call-service
      service: automation.trigger
      service_data:
        entity_id: automation.morning_preheat_downstairs
        skip_condition: false

show_header_toggle: false
state_color: true
```

---

## Step 7: Test & Verify

### Manual Testing Checklist

**Test 1: Preheat Automation**
- [ ] Set outside temp sensor to simulate cold morning (<10°C)
- [ ] Trigger automation manually from Developer Tools
- [ ] Verify climate entity switches to heat mode
- [ ] Verify correct preset selected based on temperature
- [ ] Check notification sent (if configured)

**Test 2: Lighting Automation**
- [ ] Trigger lighting automation manually
- [ ] Verify computer room light turns on to 30%
- [ ] Verify bedroom light does NOT turn on
- [ ] Check kitchen light based on selector setting

**Test 3: Motion-Based Routine**
- [ ] Set time to 5:45 AM (or wait until morning)
- [ ] Trigger kitchen motion sensor
- [ ] Verify routine triggers first time
- [ ] Trigger motion again - should NOT trigger again
- [ ] Verify gate resets at midnight

**Test 4: Preset Selection Logic**
- [ ] Test with outside temp < 5°C → Expect boost
- [ ] Test with outside temp 5-10°C → Expect comfort
- [ ] Test with outside temp > 10°C, WFH off → Expect eco
- [ ] Test with outside temp > 10°C, WFH on → Expect comfort
- [ ] Test with occupancy Away → Expect frost or off

### Live Testing (Recommended)

1. **Enable on weekend first** to test without disrupting weekday routine
2. **Monitor logs** for first week: **Settings** > **System** > **Logs**
3. **Adjust timings** based on actual wake-up times
4. **Fine-tune presets** based on comfort and energy usage

---

## Customization

### Adjust Wake-Up Times

Edit automation triggers:

**Preheat:** Change `at: "05:30:00"` to your desired time
**Lighting:** Change `at: "05:00:00"` to your desired time
**Motion window:** Change `after: "05:30:00"` and `before: "07:00:00"`

### Adjust Temperature Thresholds

Edit preset selection template:

```yaml
# Current thresholds:
# < 5°C = boost
# 5-10°C = comfort
# > 10°C = eco/comfort (based on WFH)

# Example: Make boost trigger at <8°C instead:
{% elif outside_temp < 8 %}
  boost
{% elif outside_temp < 12 %}
  comfort
```

### Add Weekend Support

Add condition to check day of week:

```yaml
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
      # Add 'sat' and 'sun' to enable weekends
```

### Add Coffee Maker Integration

In motion-based routine, add action:

```yaml
- service: switch.turn_on
  target:
    entity_id: switch.coffee_maker
```

---

## Troubleshooting

### Bedroom Light Turns On (Should NOT)

**Cause:** Entity reference error in lighting automation

**Fix:**
1. Verify automation does NOT reference `light.masterbed_lights` or `light.sleeping_light`
2. Only `light.computer_desk_light_socket_1` should be used
3. Check `light.lounge` group doesn't include bedroom lights

### Heating Doesn't Start

**Cause:** Conditions not met or preset selection error

**Debug:**
1. Check automation trace in UI
2. Verify occupancy is "Home"
3. Check manual control toggle is off
4. Verify climate entity is available
5. Test preset selection template in Developer Tools > Template

### Wrong Preset Selected

**Cause:** Template logic error or sensor issue

**Debug:**
1. Check outside temperature sensor: `sensor.essendon_airport_temp`
2. Verify WFH toggle state
3. Test template calculation in Developer Tools
4. Use override selector to force specific preset

### Motion Routine Triggers Multiple Times

**Cause:** Gate not working or reset automation failed

**Fix:**
1. Verify `input_boolean.morning_routine_triggered_today` exists
2. Check gate reset automation at midnight
3. Manually reset gate if needed
4. Check automation mode is `single` not `restart`

---

## Next Steps

1. **Monitor energy usage** before and after to measure efficiency
2. **Adjust preset thresholds** based on comfort preferences
3. **Add voice control** integration (optional)
4. **Create similar routines** for evening/night (e.g., bedtime routine)
5. **Integrate with wake-up alarm** for dynamic timing

---

## Related Documentation

- Template automation: `automations/99_morning_preheat_template.yaml`
- Lighting automation: `automations/99_morning_lights_template.yaml`
- Motion routine: `automations/99_motion_morning_routine_template.yaml`
- Dashboard card: `config/lovelace/morning_routine_control.yaml`
- Climate helper scripts: `config/domains/scripts.yaml` (section: Climate Helper Scripts)

---

**Status:** Template ready for deployment
**Last Updated:** 2025-11-17
