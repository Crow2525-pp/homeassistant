# Automated Backup Setup Guide

**Created:** 2025-11-17
**Purpose:** Set up automated daily backups for Home Assistant
**Complexity:** Low (15-20 minutes)
**Category:** System Maintenance

---

## Overview

This guide sets up automated daily backups of your Home Assistant configuration at 3:00 AM, with success/failure notifications and optional off-site backup storage.

**Benefits:**
- Automatic daily backups without manual intervention
- Notifications if backup fails
- Protection against configuration corruption
- Easy restoration if changes break your system
- Optional off-site storage for disaster recovery

**How it works:**
1. Automation triggers at 3:00 AM daily
2. Calls Home Assistant backup service
3. Sends notification on success or failure
4. (Optional) Uploads backup to cloud storage or NAS

---

## Prerequisites

- Home Assistant 2024.9 or newer (`backup.create` service)
- Sufficient disk space for backups (2-5 GB recommended)
- Notification service configured (persistent, mobile app, or email)
- (Optional) Cloud storage integration for off-site backup

**Estimated Time:** 15-20 minutes

---

## Step 1: Verify Backup Service Available

Check if `backup.create` service exists:

1. Go to **Developer Tools** > **Services**
2. Search for `backup.create`
3. If found: Home Assistant 2024.9+ - continue
4. If not found: Update Home Assistant or use legacy backup method

---

## Step 2: Create Daily Backup Automation

Copy the template automation from `automations/99_daily_backup_template.yaml` or create via UI:

### Via Home Assistant UI

1. Navigate to **Settings** > **Automations & Scenes**
2. Click **+ CREATE AUTOMATION**
3. Choose **Create new automation**

**Trigger:**
- Trigger type: **Time**
- At: `03:00:00`

**Conditions:**
- (Optional) Add condition to skip on specific days or when maintenance mode is active

**Actions:**

1. **Action 1:** Create backup
   - Action type: **Call service**
   - Service: `backup.create`
   - Service data: (leave empty for default)

2. **Action 2:** Notify on success
   - Action type: **Call service**
   - Service: `notify.persistent_notification`
   - Service data:
     ```yaml
     title: "Backup Successful"
     message: "Daily backup completed at {{ now().strftime('%H:%M on %B %d, %Y') }}"
     ```

**Details:**
- Name: `System - Daily Backup (3 AM)`
- Mode: `single`

### Via YAML (Recommended)

See `automations/99_daily_backup_template.yaml` for full template.

---

## Step 3: Create Backup Status Sensor

Track last backup time and calculate days since backup:

Add to `configuration.yaml`:

```yaml
template:
  - sensor:
      - name: "Last Backup Time"
        unique_id: last_backup_time
        state: "{{ state_attr('sensor.backup_state', 'last_backup') | default('unknown') }}"
        device_class: timestamp

      - name: "Days Since Last Backup"
        unique_id: days_since_last_backup
        state: >
          {% set last_backup = state_attr('sensor.backup_state', 'last_backup') %}
          {% if last_backup %}
            {{ (now() - (last_backup | as_datetime)).days }}
          {% else %}
            unknown
          {% endif %}
        unit_of_measurement: "days"
```

Or use the template file: `config/templates/backup_status_sensor.yaml`

---

## Step 4: Test Backup Automation

### Manual Test

1. Go to **Settings** > **Automations & Scenes**
2. Find `System - Daily Backup (3 AM)`
3. Click **⋮** (menu) > **Run**
4. Wait for backup to complete (30 seconds - 2 minutes)
5. Verify notification appears
6. Check backup exists: **Settings** > **System** > **Backups**

### Verify Backup Created

1. Navigate to **Settings** > **System** > **Backups**
2. Verify new backup appears with today's date
3. Check backup size is reasonable (typically 50-500 MB)
4. (Optional) Download backup to verify it's not corrupted

---

## Step 5: (Optional) Set Up Off-site Backup

### Option A: Google Drive Backup Add-on

