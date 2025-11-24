# Lovelace UI Migration Plan - YAML + UI Hybrid Mode

## Goal
Enable UI editing for easy card repositioning and grid layout management while keeping YAML files for version control and automation.

---

## Background

### Current Setup (YAML Mode)
- **Configuration:** `ui-lovelace.yaml` defines all views
- **Card Organization:** Uses `!include` for modular YAML files
- **Advantages:**
  - Full version control
  - Easy to bulk edit
  - Reusable card definitions
- **Disadvantages:**
  - Can't drag/drop cards in UI
  - No visual grid editor
  - Must edit YAML for layout changes

### Target Setup (Storage/UI Mode with YAML Integration)
- **Primary:** UI-managed dashboards stored in `.storage/lovelace`
- **YAML Cards:** Import specific cards from YAML files as needed
- **Advantages:**
  - Drag/drop repositioning in UI
  - Visual grid editor for layouts
  - Keep YAML for complex cards and automation-generated content
  - Best of both worlds

---

## Migration Strategy

### Phase 1: Preparation (Pre-Migration)

#### 1.1 Backup Current Configuration
```bash
# Create backup of current YAML dashboard
cp ui-lovelace.yaml ui-lovelace.yaml.backup
cp -r lovelace lovelace_backup

# Commit to git
git add -A
git commit -m "Backup before Lovelace UI migration"
```

#### 1.2 Document Current Dashboard Structure

**Current Views:**
1. **Control Panel** (`control_panel.yaml`) - Main home dashboard
   - Purpose: Quick actions, alerts, climate controls
   - Cards: navbar, alerts, media control, quick actions, HVAC, switches

2. **Climate** (`climate.yaml`) - HVAC management
   - Purpose: Detailed climate control and monitoring
   - Cards: thermostats, temperature sensors, automation status

3. **Energy** (`energy.yaml`) - Solar and energy monitoring
   - Purpose: Track solar production and energy usage
   - Cards: solar graphs, power consumption

4. **Calendar** (`calendar.yaml`) - Family calendar and events
   - Purpose: Schedule tracking

5. **Alarm** (`alarm.yaml`) - Security and alarm management
   - Purpose: Alarm controls, door sensors, cameras

6. **Network** (`network.yaml`) - Network monitoring
   - Purpose: Device status, connectivity monitoring

7. **Laundry** (`laundry.yaml`) - Appliance tracking
   - Purpose: Washing machine, dryer notifications

8. **Maintenance** (`maintenance.yaml`) - System maintenance
   - Purpose: Updates, diagnostics

9. **Media** (`media.yaml`) - Media players
   - Purpose: Music and TV control

#### 1.3 Identify Cards to Keep in YAML

**Recommended to stay in YAML:**
- **Navbar** - Auto-generated navigation
- **Smart Suggestions** - Dynamic context-aware cards
- **Quick Actions** - Complex conditional logic with binary sensors
- **Automation Status Cards** - Dynamic debugging cards
- **Climate Principles/Debug Status** - Development cards

**Can move to UI:**
- Simple entity cards
- Basic button cards
- Static entity lists
- Media player cards

---

### Phase 2: Migration Process

#### 2.1 Switch to UI Mode

**Option A: Convert Existing (Recommended)**

1. **Enable UI Mode in Configuration:**
   ```yaml
   # In configuration.yaml
   lovelace:
     mode: storage
     # Remove or comment out:
     # mode: yaml
     # resources: ...
   ```

2. **Restart Home Assistant**

3. **Import Your YAML Dashboard:**
   - Settings → Dashboards → Add Dashboard
   - Select "Import from YAML"
   - Choose `ui-lovelace.yaml`
   - This creates a UI dashboard with your current layout

**Option B: Fresh Start (Alternative)**

1. Create new UI dashboard alongside YAML
2. Manually recreate layouts in UI
3. Import YAML cards as needed
4. Switch when ready

#### 2.2 Convert YAML Cards to Manual Cards (Where Needed)

For cards you want UI-editable, use the "Manual Card" type:

```yaml
# In UI dashboard, add a Manual Card with YAML:
type: vertical-stack
cards: !include lovelace/cards/quick_actions.yaml
```

**Note:** `!include` works in Manual Cards in UI mode!

#### 2.3 Create Reusable YAML Snippets

For frequently used cards, create YAML templates:

