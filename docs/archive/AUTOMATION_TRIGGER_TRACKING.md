# Automation Trigger Tracking System

**Created:** 2025-10-24
**Purpose:** Historical analysis of climate automation trigger patterns for debugging, optimization, and understanding system behavior

---

## Overview

The automation trigger tracking system captures when and how often climate automations execute, enabling you to:

- **Understand behavior**: See which automations are active and when
- **Debug issues**: Identify over-triggering, under-triggering, or unexpected patterns
- **Optimize thresholds**: Find inefficiencies by analyzing trigger frequency
- **Track trends**: Compare patterns across days/weeks/seasons
- **Validate automations**: Confirm automations are running as expected

---

## How It Works

### Two-Part Tracking System

#### 1. **Last Trigger Time** (input_datetime helpers)
Records the most recent execution timestamp for key automations:
- `input_datetime.last_trigger_seasonal_climate_manager`
- `input_datetime.last_trigger_morning_blinds`
- `input_datetime.last_trigger_preheat_530am`
- `input_datetime.last_trigger_evening_cooling`
- `input_datetime.last_trigger_frost_protection`
- `input_datetime.last_trigger_afternoon_recheck`

Updated whenever the automation runs.

#### 2. **Daily Trigger Counter** (input_number helpers)
Counts how many times each automation triggered today:
- `input_number.seasonal_climate_triggers_today`
- `input_number.morning_blinds_triggers_today`
- `input_number.preheat_triggers_today`
- `input_number.evening_cooling_triggers_today`
- `input_number.frost_protection_triggers_today`
- `input_number.afternoon_recheck_triggers_today`

Reset to 0 at 00:00:00 every day by "Reset Daily Automation Trigger Counters (Midnight)" automation.

### Tracking in Automations

Each tracked automation includes tracking actions at the start:

```yaml
actions:
  # Track automation trigger (for historical analysis)
  - action: input_datetime.set_datetime
    target:
      entity_id: input_datetime.last_trigger_seasonal_climate_manager
    data:
      datetime: "{{ now().isoformat() }}"
  - action: input_number.increment
    target:
      entity_id: input_number.seasonal_climate_triggers_today
  # End tracking

  # ... rest of automation actions
```

This happens **before** any conditional logic, so every execution is recorded regardless of outcome.

---

## Understanding the Data

### Expected Trigger Counts by Automation

#### Seasonal Climate Manager (Most Important)
- **Target**: 50-100 triggers/day in active season (varies by triggers)
- **Reason**: Runs on 15-minute time pattern, temperature changes, time-based triggers
- **HIGH (>150)**: May indicate:
  - Temperature oscillating around threshold (hysteresis issue)
  - Sensor noise causing rapid temperature fluctuations
  - AC over-cycling (turning on/off frequently)
- **LOW (<20)**: May indicate:
  - Season doesn't require active management
  - Manual overrides active
  - Automation disabled
  - HVAC master switch OFF

#### Morning Blinds Controller
- **Target**: 1-3 triggers/day during relevant season
- **Should trigger**:
  - Summer: Daily (adjusting blinds based on time and solar position)
  - Winter: Rarely or never (blinds not managed)
  - Spring/Fall: 1-2 times (seasonal transitions)
- **ZERO in summer**: Problem - blinds automation not running

#### Living Room Preheat 5:30am
- **Target**: 0-1 trigger/day in winter, 0 in summer
- **Should trigger**: Once per day at 5:30am if temp <19°C and winter
- **ZERO in winter**: Normal if room is already warm, OR automation disabled
- **Triggers in summer**: Unexpected - check season setting

#### Evening Cooling Night
- **Target**: 0-1 trigger/day in summer
- **Should trigger**: When room gets hot (>24°C) in evening during summer
- **HIGH (>5)**: Room staying hot all night:
  - Check: Are blinds closing during day?
  - Check: Is AC turning off again?
  - Check: Is room getting hot again after cooling?
- **ZERO in summer on hot days**: May need better daytime cooling

#### Frost Protection Night
- **Target**: 1 trigger/day on cool nights without hot day flags
- **Should trigger**: At 18:00 on nights when no hot day flags are set
- **Pattern**: High count in winter/shoulder season, zero in summer

#### Afternoon Re-check 15:30
- **Target**: 1 trigger/day in spring/summer/autumn, 0 in winter
- **Should trigger**: Once daily at 15:30 to validate morning forecast
- **ZERO**: Either not in warm season, or automation disabled

### Daily Pattern Examples

#### Typical Summer Day
```
Seasonal Climate: 85 triggers
Morning Blinds: 2 triggers
Preheat: 0 triggers
Evening Cooling: 1 trigger
Frost Protection: 0 triggers
Afternoon Re-check: 1 trigger
TOTAL: 89 triggers
```

#### Typical Winter Day
```
Seasonal Climate: 55 triggers
Morning Blinds: 0 triggers
Preheat: 1 trigger
Evening Cooling: 0 triggers
Frost Protection: 1 trigger
Afternoon Re-check: 0 triggers
TOTAL: 57 triggers
```

#### Day with Problems (Over-cycling)
```
Seasonal Climate: 245 triggers ⚠️ VERY HIGH
Morning Blinds: 2 triggers
Preheat: 0 triggers
Evening Cooling: 8 triggers ⚠️ HIGH
Frost Protection: 0 triggers
Afternoon Re-check: 1 trigger
TOTAL: 256 triggers (3x normal)
```
→ Indicates temperature instability (check sensors, thresholds, hysteresis)

---

## Using the Dashboard

### Location
**Climate View > 📊 Automation Trigger History & Patterns**

### What You See

1. **Today's Trigger Summary Table**
   - Quick overview of all tracked automations
   - Current count and last trigger time
   - Status indicator (High/Normal/No triggers)

