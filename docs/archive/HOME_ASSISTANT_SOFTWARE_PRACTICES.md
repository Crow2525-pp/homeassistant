# Home Assistant Software Development Best Practices

## Overview
This guide establishes professional software development practices for your Home Assistant deployment, ensuring maintainability, reliability, and ease of collaboration.

---

## 1. Version Control & Git Workflow

### Current Git Setup
✅ Already using Git
✅ Regular commits with descriptive messages
⚠️ Needs: Structured branching strategy

### Recommended Git Workflow

#### Branching Strategy

```
master (main)
  ├─ development
  │   ├─ feature/morning-automation-improvements
  │   ├─ feature/new-climate-sensors
  │   └─ fix/blind-position-tracking
  └─ hotfix/critical-automation-bug
```

**Branch Types:**
- `master` - Production-ready, stable code (currently deployed)
- `development` - Integration branch for testing
- `feature/*` - New features or enhancements
- `fix/*` - Bug fixes
- `hotfix/*` - Critical fixes that bypass development

**Workflow:**
1. Create feature branch from `development`
2. Make changes and test thoroughly
3. Merge to `development` for integration testing
4. After validation, merge to `master`
5. Deploy from `master` only

#### Commit Message Convention

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `refactor` - Code restructuring
- `docs` - Documentation only
- `chore` - Maintenance (updates, cleanup)
- `test` - Adding tests or test automation

**Examples:**
```bash
feat(climate): add morning pre-heating for living room

- Triggers at 5:30 AM on cold days
- Uses 18°C threshold
- Prevents auto-shutdown until 8:00 AM

Fixes #23
```

```bash
fix(blind): correct position drift in roller blind tracking

The position calculation was accumulating errors over time.
Simplified to three-state system (open/partial/closed).

Closes #45
```

```bash
refactor(scripts): consolidate media player scripts

- Merged spotify_tv and play_music logic
- Created reusable Spotify source selection
- Updated 3 dashboard buttons to use new scripts
```

### .gitignore Best Practices

**Current .gitignore should include:**
```gitignore
# Secrets - CRITICAL
secrets.yaml
*.db
*.db-shm
*.db-wal

# User-specific
.storage/auth*
.storage/onboarding
.storage/person_*

# System files
.DS_Store
Thumbs.db
*.log
*.pid

# Backups
*.backup
*_backup/
*.bak

# IDE
.vscode/
.idea/
*.swp

# Keep these for backup (recommended)
# .storage/lovelace
# .storage/lovelace.*

# Python
__pycache__/
*.pyc

# Home Assistant specific
home-assistant_v2.db*
home-assistant.log*
OZW_Log.txt
```

**What to KEEP in git:**
- ✅ All YAML configuration files
- ✅ `.storage/lovelace` (dashboard config)
- ✅ Custom components
- ✅ Themes
- ✅ WWW assets
- ✅ Documentation

**What to EXCLUDE:**
- ❌ secrets.yaml (use secrets.yaml.example instead)
- ❌ Database files
- ❌ Auth tokens/storage
- ❌ Log files

---

## 2. Configuration Management

### File Organization

**Current structure is good! Improvements:**

```
config/
├── configuration.yaml          # Main config (keep minimal)
├── automations.yaml           # Remove (replaced by folder)
├── secrets.yaml.example       # ADD: Template for secrets
├── domains/                   # Component configs
│   ├── scripts.yaml
│   ├── templates.yaml
│   ├── climate.yaml
│   └── [component].yaml
├── automations/               # Organized by function
│   ├── 01_occupancy.yaml
│   ├── 02_security_alarmo.yaml
│   ├── 03_climate_control_core.yaml
│   ├── 04_climate_flags_and_notifications.yaml
│   ├── 05a_lighting.yaml
│   ├── 05b_blinds_shades.yaml
│   ├── 05c_garage_appliances.yaml
│   ├── 06_living_room_climate_split.yaml
│   ├── 07_study_climate_manager.yaml
│   ├── 08_kids_room_climate_manager.yaml
│   └── 09_miscellaneous.yaml
└── lovelace/
    ├── views/
    ├── cards/
    ├── badges/
    └── config/
```

