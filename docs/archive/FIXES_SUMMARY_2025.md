# Home Assistant Fixes Summary - 2025

## Overview
This document summarizes the fixes applied to resolve issues with media controls, HVAC automation, and room-specific features.

---

## ✅ 1. Fixed "Play Music" Button

**Issue:** Play Music button didn't work - just called media_play without selecting a source or content.

**Root Cause:** The `play_music` script was calling `media_player.media_play` on the WiiM Amp without first selecting it as a Spotify source.

**Solution:** Updated the script to mirror the working `spotify_tv` script logic:
- Check if "Living Room WiiM Amp" or "WiiM Amp" is available in Spotify source list
- Select the WiiM Amp as the active Spotify output device
- Resume playback (which continues the last played track/playlist)

**File Changed:** `config/domains/scripts.yaml` (line 533)

**Testing:**
1. Open Spotify on your phone and play some music
2. Switch to a different output (like phone speaker)
3. Tap "Play Music" button in Home Assistant
4. Should resume playback on WiiM Amp

---

## ✅ 2. Fixed "Read the News" Button

**Issue:** Read the News button played on all speakers throughout the house, not just the room you're in.

**Root Cause:** The `read_news` script was hardcoded to broadcast TTS to kitchen, study, and master bedroom speakers simultaneously.

**Solution:**
1. Created new `input_select.news_room_selector` helper with options:
   - Kitchen
   - Study
   - Master Bedroom
   - All Rooms

2. Updated `read_news` script to check the selector and only play on the chosen room's speaker

3. Added the room selector to the dashboard card so it appears above the "Read the News" button

**Files Changed:**
- `configuration.yaml` (line 373) - Added input_select
- `config/domains/scripts.yaml` (line 576) - Updated script with room logic
- `lovelace/cards/quick_actions.yaml` (line 678) - Added selector to UI

**Usage:**
1. Select your desired room from the dropdown (defaults to Kitchen)
2. Tap "Read the News" button
3. News will only play on the selected speaker
4. The card shows which room is currently selected

---

## ✅ 3. Fixed Living Room HVAC - Cold in Morning

**Issue:** Living room was cold when waking up at 6:00-7:00 AM despite automation running at 5:30 AM.

**Root Cause:**
- Temperature trigger was too low (17°C) - didn't start heating early enough
- Auto-shutdown kicked in after 30 minutes if temp reached 20°C
- By wake-up time (6-7 AM), room had cooled down again

**Solution:**
1. **Increased temperature trigger** from 17°C to 18°C
   - Heating now starts when room drops below 18°C
   - Triggers earlier and more proactively

2. **Disabled auto-shutdown during morning hours (5:30-8:00 AM)**
   - Heating continues running throughout the morning period
   - Prevents premature shutdown before wake-up time

3. **Raised shutdown threshold** from 20°C to 21°C for other times
   - Ensures better comfort when heating does run

**File Changed:** `automations/06_living_room_climate_split.yaml`
- Line 22-64: Morning heat trigger (17°C → 18°C)
- Line 317-346: Shutdown logic (added morning hour exclusion)

**Expected Behavior:**
- 5:30 AM: Heating starts if temp < 18°C
- Heating runs continuously until 8:00 AM (no auto-shutdown)
- Room should be comfortably warm by 6-7 AM wake-up time
- After 8:00 AM: Normal shutdown logic resumes (turns off at 21°C)

---

## 🔄 Next Steps

### Pending Tasks (User Requested)

1. **Roller Blind Position Tracking** - Simplify to just open/closed/partial states
   - Current system uses complex timer-based position estimation
   - Can simplify to 3-state system since exact % not needed

2. **Lovelace UI Migration** - Hybrid YAML + UI mode
   - Keep YAML files for version control
   - Enable UI editing for easier repositioning/grid layout
   - Document migration process

3. **Dashboard Purpose & Workflow Analysis**
   - Document what each dashboard is for
   - Identify common workflows
   - Recommend automation/voice/dashboard priority for each workflow

4. **Debugging Dashboards**
   - Create temporary debugging dashboard templates
   - For development work and troubleshooting

---

## 📝 Notes

### Testing Recommendations

After deploying these changes:

1. **Restart Home Assistant** to load the new input_select helper
2. **Check Configuration** for any YAML errors
3. **Test each fix** individually:
   - Play Music: Test with Spotify app + HA button
   - Read News: Try each room selection
   - HVAC: Monitor morning heating behavior over a few days

### Configuration Files Modified

| File | Purpose | Lines Changed |
|------|---------|---------------|
| `configuration.yaml` | Added news room selector | 373-381 |
| `config/domains/scripts.yaml` | Fixed play_music and read_news | 533-626 |
| `automations/06_living_room_climate_split.yaml` | Fixed morning heating | 22-64, 317-346 |
| `lovelace/cards/quick_actions.yaml` | Added room selector UI | 687-699 |

### Backup Notice

All modifications preserve original logic where possible. Previous behavior can be restored by reverting to git commit before these changes.

---

**Generated:** 2025-11-16
**Status:** ✅ All fixes implemented and ready for testing