```yaml
# lovelace/templates/climate_tile_template.yaml
type: tile
entity: {{ climate_entity }}
features:
  - type: climate-hvac-modes
  - type: climate-preset-modes
    style: dropdown
  - type: target-temperature
```

---

### Phase 3: Hybrid Workflow

#### 3.1 Day-to-Day Usage

**For Layout Changes:**
1. Enter Edit Mode in UI (three dots → Edit Dashboard)
2. Drag and drop cards
3. Resize cards in grid
4. Add/remove sections
5. Changes auto-save to `.storage/lovelace`

**For Complex Cards:**
1. Edit YAML files in `lovelace/cards/`
2. Reload dashboard (Settings → Dashboards → Resources → Reload)
3. Changes appear immediately

**For New Cards:**
- Simple cards: Add in UI directly
- Complex cards: Create YAML file and add Manual Card with `!include`

#### 3.2 Version Control Strategy

**.gitignore additions:**
```gitignore
# Ignore storage UI changes (optional - see below)
# .storage/lovelace*

# OR keep them tracked for backup:
# (recommended - track everything)
```

**Recommended approach:**
- **Keep `.storage/lovelace` in git** for backup
- Commit UI changes with descriptive messages
- Major card changes still in YAML files

**Commit workflow:**
```bash
# UI layout changes
git add .storage/lovelace
git commit -m "dashboard: rearranged climate view cards"

# YAML card changes
git add lovelace/cards/climate/debug_status.yaml
git commit -m "climate: add new debug sensor to status card"
```

---

### Phase 4: Dashboard Purpose Optimization

After migration, optimize each dashboard for specific workflows:

#### Control Panel (Main Dashboard)
**Purpose:** Single screen for common actions when opening app

**Workflow Optimization:**
- **Top Section:** Alerts (laundry done, garage open, alarms)
- **Second Section:** Quick Actions (Good Morning, Arriving Home, etc.)
- **Third Section:** Currently Playing Media (conditional)
- **Bottom Sections:** Climate quick view, Light toggles

**Recommended:**
- ✅ Keep Quick Actions (automation + dashboard)
- ✅ Add voice shortcuts for all quick actions
- 🎯 Focus: "What needs attention?" and "Quick common actions"

#### Climate Dashboard
**Purpose:** Detailed HVAC control and debugging

**Workflow Optimization:**
- **For Users:** Simple thermostat tiles only
- **For Debugging:** Automation status, flags, temperature graphs
- **Split into sections:**
  - Section 1: Active climate controls (thermostats)
  - Section 2: Temperature sensors (all rooms)
  - Section 3: Debug & Automation Status (collapsible)

**Recommended:**
- ✅ Main climate control via automation (minimal dashboard usage)
- ✅ Voice control for preset changes
- 🎯 Dashboard for debugging only

#### Energy Dashboard
**Purpose:** Monitor solar production and energy usage

**Workflow:**
- Most users: Just check once a day
- No actions needed, pure monitoring

**Recommended:**
- ✅ Keep as dashboard (no automation possible)
- 🎯 Add notifications for low solar days or high usage

#### Network Dashboard
**Purpose:** Monitor network devices and connectivity

**Workflow:**
- Only checked when issues occur
- Debugging-focused

**Recommended:**
- ✅ Keep as dashboard
- ✅ Add automation for critical device offline alerts
- 🎯 Hide from main navigation, access when needed

#### Media Dashboard
**Purpose:** Media player controls

**Workflow Optimization:**
- Most controls available from Control Panel when media playing
- Detailed controls here for playlist management, etc.

**Recommended:**
- ✅ Primary control via voice ("Play music")
- ✅ Quick actions on Control Panel
- 🎯 Media dashboard for advanced controls only

---

## Implementation Steps

### Step 1: Enable UI Mode (5 minutes)

1. Edit `configuration.yaml`:
   ```yaml
   lovelace:
     mode: storage
     # Comment out:
     # mode: yaml
   ```

2. Restart Home Assistant

3. Go to Settings → Dashboards
   - Your current YAML dashboard will still work as a separate dashboard
   - Create new UI dashboard by importing YAML

### Step 2: Test Hybrid Approach (30 minutes)

1. Create a new test card in YAML:
   ```yaml
   # lovelace/cards/test_hybrid.yaml
   type: markdown
   content: "This is a YAML-managed test card!"
   ```

2. In UI dashboard, add a Manual Card:
   ```yaml
   type: vertical-stack
   cards: !include lovelace/cards/test_hybrid.yaml
   ```

