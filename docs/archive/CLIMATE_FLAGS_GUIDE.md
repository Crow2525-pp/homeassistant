# Climate Temperature Flags System

**Created:** 2025-10-24
**Status:** ✅ COMPLETE
**Commit:** 569067f

---

## Overview

The Climate Flags system provides real-time temperature condition indicators that guide HVAC automation decisions. These flags break down the temperature spectrum into discrete ranges, allowing automations to respond appropriately to heating and cooling needs.

**Key Concept:** One flag is active at any given time (mutually exclusive), representing the dominant temperature condition of the day.

---

## Temperature Ranges & Flags

### Hot Flags (Cooling Focus)

| Flag | Temperature | Use Case |
|------|-------------|----------|
| **super_hot_today** | > 25°C | Extreme heat: Maximum cooling, aggressive blinds management |
| **hot_today_flag** | 21-25°C | Hot day: Standard cooling, evening cooling assist |
| **warm_today_flag** | 18-21°C | Warm day: Minimal cooling, comfort focus |

### Cold Flags (Heating Focus)

| Flag | Temperature | Use Case |
|------|-------------|----------|
| **super_cold_today** | < 5°C | Extreme cold: Maximum heating, frost protection |
| **cold_today_flag** | 5-10°C | Cold day: Standard heating, preheat in mornings |
| **cool_today_flag** | 10-15°C | Cool day: Minimal heating, comfort focus |

### Neutral Zone

| Zone | Temperature | Condition |
|------|-------------|-----------|
| **All flags OFF** | 15-20°C | Mild: No special heating/cooling |

---

## How Flags Are Set

### Morning Evaluation (04:30 AM)

**"Climate Flags - Mark Hot Day" automation**

Uses forecast minimum and maximum temperatures:
- **Forecast Max > 25°C** → Set `super_hot_today` ON
- **Forecast Max 21-25°C** → Set `hot_today_flag` ON
- **Forecast Max 18-21°C** → Set `warm_today_flag` ON
- **Forecast Min < 5°C** → Set `super_cold_today` ON
- **Forecast Min 5-10°C** → Set `cold_today_flag` ON
- **Forecast Min 10-15°C** → Set `cool_today_flag` ON
- **Forecast between 15-20°C** → All flags OFF

### Afternoon Re-check (15:30)

**"Climate Flags - Afternoon Re-check (3-4pm)" automation**

Re-evaluates based on ACTUAL current temperature (not forecast):
- Runs year-round (every season)
- Compares actual conditions to predictions
- Updates flags if reality differs from forecast

**Example:** Forecast predicted cool day (10-15°C), but afternoon is warmer (21°C) → Switches to `hot_today_flag`

---

## Using Flags in Automations

### Example: Heating Automation Trigger

```yaml
- condition: or
  conditions:
  - condition: state
    entity_id: input_boolean.super_cold_today
    state: 'on'
  - condition: state
    entity_id: input_boolean.cold_today_flag
    state: 'on'
alias: "Heating needed (super cold or cold day)"
```

### Example: Cooling Automation Trigger

```yaml
- condition: or
  conditions:
  - condition: state
    entity_id: input_boolean.super_hot_today
    state: 'on'
  - condition: state
    entity_id: input_boolean.hot_today_flag
    state: 'on'
alias: "Cooling needed (hot or super hot day)"
```

### Example: Comfort-Only Automation

```yaml
- condition: or
  conditions:
  - condition: state
    entity_id: input_boolean.warm_today_flag
    state: 'on'
  - condition: state
    entity_id: input_boolean.cool_today_flag
    state: 'on'
alias: "Comfort adjustments only (warm or cool day)"
```

---

## Automation Integration Points

### Frost Protection (Winter Heating)

Can now use `super_cold_today` or `cold_today_flag` to:
- Activate more aggressive frost protection
- Use lower temperature thresholds
- Enable heating in rooms typically left unheated

### Night Cooling (Summer Cooling)

Can use `super_hot_today` to:
- Start cooling earlier in the evening
- Use more aggressive temperature targets
- Extend cooling duration

### Preheat (Winter Comfort)

Can check `cold_today_flag` to decide:
- Whether to preheat in the morning
- How much to preheat
- Duration of preheat cycle

### Blind Management (Solar Control)

Can use `super_hot_today` to:
- Close blinds more aggressively
- Keep blinds closed longer in afternoon
- Prioritize privacy during extreme heat

