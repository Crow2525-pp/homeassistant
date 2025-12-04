# Backup Automation Error Fixes

## Issue Summary

Two backup automations were reporting "unknown action" errors:

1. **"System - Daily Backup (3 AM)"** - Error: `backup.create` action unknown
2. **"System - Backup to NAS"** - Error: `shell_command.backup_to_nas` action unknown

## Root Causes

### Issue 1: backup.create action
- **Problem**: The automation was attempting to use `backup.create` service which is not widely available
- **Cause**: Confusion between old and new Home Assistant backup service names
- **Solution**: Use `hassio.backup_full` instead (works across all HA versions)

### Issue 2: shell_command.backup_to_nas action
- **Problem**: The shell command `backup_to_nas` doesn't exist in the configuration
- **Cause**: Shell command was never properly configured or defined
- **Solution**: Either properly define the shell command or use native Home Assistant services

## Fixes Applied

### Fix 1: Daily Backup Template Updated
File: `automations/99_daily_backup_template.yaml`

**Changes:**
- Explicitly documented to use `hassio.backup_full` ONLY
- Removed confusing note about `backup.create`
- Added warning comment to prevent future mistakes
- Clarified that this service works across all HA versions

**Correct Service:**
```yaml
- service: hassio.backup_full
  data:
    name: "Auto Backup {{ now().strftime('%Y-%m-%d') }}"
```

**Incorrect (DO NOT USE):**
```yaml
- service: backup.create  # ← WILL CAUSE ERRORS
```

### Fix 2: NAS Backup Automation
The "System - Backup to NAS" automation requires a properly configured shell command.

**Options:**
1. **Define the shell command** in `configuration.yaml`:
```yaml
shell_command:
  backup_to_nas: "rsync -av /backup /nas/backup/"  # Customize command
```

2. **Use native services instead:**
```yaml
# For SMB/Samba shares
- service: shell_command.exec
  data:
    command: "cp /path/to/backup /path/to/nas/backup"
```

3. **Comment out/disable** if not needed

## Prevention

To avoid these errors in the future:

1. **Always verify service names exist** before using them
   - Check: Developer Tools > Services in Home Assistant UI
   - Search for "backup" to see available services

2. **For daily backups:** Use the corrected template
   - File: `automations/99_daily_backup_template.yaml`
   - Service: `hassio.backup_full` (verified compatible)

3. **For NAS backups:** Define shell_command first
   - Add to `configuration.yaml` under `shell_command:` section
   - Test command manually before using in automation

## Testing

To verify the fix works:

1. Check Home Assistant logs for backup-related errors
2. Verify automation shows no validation errors
3. Run automation manually (Developer Tools > Automations)
4. Confirm backup completes successfully
5. Check Settings > System > Backups for new backup files

## References

- [Home Assistant Backup Service Documentation](https://www.home-assistant.io/docs/backup/)
- [Supervisor Backup API](https://developers.home-assistant.io/docs/supervisor_api/)
- [Shell Command Integration](https://www.home-assistant.io/integrations/shell_command/)
