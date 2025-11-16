# Dashboard Migration: YAML to UI Mode

## Overview

Migrate your Lovelace dashboard from YAML mode (`ui-lovelace.yaml`) to UI mode while preserving your existing configuration as a backup.

**Current Setup:**
- YAML mode with `ui-lovelace.yaml`
- 63 card files in `lovelace/` directory
- 9 views defined in YAML

**Goal:**
- UI mode for easy editing via Home Assistant interface
- Keep YAML files as backup/reference
- Maintain all current functionality

---

## Migration Strategy

### **Recommended Approach: Gradual Migration**

Instead of migrating everything at once, migrate one view at a time while keeping backups.

**Benefits:**
- ✅ Low risk - can revert at any time
- ✅ Test each view before moving to the next
- ✅ Keep YAML as documentation
- ✅ Learn UI editor gradually

---

## Step-by-Step Migration Plan

### **Phase 0: Preparation (15 minutes)**

#### 1. Backup Current Configuration

```bash
# Create backup directory
mkdir -p backups/lovelace-$(date +%Y%m%d)

# Backup entire lovelace directory
cp -r lovelace/ backups/lovelace-$(date +%Y%m%d)/
cp ui-lovelace.yaml backups/lovelace-$(date +%Y%m%d)/
```

#### 2. Document Current State

```bash
# Take screenshots of each view
# - Settings → Dashboards → Home Dashboard
# - Screenshot each view for reference
```

#### 3. Enable UI Mode

**Option A: Fresh Start (Recommended)**
1. Rename `ui-lovelace.yaml` to `ui-lovelace.yaml.backup`
2. Restart Home Assistant
3. HA will automatically create UI mode dashboard
4. You'll manually recreate views using the UI

**Option B: Import YAML Configuration**
1. Keep `ui-lovelace.yaml` as-is temporarily
2. Manually copy configuration to UI mode
3. Once complete, rename YAML file

**We'll use Option A for clean migration.**

---

### **Phase 1: Setup UI Mode (30 minutes)**

#### Step 1: Switch to UI Mode

```bash
# Rename YAML config
cd /config
mv ui-lovelace.yaml ui-lovelace.yaml.backup
```

#### Step 2: Restart Home Assistant

- Settings → System → Restart Home Assistant
- Wait for restart to complete

#### Step 3: Access UI Editor

- Navigate to your dashboard
- Click three-dot menu (top right) → "Edit Dashboard"
- You're now in UI mode!

---

### **Phase 2: Migrate Views (One at a Time)**

Migrate in this order (simplest to most complex):

1. ✅ **Control Panel** (main view with quick actions)
2. ✅ **Alarm** (security/cameras)
3. ✅ **Energy** (solar/consumption)
4. ✅ **Calendar** (schedules/presence)
5. ✅ **Climate** (HVAC/temperature)
6. ✅ **Network** (servers/services)
7. ✅ **Laundry** (appliances)
8. ✅ **Maintenance** (tasks/tracking)
9. ✅ **Media** (Sonarr/media players)

**For each view:**

#### Step 1: Create View in UI

1. Click "Edit Dashboard"
2. Click "+ Add View" tab
3. Set view details:
   - Title: (from YAML)
   - Icon: (from YAML)
   - Path: (from YAML)
   - Type: Usually "Panel" or "Sections"

#### Step 2: Add Cards One-by-One

**Method A: Manual Recreation (Recommended)**
- Click "+ Add Card"
- Select card type
- Configure using YAML file as reference
- Much cleaner - skip card_mod if using themes

**Method B: Raw YAML Import**
- Add a manual card
- Switch to "Show Code Editor"
- Copy/paste from YAML file
- Works but brings over card_mod complexity

#### Step 3: Test View

- Exit edit mode
- Navigate through view
- Test all buttons/cards
- Check responsiveness on mobile

#### Step 4: Mark as Complete

