# MQTT GoSungrow Configuration Issues & Solutions

## Problem Summary

The GoSungrow solar monitoring integration publishes MQTT discovery messages with invalid Home Assistant configurations, causing log errors.

## Error Messages Observed

```
Error 'The unit of measurement `kWp` is not valid together with device class `power`'
Error 'The unit of measurement `W/㎡` is not valid together with device class `irradiance`'
Error 'The unit of measurement `Wh/㎡` is not valid together with device class `irradiance`'
Value error while updating state of sensor.gosungrow_* has device class 'None', state class 'measurement' unit 'None' ... has the non-numeric value: 'false'
```

## Root Cause Analysis

The GoSungrow application (https://github.com/MickMake/GoSungrow) publishes MQTT discovery messages for Home Assistant with:

1. **Invalid Unit/Device Class Combinations:**
   - `kWp` unit with `power` device class (should be `W` for power)
   - `W/㎡` unit with `irradiance` device class (should be `W/m²` - proper SI unit)
   - `Wh/㎡` unit with `irradiance` device class (should be `Wh/m²`)

2. **String Values in Numeric Sensors:**
   - Sensors with `state_class: measurement` or `state_class: total` receive string values
   - Examples: `"false"`, `"true"`, `"GMT+10"`, sensor names, URLs
   - These should be filtered as non-numeric or use `state_class: None`

3. **Invalid Select Options:**
   - `select.gosungrow_option_mqtt_loglevel` expects options but receives 'info'

## Why This Happens

GoSungrow's MQTT discovery schema doesn't properly validate against Home Assistant's strict entity configuration requirements in recent HA versions (2025.x+).

## Solution Options

### Option 1: Accept the Errors (Current Approach)
The errors don't break functionality - they're just log noise. GoSungrow sensors still work despite the configuration errors.

**Pros:** No action needed, sensors function normally
**Cons:** Logs are polluted with error messages

### Option 2: Disable GoSungrow Integration (If Not Critical)
If solar monitoring is not essential, disable the GoSungrow MQTT publication entirely.

In GoSungrow application settings:
- Disable MQTT mode
- Or disable solar sensors in MQTT discovery

**Pros:** Clean logs, no configuration errors
**Cons:** Loss of solar monitoring data

### Option 3: Filter MQTT Discovery (Advanced)
Create a Node-RED flow or Python script to intercept and fix GoSungrow MQTT discovery messages before Home Assistant processes them.

Example fixes:
```python
# Correct invalid configurations
if unit_of_measurement == "kWp" and device_class == "power":
    unit_of_measurement = "W"  # Change to watts

if unit_of_measurement in ["W/㎡", "Wh/㎡"] and device_class == "irradiance":
    unit_of_measurement = unit_of_measurement.replace("㎡", "m²")  # Fix Unicode

if isinstance(value, str) and state_class in ["measurement", "total"]:
    state_class = None  # Remove state_class for string values
```

### Option 4: Report Upstream
File an issue with GoSungrow project to fix their MQTT discovery schema.

Issue: https://github.com/MickMake/GoSungrow/issues

## Current Workaround

**Using Option 1** - The errors are logged but don't affect functionality. This is acceptable for a working system where log noise is the only issue.

### To Verify GoSungrow Sensors Still Work:

1. Go to Settings → Devices & Services → Devices
2. Filter by "GoSungrow"
3. Verify sensors show state values (even if configuration is technically invalid)
4. Check solar production graphs in Energy dashboard

## Recommended Action

If solar monitoring is critical and log noise is a problem:
- Consider implementing Option 3 (MQTT filtering via Node-RED)
- Or file a GitHub issue with GoSungrow to fix discovery schema

If logs are acceptable with these warnings:
- Leave as-is (current state)

## Related Files

- MQTT Configuration: `/config/domains/mqtt.yaml`
- GoSungrow Integration: Installed via HACS (automatically installed custom integration)
- Affected Sensors: All sensors with `sensor.gosungrow_*` entity IDs

## Log Reference

Last occurrence: 2025-11-04 in `home-assistant.log`
Frequency: Appears during MQTT startup and sensor updates (every ~5-10 minutes)

## Next Steps

1. Monitor logs - if error volume becomes problematic, implement filtering
2. Consider upgrading GoSungrow when a fix is available
3. Evaluate if solar monitoring value justifies the log pollution