**Naming Conventions:**
- Prefix numbers for load order (01_, 02_, etc.)
- Use descriptive names (`climate_control` not `cc`)
- Group related automations in same file
- Max 500 lines per file (split if larger)

### Secrets Management

**Create `secrets.yaml.example`:**
```yaml
# Example secrets file - Copy to secrets.yaml and fill in real values

# Wi-Fi
wifi_ssid: "YourNetworkName"
wifi_password: "your_password_here"

# Home Assistant
http_base_url: "https://yourdomain.com"

# API Keys
weather_api_key: "your_api_key_here"
spotify_client_id: "your_client_id"
spotify_client_secret: "your_client_secret"

# Notifications
mobile_app_phil: "mobile_app_device_name"
mobile_app_steph: "mobile_app_device_name"

# Geographic
latitude: !secret home_latitude
longitude: !secret home_longitude

# Integrations
# Add your integration secrets here
```

**Usage in configs:**
```yaml
# Instead of hardcoding:
notify:
  - name: Phil
    platform: mobile_app
    target: mobile_app_samsung_galaxy_s22_ultra  # BAD

# Use secrets:
notify:
  - name: Phil
    platform: mobile_app
    target: !secret mobile_app_phil  # GOOD
```

---

## 3. Testing & Validation

### Pre-Deployment Checklist

**Before every commit:**
```bash
# 1. Check configuration
cd /config
ha core check

# 2. Validate YAML syntax
yamllint configuration.yaml
yamllint automations/*.yaml

# 3. Check for secrets exposure
grep -r "password\|token\|api_key" --exclude-dir=.git .

# 4. Review changed files
git status
git diff

# 5. Test in development first (if available)
```

### Automation Testing

**Test new automations:**
1. **Manual trigger test:**
   - Go to Developer Tools → Services
   - Call `automation.trigger` with your automation ID
   - Verify expected behavior

2. **Condition testing:**
   - Go to Developer Tools → Template
   - Test template conditions
   - Verify logic is correct

3. **Integration test:**
   - Wait for natural trigger
   - Monitor logs: Settings → System → Logs
   - Check automation trace: Settings → Automations → [automation] → Traces

**Example test plan template:**
```markdown
## Automation Test Plan: Living Room Morning Heat

### Test Cases
1. **Normal trigger (5:30 AM, temp < 18°C)**
   - [ ] Automation triggers at 5:30 AM
   - [ ] Climate turns on to comfort mode
   - [ ] Heating continues until 8:00 AM
   - [ ] No auto-shutdown during 5:30-8:00 window

2. **Temperature already warm**
   - [ ] Automation doesn't trigger if temp > 18°C
   - [ ] No unnecessary heating

3. **Manual override**
   - [ ] Respects manual_control flag
   - [ ] Doesn't interfere with user changes

4. **Edge cases**
   - [ ] Works on first day of winter season change
   - [ ] Handles HA restart during heating
   - [ ] Correct behavior if occupancy changes
```

### YAML Linting

**Install yamllint:**
```bash
pip install yamllint
```

**Create `.yamllint` config:**
```yaml
extends: default

rules:
  line-length:
    max: 120
    level: warning
  indentation:
    spaces: 2
  comments:
    min-spaces-from-content: 1
```

**Run linting:**
```bash
yamllint configuration.yaml
yamllint automations/
yamllint lovelace/
```

---

## 4. Documentation Standards

### Code Documentation

**Automation documentation:**
```yaml
- id: living_room_morning_heat_winter
  alias: "Living Room - Morning Heat (Winter)"
  description: |
    Warms living room during morning hours (5:30-8:00) in winter season.

    Behavior:
    - Triggers at 5:30 AM or when temp drops below 18°C
    - Uses comfort preset for optimal warmth
    - Disabled auto-shutdown during morning hours
    - Respects manual control and occupancy settings

    Updated: 2025-01-16
    Reason: Increased temp threshold from 17°C to 18°C for better comfort
  triggers:
    # ... triggers
```

