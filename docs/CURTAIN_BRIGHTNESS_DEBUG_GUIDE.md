# Curtain Brightness Debug Guide

## Overview

Your curtains are controlled by a Blueprint automation that closes them based on multiple factors, including **brightness level**. The current threshold is set to **11,940 lux**, which may be too low for your needs.

This guide helps you debug and adjust the brightness threshold.

---

## Debug Sensors Created

I've created three new debug sensors in `config/domains/templates.yaml` to help you monitor and understand the curtain closing behavior:

### 1. **Curtain - Should Close (Brightness)**
- **Entity ID:** `binary_sensor.curtain_should_close_brightness`
- **Type:** Binary Sensor (On/Off)
- **Shows:** Whether the brightness level would trigger a close
- **Attributes:**
  - `current_brightness`: Current lux reading
  - `threshold`: 11,940 lux
  - `status`: Human-readable explanation

**How to use:**
- Check this sensor in Developer Tools → States
- When it says "On" = Brightness is too low, curtains can close
- When it says "Off" = Brightness is still too high, curtains won't close

### 2. **Curtain Brightness Status**
- **Entity ID:** `sensor.curtain_brightness_status`
- **Type:** Sensor (Text)
- **Shows:** Visual status of current brightness level
- **Example values:**
  - "Very Bright ☀️" (> 15,000 lux)
  - "Bright 🌞" (11,940-15,000 lux)
  - "Moderate 🌤️" (5,000-11,940 lux)
  - "Dim 🌅" (2,000-5,000 lux)
  - "Very Dim 🌙" (500-2,000 lux)
  - "Dark 🌑" (< 500 lux)

**How to use:**
- Quick visual check of brightness category
- Helps understand if your room lighting is normal for the time of day
- Good for daily monitoring

### 3. **Curtain Close Decision**
- **Entity ID:** `sensor.curtain_close_decision`
- **Type:** Sensor (Text)
- **Shows:** Complete decision logic including time window
- **Possible states:**
  - "Outside close window (16:00-22:00)" - Not in closing timeframe
  - "❌ TOO BRIGHT (12,500/11,940 lux)" - Brightness too high
  - "✅ READY TO CLOSE (10,000/11,940 lux)" - All conditions met

**Attributes provided:**
- `current_time`: Current time
- `brightness_lux`: Current brightness in lux
- `brightness_percent`: How close to threshold (negative = too bright)
- `threshold_lux`: 11,940 (the threshold)
- `in_close_window`: Whether in 16:00-22:00 window

**How to use:**
- Most comprehensive debug sensor
- Shows exactly why curtains did/didn't close
- Use when investigating unexpected behavior

---

## How to Monitor in Home Assistant

### Option 1: Developer Tools (Quick Check)
1. Go to **Settings → Developer Tools → States**
2. Search for:
   - `sensor.curtain_brightness_status`
   - `sensor.curtain_close_decision`
   - `binary_sensor.curtain_should_close_brightness`
3. Click each to see current state and attributes

### Option 2: Create Dashboard Card (Recommended)

Create a new card in your dashboard using this YAML:

```yaml
type: entities
title: "🪟 Curtain Brightness Debug"
entities:
  - sensor.curtain_brightness_status
  - sensor.curtain_close_decision
  - binary_sensor.curtain_should_close_brightness
  - sensor.hub_2_0be5_illuminance

state_color: true
show_header_toggle: false
```

Or use a more detailed markdown card:

```yaml
type: markdown
title: "🪟 Curtain Brightness Debug"
content: |
  **Current Brightness:** {{ states('sensor.hub_2_0be5_illuminance') }} lux

  **Status:** {{ states('sensor.curtain_brightness_status') }}

  **Decision:** {{ states('sensor.curtain_close_decision') }}

  **Will Close?** {% if is_state('binary_sensor.curtain_should_close_brightness', 'on') %}✅ Yes{% else %}❌ No{% endif %}

  ---

  Threshold: 11,940 lux
```

### Option 3: Automation Trace

When curtains close unexpectedly:
1. Go to **Settings → Automations and Scenes → Automations**
2. Find "Curtains - Cover Control Automation"
3. Click **History** or **Trigger** to see recent executions
4. This shows what triggered the close action

---

## Understanding the Brightness Threshold

### Current Setting: 11,940 lux

This is roughly equivalent to:
- **Indoor:** Well-lit room with multiple lights on (no direct sun)
- **Outdoor:** Late afternoon with some sun (around 4-5 PM on a clear day)
- **Comparison:** About 45-50% of peak afternoon brightness

### Common Brightness Levels

