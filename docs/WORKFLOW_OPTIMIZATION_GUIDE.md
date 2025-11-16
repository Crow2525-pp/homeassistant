# Workflow Optimization Guide - Automation vs Voice vs Dashboard

## Philosophy

**Goal:** Minimize dashboard usage by automating everything possible, with voice as the primary manual trigger.

**Priority Order:**
1. **Automation** (Best) - Happens automatically, no interaction needed
2. **Voice** (Good) - Hands-free, natural interaction
3. **Dashboard** (Last Resort) - Visual feedback, complex inputs

---

## Current Workflows Analysis

### 1. Morning Routine

**Current Implementation:** "Good Morning" button on dashboard

**Workflow Steps:**
- Opens blinds and curtains
- Sets occupancy to "Home"
- (Could add: Turn on morning lights, start coffee, etc.)

**Optimization Recommendations:**

✅ **Primary: Automation**
```yaml
# Trigger on:
- First motion detected after 6:00 AM
- OR person arrives home between 6:00-9:00 AM
- OR bedroom lights turned on between 6:00-9:00 AM

# Actions:
- Open blinds/curtains
- Set occupancy to Home
- Turn on kitchen lights if before sunrise
- (Optional) Announce weather forecast
```

🔊 **Backup: Voice Command**
- "Hey Google, good morning"
- Triggers same script as automation
- Used when automation doesn't trigger

📱 **Keep Dashboard Button as Fallback**
- Manual trigger if automation fails
- Useful for guests or unusual schedules

**Priority:** 70% automation, 25% voice, 5% dashboard

---

### 2. Arriving Home

**Current Implementation:** "Arriving Home" button (shows for 30 min after person arrives)

**Workflow Steps:**
- Adjusts climate based on weather
- Turns on lights if after dark
- Sets occupancy to Home

**Optimization Recommendations:**

✅ **Primary: Automation (Already Mostly Automated)**
```yaml
# Trigger on:
- Zone.home count changes from 0 to >0 (someone arrives)

# Actions:
- Wait 2 minutes (time to get inside)
- Check if occupancy is still "Away"
- If yes, run arriving home script
```

🔊 **Voice Redundant** - Already automated well

📱 **Dashboard Button Still Useful**
- Override when automation thinks you're away but you're home
- Manual trigger when tracker fails

**Priority:** 90% automation, 0% voice, 10% dashboard

---

### 3. Leaving Home

**Current Implementation:** "Leaving Home" button

**Workflow Steps:**
- Closes garage door
- Turns off all climate and lights
- Sets occupancy to Away

**Optimization Recommendations:**

✅ **Primary: Automation**
```yaml
# Trigger on:
- Zone.home count changes from >0 to 0 (everyone leaves)
- Front door closes AND no motion for 10 minutes

# Actions:
- Wait 5 minutes (allow for quick returns)
- Check if zone.home still = 0
- If yes, run leaving home script
```