```bash
# Rename YAML view file to indicate it's migrated
mv lovelace/views/control_panel.yaml lovelace/views/control_panel.yaml.migrated
```

---

### **Phase 3: View-by-View Migration Guide**

#### **View 1: Control Panel (Start Here - 1 hour)**

**Current cards:**
- Navbar
- Quick Actions
- Smart Suggestions
- Alerts

**Migration steps:**

1. **Create Control Panel View**
   ```
   Title: Home
   Icon: mdi:home
   Path: control_panel
   Type: Panel (or Sections)
   ```

2. **Add Navbar Card**
   - Card type: Button
   - Or skip navbar in UI mode (HA has built-in navigation)

3. **Add Quick Actions**
   - Card type: Vertical Stack
   - Inside: Grid with 2 columns
   - Add each button as "Button" card
   - Use conditional cards for visibility
   - **Simplify:** Remove card_mod, use standard buttons

4. **Add Smart Suggestions**
   - Copy structure from `lovelace/cards/smart_suggestions.yaml`
   - Use entities card with custom formatting

5. **Add Alerts**
   - Entities card or markdown card
   - Set visibility conditions

**Result:** First view migrated! Test thoroughly before proceeding.

---

#### **View 2: Alarm (45 minutes)**

**Current cards:**
- Alarmo control
- Cameras
- Motion sensors
- Doors/water sensors
- Presence

**Migration tips:**
- Camera cards: Use "Picture Entity" or "Picture Glance"
- Alarmo: Use "Alarm Panel" card
- Conditional cards for motion/door status

---

#### **View 3: Energy (1 hour)**

**Current cards:**
- Solar current/production
- Grid status/graph
- Consumption graph
- Battery status

**Migration tips:**
- Use "Energy" card type for graphs
- ApexCharts cards if using custom graphs
- Keep solar debug as separate view

---

#### **View 4-9: Remaining Views (3-4 hours)**

Follow same pattern:
1. Create view in UI
2. Add cards one by one
3. Test functionality
4. Mark YAML as migrated

---

### **Phase 4: Cleanup (30 minutes)**

#### 1. Test Complete Dashboard

- Navigate through all views
- Test on desktop and mobile
- Verify all automations still trigger
- Check conditional card visibility

#### 2. Archive YAML Files

```bash
# Move YAML files to archive
mkdir -p archive/lovelace-yaml-backup
mv ui-lovelace.yaml.backup archive/lovelace-yaml-backup/
mv lovelace/ archive/lovelace-yaml-backup/

# Or keep as reference
# Just rename ui-lovelace.yaml so HA doesn't use it
```

#### 3. Document New Structure

Create `docs/DASHBOARD_UI_MODE.md`:
```markdown
# Dashboard UI Mode

**Mode:** UI (managed via Home Assistant interface)
**Backup:** archive/lovelace-yaml-backup/

## Views

1. Control Panel - Quick actions and alerts
2. Alarm - Security and cameras
3. Energy - Solar and consumption
...

## Editing

Settings → Dashboards → Home Dashboard → Edit Dashboard
```

---

## UI Mode Best Practices

### **1. Use Sections Layout (Recommended)**

Sections layout is the modern HA approach:
- Better mobile support
- Automatic responsive design
- Easier to reorganize

**Enable sections:**
- Edit Dashboard → Settings → "Sections"

### **2. Organize Cards Logically**

Group related cards together:
- Climate: All HVAC controls in one section
- Energy: Solar + Grid + Consumption together
- Security: Cameras + Alarmo + Sensors together

### **3. Use Card Visibility**

Hide cards when not relevant:
- Good Morning button: Only show 6am-11am
- Laundry alerts: Only when laundry running
- Climate warnings: Only when extreme temps

**Set in UI:**
- Edit card → Show/Hide → Visibility → Add condition

### **4. Leverage Themes**

Since you're migrating anyway, perfect time to:
- Remove card_mod styling
- Apply custom theme
- Use standard card types

