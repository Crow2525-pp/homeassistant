# RFID Tag Fixes and Additions

## Overview
This document addresses issues with NFC/RFID tag tracking for toilet cleaning and AC filter maintenance.

---

## Issues Identified

### 1. Downstairs Toilet RFID Tag Not Working

**Problem:** Downstairs toilet shows "Never" cleaned despite having RFID tag.

**Root Cause Analysis:**
1. Tag ID might be incorrect in automation
2. Tag might not be properly initialized
3. `input_datetime.downstairs_toilet_last_cleaned` might not exist

**Current Configuration:**
- **Automation:** `automations/05c_garage_appliances.yaml` (line 1119-1178)
- **Tag ID:** `859e3818-e623-47aa-9062-d89afd44489b`
- **Entity:** `input_datetime.downstairs_toilet_last_cleaned`
- **Sensor:** `sensor.downstairs_toilet_last_cleaned_date`

### 2. Downstairs AC RFID Tag Missing

**Problem:** No RFID tag or tracking for downstairs AC filter.

**Current State:**
- No input_datetime helper
- No sensor template
- Not in maintenance dashboard
- No automation trigger

---

## Fix Plan

### Step 1: Verify Downstairs Toilet Tag ID

**Option A: Scan tag and check event log**
1. Open Home Assistant → Developer Tools → Events
2. Listen to `tag_scanned` event
3. Scan the downstairs toilet NFC tag
4. Check the `tag_id` in event data
5. Compare with automation tag ID: `859e3818-e623-47aa-9062-d89afd44489b`

**Option B: Check if tag exists in integrations**
- Settings → Integrations → Tags
- Find "Downstairs Toilet" tag
- Verify ID matches automation

**If tag ID is wrong:**
- Update automation with correct ID
- Restart Home Assistant

### Step 2: Verify input_datetime Entity Exists

**Check if entity exists:**
1. Developer Tools → States
2. Search for `input_datetime.downstairs_toilet_last_cleaned`
3. If missing, create it

**Create input_datetime helper (if missing):**

Settings → Devices & Services → Helpers → Create Helper

OR add to configuration:

```yaml
# configuration.yaml or config/domains/input_datetime.yaml
input_datetime:
  downstairs_toilet_last_cleaned:
    name: Downstairs Toilet Last Cleaned
    has_date: true
    has_time: true
    icon: mdi:toilet
```

**Restart Home Assistant after adding**

### Step 3: Initialize Toilet Cleaning Date

**Manual initialization:**
1. Developer Tools → Services
2. Service: `input_datetime.set_datetime`
3. Entity: `input_datetime.downstairs_toilet_last_cleaned`
4. Data:
   ```yaml
   timestamp: {{ now().timestamp() }}
   ```
5. Call service

OR scan the NFC tag to set current date

### Step 4: Test Downstairs Toilet Tag

1. Scan NFC tag
2. Check notification appears
3. Verify `sensor.downstairs_toilet_last_cleaned_date` updates
4. Check maintenance dashboard shows correct date

---

## Adding Downstairs AC Filter Tracking

### Required Components

1. **input_datetime helper** - Stores last changed date
2. **Template sensor** - Displays formatted date
3. **NFC tag** - Physical tag to scan
4. **Automation** - Updates date when tag scanned
5. **Dashboard card** - Shows status

### Implementation Steps

#### 1. Create input_datetime Helper

**Add to configuration.yaml or create via UI:**

```yaml
input_datetime:
  ac_filter_downstairs:
    name: Downstairs AC Filter Last Changed
    has_date: true
    has_time: true
    icon: mdi:air-filter
```

#### 2. Create Template Sensor

**Add to config/domains/templates.yaml (around line 1670):**

```yaml
# Add after existing AC filter sensors

- name: "Downstairs AC Filter Last Changed Date"
  unique_id: downstairs_ac_filter_last_changed_date
  state: >-
    {{ states('input_datetime.ac_filter_downstairs') | as_datetime | as_local | string | regex_replace(' .*', '') if states('input_datetime.ac_filter_downstairs') not in ['unknown', 'unavailable'] else 'Never' }}
  icon: mdi:air-filter
```

#### 3. Register New NFC Tag

**Physical setup:**
1. Purchase NFC tag (NTAG213/215/216)
2. Write unique identifier using NFC Tools app
3. Attach to downstairs AC unit or filter compartment