3. Test editing:
   - Edit `test_hybrid.yaml` file
   - Reload dashboard
   - Confirm changes appear

4. Test UI editing:
   - Drag the card to new position
   - Resize in grid
   - Add new UI card
   - Confirm changes persist

### Step 3: Migrate Cards Gradually (1-2 hours)

**Recommended order:**

1. **Keep as YAML:**
   - navbar.yaml
   - quick_actions.yaml
   - smart_suggestions.yaml
   - All climate debug cards
   - automation_trigger_history.yaml

2. **Convert to UI:**
   - Simple entity lists
   - Basic climate tiles
   - Media player cards
   - Switch cards

3. **Convert to Manual Cards (YAML via UI):**
   - Complex conditional cards
   - Dynamic cards with templating

### Step 4: Optimize Layouts (1-2 hours)

Use UI grid editor to:
- Rearrange card order for better workflow
- Resize cards for better visibility
- Create sections for logical grouping
- Add headings and visual separators

---

## Debugging Dashboard Strategy

### Temporary Debugging Views

Create a dedicated "Debug" dashboard (hidden from main nav) with sections:

#### 1. Climate Debug Section
```yaml
# lovelace/cards/debug/climate_full.yaml
type: vertical-stack
cards:
  - !include ../climate/debug_status.yaml
  - !include ../climate/automation_trigger_history.yaml
  - !include ../climate/principles_status.yaml
  - type: entities
    title: All Temperature Sensors
    entities:
      - sensor.living_room_temperature_offset
      - sensor.ble_temperature_masterbed_temp_humidity_sensor
      # ... all temp sensors
  - type: entities
    title: All Climate Flags
    entities:
      - input_boolean.hot_today_flag
      - input_boolean.super_hot_today
      # ... all flags
```

#### 2. Automation Debug Section
```yaml
# lovelace/cards/debug/automation_status.yaml
type: entities
title: Automation Status
entities:
  - automation.living_room_morning_heat_winter
    secondary_info: last-triggered
  - automation.covers_roller_blind_timer_finished_full_open
    secondary_info: last-triggered
  # ... key automations
```

#### 3. Roller Blind Debug Section
```yaml
# lovelace/cards/debug/roller_blind_status.yaml
type: entities
title: Roller Blind Position Tracking
entities:
  - input_number.roller_blind_position
    name: Current Position (%)
  - input_number.roller_blind_target_position
    name: Target Position (%)
  - input_select.roller_blind_state
    name: State
  - timer.roller_blind_timer
    name: Movement Timer
  - cover.roller_blinds_chan1
    name: Actual Cover Entity
```

### Accessing Debug Dashboard

**Option 1: Sidebar Link (visible to admins only)**
```yaml
# In dashboard settings, set visibility:
visible:
  - user: YOUR_ADMIN_USER_ID
```

**Option 2: URL Bookmark**
- Keep the debug dashboard URL
- Access directly when needed
- Doesn't clutter main navigation

---

## Rollback Plan

If migration causes issues:

### Quick Rollback to YAML Mode

1. Edit `configuration.yaml`:
   ```yaml
   lovelace:
     mode: yaml
   ```

2. Restore backup:
   ```bash
   cp ui-lovelace.yaml.backup ui-lovelace.yaml
   ```

3. Restart Home Assistant

### Hybrid Rollback

Keep both dashboards:
- UI dashboard for daily use
- YAML dashboard for backup
- Switch between them in Settings → Dashboards

---

## Summary

### Benefits of Hybrid Approach

✅ **Best of both worlds:**
- UI editing for layouts and simple cards
- YAML for complex logic and version control
- Automation-generated cards stay in YAML

✅ **Workflow improvements:**
- Faster card repositioning
- Visual grid management
- Maintain git history for important changes

✅ **Flexibility:**
- Choose UI or YAML per-card
- Easy testing without breaking production
- Gradual migration at your own pace

### Recommended Next Actions

1. **Create backup** (git commit)
2. **Enable UI mode** (5 min)
3. **Test with one dashboard** (30 min)
4. **Migrate cards gradually** (over several days)
5. **Optimize layouts** in UI (1-2 hours)
6. **Create debug dashboard** (1 hour)

---

**Generated:** 2025-11-16
**Status:** Ready for implementation
**Estimated Time:** 3-5 hours total (can be done incrementally)