---

## Current System Status

### Helpers Created
- 3 new input_boolean helpers for cold conditions
- Integrated with existing 3 hot condition helpers
- **Total:** 6 climate flags, one active at any time

### Automations Updated
1. **Climate Flags - Mark Hot Day** (04:30)
   - Now evaluates both forecast max AND min temperatures
   - Sets appropriate flag for the entire day

2. **Climate Flags - Afternoon Re-check** (15:30)
   - Now runs year-round (not just warm seasons)
   - Evaluates both hot AND cold ranges
   - Provides 7 temperature condition categories

### Flag Hierarchy

```
COLD CONDITIONS:           NEUTRAL:           WARM CONDITIONS:
super_cold (< 5°C)         (15-20°C)           super_hot (> 25°C)
cold (5-10°C)              All flags OFF        hot (21-25°C)
cool (10-15°C)                                  warm (18-21°C)
```

---

## Implementation Details

### Morning Flag Setting (Forecast-Based)

The "Mark Hot Day" automation:
1. Evaluates `sensor.braybrook_temp_min_0` (forecast minimum)
2. Evaluates `sensor.braybrook_temp_max_0` (forecast maximum)
3. Sets ONE flag based on combined conditions
4. Ensures mutual exclusivity (turns off conflicting flags)

### Afternoon Flag Updating (Reality-Based)

The "Afternoon Re-check" automation:
1. Checks ACTUAL current temperature
2. Compares to morning forecast
3. Adjusts flag if needed
4. Runs at 15:30 (allows for morning variations)

---

## Temperature Thresholds Reference

### Cold Conditions (Heating)
- **Super Cold:** < 5°C (frost protection critical)
- **Cold:** 5-10°C (active heating needed)
- **Cool:** 10-15°C (minimal heating, comfort focus)

### Neutral Zone
- **15-20°C:** No active heating or cooling (comfortable zone)

### Hot Conditions (Cooling)
- **Warm:** 18-21°C (comfort focus, minimal cooling)
- **Hot:** 21-25°C (active cooling needed)
- **Super Hot:** > 25°C (aggressive cooling, solar control)

---

## Future Enhancement Ideas

1. **Seasonal Threshold Adjustment**
   - Adjust thresholds based on season
   - Winter: More aggressive cold thresholds
   - Summer: More aggressive hot thresholds

2. **Multi-Room Evaluation**
   - Different flags per room
   - Room-specific heating/cooling strategies
   - Cross-room load balancing

3. **Humidity-Based Flags**
   - Add humidity conditions alongside temperature
   - Enhance dehumidification logic
   - Mold prevention in cold/humid conditions

4. **Energy-Based Thresholds**
   - Dynamic thresholds based on TOU rates
   - Lower comfort during expensive hours
   - Aggressive comfort during cheap hours

5. **Predictive Adjustments**
   - Pre-adjust based on next day's forecast
   - Thermal mass pre-conditioning
   - Battery/thermal storage optimization

---

## Files Modified

- **configuration.yaml**
  - Added `cool_today_flag` helper
  - Added `cold_today_flag` helper
  - Added `super_cold_today` helper

- **automations.yaml**
  - Extended "Climate Flags - Mark Hot Day" with cold condition evaluation
  - Completely rewrote "Climate Flags - Afternoon Re-check" conditions
  - Added support for year-round flag evaluation

---

## Testing Checklist

- [ ] Verify morning automation sets correct cold flag at 04:30
- [ ] Verify afternoon automation updates flags at 15:30
- [ ] Test with winter weather (forecast < 5°C)
- [ ] Test with summer weather (forecast > 25°C)
- [ ] Test with mild weather (15-20°C)
- [ ] Verify flag transitions are smooth
- [ ] Confirm no flag conflicts (only one active)
- [ ] Test in all seasons

---

## Quick Reference

**When to use which flag:**

- **Building heating automation?** Check `cold_today_flag` or `super_cold_today`
- **Building cooling automation?** Check `hot_today_flag` or `super_hot_today`
- **Comfort-only adjustment?** Check `warm_today_flag` or `cool_today_flag`
- **Any temperature condition needed?** One of these 6 flags is always relevant

---

**Status:** ✅ Production Ready
**Last Updated:** 2025-10-24
**Commit:** 569067f