1. Install **Google Drive Backup** add-on:
   - **Settings** > **Add-ons** > **Add-on Store**
   - Search for "Home Assistant Google Drive Backup"
   - Click **INSTALL**

2. Configure Google Drive Backup:
   - Open add-on configuration
   - Authenticate with Google account
   - Set upload schedule: `3:30 AM` (30 minutes after local backup)
   - Set retention: `7 daily, 4 weekly, 12 monthly`

3. Test upload:
   - Click **Upload** in add-on UI
   - Verify backup appears in Google Drive

### Option B: NAS/Samba Backup

Use the template automation `automations/99_offsite_backup_template.yaml`:

1. Ensure Samba Share integration is configured
2. Mount network share in Home Assistant
3. Create automation to copy backup file to NAS

**Example:**
```yaml
- id: backup_to_nas
  alias: "System - Backup to NAS"
  trigger:
    - platform: time
      at: "03:30:00"
  action:
    - service: shell_command.backup_to_nas
```

Define shell command in `configuration.yaml`:
```yaml
shell_command:
  backup_to_nas: "cp /backup/*.tar /media/nas/ha_backups/"
```

### Option C: Dropbox, OneDrive, or Other Cloud

1. Install appropriate add-on or integration
2. Configure authentication
3. Create automation similar to Google Drive example
4. Test upload and restore

---

## Step 6: Configure Backup Retention

### Via Google Drive Backup Add-on

- **Daily backups:** Keep 7
- **Weekly backups:** Keep 4
- **Monthly backups:** Keep 12
- **Total storage:** ~15-20 backups

### Manual Cleanup

Create automation to delete old local backups:

```yaml
- id: cleanup_old_backups
  alias: "System - Cleanup Old Backups"
  trigger:
    - platform: time
      at: "04:00:00"
  action:
    - service: backup.remove
      data:
        keep_days: 7  # Keep only last 7 days locally
```

---

## Step 7: Add Dashboard Monitoring

Add backup status to your dashboard:

```yaml
type: entities
title: Backup Status
entities:
  - entity: sensor.last_backup_time
    name: Last Backup
    icon: mdi:backup-restore
  - entity: sensor.days_since_last_backup
    name: Days Since Backup
    icon: mdi:calendar-clock
  - type: button
    name: Create Backup Now
    icon: mdi:backup-restore
    tap_action:
      action: call-service
      service: backup.create
      service_data: {}
show_header_toggle: false
```

---

## Troubleshooting

### Backup Fails with "Insufficient Disk Space"

**Solution:**
1. Check available disk space: **Settings** > **System** > **Storage**
2. Delete old backups manually
3. Enable automatic cleanup (see Step 6)
4. Consider moving backups to external storage

### No Notification Received

**Solution:**
1. Check automation executed: **Settings** > **Automations** > View traces
2. Verify notification service is configured correctly
3. Test notification service manually from Developer Tools
4. Check Home Assistant logs for errors

### Backup Created But Empty/Corrupted

**Solution:**
1. Verify sufficient disk space during backup
2. Check for file system errors
3. Test backup restore in development environment
4. Consider switching to different storage location

---

## Maintenance

### Weekly
- [ ] Verify last backup completed successfully
- [ ] Check backup file size is reasonable

### Monthly
- [ ] Test restore process with a backup
- [ ] Verify off-site backups uploading correctly
- [ ] Clean up old backups if retention policy not automated

### Quarterly
- [ ] Perform full restore test in development environment
- [ ] Verify backup includes all critical data
- [ ] Review and update retention policy

---

## Related Documentation

- Template automation: `automations/99_daily_backup_template.yaml`
- Off-site backup template: `automations/99_offsite_backup_template.yaml`
- Backup status sensors: `config/templates/backup_status_sensor.yaml`
- Home Assistant Backup docs: https://www.home-assistant.io/integrations/backup/

---

**Status:** Template ready for deployment
**Last Updated:** 2025-11-17