**Register in Home Assistant:**
1. Settings → Tags
2. Create new tag
3. Name: "Downstairs AC Filter"
4. Scan tag to register ID
5. Note the tag ID for automation

#### 4. Update Automation

**Add trigger to existing maintenance automation:**

Edit `automations/05c_garage_appliances.yaml` (line ~1119):

```yaml
- id: '1742615433146'
  alias: Maintenance - Update Cleaning Timestamp via NFC
  description: Records the last-cleaned timestamps when maintenance NFC tags are scanned.
  triggers:
  - tag_id: 859e3818-e623-47aa-9062-d89afd44489b
    id: downstairs_toilet
    trigger: tag
  - tag_id: 14544260-abc9-4e84-be5b-20b3df57978d
    id: masterbed_toilet
    trigger: tag
  - tag_id: 0dba78a1-9dd0-439b-9d5b-386fa0f5df85
    id: omas_toilet
    trigger: tag
  - tag_id: [kids toilet tag ID]
    id: kids_toilet
    trigger: tag
  - tag_id: [NEW DOWNSTAIRS AC TAG ID]  # Add this
    id: downstairs_ac
    trigger: tag
  actions:
    - choose:
        # ... existing toilet choices ...

        # Add this new choice
        - conditions:
            - condition: template
              value_template: '{{ trigger.id == ''downstairs_ac'' }}'
          sequence:
            - target:
                entity_id: input_datetime.ac_filter_downstairs
              data:
                timestamp: '{{ now().timestamp() }}'
              service: input_datetime.set_datetime
            - service: notify.std_information
              data:
                title: "✅ Downstairs AC Filter Changed"
                message: "Filter change recorded. Next change due in 90 days."
  mode: single
```

#### 5. Update Dashboard

**Edit `lovelace/cards/maintenance/last_times.yaml`:**

```yaml
- type: entities
  title: "❄️ AC Filter Maintenance"
  state_color: false
  entities:
    - entity: sensor.living_room_ac_filter_last_changed_date
      name: Living Room AC Filter
    - entity: sensor.master_bedroom_ac_filter_last_changed_date
      name: Master Bedroom AC Filter
    - entity: sensor.otto_s_room_ac_filter_last_changed_date
      name: Otto's Room AC Filter
    - entity: sensor.study_henry_s_room_ac_filter_last_changed_date
      name: Study/Henry's Room AC Filter
    - entity: sensor.downstairs_ac_filter_last_changed_date  # ADD THIS
      name: Downstairs AC Filter                             # ADD THIS
  card_mod:
    style: |
      ha-card {
        border-radius: 12px;
        transition: all 0.3s ease;
      }
      ha-card:hover {
        transform: translateY(-2px);
      }
```

#### 6. Add Reminder Automation (Optional)

**Create reminder when filter is due:**

```yaml
# automations/05c_garage_appliances.yaml

- id: ac_filter_downstairs_reminder
  alias: Maintenance - Downstairs AC Filter Reminder
  description: Reminds to change downstairs AC filter every 90 days
  triggers:
    - trigger: time
      at: "09:00:00"
  conditions:
    - condition: template
      value_template: >-
        {% set last = states('input_datetime.ac_filter_downstairs') %}
        {% if last in ['unknown', 'unavailable', ''] %}
          true
        {% else %}
          {{ (as_timestamp(now()) - as_timestamp(last)) / 86400 > 90 }}
        {% endif %}
  actions:
    - action: notify.std_information
      data:
        title: "🔧 Downstairs AC Filter Due"
        message: >
          Downstairs AC filter needs replacement.
          Last changed: {{ states('sensor.downstairs_ac_filter_last_changed_date') }}
          {% set last = states('input_datetime.ac_filter_downstairs') %}
          {% if last not in ['unknown', 'unavailable', ''] %}
          Days since last change: {{ ((as_timestamp(now()) - as_timestamp(last)) / 86400) | round(0) }}
          {% endif %}
  mode: single
```

---

## Testing Checklist

### Downstairs Toilet Fix

- [ ] Verify tag ID in automation matches physical tag
- [ ] Confirm `input_datetime.downstairs_toilet_last_cleaned` exists
- [ ] Initialize date to current time
- [ ] Scan tag and verify:
  - [ ] Notification appears
  - [ ] `input_datetime` updates
  - [ ] Sensor shows correct date
  - [ ] Dashboard displays new date