**Script documentation:**
```yaml
play_music:
  alias: Play Music
  description: |
    Resumes Spotify playback on WiiM Amp.

    Process:
    1. Checks if WiiM Amp is in Spotify source list
    2. Selects WiiM Amp as active Spotify device
    3. Resumes playback (continues last track/playlist)

    Dependencies:
    - media_player.spotify_philip_patterson
    - media_player.living_room_wiimamp

    Used by:
    - Dashboard: Control Panel → Play Music button
    - Voice: "Hey Google, play music"
  sequence:
    # ... sequence
```

### Documentation Files

**Required documentation:**

1. **README.md** (Project overview)
```markdown
# Home Assistant Configuration

Smart home automation for Patterson residence.

## Quick Links
- [Setup Guide](docs/SETUP.md)
- [Automation Guide](docs/AUTOMATION_GUIDE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Changelog](CHANGELOG.md)

## Key Features
- Climate automation with seasonal adjustments
- Solar excess detection for smart appliance scheduling
- NFC-based maintenance tracking
- Voice-first interaction design

## System Info
- Home Assistant version: 2024.x
- Installation: Home Assistant OS on Proxmox
- Integrations: See [integrations.md](docs/integrations.md)
```

2. **CHANGELOG.md** (Track major changes)
```markdown
# Changelog

## [Unreleased]

## [2025.01.16]
### Added
- Room selector for "Read News" function
- Morning heating improvements for living room

### Fixed
- Play Music button now correctly resumes Spotify on WiiM Amp
- HVAC auto-shutdown during morning hours

### Changed
- Cleaned up energy dashboard debugging section
- Increased living room morning heat trigger from 17°C to 18°C

## [2025.01.01]
...
```

