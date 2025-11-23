# RFID AC Filter Tracking Setup Guide

**Created:** 2025-11-17
**Purpose:** Track AC filter changes using RFID/NFC tag scans
**Complexity:** Low (15-20 minutes)
**Category:** Automation Template

---

## Overview

This guide helps you set up automated AC filter tracking using RFID/NFC tags. When you scan the tag after changing your AC filter, Home Assistant automatically updates a timestamp and calculates how many days have passed since the last change.

**Benefits:**
- Never forget when you last changed the AC filter
- Get automatic notifications when filter is due for replacement
- Simple one-tap tracking (just scan the tag)
- Dashboard visibility of filter status

**How it works:**
1. Attach an RFID/NFC tag to your AC filter unit
2. Register the tag with Home Assistant
3. When you change the filter, scan the tag
4. Automation updates the timestamp automatically
5. Dashboard shows days since last change

---

## Prerequisites

- Home Assistant with RFID/NFC integration configured
- RFID/NFC tag (13.56 MHz tags recommended, e.g., NTAG213/215/216)
- Mobile app or NFC reader integrated with HA
- Basic knowledge of Home Assistant automation creation

**Estimated Time:** 15-20 minutes

---

## Step 1: Create Input Helper for Last Change Date

First, create an input helper to store the date of the last filter change.

### Option A: Via Home Assistant UI (Recommended)

1. Navigate to **Settings** > **Devices & Services** > **Helpers**
2. Click **+ CREATE HELPER**
3. Select **Date and/or time**
4. Configure:
   - **Name:** `AC Filter Downstairs Last Changed`
   - **Entity ID:** `input_datetime.ac_filter_downstairs` (auto-generated)
   - **Has date:** ✓ (checked)
   - **Has time:** ☐ (unchecked - date only is sufficient)
   - **Icon:** `mdi:air-filter` (optional)
5. Click **CREATE**

### Option B: Via configuration.yaml

Add to your `configuration.yaml`:

```yaml
input_datetime:
  ac_filter_downstairs:
    name: AC Filter Downstairs Last Changed
    has_date: true
    has_time: false
    icon: mdi:air-filter
```

Then restart Home Assistant or reload YAML configuration.

---

## Step 2: Register Your RFID/NFC Tag

### Scan and Register Tag

1. Navigate to **Settings** > **Devices & Services** > **Tags**
2. Click **+ ADD TAG** (or scan will auto-create)
3. Scan your RFID/NFC tag with your phone (HA Companion App)
4. When prompted:
   - **Name:** `AC Filter Downstairs`
   - **Tag ID:** (auto-detected, something like `859e3818-e623-47aa-9062-d89afd44489b`)
   - **Icon:** `mdi:air-filter`
5. Click **CREATE**

**Note the Tag ID** - you'll need it for the automation (or use the automation UI to select it).

### Alternative: Find Existing Tag ID

If your tag is already registered:

1. Go to **Settings** > **Devices & Services** > **Tags**
2. Find your tag in the list
3. Click to view details and copy the Tag ID

---

## Step 3: Create Automation for Tag Scan

### Option A: Via Home Assistant UI (Recommended)

1. Navigate to **Settings** > **Automations & Scenes**
2. Click **+ CREATE AUTOMATION**
3. Click **Create new automation** (blank)

**Configure Trigger:**
- Trigger type: **Tag**
- Tag: Select **AC Filter Downstairs** (or your tag name)

**Configure Conditions:**
- (Optional) Add condition to check entity exists:
  - Condition type: **State**
  - Entity: `input_datetime.ac_filter_downstairs`
  - State: Not `unavailable`

**Configure Actions:**
1. Action 1: Update datetime helper
   - Action type: **Call service**
   - Service: `input_datetime.set_datetime`
   - Target: `input_datetime.ac_filter_downstairs`
   - Service data:
     ```yaml
     date: "{{ now().strftime('%Y-%m-%d') }}"
     ```

2. Action 2: Send confirmation notification
   - Action type: **Call service**
   - Service: `notify.persistent_notification`
   - Service data:
     ```yaml
     title: "AC Filter Changed"
     message: "Filter change recorded on {{ now().strftime('%B %d, %Y') }}"
     ```

**Configure Details:**
- Name: `RFID - AC Filter Downstairs Updated`
- Mode: `single`

4. Click **SAVE**

### Option B: Copy Template YAML

Copy the automation template from `automations/99_rfid_ac_filter_template.yaml` to your automations directory and customize the tag ID.

---

## Step 4: Create Template Sensor for Days Since Last Change

This sensor calculates how many days have passed since the last filter change.

### Add Template Sensor

Add to `configuration.yaml` (or create in `config/templates/ac_filter_days_sensor.yaml` if using packages):

