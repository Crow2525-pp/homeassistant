# LLM Execution Plan - Home Assistant Implementation
**Created:** 2025-11-17
**Target Audience:** Claude or other LLMs executing tasks autonomously
**Status:** Ready for execution
**Total Estimated LLM Work:** 8-12 hours

---

## Table of Contents
1. [Overview & Architecture](#overview--architecture)
2. [Phase 1: Validation & Analysis (2-3 hours)](#phase-1-validation--analysis-2-3-hours)
3. [Phase 2: Template Generation (3-4 hours)](#phase-2-template-generation-3-4-hours)
4. [Phase 3: Configuration Creation (2-3 hours)](#phase-3-configuration-creation-2-3-hours)
5. [Phase 4: Documentation & Guides (1-2 hours)](#phase-4-documentation--guides-1-2-hours)
6. [Manual User Tasks (Checklists)](#manual-user-tasks-checklists)
7. [Integration & Testing Strategy](#integration--testing-strategy)

---

## Overview & Architecture

### Current State
- Home Assistant instance with 3 core fixes already applied
- 3 configuration files modified
- 3 dashboard files updated
- 7 comprehensive documentation guides created
- Multiple pending tasks requiring implementation

### LLM Responsibilities
This plan is designed for an LLM to autonomously:
1. Validate existing fixes for syntax/compatibility errors
2. Create production-ready YAML configurations
3. Generate automation templates with proper templating
4. Create step-by-step implementation guides
5. Generate code snippets for integration

### User Responsibilities
- Manual testing of existing fixes
- Hardware/physical tasks (RFID tag registration)
- Configuration decisions (feature specs)
- Deployment execution and monitoring

### Success Criteria
- All generated files are syntactically valid YAML
- All templates include detailed comments and instructions
- All guides include step-by-step numbered instructions
- All code is properly formatted for direct copy-paste deployment
- Documentation explains why each step is necessary
- Climate controls use versatile climate entities (not standard climate) and operate via presets (eco/comfort/frost/boost) rather than hard-coded temperatures, selected based on outside temperature, time of day, WFH/home presence, and heating state.

---

## Phase 1: Validation & Analysis (2-3 hours)

### 1.1 Validate Existing Fix Files
**Objective:** Ensure all modified files are syntactically correct and HA-compatible

**Files to Validate:**
- `config/domains/scripts.yaml` - Play Music & Read News fixes
- `automations/06_living_room_climate_split.yaml` - Morning heating fix
- `configuration.yaml` - input_select additions
- `lovelace/cards/quick_actions.yaml` - Room selector integration
- `lovelace/cards/solar.yaml` - Debugging cleanup
- `lovelace/cards/energy/solar_debug.yaml` - New debug card

**Validation Steps:**
1. Read each file completely
2. Check YAML syntax (proper indentation, quote styles, list formatting)
3. Verify Home Assistant specific syntax:
   - Service call formatting
   - Template syntax ({% %} and {{ }})
   - Entity ID naming conventions
   - Automation condition/action structure
4. Check for common HA errors:
   - Missing required fields (automation: entity_id, service)
   - Invalid service names
   - Missing quotes on values with special characters
   - Improper use of includes/references
5. Climate-specific checks:
   - Use versatile climate entities (not standard climate)
   - Use `climate.set_preset_mode` with presets (eco/comfort/frost/boost) instead of hard-coded temperatures
   - Preset selection driven by outside temperature, time of day, WFH/home presence, and heating state
5. Document any issues found with line numbers and suggested fixes

**Output Format:**
Create file: `docs/VALIDATION_REPORT_2025-11-17.md`
- Section for each file
- Summary table: Filename | Status | Issues Found | Severity
- Detailed fix recommendations for each issue
- If no issues: confirm ready for deployment

**Tools to Use:**
- Read tool to examine each file
- Grep to search for common error patterns
- Document findings in markdown

---

### 1.2 Analyze Codebase Structure
**Objective:** Map current configuration organization for template generation

**Analysis Tasks:**

1. **Script Structure Analysis**
   - Read `config/domains/scripts.yaml`
   - Document script format: sequence structure, condition syntax, service calls
   - Identify naming patterns (snake_case, prefixes used)
   - Note any custom helpers or input_select entities referenced

2. **Automation Organization**
   - Read `automations/06_living_room_climate_split.yaml`
   - Document automation structure: triggers, conditions, actions
   - Check for template usage patterns (variables, state conditions)
   - Identify time-based triggers and their format
   - Note any custom templates or advanced HA features used

3. **Input Helper Patterns**
   - Search for all input_select, input_number, input_datetime definitions
   - Document naming conventions
   - Identify usage patterns (automation triggers, script inputs, frontend displays)

4. **Dashboard Structure**
   - Read Lovelace YAML files
   - Document card types, layout patterns, entity mappings
   - Note custom styling or advanced UI patterns

**Output Format:**
Create file: `docs/CODEBASE_STRUCTURE_ANALYSIS.md`
- YAML structure patterns used in this instance
- Naming conventions discovered
- Common automation templates/patterns
- Entity reference patterns
- Template syntax preferences

**Purpose:** Ensures all generated templates match existing style and structure

---

### 1.3 Inventory Current Entities
**Objective:** Create comprehensive list of all entities needed for future automations

**Tasks:**
1. Search for all input_select definitions and document them
2. Search for all input_datetime definitions and document them
3. Search for all input_number definitions and document them
4. Search for all template sensors and document them
5. Search for all scripts and document their parameters
6. Map out existing automations and their triggers

**Output Format:**
Create file: `docs/ENTITY_INVENTORY.md`
- Input Selectors (with options, current value)
- Input DateTime helpers (with current value)
- Input Number helpers (with min/max/unit)
- Available Scripts (with parameters)
- Automation triggers (with entity dependencies)
- Template sensors (with logic)

**Purpose:** Reference for ensuring no duplicate entity names in new creations

---

## Phase 2: Template Generation (3-4 hours)

### 2.1 Create RFID Tag Automation Template
**Objective:** Generate ready-to-deploy automation for AC filter tracking

**Specification from docs:**
- Need: `input_datetime.ac_filter_downstairs` helper
- Trigger: RFID tag scan with ID (user will provide)
- Action: Update input_datetime to current timestamp
- Optional: Send notification on tag scan

**Generation Steps:**

1. **Create input_datetime helper YAML**
   - Filename: Template output for manual creation or automation helper creation
   - Fields: name, initial_value (today), has_time (false - date only)
   - Include comments explaining each field
   - Document manual creation steps if needed

2. **Create RFID trigger automation**
   - Analyze existing tag format from RFID docs
   - Generate automation with:
     - Trigger: `tag_scanned` event with specific tag_id
     - Condition: Entity exists check
     - Action: Call `input_datetime.set_datetime` service
     - Action: Send persistent notification (optional)
   - Include full inline comments
   - Add instructions for obtaining tag_id during registration
   - Include debugging steps if tag doesn't trigger

3. **Create template sensor for days tracking**
   - Calculate days since last AC filter change
   - Format: "X days ago" or "X days since last filter change"
   - Include in automation documentation

4. **Create dashboard card snippet**
   - Lovelace YAML for showing:
     - AC Filter Last Changed date
     - Days since filter change
     - Button to manually update (for emergencies)

**Output Files to Create:**

**File 1:** `templates/RFID_AC_FILTER_SETUP.md`
- Step-by-step guide with all code blocks
- Section 1: Create input_datetime helper (manual or code)
- Section 2: Create template sensor for days calculation
- Section 3: Create automation YAML with detailed comments
- Section 4: Add to dashboard (copy-paste Lovelace YAML)
- Section 5: Test & Verify checklist
- Section 6: Troubleshooting guide

**File 2:** `automations/99_rfid_ac_filter_template.yaml` (ready to rename/adapt)
- Full automation code with inline comments
- Placeholder for tag_id with instructions
- Sample service calls and conditions

**File 3:** `config/templates/ac_filter_days_sensor.yaml` (if using template sensors)
- Template sensor calculating days since last update
- Proper formatting for HA template sensors

---

### 2.2 Create Git Setup & Pre-commit Hooks
**Objective:** Generate git configuration for version control and CI

**Generation Steps:**

1. **Create .gitignore for Home Assistant**
   - Standard HA exclusions (secrets, deps, tts, etc.)
   - Research what shouldn't be in git
   - Create comprehensive file with comments

2. **Create branch strategy document**
   - Development branch setup commands
   - Feature branch naming convention (feature/*, bugfix/*, docs/*)
   - Commit message conventions
   - PR template

3. **Create pre-commit hooks configuration**
   - `.pre-commit-config.yaml` for yamllint, prettier, etc.
   - Installation instructions
   - How to bypass if necessary (emergency deploys)

4. **Re-use/extend existing GitHub Actions** (already present in `.github/workflows/ha-validate.yml` and `yaml-lint.yml`)
   - Keep current lint + config-check jobs; only adjust paths or versions if needed
   - Ensure PRs block on these checks and allow auto-merge when both are green
   - Add a short “LLM runbook” snippet describing how to trigger checks (`gh workflow run ha-validate.yml -f ref=...`) from Claude Code/Codex online
   - Success/failure notifications

**Output Files to Create:**

**File 1:** `docs/GIT_WORKFLOW_SETUP.md`
- Prerequisites: Git installed, GitHub repo ready
- Step 1: Create .gitignore
- Step 2: Create development branch locally
- Step 3: Set up pre-commit hooks
- Step 4: Create initial commit
- Step 5: Configure GitHub Actions (if applicable)
- Troubleshooting section

**File 2:** `.gitignore`
- Complete HA-specific exclusions

**File 3:** `.pre-commit-config.yaml`
- yamllint configuration
- Optional: prettier, trailing-whitespace, etc.

**File 4:** `.github/workflows/ha-validate.yml` (already present — update only if needed)
- Home Assistant config validation job (keep docker check)
- Use dummy secrets generation already present; tweak paths only if config layout changes
- Keep branch filters aligned with protected branches

**File 5:** `.github/workflows/yaml-lint.yml` (already present — update only if needed)
- YAML linting job
- Add markdown linting if desired
- Keep path filters in sync with config files

**File 6:** `CONTRIBUTING.md`
- Branch naming: feature/feature-name
- Commit message: "fix: description" or "feat: description"
- PR template with checklist

---

### 2.3 Create Automated Backup Automation
**Objective:** Generate automation for daily backups with off-site storage

**Specification:**
- Daily backup at 3:00 AM
- Keep 7 daily + 4 weekly backups (cloud storage implementation)
- Send notification on success/failure
- Optional: Upload to Google Drive or NAS

**Generation Steps:**

1. **Create backup automation**
   - Trigger: Time pattern 3:00 AM daily
   - Action: Call `backup.create` service (HA 2024.9+)
   - Action: Send notification
   - Condition: Check if automation enabled
   - Include error handling

2. **Create backup status sensor**
   - Template sensor showing last backup time
   - Days since last backup
   - Backup file size (if possible)

3. **Create optional off-site backup automation**
   - For Google Drive: Use `google_drive` integration (if configured)
   - For NAS: Use `samba` or SSH shell command
   - Daily execution at 3:30 AM (after local backup completes)

4. **Create notification service template**
   - Telegram, Email, or Persistent Notification
   - Include: backup success/failure, timestamp, backup name

**Output Files to Create:**

**File 1:** `docs/BACKUP_AUTOMATION_SETUP.md`
- Overview of backup strategy
- Step 1: Verify backup service available (HA 2024.9+)
- Step 2: Create automation YAML
- Step 3: (Optional) Set up off-site backup
- Step 4: Create backup sensor template
- Step 5: Test backup process
- Monitoring & Maintenance section

**File 2:** `automations/99_daily_backup_template.yaml`
- Daily backup automation
- Inline comments explaining each component
- Notification service call
- Error handling

**File 3:** `automations/99_offsite_backup_template.yaml` (optional)
- Google Drive or NAS backup automation
- Service-specific configuration
- Path and credentials notes

**File 4:** `config/templates/backup_status_sensor.yaml`
- Template sensors for last backup time
- Days since backup calculation

---

### 2.4 Create YAML Linting Configuration
**Objective:** Generate yamllint setup for code quality

**Generation Steps:**

1. **Create .yamllint config file**
   - Rules: indentation (spaces: 2), line-length (120), colons, brackets
   - HA-specific adjustments (relax rules for HA-specific syntax)
   - Document reasoning for each rule

2. **Create linting guide**
   - How to run yamllint manually
   - How to integrate with pre-commit hooks
   - Common HA violations and fixes
   - Ignoring specific rules when necessary

**Output Files to Create:**

**File 1:** `.yamllint`
- Complete configuration with comments
- Tailored for Home Assistant YAML
- Allow for HA-specific syntax exceptions

**File 2:** `docs/YAML_LINTING_GUIDE.md`
- Setup instructions
- Command to run: `yamllint config/`
- Integration with pre-commit hooks
- Common errors and solutions
- When to suppress warnings (edge cases)

---

### 2.5 Create Roller Blind Simplification Migration Template
**Objective:** Generate migration code from 0-100% to Open/Partial/Closed states

**Analysis Required:**
1. Find all existing roller blind automations
2. Find all roller blind entities and their templates
3. Document current position tracking logic
4. Identify all references in dashboards and automations

**Generation Steps:**

1. **Create migration guide document**
   - Overview: why simplify (eliminate drift, improve reliability)
   - Backup current state
   - Migration steps with rollback plan

2. **Create new state automation templates**
   - Open automation (trigger: time of day or manual)
   - Close automation (trigger: sunset, security mode)
   - Partial automation (trigger: specific conditions)
   - Manual override handling

3. **Create input_select helper for blind states**
   - Options: Open, Partial, Closed, Manual
   - Automation to update state on blind movement
   - Template to convert to icon (open/close/pause)

4. **Create dashboard cards**
   - Button row: Open, Partial, Closed buttons
   - Status display with icon and last change time
   - Manual override toggle

5. **Create position conversion sensors** (if keeping legacy data)
   - Template to convert 0-100% position to new state
   - For transition period monitoring

**Output Files to Create:**

**File 1:** `docs/ROLLER_BLIND_MIGRATION_GUIDE.md`
- Step-by-step migration with rollback plan
- Why each step is necessary
- Rollback instructions at each major step
- Monitoring and verification

**File 2:** `automations/99_roller_blind_states_template.yaml`
- Template for Open automation
- Template for Close automation
- Template for Partial automation
- Include entity ID mappings that need customization

**File 3:** `config/templates/roller_blind_state_input.yaml`
- input_select for blind states
- Initial value setup
- Reset automation for daily schedule

**File 4:** `lovelace/cards/roller_blind_control_template.yaml`
- Lovelace card with Open/Partial/Close buttons
- Status display
- Design matching existing dashboard style

---

### 2.6 Create Motion Detection & Face Recognition Automation
**Objective:** Generate template for outside motion alerts with face detection

**Analysis Required:**
1. Find existing motion sensor configurations
2. Identify available face detection integrations (frigate, doods, etc.)
3. Understand current alert notification setup

**Generation Steps:**

1. **Create motion detection trigger automation**
   - Trigger: Motion sensor state change
   - Condition: Motion detected (on), not duplicate trigger (2 min debounce)
   - Action: Call face detection service (if available)
   - Action: Send notification with camera snapshot

2. **Create face recognition response**
   - If person detected: Log event, send notification with person name
   - If unknown: Send high-priority alert with snapshot
   - If no face: Send standard motion alert

3. **Create time-based filtering**
   - Disable during daytime (8 AM - 6 PM)
   - Higher sensitivity at night
   - Different actions on weekends vs weekdays

4. **Create dashboard card**
   - Recent motion events with timestamps
   - Camera feed if available
   - Unknown person alerts highlighted

**Output Files to Create:**

**File 1:** `docs/MOTION_FACE_DETECTION_SETUP.md`
- Prerequisites: Face detection integration required
- Step 1: Verify motion sensors available
- Step 2: Configure face detection service
- Step 3: Create automations
- Step 4: Add to dashboard
- Testing checklist
- Troubleshooting (common detection issues)

**File 2:** `automations/99_motion_detection_template.yaml`
- Motion trigger with debounce
- Integration point for face detection

**File 3:** `automations/99_face_recognition_response_template.yaml`
- Face detected action (if applicable)
- Unknown person high-priority alert
- Service calls for notifications

---

### 2.7 Create Morning Wake-up & Downstairs Preheat Automations
**Objective:** Generate automations for 5:00 AM lighting and downstairs temperature

**Specification from issues:**
1. 5:00 AM lights-on routine should NOT turn on bedroom light (only computer room)
2. Ensure downstairs area is pre-warmed for morning wake-up
3. Motion-based routine for additional morning triggers

**Generation Steps:**

1. **Create 5:00 AM lighting automation**
   - Trigger: Time 5:00 AM (weekdays only, configurable)
   - Action: Turn on computer room light to 30% brightness (gradual)
   - Action: NOT bedroom light
   - Condition: Only if not already on
   - Include: Can disable automation via input_boolean

2. **Create downstairs preheat automation**
   - Trigger: Time 5:30 AM (30 min before wake-up)
   - Action: Choose versatile climate preset (eco/comfort/boost/frost) based on outside temperature, time of day, WFH status, and home presence; call `climate.set_preset_mode` on the versatile climate entity (no standard climate, no hard-coded temps)
   - Action: Send notification (optional, for confirmation)
   - Condition: Only if current preset differs from desired preset
   - Include: Max heating duration (stop at 6:30 AM)

3. **Create motion-based morning routine**
   - Trigger: Motion detected in kitchen 5:30-7:00 AM
   - Action: Turn on kitchen lights to 50% brightness
   - Action: Start coffee maker script (if available)
   - Condition: Only once per morning (input_boolean gate)

4. **Create override helpers**
   - input_boolean: Disable morning routine (vacation mode)
   - input_select: Morning climate preset preference (comfort/eco/boost) used to resolve ties with outside-temperature logic
   - input_boolean or binary_sensor: WFH / user home indicator used in preset selection
   - input_select: Which rooms to light (Kitchen, Computer, Both)

**Output Files to Create:**

**File 1:** `docs/MORNING_ROUTINE_SETUP.md`
- Overview of morning routine architecture
- Step 1: Create input helpers (morning preset selector, WFH/home indicator, disable toggles, room selection)
- Step 2: Create preheat automation
- Step 3: Create lighting automation
- Step 4: Create motion-based routine
- Step 5: Dashboard integration
- Testing checklist (test on weekend first)
- Adjustments: How to modify times and preset selection rules (outside temp/WFH/home presence)

**File 2:** `automations/99_morning_preheat_template.yaml`
- Downstairs preheat automation
- Preset selection logic tied to outside temperature, time-of-day, WFH/home presence
- Safety: max heating duration

**File 3:** `automations/99_morning_lights_template.yaml`
- 5:00 AM computer room light
- Explicitly excludes bedroom
- Gradual turn-on option

**File 4:** `automations/99_motion_morning_routine_template.yaml`
- Motion detection 5:30-7:00 AM
- One-time per morning gate (input_boolean)

**File 5:** `config/lovelace/morning_routine_control.yaml`
- Input helpers dashboard card
- Quick disable toggle
- Morning preset selector and WFH toggle
- Recent execution log

---

### 2.8 Create Computer Desk Button Control Automation
**Objective:** Generate automation to power on computer (not just lights)

**Analysis Required:**
1. Determine computer device type (what integration controls it?)
2. Understand current "Computer Desk" button configuration
3. Identify power control method (wake-on-LAN, USB relay, smart outlet, etc.)

**Generation Steps:**

1. **Decision tree documentation**
   - If using WOL (Wake-on-LAN):
     - Create script to send WOL packet
     - Configure MAC address and broadcast IP
   - If using smart outlet/relay:
     - Use existing switch entity
     - Create script to turn on
   - If using USB relay:
     - May require shell command script

2. **Create control script**
   - Script to power on computer
   - Script to power off (if applicable)
   - Include: Success/failure notifications
   - Include: Conditional logic (don't turn on if already on)

3. **Create dashboard button**
   - Replace current light toggle with computer power script call
   - Add status display showing computer power state (if available)
   - Add shutdown button (with confirmation)

4. **Create automation for auto-shutdown** (optional)
   - Turn off computer at specific time if idle
   - Send warning notification 5 min before shutdown

**Output Files to Create:**

**File 1:** `docs/COMPUTER_DESK_CONTROL_SETUP.md` (decision document)
- Prerequisites & decision tree:
  - "What method controls your computer power?"
  - Option A: Wake-on-LAN (WOL)
  - Option B: Smart outlet (if available)
  - Option C: USB relay (if available)
- Once user decides: Generate specific files

**File 2a:** `config/domains/scripts.yaml` (add WOL section if WOL chosen)
- Wake-on-LAN script block
- Configurable MAC address and broadcast IP
- Notification on completion

**File 2b:** `config/domains/scripts.yaml` (add outlet section if smart outlet chosen)
- Simple outlet control script block
- Shutdown script if relay available

**File 3:** `lovelace/cards/computer_desk_control_template.yaml`
- Computer power button
- Status indicator
- Shutdown button (with confirmation)

---

## Phase 3: Configuration Creation (2-3 hours)

### 3.1 Generate Master Implementation Checklist
**Objective:** Create comprehensive checklist for all generated templates

**File:** `docs/IMPLEMENTATION_CHECKLIST.md`

**Content:**
- Checklist matrix with columns:
  - Task ID | Task Name | File(s) Affected | User Decision Needed | Complexity | Time Estimate
- Grouped by priority:
  - Critical (this week): RFID toilet investigation, testing current fixes
  - High (next week): Backup, git setup, preheat automation
  - Medium (next month): Roller blind, face detection, computer desk
  - Low (future): Nice-to-haves

- For each task:
  - Prerequisites (what must be done first)
  - Files to read (documentation reference)
  - Files to create/modify (exact paths)
  - Validation steps (how to verify success)
  - Rollback plan (if deployment fails)

---

### 3.2 Generate Entity Reference Spreadsheet
**Objective:** Create comprehensive entity mapping document

**File:** `docs/ENTITY_REFERENCE.md`

**Tables:**
1. Input Helpers (name, type, options, purpose, automation reference)
2. Scripts (name, parameters, trigger event, output)
3. Automations (ID, name, triggers, conditions, actions, related entities)
4. Sensors (template sensors, binary sensors, calculations)
5. Lovelace Cards (location, entities used, card type)

**Purpose:** Quick reference to prevent duplicate entity creation

---

### 3.3 Create Implementation Dependencies Graph
**Objective:** Document which tasks must be completed before others

**File:** `docs/IMPLEMENTATION_DEPENDENCIES.md`

**Visualization:**
```
Phase 1: Validation (NO DEPENDENCIES)
├── Input: Current code
├── Output: Validation report, structure analysis
└── Blocking: Nothing - all can start simultaneously

Phase 2a: Git Setup (AFTER Validation)
├── Input: Validation report, codebase structure
├── Output: .gitignore, pre-commit config
└── Blocking: Phase 2b, 2c tasks (optional dependency)

Phase 2b: Backup (INDEPENDENT)
├── Input: Automation patterns from analysis
├── Output: Backup automation templates
└── No blocking dependencies

Phase 2c: RFID AC Filter (INDEPENDENT)
├── Input: Codebase analysis, entity inventory
├── Output: RFID automation templates
└── Depends on: User provides tag ID

Phase 2d-2h: Other templates (INDEPENDENT)
└── Each depends on: Codebase analysis, automation patterns

Phase 3: Configuration merging (AFTER Phase 2)
├── Input: All templates from Phase 2
├── Output: Merged configurations ready to deploy
└── Depends on: User decisions for computer desk, motion alerts

Phase 4: Testing & Documentation (AFTER Phase 3)
└── Input: Generated configurations
```

---

### 3.4 Create Configuration Merge Strategy
**Objective:** Document how to safely integrate all generated templates into existing config

**File:** `docs/CONFIG_MERGE_STRATEGY.md`

**Content:**
1. **Backup & Safety**
   - Create backup before any merge
   - Git commit before merge
   - How to rollback if issues

2. **Merge approach for each file type:**
   - **Automations:** Append to `automations/` with numbered files (01_, 02_, etc.)
   - **Scripts:** Append to existing `config/domains/scripts.yaml` with clear section headers
   - **Input helpers:** Add to `configuration.yaml` with organization comments
   - **Templates:** Create in `config/templates/` or inline where appropriate
   - **Lovelace:** Add to appropriate dashboard files with section markers

3. **Testing after each merge:**
   - Run `ha core check`
   - Verify in UI
   - Check logs for errors

4. **Rollback procedure:**
   - Git revert to previous commit
   - `ha core restart`
   - Verify functionality

---

## Phase 4: Documentation & Guides (1-2 hours)

### 4.1 Create Quick Start Guides for Each Feature
**Objective:** Generate user-friendly implementation guides

**For each major feature, create:**

**File:** `docs/QUICKSTART_[FEATURE].md`

**Template structure:**
1. Overview (1 paragraph)
2. What you'll need (prerequisites, time, complexity)
3. Step-by-step instructions (numbered, copy-paste ready)
4. Verification checklist (how to confirm it works)
5. Troubleshooting (common issues and solutions)
6. Rollback instructions (if something goes wrong)
7. Next steps (what to do after feature is working)

**Features requiring guides:**
- RFID Tag Tracking (AC Filter)
- Automated Backups
- Git Version Control
- YAML Linting
- Roller Blind Migration
- Motion & Face Detection
- Morning Wake-up Routine
- Computer Desk Control

---

### 4.2 Create Troubleshooting Guide
**Objective:** Collect all potential issues and solutions

**File:** `docs/TROUBLESHOOTING_GUIDE.md`

**Structure:**
1. Configuration validation errors (YAML syntax issues)
2. Automation doesn't trigger (common causes and fixes)
3. Service calls fail (entity not found, invalid syntax)
4. Notifications don't send (notification service issues)
5. Git conflicts and resolution
6. Backup failures and solutions
7. Template sensor errors
8. Lovelace card display issues

**For each issue:**
- Symptom (what the user observes)
- Root causes (why it happens)
- Diagnostic steps (how to identify the issue)
- Solutions (numbered steps to fix)
- Prevention (how to avoid in future)

---

### 4.3 Create Future Enhancements Document
**Objective:** Document next steps and advanced features

**File:** `docs/FUTURE_ENHANCEMENTS.md`

**Sections:**
1. Advanced workflow optimizations (voice command integration)
2. Machine learning features (predictive heating, learning schedules)
3. Integration with other platforms (Google Home, Alexa)
4. Mobile app optimization
5. Remote access setup (secure tunneling)
6. Energy optimization features
7. Advanced security (2FA, API tokens rotation)
8. Performance optimization (database cleanup, sensor aggregation)

**For each enhancement:**
- Benefit (why do this)
- Complexity (time and difficulty)
- Dependencies (what must be in place first)
- Resources (documentation links)
- Implementation approach (high-level steps)

---

## Manual User Tasks (Checklists)

### This Week (Testing - 2-3 hours)

**Task 1: Test Current Fixes**
- [ ] Create Home Assistant backup (Settings  >  System  >  Backups)
- [ ] Run `ha core check` via SSH/terminal
- [ ] Run `ha core restart`
- [ ] Monitor logs: `ha core logs -f` (5 minutes)
- [ ] Test Play Music button:
  - [ ] Open Spotify on phone, play music
  - [ ] Switch output to different device
  - [ ] Tap "Play Music" in HA
  - [ ] Verify music resumes on WiiM Amp
- [ ] Test Read the News button:
  - [ ] Select "Kitchen" from room dropdown
  - [ ] Tap "Read the News"
  - [ ] Verify audio on kitchen speaker only
  - [ ] Repeat for Study, Master Bedroom, All Rooms
- [ ] Monitor living room temperature:
  - [ ] Check temp at 6:00-7:00 AM
  - [ ] Record for 5 days
  - [ ] Compare to previous week (should be warmer)
- [ ] Verify energy dashboard:
  - [ ] Navigate to Energy & Solar tab
  - [ ] Confirm no debugging section visible
  - [ ] Confirm only production data shown

**Task 2: Investigate Downstairs Toilet RFID Tag** (1-2 hours)
- [ ] Locate automation file for RFID tags
- [ ] Find automation for tag ID: `859e3818-e623-47aa-9062-d89afd44489b`
- [ ] Check if `input_datetime.downstairs_toilet_last_cleaned` exists:
  - [ ] Go to Settings  >  Devices & Services  >  Helpers
  - [ ] Search for "downstairs_toilet_last_cleaned"
  - [ ] If exists: Check current value (should be today's date)
  - [ ] If missing: Note that entity creation needed
- [ ] Scan the RFID tag in HA:
  - [ ] Go to Settings  >  Devices & Services  >  RFID/NFC integration
  - [ ] Scan the tag at downstairs toilet
  - [ ] Check if read successfully
  - [ ] Monitor Home Assistant logs for event
- [ ] If entity missing, create manually:
  - [ ] Settings  >  Devices & Services  >  Helpers
  - [ ] Create  >  Date and Time
  - [ ] Name: `downstairs_toilet_last_cleaned`
  - [ ] Set initial value: Today
- [ ] Take screenshot of final state
- [ ] Document findings in: `docs/RFID_TAG_INVESTIGATION_RESULTS.md`

**Task 3: Prepare for Next Phase** (30 min)
- [ ] Review `docs/LLM_EXECUTION_PLAN_2025-11-17.md` (this file)
- [ ] Identify which features you want implemented (mark with * in checklist)
- [ ] Decide on computer desk control method (WOL, outlet, relay)
- [ ] Decide on face detection setup (do you have frigate/doods?)
- [ ] Decide on morning preset rules (when to use comfort/eco/boost based on outside temp, time, WFH/home)

---

### Next Week (Implementation - 3-4 hours)

**Task 4: Hardware Procurement (if applicable)**
- [ ] Purchase NFC tag for AC filter tracking (if not purchased)
- [ ] Register tag with Home Assistant:
  - [ ] Settings  >  Devices & Services  >  RFID/NFC
  - [ ] Scan tag to register
  - [ ] Note the tag ID: `_______________`
  - [ ] Place tag on AC filter unit in downstairs area
- [ ] Verify computer desk power control method:
  - [ ] Test Wake-on-LAN (if using)
  - [ ] Test smart outlet (if using)
  - [ ] Confirm power control works from terminal/app

**Task 5: Deploy Generated Automations** (2 hours)
- [ ] Create new git branch: `git checkout -b feature/automation-improvements`
- [ ] Copy automation files from templates to `automations/`
- [ ] Add/merge script blocks into `config/domains/scripts.yaml`
- [ ] Create input helpers as documented
- [ ] Run `ha core check`
- [ ] If no errors: `ha core restart`
- [ ] Test each automation:
  - [ ] Backup automation (check if backup created at 3:00 AM)
  - [ ] Preheat automation (check if triggered at 5:30 AM)
  - [ ] Lighting automation (check if triggered at 5:00 AM)
  - [ ] RFID AC filter (scan tag and verify datetime updated)
- [ ] Commit changes: `git add . && git commit -m "feat: add automation improvements"`

**Task 6: Configure Dashboard Updates** (1 hour)
- [ ] Update Lovelace dashboard files with new cards:
  - [ ] Morning routine control card
  - [ ] Computer desk control card
  - [ ] AC filter status card
- [ ] Verify cards display correctly
- [ ] Adjust card sizes/positions as needed
- [ ] Restart Lovelace (browser refresh)

---

### Next Month (Optimization - 5+ hours)

**Task 7: Roller Blind Migration** (2-3 hours)
- [ ] Read: `docs/ROLLER_BLIND_MIGRATION_GUIDE.md`
- [ ] Backup existing blind configurations
- [ ] Create git branch: `git checkout -b feature/roller-blind-states`
- [ ] Create input_select helpers for blind states
- [ ] Update existing blind automations (one at a time)
- [ ] Test each blind: Open  >  Partial  >  Closed
- [ ] Update dashboard cards
- [ ] Monitor for state drift over 1 week
- [ ] If stable: Delete old position-based automations

**Task 8: Advanced Features** (as time permits)
- [ ] Set up voice command optimization
- [ ] Configure advanced notifications
- [ ] Set up remote access (if needed)
- [ ] Implement energy optimization routines

---

## Integration & Testing Strategy

### CI & Remote LLM Workflow
- Use existing GitHub Actions (`.github/workflows/ha-validate.yml` and `yaml-lint.yml`) as the gate; keep PRs blocked until both are green.
- When working from Claude Code/Codex online, push to a feature branch, open a PR, then trigger the workflows (e.g., `gh workflow run ha-validate.yml -f ref=feature/branch` followed by `gh workflow run yaml-lint.yml -f ref=feature/branch`).
- Configure branch protection to allow auto-merge once required checks pass; avoid bypassing checks.
- Keep a small runbook in the repo (or PR body) with the exact commands the hosted LLM should run to validate/merge.
- Ensure dummy `secrets.yaml` generation in `ha-validate.yml` still matches repo layout after any path changes.

### Pre-Deployment Testing (Before Any LLM Changes)

1. **Review generated files:**
   - Each file matches existing code style
   - Entity names follow convention (no duplicates)
   - YAML syntax is valid

2. **Understand dependencies:**
   - What must be created first (input helpers)
   - What services must be available (backup.create)
   - What entities must exist (climate devices)

3. **Create safety plan:**
   - Backup location and recovery procedure
   - Git rollback strategy
   - Testing order (safest to riskiest)

### Deployment Testing Order

**Order 1 (Safest - No Side Effects):**
1. YAML linting setup (.yamllint, pre-commit)
2. Git workflow setup (.gitignore)
3. Input helpers (input_select, input_datetime, input_number)
4. Documentation updates

**Order 2 (Safe - Isolated Features):**
5. Backup automation (runs at 3 AM, doesn't affect other systems)
6. RFID AC filter automation (isolated, only triggers on tag scan)
7. Roller blind state helpers (preparation for future migration)

**Order 3 (Moderate - Impacts Daily Routine):**
8. Morning preheat automation (5:30 AM, isolated climate control)
9. Morning lighting automation (5:00 AM, isolated lighting)
10. Computer desk button (doesn't change existing behavior, just replaces old)

**Order 4 (Higher Impact - External Systems):**
11. Motion detection automation (affects notifications, monitoring)
12. Face recognition (if available, advanced feature)

**Order 5 (Major Changes - Complex Features):**
13. Roller blind migration (large refactor, requires extensive testing)

### Testing Procedure for Each Feature

1. **Pre-test checklist:**
   - [ ] Entity dependencies exist
   - [ ] Required services available
   - [ ] Git committed (before deployment)
   - [ ] Backup created

2. **Deployment:**
   - [ ] Copy files to config directory
   - [ ] Run `ha core check` (syntax validation)
   - [ ] Run `ha core restart`
   - [ ] Monitor logs: `ha core logs -f` (5-10 minutes)

3. **Functional testing:**
   - [ ] Manually trigger automation (Developer Tools  >  Actions)
   - [ ] Verify expected action occurs
   - [ ] Check Home Assistant logs for errors
   - [ ] Verify any notifications send correctly

4. **Integration testing:**
   - [ ] Test with existing automations running
   - [ ] Verify no conflicts or race conditions
   - [ ] Check related automations still work

5. **Rollback testing (optional but recommended):**
   - [ ] Break automation (change service name, disable trigger)
   - [ ] Verify rollback procedure works
   - [ ] Restore and re-enable

### Success Criteria

✅ **Feature is successful if:**
- No configuration validation errors (`ha core check` passes)
- Feature triggers correctly when expected
- Feature performs intended action
- No error messages in HA logs
- No impact on other automations/features
- Related dashboard cards display correctly

⚠️ **Known issues to watch for:**
- Template syntax errors (mismatched {{ }} or {% %})
- Service call parameter mismatches
- Entity ID case sensitivity issues
- State value case mismatches ("on" vs "On")
- Automation condition logic errors
- Missing required fields in service calls

### Monitoring & Maintenance

**Weekly:**
- [ ] Check automation execution logs
- [ ] Verify backup completed successfully
- [ ] Monitor any sensors for data quality issues

**Monthly:**
- [ ] Review automation statistics (execution count, errors)
- [ ] Clean up old logs and backups
- [ ] Update documentation if procedures changed
- [ ] Test rollback procedures (once per quarter)

---

## Summary Table

| Phase | Task | Time | User Input | LLM Output |
|-------|------|------|-----------|-----------|
| 1 | Validate fix files | 1 hr | None | Validation report |
| 1 | Analyze codebase | 1 hr | None | Structure & patterns doc |
| 1 | Inventory entities | 1 hr | None | Entity reference |
| 2.1 | RFID AC filter template | 1 hr | Tag ID (later) | Setup guide + YAML |
| 2.2 | Git setup | 1 hr | None | .gitignore, config, guide |
| 2.3 | Backup automation | 1 hr | Backup service check | Automation YAML |
| 2.4 | YAML linting | 30 min | None | .yamllint config |
| 2.5 | Roller blind template | 1 hr | Blind entity list | Migration guide |
| 2.6 | Motion detection | 1 hr | Integration available | Automation templates |
| 2.7 | Morning routine | 1 hr | Temperature preference | Automation templates |
| 2.8 | Computer desk control | 1 hr | Control method decision | Decision tree doc |
| 3 | Config merge strategy | 1 hr | None | Merge guide |
| 3 | Implementation checklist | 1 hr | None | Master checklist |
| 4 | Quick start guides | 1 hr | None | 8 guides |
| 4 | Troubleshooting guide | 1 hr | None | Troubleshooting doc |
| 4 | Future enhancements | 30 min | None | Enhancement roadmap |
| **User Testing** | **Test fixes** | **2-3 hrs** | **Active testing** | Feedback |
| **User Testing** | **RFID investigation** | **1-2 hrs** | **Investigation** | Documentation |
| **User Deployment** | **Deploy automations** | **2-3 hrs** | **Copy files, test** | Ready-to-deploy code |

---

## LLM Workflow (Recommended Execution Order)

**If running with fresh start:**

Start LLM Session

- Phase 1: Validation & Analysis (2-3 hours)
  - Read all modified config files
  - Validate YAML syntax
  - Create validation report
  - Analyze codebase structure
  - Inventory all entities

- Phase 2: Template Generation (3-4 hours) — can run partially in parallel
  - RFID AC filter template (1 hr)
  - Git setup & pre-commit (1 hr)
  - Backup automation (1 hr)
  - YAML linting config (30 min)
  - Roller blind template (1 hr)
  - Motion detection template (1 hr)
  - Morning routine template (1 hr)
  - Computer desk control template (1 hr)

- Phase 3: Configuration & Merge (2-3 hours)
  - Create merge strategy guide
  - Create implementation checklist
  - Create entity reference spreadsheet
  - Create dependency graph

- Phase 4: Documentation (1-2 hours)
  - Quick start guides (8 features)
  - Troubleshooting guide
  - Future enhancements roadmap

TOTAL LLM TIME: 8-12 hours
USER TIME: 5-7 hours (this week + next week)

---

## Document Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2025-11-17 | 1.0 | Initial comprehensive LLM execution plan |

---

**Status:** Ready for LLM execution
**Last Updated:** 2025-11-17
**Next Review:** After user testing of current fixes (end of week)