3. **docs/** folder organization:
```
docs/
├── README.md                              # Docs index
├── SETUP.md                               # Initial setup guide
├── AUTOMATION_GUIDE.md                    # How automations work
├── TROUBLESHOOTING.md                     # Common issues
├── integrations.md                        # Integration list
├── FIXES_SUMMARY_2025.md                  # Recent fixes
├── LOVELACE_UI_MIGRATION_PLAN.md         # UI migration guide
├── WORKFLOW_OPTIMIZATION_GUIDE.md         # Workflow recommendations
├── ROLLER_BLIND_SIMPLIFICATION_PLAN.md   # Blind tracking plan
└── HOME_ASSISTANT_SOFTWARE_PRACTICES.md  # This file
```

---

## 5. Deployment & Release Process

### Development Environment

**Option 1: Separate Dev Instance (Recommended)**
- Install second HA instance on same Proxmox server
- Clone production config
- Test all changes here first
- Advantages:
  - Safe testing without affecting production
  - Can test integrations with real devices
  - Parallel environments

**Option 2: Backup & Restore Testing**
- Take snapshot before changes
- Test changes on production
- Restore if issues occur
- Simpler but riskier

### Deployment Process

**Standard deployment:**
```bash
# 1. Ensure you're on correct branch
git checkout master

# 2. Pull latest changes (if working from multiple locations)
git pull

# 3. Review what's being deployed
git log --oneline -5

# 4. Backup current state
# Settings → System → Backups → Create Backup

# 5. Check configuration validity
ha core check

# 6. Restart Home Assistant (if needed)
ha core restart

# 7. Monitor logs after restart
ha core logs -f

# 8. Test critical automations
# Developer Tools → Services → automation.trigger

# 9. Tag release
git tag -a v2025.01.16 -m "Morning heating fixes and dashboard cleanup"
git push --tags
```

**Hotfix deployment:**
```bash
# 1. Create hotfix branch from master
git checkout master
git checkout -b hotfix/critical-automation-bug

# 2. Make minimal fix
# Edit files...

# 3. Test fix
ha core check

# 4. Commit
git add .
git commit -m "hotfix: fix critical automation bug"

# 5. Merge to master
git checkout master
git merge hotfix/critical-automation-bug

# 6. Deploy (backup first!)
ha core restart

# 7. Tag and push
git tag -a v2025.01.16-hotfix.1 -m "Critical automation fix"
git push --tags
git push
```

### Rollback Procedure

**If deployment fails:**

1. **Check logs immediately:**
   ```bash
   ha core logs
   ```

2. **Restore from backup:**
   - Settings → System → Backups
   - Select pre-deployment backup
   - Click Restore

3. **OR revert git changes:**
   ```bash
   # Find commit hash before bad changes
   git log --oneline

   # Revert to that commit
   git revert <commit-hash>

   # Or hard reset (caution!)
   git reset --hard <good-commit-hash>
   git push --force

   # Restart HA
   ha core restart
   ```

---

## 6. Monitoring & Logging

### Log Management

**Enable debug logging for specific components:**
```yaml
# configuration.yaml
logger:
  default: info
  logs:
    # Debug specific integrations
    homeassistant.components.climate: debug
    homeassistant.components.automation: debug

    # Suppress noisy integrations
    homeassistant.components.mqtt: warning
    custom_components.gosungrow: warning
```

**View logs:**
```bash
# Real-time logs
ha core logs -f

# Last 50 lines
ha core logs --lines 50

# Search for errors
ha core logs | grep ERROR

# Filter by component
ha core logs | grep climate
```

### Automation Debugging

**Add logging to automations:**
```yaml
actions:
  - service: system_log.write
    data:
      message: "Living room heating triggered: temp={{ states('sensor.living_room_temperature_offset') }}"
      level: info
      logger: homeassistant.automation.living_room_morning_heat
```

**Use automation traces:**
- Settings → Automations → [Select automation]
- Click "Traces" tab
- View step-by-step execution
- See which conditions passed/failed

---

## 7. Backup Strategy

### Automated Backups

**Schedule regular backups:**
```yaml
# automations/backup.yaml
- id: daily_backup
  alias: "System - Daily Backup"
  description: "Creates daily backup at 3:00 AM"
  trigger:
    - platform: time
      at: "03:00:00"
  action:
    - service: hassio.backup_full
      data:
        name: "Auto Backup {{ now().strftime('%Y-%m-%d') }}"
    - service: notify.std_information
      data:
        title: "Backup Complete"
        message: "Daily backup created successfully"
```

**Backup retention:**
- Keep daily backups for 7 days
- Keep weekly backups for 4 weeks
- Keep monthly backups for 6 months
- Store off-site (Google Drive, Nextcloud, NAS)

### Git as Backup

**Regular git commits = configuration backup:**
```bash
# Daily commit of any changes
git add -A
git commit -m "chore: daily backup $(date +%Y-%m-%d)"
git push
```

**Restore from git:**
```bash
# Clone config to fresh HA install
git clone https://github.com/yourusername/homeassistant-config.git /config

# Restore secrets.yaml manually (never committed)
cp secrets.yaml.backup /config/secrets.yaml

# Restart HA
ha core restart
```

---

## 8. Performance & Optimization

### Database Optimization

**Purge old data regularly:**
```yaml
# configuration.yaml
recorder:
  purge_keep_days: 7
  purge_interval: 1
  commit_interval: 30

  # Exclude noisy sensors
  exclude:
    domains:
      - automation
      - updater
    entity_globs:
      - sensor.*_last_seen
    entities:
      - sun.sun
      - sensor.date
      - sensor.time
```

**Use InfluxDB for long-term data:**
```yaml
influxdb:
  host: localhost
  port: 8086
  database: homeassistant
  username: !secret influxdb_user
  password: !secret influxdb_password
  max_retries: 3
  default_measurement: state
```

### Automation Optimization

**Use mode correctly:**
```yaml
- id: example_automation
  mode: restart  # Stop and restart if triggered again
  # OR
  mode: single   # Ignore new triggers while running
  # OR
  mode: queued   # Queue triggers, run sequentially
  # OR
  mode: parallel # Allow multiple concurrent runs
```

**Avoid polling when possible:**
```yaml
# BAD - Polls every 60 seconds
- trigger:
    - platform: time_pattern
      seconds: "/60"

# GOOD - Triggers on state change
- trigger:
    - platform: state
      entity_id: sensor.temperature
```

---

## 9. Security Best Practices

### Access Control

**Use strong authentication:**
- Enable two-factor authentication
- Use long, unique passwords
- Create separate users for family members
- Limit access by user (visibility conditions)

**Network security:**
- Use HTTPS (SSL certificate)
- Firewall rules (only allow necessary ports)
- VPN for remote access
- Disable unnecessary integrations

### Secrets Protection

**Never commit secrets:**
```bash
# Check for leaked secrets before commit
git add -A
git diff --cached | grep -i "password\|token\|api_key"

# If found:
git reset  # Unstage changes
# Move secrets to secrets.yaml
```

**Rotate secrets regularly:**
- API keys: Every 6-12 months
- Passwords: Every 3-6 months
- Access tokens: When compromised

---

## 10. Collaboration & Team Workflow

### Code Review Process

**Pull Request template:**
```markdown
## Description
Brief description of changes

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Passed `ha core check`
- [ ] Tested manually
- [ ] No errors in logs
- [ ] Automations work as expected

## Checklist
- [ ] Code follows naming conventions
- [ ] Documentation updated
- [ ] Secrets not exposed
- [ ] CHANGELOG.md updated
```

### Issue Tracking

**Use GitHub Issues for:**
- Bug reports
- Feature requests
- Improvement ideas
- Questions

**Issue template:**
```markdown
**Bug Report**
**Description:** Brief description
**Expected behavior:** What should happen
**Actual behavior:** What actually happens
**Steps to reproduce:**
1. Step one
2. Step two
**Logs:** Paste relevant logs
**Version:** HA version number
```

---

## 11. Continuous Integration (Optional)

### GitHub Actions Workflow

**Automate testing:**
```yaml
# .github/workflows/ha-check.yml
name: Home Assistant Config Check

on:
  push:
    branches: [ master, development ]
  pull_request:
    branches: [ master ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Home Assistant Config Check
        uses: frenck/action-home-assistant@v1
        with:
          path: "."
          secrets: secrets.yaml.example
```

---

## 12. Migration & Disaster Recovery

### Full System Migration Plan

**Backup everything:**
1. Home Assistant full backup (Settings → System → Backups)
2. Git push all configuration
3. Export integration configs
4. Document custom components
5. List all add-ons

**Restore on new system:**
1. Install Home Assistant
2. Clone git repository
3. Restore secrets.yaml
4. Restore full backup
5. Reinstall custom components
6. Verify all integrations

---

## Summary: Quick Reference

### Daily Workflow
```bash
# 1. Pull latest changes
git pull

# 2. Make changes
# Edit files...

# 3. Test changes
ha core check

# 4. Commit
git add .
git commit -m "feat(climate): add evening cooling automation"
git push

# 5. Deploy
ha core restart
```

### Monthly Tasks
- [ ] Review and clean up automations
- [ ] Update documentation
- [ ] Check for Home Assistant updates
- [ ] Review logs for errors
- [ ] Test backup restoration
- [ ] Rotate secrets (quarterly)

### Best Practices Checklist
- [ ] Use git for all configuration changes
- [ ] Test in development before production
- [ ] Keep secrets in secrets.yaml
- [ ] Document complex automations
- [ ] Use descriptive commit messages
- [ ] Take backup before major changes
- [ ] Monitor logs after deployments
- [ ] Tag releases
- [ ] Update CHANGELOG.md

---

**Created:** 2025-11-16
**Status:** Living document - update as practices evolve
**Next Review:** 2025-02-16