```yaml
template:
  - sensor:
      - name: "AC Filter Downstairs Days Since Change"
        unique_id: ac_filter_downstairs_days_since_change
        state: >
          {% set last_changed = states('input_datetime.ac_filter_downstairs') %}
          {% if last_changed not in ['unknown', 'unavailable', 'none'] %}
            {{ (now().date() - (last_changed | as_datetime | as_local).date()).days }}
          {% else %}
            unknown
          {% endif %}
        unit_of_measurement: "days"
        icon: mdi:calendar-clock
        attributes:
          last_changed_date: "{{ states('input_datetime.ac_filter_downstairs') }}"
          last_changed_friendly: >
            {% set last_changed = states('input_datetime.ac_filter_downstairs') %}
            {% if last_changed not in ['unknown', 'unavailable', 'none'] %}
              {{ (last_changed | as_datetime | as_local).strftime('%B %d, %Y') }}
            {% else %}
              Never changed
            {% endif %}
          status: >
            {% set days = this.state | int(0) %}
            {% if days < 30 %}
              Good
            {% elif days < 60 %}
              Due Soon
            {% else %}
              Overdue
            {% endif %}
```

**Restart Home Assistant** or reload template entities.

---

## Step 5: Add Dashboard Card

Add the following card to your Lovelace dashboard to display filter status:

```yaml
type: entities
title: AC Filter Status
entities:
  - entity: input_datetime.ac_filter_downstairs
    name: Last Changed
    icon: mdi:air-filter
  - entity: sensor.ac_filter_downstairs_days_since_change
    name: Days Since Change
    icon: mdi:calendar-clock
  - type: button
    name: Manually Update
    icon: mdi:pencil
    tap_action:
      action: call-service
      service: input_datetime.set_datetime
      service_data:
        entity_id: input_datetime.ac_filter_downstairs
        date: "{{ now().strftime('%Y-%m-%d') }}"
show_header_toggle: false
state_color: true
```

**Enhanced Card with Color Coding:**

```yaml
type: custom:auto-entities
card:
  type: entities
  title: AC Filter Status
  state_color: true
filter:
  include:
    - entity_id: input_datetime.ac_filter_downstairs
      options:
        name: Last Changed
        icon: mdi:air-filter
    - entity_id: sensor.ac_filter_downstairs_days_since_change
      options:
        name: Days Since Change
        type: custom:multiple-entity-row
        secondary_info:
          attribute: status
          name: Status
show_empty: false
```

---

## Step 6: Test & Verify

### Testing Checklist

- [ ] **Test tag scan:**
  1. Open Home Assistant Companion App
  2. Scan the RFID/NFC tag
  3. Verify you see notification: "AC Filter Changed"
  4. Check `input_datetime.ac_filter_downstairs` is updated to today

- [ ] **Test sensor calculation:**
  1. Navigate to **Developer Tools** > **States**
  2. Find `sensor.ac_filter_downstairs_days_since_change`
  3. Verify it shows `0` (if changed today) or correct number of days

- [ ] **Test dashboard card:**
  1. Navigate to your dashboard
  2. Verify AC Filter card displays
  3. Check "Last Changed" shows today's date
  4. Check "Days Since Change" shows `0`

- [ ] **Test manual update button:**
  1. Click "Manually Update" button on dashboard
  2. Verify date updates to today

### Manual Trigger Test

Test the automation without scanning tag:

1. Go to **Settings** > **Automations & Scenes**
2. Find `RFID - AC Filter Downstairs Updated`
3. Click **⋮** (three dots) > **Run**
4. Check notification appears
5. Verify datetime updated

---

## Step 7: Optional Enhancements

### Add Replacement Reminder Automation

Get notified when filter needs replacement (after 60 days):

```yaml
- id: ac_filter_replacement_reminder
  alias: "AC Filter - Replacement Reminder"
  description: "Remind to change AC filter after 60 days"
  trigger:
    - platform: numeric_state
      entity_id: sensor.ac_filter_downstairs_days_since_change
      above: 60
      for:
        hours: 1
  condition:
    - condition: time
      after: "09:00:00"
      before: "21:00:00"
  action:
    - service: notify.mobile_app_your_phone
      data:
        title: "AC Filter Overdue"
        message: >
          AC filter downstairs is overdue for replacement
          ({{ states('sensor.ac_filter_downstairs_days_since_change') }} days).
          Last changed: {{ state_attr('sensor.ac_filter_downstairs_days_since_change', 'last_changed_friendly') }}
        data:
          tag: "ac_filter_reminder"
          actions:
            - action: "ac_filter_changed"
              title: "Mark as Changed"
  mode: single
```

### Add Action Handler for Mobile Notification

Handle "Mark as Changed" action from notification:

```yaml
- id: ac_filter_mark_changed_from_notification
  alias: "AC Filter - Mark Changed from Notification"
  description: "Update filter change date when action button pressed"
  trigger:
    - platform: event
      event_type: mobile_app_notification_action
      event_data:
        action: "ac_filter_changed"
  action:
    - service: input_datetime.set_datetime
      target:
        entity_id: input_datetime.ac_filter_downstairs
      data:
        date: "{{ now().strftime('%Y-%m-%d') }}"
    - service: notify.mobile_app_your_phone
      data:
        title: "AC Filter Updated"
        message: "Filter change recorded successfully!"
  mode: single
```

---

## Troubleshooting

### Tag Scan Not Triggering Automation

**Symptom:** Scanning tag does nothing, no notification appears.

**Solutions:**
1. Check tag is registered:
   - Go to **Settings** > **Devices & Services** > **Tags**
   - Verify tag appears in list
   - Re-register if missing

2. Check automation is enabled:
   - Go to **Settings** > **Automations & Scenes**
   - Find `RFID - AC Filter Downstairs Updated`
   - Ensure toggle is **ON** (blue)

3. Check logs for errors:
   - Go to **Settings** > **System** > **Logs**
   - Look for errors related to tag scanning or automation

4. Test tag scan detection:
   - Go to **Developer Tools** > **Events**
   - Click **LISTEN TO EVENTS**
   - Event type: `tag_scanned`
   - Scan tag and verify event appears

### Sensor Shows "Unknown"

**Symptom:** `sensor.ac_filter_downstairs_days_since_change` shows `unknown`.

**Solutions:**
1. Check input_datetime has a value:
   - Go to **Developer Tools** > **States**
   - Find `input_datetime.ac_filter_downstairs`
   - Ensure it has a date value (not `unknown` or `unavailable`)

2. Set initial value manually:
   - Go to **Settings** > **Devices & Services** > **Helpers**
   - Click on `AC Filter Downstairs Last Changed`
   - Set to today's date or actual last change date

3. Reload template entities:
   - Go to **Developer Tools** > **YAML**
   - Click **TEMPLATE ENTITIES** > **RELOAD**

### Dashboard Card Not Showing

**Symptom:** Dashboard card doesn't appear or shows error.

**Solutions:**
1. Verify entities exist:
   - Check `input_datetime.ac_filter_downstairs` exists
   - Check `sensor.ac_filter_downstairs_days_since_change` exists

2. Check YAML syntax:
   - Use **Developer Tools** > **YAML** configuration check
   - Fix any indentation or syntax errors

3. Refresh browser:
   - Press `Ctrl+Shift+R` (or `Cmd+Shift+R` on Mac)
   - Clear browser cache if needed

---

## Maintenance

### Updating Filter Change Date Manually

If you changed the filter but forgot to scan the tag:

**Via UI:**
1. Go to **Settings** > **Devices & Services** > **Helpers**
2. Click on `AC Filter Downstairs Last Changed`
3. Set the date to when you actually changed the filter
4. Click **UPDATE**

**Via Dashboard:**
1. Click the "Manually Update" button on your AC Filter card
2. This sets the date to today

### Multiple AC Filters

To track multiple filters (e.g., upstairs, downstairs), repeat Steps 1-5 for each filter:

1. Create additional input helpers: `ac_filter_upstairs`, `ac_filter_garage`, etc.
2. Register separate RFID tags for each location
3. Create separate automations for each tag
4. Create separate sensors for each filter
5. Add all to dashboard card

---

## Next Steps

After successful setup:

1. **Physically attach tag:** Use adhesive backing to stick tag on AC filter unit
2. **Document location:** Note where tag is located for future reference
3. **Set baseline:** Scan tag today to set initial "last changed" date
4. **Add to maintenance schedule:** Include in home maintenance routine
5. **Consider other trackable items:**
   - Water filter changes
   - HVAC maintenance
   - Smoke detector battery replacement
   - Any periodic maintenance task

---

## Related Documentation

- Template automation file: `automations/99_rfid_ac_filter_template.yaml`
- Template sensor file: `config/templates/ac_filter_days_sensor.yaml`
- Home Assistant Tags documentation: https://www.home-assistant.io/integrations/tag/
- Template sensors guide: https://www.home-assistant.io/integrations/template/

---

## Rollback Plan

If you need to remove this feature:

1. Delete automation: `RFID - AC Filter Downstairs Updated`
2. Delete helper: `input_datetime.ac_filter_downstairs`
3. Delete template sensor from `configuration.yaml`
4. Remove dashboard card
5. Unregister RFID tag (optional)

No impact on other automations or systems.

---

**Status:** Template ready for deployment
**Last Updated:** 2025-11-17