| Condition | Lux | Will Close? |
|-----------|-----|-----------|
| Bright sunny day at noon | 40,000 | ❌ No |
| Clear afternoon (2-3 PM) | 20,000 | ❌ No |
| Late afternoon (4 PM) | 12,000-15,000 | ⚠️ Maybe |
| Overcast afternoon | 8,000-10,000 | ✅ Yes |
| Early evening (5-6 PM) | 3,000-5,000 | ✅ Yes |
| Twilight | 500-1,000 | ✅ Yes |
| Night | < 100 | ✅ Yes |

---

## Why Curtains Close at 4 PM

When your curtains closed at 4 PM, one of these happened:

1. **Brightness dropped below 11,940 lux** - Most likely
   - Check `sensor.curtain_brightness_status` at that time
   - Note the weather conditions (cloudy, clear, etc.)

2. **Temperature triggered closing** - Blueprint also has temp triggers
   - Check if room was too warm
   - Look at `sensor.ble_temperature_masterbed_temp_humidity_sensor`

3. **Sun position (elevation) triggered closing** - Blueprint has sun elevation trigger
   - Sun gets lower in the sky as afternoon progresses
   - Even if bright, low sun angle can trigger close

---

## Adjusting the Brightness Threshold

### Problem
Curtains close while it's still bright in your room (11,940 lux threshold too low)

### Solution
Increase the threshold so curtains wait until it's actually dark

### Step 1: Find Ideal Threshold
Monitor the brightness levels throughout the afternoon:

1. At **3 PM** (should be open): Check brightness
2. At **4 PM** (when they closed): Check brightness
3. At **5 PM** (what time you prefer closing): Check brightness

Record these values. The desired threshold should be:
- **Higher than** the 4 PM reading (so they don't close early)
- **Lower than** the 3 PM reading (so they can close eventually)

### Step 2: Locate the Setting

The brightness threshold is in the Blueprint automation:

**File:** `automations/05b_blinds_shades.yaml`
**Line:** Look for the Curtains automation (around line 131-158)
**Setting:** `brightness_down: 11940`

### Step 3: Adjust the Value

Common recommended values:

- **Keep as is (11,940):** For spring/fall (moderate daylight)
- **Increase to 15,000:** For summer (longer daylight, brighter afternoons)
- **Increase to 18,000:** For very bright conditions/high latitude
- **Increase to 20,000:** For very bright, sunny climate

### Step 4: Make the Change

Edit `automations/05b_blinds_shades.yaml`:

Find this section:
```yaml
- id: '1749869631608'
  alias: Curtains - Cover Control Automation
  use_blueprint:
    path: hvorragend/cover_control_automation.yaml
    input:
      brightness_down: 11940
```

Change `11940` to your new value, e.g.:
```yaml
      brightness_down: 15000
```

### Step 5: Test

1. **Save and reload automations:**
   - Settings → Developer Tools → YAML → Automation Reloader

2. **Monitor the next day at 4 PM:**
   - Check `sensor.curtain_close_decision`
   - Watch `sensor.curtain_brightness_status`
   - Note if curtains open/close as expected

3. **Adjust again if needed:**
   - Still closing too early? → Increase threshold more
   - Not closing by evening? → Decrease threshold slightly

---

## Debugging Checklist

If curtains still close unexpectedly:

- [ ] **Check time window:** Is it between 16:00-22:00?
  - If outside this window, time control is preventing close
  - Check the blueprint settings for close time window

- [ ] **Check brightness sensor location:**
  - Is `sensor.hub_2_0be5_illuminance` measuring room light or window light?
  - Direct sun on sensor can cause unexpected readings

- [ ] **Check temperature triggers:**
  - Blueprint also has temperature-based triggers
  - Monitor `sensor.ble_temperature_masterbed_temp_humidity_sensor`
  - Room temperature may be closing curtains, not brightness

- [ ] **Check weather:**
  - Cloudy days drop brightness quickly
  - Check `weather.braybrook` conditions at close time

- [ ] **Check for other automations:**
  - Is another automation also controlling curtains?
  - Check all automations mentioning `cover.curtain_3_b3bb`

---

## Alternative: Use Brightness + Temperature

Instead of just brightness, you could also consider:

```yaml
Curtains close when BOTH:
- Time between 16:00-22:00 AND
- Brightness < [your_value] lux AND
- Outdoor temp < 25°C (so not closing on bright hot days)
```

This prevents closing on bright but cool evenings.

---

## Restore to Default

If you want to revert to the original setting:

```yaml
brightness_down: 11940
```

This was the default, which corresponds to:
- Late afternoon (4-5 PM) brightness
- Slightly brighter than twilight
- More suitable for spring/fall with shorter days

---

## Questions?

Use the debug sensors to understand the current behavior:

**"Why did curtains close?"**
→ Check `sensor.curtain_close_decision` at that time

**"What's the brightness right now?"**
→ Check `sensor.hub_2_0be5_illuminance` and `sensor.curtain_brightness_status`

**"Should curtains close now?"**
→ Check `binary_sensor.curtain_should_close_brightness`

---

Last Updated: 2025-11-05