### Downstairs AC Addition

- [ ] Create `input_datetime.ac_filter_downstairs`
- [ ] Add template sensor
- [ ] Register NFC tag
- [ ] Update automation with new tag ID
- [ ] Update dashboard card
- [ ] Test tag scan:
  - [ ] Notification appears
  - [ ] Date updates correctly
  - [ ] Dashboard shows new entry
- [ ] Test reminder automation (optional)

---

## Troubleshooting

### Tag Scan Not Working

**Check event log:**
1. Developer Tools → Events
2. Listen to `tag_scanned`
3. Scan tag
4. Verify event appears

**If event doesn't appear:**
- Tag might not be registered
- Phone NFC might be disabled
- Tag might be faulty/not writable

**If event appears but automation doesn't trigger:**
- Check tag ID in automation matches event data
- Verify automation is enabled
- Check automation mode (should be `single`)

### Date Not Updating

**Verify entity exists:**
```bash
# Check logs for errors
ha core logs | grep "input_datetime"
```

**Common issues:**
- Entity doesn't exist (create it)
- Entity name typo in automation
- Service call failed (check logs)

### Dashboard Not Showing Date

**Verify sensor template:**
1. Developer Tools → States
2. Search for `sensor.downstairs_toilet_last_cleaned_date`
3. Check state value

**If sensor doesn't exist:**
- Check template syntax in templates.yaml
- Restart Home Assistant
- Verify input_datetime has value

### Notification Not Appearing

**Check notification service:**
```yaml
# Test notification
service: notify.std_information
data:
  title: Test
  message: This is a test
```

**If no notification:**
- Service might not be configured
- Device might not be registered
- Notification permissions might be disabled

---

## Future Improvements

### 1. Automatic Overdue Alerts

**Add to existing reminder automations:**
```yaml
conditions:
  - condition: template
    value_template: >-
      {% set last = states('input_datetime.downstairs_toilet_last_cleaned') %}
      {% if last in ['unknown', 'unavailable', ''] %}
        false
      {% else %}
        {{ (as_timestamp(now()) - as_timestamp(last)) / 86400 > 14 }}
      {% endif %}
```

### 2. Dashboard Visual Indicators

**Color-code by due date:**
```yaml
card_mod:
  style: |
    :host {
      {% set last = states('input_datetime.downstairs_toilet_last_cleaned') %}
      {% if last not in ['unknown', 'unavailable', ''] %}
        {% set days = (as_timestamp(now()) - as_timestamp(last)) / 86400 %}
        {% if days > 14 %}
          --card-background-color: rgba(239, 68, 68, 0.2);
        {% elif days > 10 %}
          --card-background-color: rgba(234, 179, 8, 0.2);
        {% endif %}
      {% endif %}
    }
```

### 3. Maintenance History

**Track history in sensors:**
```yaml
sensor:
  - platform: history_stats
    name: Downstairs Toilet Cleanings This Month
    entity_id: input_datetime.downstairs_toilet_last_cleaned
    state: "on"
    type: count
    start: "{{ now().replace(day=1, hour=0, minute=0, second=0) }}"
    end: "{{ now() }}"
```

---

## Quick Reference

### Create NFC Tag Automation

```yaml
- id: unique_id_here
  alias: "Maintenance - [Task] via NFC"
  triggers:
    - tag_id: your-tag-id-here
      id: task_name
      trigger: tag
  actions:
    - target:
        entity_id: input_datetime.task_last_done
      data:
        timestamp: '{{ now().timestamp() }}'
      service: input_datetime.set_datetime
    - service: notify.std_information
      data:
        title: "✅ [Task] Complete"
        message: "Recorded at {{ now().strftime('%H:%M on %d/%m/%Y') }}"
  mode: single
```

### Test Tag Scan

```bash
# Listen for tag events
# Developer Tools → Events → Listen to 'tag_scanned'

# Scan tag and check:
{
  "event_type": "tag_scanned",
  "data": {
    "tag_id": "your-tag-id-here",
    "device_id": "your-device-id"
  }
}
```

---

**Created:** 2025-11-16
**Status:** Ready for implementation
**Testing Required:** Yes - Both fixes need physical tag scanning