2. **Daily Trigger Counters**
   - Shows current count for each automation
   - Can be manually adjusted for testing
   - Resets at midnight automatically

3. **Last Trigger Times**
   - Shows exactly when each automation last ran
   - Useful for debugging "automation didn't run" issues
   - Updates in real-time

4. **Pattern Analysis Guide**
   - Explains what each counter means
   - Expected ranges for different seasons
   - How to interpret high/low counts

5. **Troubleshooting Guide**
   - Solutions for high trigger counts
   - Debugging steps for failed triggers
   - Common issues and fixes

---

## Debugging with Trigger Data

### Scenario 1: "Nothing's happening"
**Check**:
1. Is Seasonal Climate Manager trigger count = 0?
   - YES → Check: Manual override ON? Master switch OFF? Season wrong?
   - NO → Automation is running, maybe just not taking action

2. Check specific automation last trigger time
   - If it says "Never" → Automation never ran (check triggering conditions)
   - If recent → Automation ran but conditions blocked action

### Scenario 2: "AC is cycling on and off constantly"
**Check**:
1. Seasonal Climate Manager trigger count
   - If >150 → Temperature oscillating around threshold
   - Fix: Increase `for:` minutes in temperature triggers
   - Or: Adjust temperature threshold (increase comfort range)

2. Evening Cooling trigger count
   - If >10 → Room getting hot again repeatedly
   - Fix: Improve daytime cooling (earlier cooling start?)
   - Check: Are blinds actually closing?

### Scenario 3: "Preheat never runs"
**Check**:
1. Last trigger time for Preheat
   - If "Never" → Check season, time, temperature at 5:30am

2. Look at previous days' counter
   - If it was 1 yesterday, 0 today → Temperature probably above 19°C already
   - If it was 0 both days → Check season and automation enable state

### Scenario 4: "Blinds not closing in morning"
**Check**:
1. Morning Blinds trigger count
   - If 0 in summer → Automation not running (check season, check enabled)
   - If 1-2 → Automation ran, might not be closing as expected (check automation logic, not tracking issue)

---

## Analyzing Trends

### Day-to-Day Analysis
Keep a simple log:
```
Monday:   85 Seasonal, 2 Blinds, 0 Preheat, 1 Evening, 0 Frost, 1 Recheck = 89 total
Tuesday:  88 Seasonal, 2 Blinds, 0 Preheat, 1 Evening, 0 Frost, 1 Recheck = 92 total
Wednesday: 92 Seasonal, 2 Blinds, 0 Preheat, 2 Evening, 0 Frost, 1 Recheck = 97 total
```
→ Consistent pattern = Normal behavior, no issues

### Week-to-Week Analysis
Same week next week should show similar totals (accounting for weather/occupancy changes):
```
Week 1 (Summer): 89-97 triggers/day = 620 total
Week 2 (Same season): 85-95 triggers/day = 615 total
→ Consistent = System stable
```

### Seasonal Analysis
Track different seasons to understand baseline:
```
SUMMER:   80-100 triggers/day (active cooling)
WINTER:   40-60 triggers/day (active heating, less frequent)
SPRING:   30-50 triggers/day (transitioning)
FALL:     40-70 triggers/day (transitioning to winter)
```

---

## Configuration Reference

### Reset Counters Automation
```yaml
alias: Reset Daily Automation Trigger Counters (Midnight)
triggers:
  - at: '00:00:00'
    trigger: time
actions:
  - action: input_number.set_value
    target:
      entity_id:
        - input_number.seasonal_climate_triggers_today
        - input_number.morning_blinds_triggers_today
        # ... etc
    data:
      value: 0
```

### Adding Tracking to New Automations
To track a new automation, add to its actions:
```yaml
actions:
  # Track automation trigger
  - action: input_datetime.set_datetime
    target:
      entity_id: input_datetime.last_trigger_[your_automation]
    data:
      datetime: "{{ now().isoformat() }}"
  - action: input_number.increment
    target:
      entity_id: input_number.[your_automation]_triggers_today
  # End tracking

  # ... rest of your automation
```

And add helpers to configuration.yaml:
```yaml
input_datetime:
  last_trigger_[your_automation]:
    name: Last Trigger - [Your Automation Name]
    has_date: true
    has_time: true

input_number:
  [your_automation]_triggers_today:
    name: [Your Automation] Triggers Today
    min: 0
    max: 100
    step: 1
    initial: 0
    unit_of_measurement: triggers
    icon: mdi:counter
```

---

## Files Modified

- **configuration.yaml**: Added 6 input_datetime helpers + 6 input_number counters
- **automations.yaml**:
  - Added "Reset Daily Automation Trigger Counters (Midnight)" automation
  - Added tracking actions to "Master Bedroom - Seasonal Climate Manager"
- **lovelace/cards/climate/automation_trigger_history.yaml**: NEW - Dashboard card for visualization
- **lovelace/views/climate.yaml**: Updated to include new tracking card

---

## Related Documentation

- **HVAC_PRINCIPLES_DASHBOARD.md**: Understand what principles each automation implements
- **hvac_principles.md**: Core automation design principles
- **automations.yaml**: Detailed automation logic and conditions
- **configuration.yaml**: Helper definitions

---

## Future Enhancements

Potential improvements to tracking system:
- [ ] Long-term statistics (weekly/monthly totals)
- [ ] Trend graphs (showing trigger count over time)
- [ ] Anomaly detection (alerting when patterns change unexpectedly)
- [ ] Performance metrics (average time per automation execution)
- [ ] Integration with Home Assistant history statistics
- [ ] Export trigger data for external analysis

---

**Last Updated:** 2025-10-24
**System Status:** ✅ Operational
**Tracking Coverage:** 6 key automations (can be expanded)
