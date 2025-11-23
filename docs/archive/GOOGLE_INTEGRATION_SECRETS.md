# Google Integration Secrets Reference

## Overview
Google credentials stored in `secrets.yaml` for Google Assistant, Calendar, and other Google Cloud integrations.

---

## Secrets Added

```yaml
# In secrets.yaml
google_project_id: "your-google-project-id"
google_client_id: "your-google-oauth-client-id.apps.googleusercontent.com"
google_client_secret: "your-google-oauth-client-secret"
```

---

## How These Are Used

### Current Setup (UI-Configured)

Your Google integrations are configured through the Home Assistant UI, not YAML. The credentials are stored in:
- `.storage/google.*` files
- Configured via Settings → Integrations → Google Assistant

**No YAML changes needed** - Your existing configuration already works!

### When to Use secrets.yaml References

If you ever need to add Google integrations via YAML (rare), you can reference these:

```yaml
# Example: Google Calendar (if configuring via YAML)
google:
  client_id: !secret google_client_id
  client_secret: !secret google_client_secret

# Example: Google Assistant SDK
google_assistant:
  project_id: !secret google_project_id
  client_id: !secret google_client_id
  client_secret: !secret google_client_secret
```

---

## Current Google Integrations

Based on `.storage/google.*` file presence, you have Google services configured via UI:
- ✅ Google Assistant / Cloud integration
- ✅ Likely Google Calendar
- ✅ Voice control integration

**Configuration location:** Settings → Integrations → Google

---

## Security Notes

### Protected in secrets.yaml

✅ **Client ID** - OAuth application identifier
✅ **Client Secret** - OAuth application secret
✅ **Project ID** - Google Cloud project identifier

### Already Gitignored

- `secrets.yaml` - Contains real credentials (protected)
- `.storage/` - Contains OAuth tokens (already in .gitignore)

### Rotation

If you need to rotate Google credentials:

1. **Generate new credentials** in Google Cloud Console
2. **Update secrets.yaml:**
   ```yaml
   google_client_id: "new_client_id"
   google_client_secret: "new_client_secret"
   ```
3. **Reconfigure integration:**
   - Settings → Integrations → Google
   - Remove and re-add integration
   - Or use "Reauthenticate" option

---

## Google Cloud Console

Your Google Cloud project: `home-assistant-456223`

**Console URL:** https://console.cloud.google.com/

**To manage credentials:**
1. Go to Google Cloud Console
2. Select project: `home-assistant-456223`
3. APIs & Services → Credentials
4. Find OAuth 2.0 Client ID: `906948335191-...`

---

## Troubleshooting

### "Invalid client" error

**Cause:** Client ID or secret incorrect

**Fix:**
1. Verify credentials in Google Cloud Console
2. Update `secrets.yaml` with correct values
3. Remove and re-add Google integration in HA

### "Project not found" error

**Cause:** Project ID incorrect or project doesn't exist

**Fix:**
1. Check project ID in Google Cloud Console
2. Update `google_project_id` in `secrets.yaml`
3. Ensure project has required APIs enabled:
   - Google Assistant API
   - Calendar API (if using calendar)
   - HomeGraph API

### OAuth redirect URI mismatch

**Fix:**
1. Go to Google Cloud Console → Credentials
2. Edit OAuth 2.0 Client ID
3. Add authorized redirect URI:
   - `https://hass.pspatt.net/auth/external/callback`
   - `https://hass.pspatt.net/auth/google/callback`

---

## Best Practices

### Keep Credentials Secure

- ✅ Store in `secrets.yaml` (gitignored)
- ✅ Never commit to git
- ✅ Use secrets.yaml.example for templates
- ❌ Don't share in screenshots/logs

### Regular Rotation

- Rotate every 6-12 months
- Immediately if compromised
- Document rotation date

### Backup OAuth Tokens

OAuth tokens are stored in `.storage/` and should be backed up:
- Include in full HA backups
- Keep `.storage/` in version control (optional)

---

## References

**Google Cloud Console:** https://console.cloud.google.com/
**HA Google Integration:** https://www.home-assistant.io/integrations/google_assistant/
**OAuth Setup Guide:** https://developers.google.com/assistant/smarthome/develop/project-setup

---

**Created:** 2025-11-16
**Project:** home-assistant-456223
**Status:** Credentials stored in secrets.yaml ✅
