# Computer Desk Power Control Setup Guide

**Status:** Decision Document - Choose Your Implementation Method
**Created:** 2025-11-17
**Prerequisites:** Home Assistant with switch/control integration for your chosen method

---

## Overview

The "Computer Desk" button in Home Assistant can control your computer power in multiple ways. This guide helps you identify which method suits your setup and provides implementation steps for each.

**Current Status:** You have a working `switch.computer_plug_switch` entity that can control power.

---

## Method Decision Tree

### Option A: Wake-on-LAN (WOL) - Recommended for Always-Powered Systems

**Use this if:**
- Your computer is already always-powered or on a UPS
- You just need to wake it from sleep mode
- You want to send a magic packet to boot the computer

**Requirements:**
- Computer with WOL-capable motherboard
- WOL enabled in BIOS
- Computer's MAC address (e.g., `AA:BB:CC:DD:EE:FF`)
- Broadcast IP address (usually your gateway or `255.255.255.255`)

**Advantages:**
- ✅ No additional hardware needed
- ✅ Reliable wake-up mechanism
- ✅ Works even if machine is completely off

**Disadvantages:**
- ❌ Cannot power OFF computer (only wake)
- ❌ Requires BIOS configuration
- ❌ Some networks block broadcast packets

**Complexity:** Medium
**Time to Deploy:** 15-20 minutes

---

### Option B: Smart Outlet / Relay Control - Best for Complete Power Control

**Use this if:**
- You want to turn the computer completely ON and OFF
- You have a smart outlet or relay already installed
- The computer is plugged into `switch.computer_plug_switch`

**Requirements:**
- Smart outlet (TP-Link, Tapo, Meross, etc.) OR
- USB relay connected to Home Assistant
- Computer plugged into the controlled outlet

**Advantages:**
- ✅ Full power control (on/off)
- ✅ Can force shutdown stuck systems
- ✅ Simple toggle button interface
- ✅ Prevents phantom power drain

**Disadvantages:**
- ❌ Forced shutdown can corrupt data
- ❌ Requires additional hardware
- ❌ Loses work not saved

**Complexity:** Low
**Time to Deploy:** 5-10 minutes (hardware already exists)

---

### Option C: Hybrid Approach - Best of Both Worlds

**Use this if:**
- You want both graceful shutdown AND forced power-off
- You have both WOL and smart outlet capabilities

**How it works:**
1. Smart button calls shutdown script first (graceful)
2. Waits 2-3 minutes for OS to shut down
3. If computer is still on, force OFF via smart outlet
4. Power back on via WOL when needed

**Advantages:**
- ✅ Prevents data corruption (graceful shutdown first)
- ✅ Reliable forced-off capability
- ✅ Flexible control

**Disadvantages:**
- ❌ More complex automation
- ❌ Requires two integration points

**Complexity:** High
**Time to Deploy:** 30-40 minutes

---

## Current Setup Status

Based on your Home Assistant configuration:

**✅ Smart Outlet:** You have `switch.computer_plug_switch` available
**⚠️ WOL:** Not yet detected - check if needed
**⚠️ Wake-on-LAN:** Computer BIOS WOL support unknown

---

## Quick Implementation Guide

### For Option B (Recommended - Smart Outlet):

#### Step 1: Create Power Control Script

Add to `config/domains/scripts.yaml`:

```yaml
computer_power_on:
  alias: "Computer - Power On"
  description: "Turn on computer via smart outlet"
  sequence:
    - action: switch.turn_on
      target:
        entity_id: switch.computer_plug_switch
    - action: notify.persistent_notification
      data:
        title: "Computer Power"
        message: "Computer powered on via outlet"
  mode: single

computer_power_off:
  alias: "Computer - Power Off"
  description: "Turn off computer via smart outlet (CAUTION: Force shutdown)"
  sequence:
    - action: notify.persistent_notification
      data:
        title: "Computer Shutdown"
        message: "⚠️ Force powering off computer - ensure all work is saved!"
    - delay:
        seconds: 5
    - action: switch.turn_off
      target:
        entity_id: switch.computer_plug_switch
  mode: single
```

#### Step 2: Add to Dashboard

In `lovelace/cards/computer_desk_control.yaml`:

```yaml
type: vertical-stack
cards:
  - type: heading
    heading: "Computer Desk Control"
    heading_style: title

  - type: grid
    columns: 2
    cards:
      # Power On Button
      - type: button
        name: Power On
        icon: mdi:power-on
        tap_action:
          action: call-service
          service: script.computer_power_on
        card_mod:
          style: |
            ha-card {
              background: linear-gradient(145deg, #059669 0%, #047857 100%);
              color: white;
              border-radius: 12px;
              box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);
            }

      # Power Off Button
      - type: button
        name: Power Off
        icon: mdi:power-off
        tap_action:
          action: call-service
          service: script.computer_power_off
        card_mod:
          style: |
            ha-card {
              background: linear-gradient(145deg, #dc2626 0%, #b91c1c 100%);
              color: white;
              border-radius: 12px;
              box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3);
            }

  # Status Card
  - type: entity
    entity: switch.computer_plug_switch
    name: "Outlet Status"
    icon: mdi:power-plug
```

#### Step 3: Test

1. Run `ha core check` to validate YAML
2. Run `ha core restart`
3. Navigate to dashboard and test buttons
4. Monitor logs for errors: `ha core logs -f`

---

## Verification Checklist

- [ ] Script created and validated
- [ ] Dashboard card displays correctly
- [ ] Power on button works (listen for computer startup sounds)
- [ ] Outlet status shows correct state
- [ ] Power off button works (verify outlet switch off)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Script not found | Verify script name matches exactly, run `ha core restart` |
| Button doesn't respond | Check outlet is properly integrated in HA, test in Developer Tools |
| State doesn't update | Restart the smart outlet integration or the outlet device |
| Notification doesn't show | Verify persistent_notification service is enabled |

---

## Future Enhancements

Once this is working:

1. **Add auto-shutdown:** Create automation to power off after idle period
2. **Add startup delay:** Script to wait for computer to boot before running tasks
3. **Add status display:** Show if computer is responding to ping
4. **Add confirmation dialog:** Require double-tap to power off to prevent accidents

---

## Files Modified

- ✅ `config/domains/scripts.yaml` - Added power control scripts
- ✅ `lovelace/cards/computer_desk_control.yaml` - Created dashboard card
- ✅ `docs/COMPUTER_DESK_CONTROL_DECISION_GUIDE.md` - This file

---

**Next Steps:**
1. Review the scripts above
2. Add them to your scripts.yaml
3. Test the power control buttons
4. Report back with success/issues