🔊 **Voice Alternative**
- "Hey Google, I'm leaving"
- Useful when you want immediate action (don't wait 5 min)

📱 **Dashboard Button Important**
- Quick trigger before leaving
- Verify garage closed

**Priority:** 60% automation, 25% voice, 15% dashboard

---

### 4. Good Night / Bedtime

**Current Implementation:** "Good Night" button

**Workflow Steps:**
- Closes blinds and curtains
- Turns off lights
- Sets occupancy to Sleeping

**Optimization Recommendations:**

✅ **Primary: Automation**
```yaml
# Trigger on:
- Time: After 9:00 PM AND before 5:00 AM
- Master bedroom lights turned off
- OR no motion detected anywhere for 30 minutes after 9:00 PM

# Actions:
- Close all blinds/curtains
- Turn off all lights (except night lights)
- Set occupancy to Sleeping
- Arm alarm (if configured)
```

🔊 **Voice Primary**
- "Hey Google, good night"
- More reliable than motion detection
- Preferred over automation for explicit control

📱 **Dashboard Button Useful**
- From bedroom while in bed
- Override automation timing

**Priority:** 30% automation, 50% voice, 20% dashboard

---

### 5. Naptime (Kids)

**Current Implementation:** "Naptime" button (shows 12:30 PM - 4:00 PM)

**Workflow Steps:**
- Closes blinds and curtains
- Turns off lights
- Stops music

**Optimization Recommendations:**

✅ **Automation Possible but Not Recommended**
- Naptime is irregular and varies day to day
- False triggers would be disruptive

🔊 **Primary: Voice**
- "Hey Google, naptime"
- Hands-free while holding child
- Most natural interaction

📱 **Dashboard Button as Backup**
- When voice fails
- Visual confirmation of action

**Priority:** 0% automation, 70% voice, 30% dashboard

---

### 6. Play Music

**Current Implementation:** "Play Music" button (now fixed to work!)

**Workflow Steps:**
- Selects WiiM Amp as Spotify output
- Resumes last played music

**Optimization Recommendations:**

🔊 **Primary: Voice**
- "Hey Google, play music in living room"
- "Hey Google, resume music"
- More natural than dashboard

✅ **Automation for Context-Aware Playback**
```yaml
# Auto-play music when:
- Morning routine completes on weekends
- Dinner time (6:00 PM) if someone is cooking (kitchen motion)
```

📱 **Dashboard Button for Convenience**
- Quick resume without speaking
- When in a meeting/call (can't use voice)

**Priority:** 10% automation, 60% voice, 30% dashboard

---

### 7. Read the News

**Current Implementation:** "Read the News" button with room selector (just fixed!)

**Workflow Steps:**
- Select room from dropdown
- Tap button to play news briefing

**Optimization Recommendations:**

🔊 **Primary: Voice (Strongly Recommended)**
- "Hey Google, play the news"
- Google Assistant automatically detects which speaker you used
- No manual room selection needed!
- Built-in news briefings from Google

✅ **Automation for Scheduled News**
```yaml
# Trigger on:
- Morning routine completes (7:00 AM weekdays)
- Playing in kitchen

# Actions:
- Play news briefing on kitchen speaker
```

📱 **Dashboard Button Redundant**
- Voice is better in every way
- Consider removing dashboard button entirely
- OR replace with "News in All Rooms" emergency broadcast

**Recommendation:** Replace dashboard button with automation + voice only

**Priority:** 20% automation, 75% voice, 5% dashboard (or remove)

---

### 8. Climate Control

**Current Implementation:** Multiple automations + dashboard tiles

**Workflow Steps:**
- Check current temperature
- Adjust thermostat settings
- Change preset modes

**Optimization Recommendations:**

✅ **Primary: Automation (Already Well-Automated)**
- Morning heating: ✅ Automated
- Away mode: ✅ Automated
- Door-open shutdown: ✅ Automated
- Seasonal adjustments: ✅ Automated

🔊 **Voice for Manual Overrides**
- "Hey Google, set living room to 22 degrees"
- "Hey Google, turn off living room heater"
- Faster than opening dashboard

📱 **Dashboard for Monitoring**
- Check current temperature
- View automation status
- Debugging
- Rarely for control

**Current Status:** Already optimized!

**Priority:** 85% automation, 10% voice, 5% dashboard

---

### 9. Lighting Control

**Current Implementation:** Light switches on dashboard

**Workflow Steps:**
- Turn lights on/off
- Adjust brightness/color

**Optimization Recommendations:**

✅ **Primary: Automation**
```yaml
# Auto lights:
- Morning: Turn on if before sunrise
- Evening: Turn on at sunset if home
- Motion-activated: Entry areas
- Arriving home: Turn on main lights
- Leaving home: Turn off all lights
```

🔊 **Voice for Specific Control**
- "Hey Google, turn on bedroom light"
- "Hey Google, dim living room lights to 20%"
- "Hey Google, set lights to movie mode"

📱 **Dashboard for Complex Scenes**
- Color adjustments
- Multiple room coordination
- Visual feedback of state

**Priority:** 50% automation, 35% voice, 15% dashboard

---

### 10. Garage Control

**Current Implementation:** Open/Close garage buttons (conditional on state)

**Workflow Steps:**
- Open garage when arriving
- Close garage when leaving or at night

**Optimization Recommendations:**

✅ **Primary: Automation**
```yaml
# Auto close:
- At 10:00 PM if still open (safety)
- 30 minutes after opening if no car detected
- When leaving home

# Auto open:
- When car arrives in driveway (if supported by opener)
```

🔊 **Voice for Manual Control**
- "Hey Google, open garage"
- "Hey Google, close garage"
- Hands-free while carrying items

📱 **Dashboard for Status Check**
- Visual confirmation of state
- Quick close button when in bed
- Security check before sleeping

**Priority:** 40% automation, 40% voice, 20% dashboard

---

### 11. Water Plants

**Current Implementation:** "Water Plants" button (shows when temp > 20°C)

**Workflow Steps:**
- Tap button to run sprinkler
- (Duration controlled by script)

**Optimization Recommendations:**

✅ **Primary: Automation (Time-Based)**
```yaml
# Trigger on:
- 6:00 AM on hot days (max temp > 25°C forecast)
- 6:00 PM on very hot days (max temp > 30°C)
- Skip if rained in last 24 hours

# Actions:
- Run sprinkler for X minutes
- Send notification when complete
```

🔊 **Voice for Ad-Hoc Watering**
- "Hey Google, water the plants"
- When you notice plants looking dry

📱 **Dashboard Button for Manual Override**
- Test sprinkler system
- Extra watering on very hot days

**Priority:** 70% automation, 20% voice, 10% dashboard

---

## Summary: Workflow Priority Matrix

| Workflow | Automation | Voice | Dashboard | Recommendation |
|----------|-----------|-------|-----------|----------------|
| Morning Routine | 70% | 25% | 5% | Add motion-based automation |
| Arriving Home | 90% | 0% | 10% | Already optimized |
| Leaving Home | 60% | 25% | 15% | Add zone-based automation |
| Good Night | 30% | 50% | 20% | Keep balanced |
| Naptime | 0% | 70% | 30% | Voice-first is correct |
| Play Music | 10% | 60% | 30% | Promote voice usage |
| Read News | 20% | 75% | 5% | **Remove dashboard button, voice only** |
| Climate | 85% | 10% | 5% | Already optimized |
| Lighting | 50% | 35% | 15% | Add more automation |
| Garage | 40% | 40% | 20% | Balanced approach |
| Water Plants | 70% | 20% | 10% | Add time-based automation |

---

## Implementation Priorities

### Quick Wins (Implement First)

1. **Replace "Read News" button with voice**
   - Remove dashboard button
   - Create voice routine "Hey Google, news"
   - Add morning automation to play news at 7 AM

2. **Add morning routine automation**
   - Trigger on first motion after 6 AM
   - Reduces dashboard button usage by 70%

3. **Automate evening lights**
   - Turn on at sunset if home
   - Reduces need for light dashboard

### Medium Priority

4. **Add leaving home automation**
   - Trigger when zone.home = 0 for 5 minutes
   - Reduces dashboard button usage

5. **Automate plant watering**
   - Time-based on hot days
   - Reduces dashboard button usage by 70%

### Lower Priority

6. **Add good night automation**
   - Tricky to get right (false triggers)
   - Voice is already working well

7. **Garage auto-close at night**
   - Safety feature
   - Reduces late-night dashboard checks

---

## Voice Command Setup

### Recommended Google Assistant Routines

#### 1. Good Morning
```
Phrase: "Good morning"
Actions:
- Call Home Assistant script: script.good_morning
```

#### 2. Good Night
```
Phrase: "Good night" or "Bedtime"
Actions:
- Call Home Assistant script: script.good_night
```

#### 3. I'm Leaving
```
Phrase: "I'm leaving" or "Goodbye home"
Actions:
- Call Home Assistant script: script.leaving_home
```

#### 4. Naptime
```
Phrase: "Naptime" or "Nap time"
Actions:
- Call Home Assistant script: script.naptime
```

#### 5. Play the News
```
Phrase: "Play the news" or "What's in the news"
Actions:
- Google's built-in news briefing
- OR call Home Assistant script: script.read_news
```

#### 6. Water Plants
```
Phrase: "Water the plants" or "Start sprinkler"
Actions:
- Call Home Assistant script: script.water_plants
```

---

## Dashboard Optimization Post-Migration

### Control Panel (Main Dashboard)

**Keep:**
- Alerts (laundry, garage open, etc.) - Visual notifications needed
- Currently playing media - Visual feedback useful
- Quick action fallback buttons - When voice fails
- HVAC status tiles - Visual temperature monitoring

**Remove/Minimize:**
- Individual light switches - Use voice/automation instead
- Individual media player cards - Use voice instead
- News button - Use voice/automation instead

**New Organization:**
```
┌─────────────────────────────────────┐
│ 🚨 ALERTS (Conditional)            │
├─────────────────────────────────────┤
│ 🎵 NOW PLAYING (Conditional)       │
├─────────────────────────────────────┤
│ 🌡️ CLIMATE QUICK VIEW             │
│  (Thermostats + Current Temps)     │
├─────────────────────────────────────┤
│ ⚡ QUICK ACTIONS                   │
│  (Only context-appropriate ones)   │
├─────────────────────────────────────┤
│ 💡 SCENES (Not individual lights) │
└─────────────────────────────────────┘
```

### Other Dashboards

**Climate:** Debugging only (collapsible sections)
**Energy:** Monitoring only (graphs and stats)
**Media:** Advanced controls only (playlists, sources)
**Network:** Debugging only (hide from nav)
**Alarm:** Visual status + manual arm/disarm

---

## Measuring Success

### Metrics to Track

**Before Optimization:**
- Count how many times you open the app per day
- Track which buttons you use most
- Note when you use dashboard vs voice

**After Optimization:**
- Target: 50% reduction in app opens
- Target: 80% of interactions via voice or automation
- Target: Dashboard only for monitoring and debugging

### User Feedback Questions

After 1 week:
- Which automations triggered when you didn't want them?
- Which voice commands feel natural?
- What still requires the dashboard?

After 1 month:
- What workflows still feel manual?
- What could be further automated?
- Are notifications enough vs checking dashboard?

---

## Next Steps

1. **Review this guide** - Identify which workflows to optimize first
2. **Test voice commands** - Set up Google Assistant routines
3. **Implement quick wins** - News automation, morning routine automation
4. **Monitor usage** - Track how often you use dashboard vs voice
5. **Iterate** - Adjust automations based on actual usage patterns

---

**Generated:** 2025-11-16
**Status:** Ready for implementation
**Goal:** Make Home Assistant invisible - everything just works!