---

## Troubleshooting

### **Issue: Dashboard is Blank After Migration**

**Solution:**
```bash
# Restore backup
cp ui-lovelace.yaml.backup ui-lovelace.yaml
# Restart HA
```

### **Issue: Cards Not Showing**

**Cause:** Entity doesn't exist or wrong entity_id

**Solution:**
- Check entity in Developer Tools → States
- Verify entity_id spelling

### **Issue: Custom Cards Not Working**

**Cause:** Custom cards need to be installed via HACS

**Solution:**
- Ensure card-mod, ApexCharts, etc. installed
- Settings → Devices & Services → HACS → Frontend

### **Issue: Want to Go Back to YAML**

**Solution:**
```bash
# Restore YAML mode
mv ui-lovelace.yaml.backup ui-lovelace.yaml
# Restart HA
```

---

## Estimated Timeline

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Preparation | 15 min | 15 min |
| Setup UI Mode | 30 min | 45 min |
| View 1: Control Panel | 1 hour | 1h 45m |
| View 2: Alarm | 45 min | 2h 30m |
| View 3: Energy | 1 hour | 3h 30m |
| Views 4-9 | 3 hours | 6h 30m |
| Testing & Cleanup | 30 min | **7 hours total** |

**Recommendation:**
- Day 1: Setup + Control Panel (2 hours)
- Day 2: Alarm + Energy (2 hours)
- Day 3: Remaining views (3 hours)
- Day 4: Testing & cleanup (1 hour)

Spread over a week, ~1 hour per day.

---

## Alternative: Hybrid Approach

**Keep YAML for complex cards, UI for simple views**

Some users prefer:
- Simple views in UI (Alarm, Calendar)
- Complex views in YAML (Climate debugging, Energy)

**Setup:**
1. Create second dashboard in UI mode
2. Keep `ui-lovelace.yaml` for complex stuff
3. Switch between dashboards as needed

**Not recommended** - more complex to maintain.

---

## Quick Start Commands

```bash
# Backup current config
mkdir -p backups/lovelace-$(date +%Y%m%d)
cp -r lovelace/ backups/lovelace-$(date +%Y%m%d)/
cp ui-lovelace.yaml backups/lovelace-$(date +%Y%m%d)/

# Enable UI mode
mv ui-lovelace.yaml ui-lovelace.yaml.backup

# Restart Home Assistant
# (via UI or: ha core restart)

# After migration, archive YAML files
mkdir -p archive/lovelace-yaml-backup
mv ui-lovelace.yaml.backup archive/lovelace-yaml-backup/
cp -r lovelace/ archive/lovelace-yaml-backup/
```

---

## Checklist

**Before Starting:**
- [ ] Backup `ui-lovelace.yaml` and `lovelace/` directory
- [ ] Take screenshots of all views
- [ ] Commit current state to git
- [ ] Set aside 7 hours over multiple days

**During Migration:**
- [ ] Switch to UI mode
- [ ] Migrate Control Panel view
- [ ] Test Control Panel thoroughly
- [ ] Migrate remaining views one by one
- [ ] Test each view before proceeding

**After Migration:**
- [ ] Test all views on desktop
- [ ] Test all views on mobile
- [ ] Verify automations still work
- [ ] Archive YAML files
- [ ] Document new setup
- [ ] Commit changes to git

---

## Ready to Start?

**Immediate next steps:**

1. **I can help you backup files** - Run the backup commands
2. **Switch to UI mode** - Rename ui-lovelace.yaml
3. **Start with Control Panel** - Recreate first view together

**Want me to:**
- Execute the backup commands now?
- Walk you through creating the first view?
- Show you how to recreate Quick Actions in UI mode?

---

**Created:** 2025-11-16
**Estimated effort:** 7 hours (can be spread over multiple days)
**Risk level:** Low (backups + gradual migration)
**Recommendation:** Start with Control Panel view, ~1 hour
