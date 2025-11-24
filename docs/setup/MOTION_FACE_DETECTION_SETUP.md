# Motion Detection & Face Recognition Setup Guide

**Created:** 2025-11-17
**Purpose:** Template for motion-triggered alerts with optional face recognition
**Complexity:** Medium-High (requires face detection integration)
**Category:** Security Automation

---

## Overview

This template provides motion-based security alerts with optional face recognition integration (Frigate, Doods, etc.).

**Features:**
- Motion detection with debounce (prevent spam)
- Time-based filtering (night mode vs day mode)
- Unknown person high-priority alerts
- Camera snapshot notifications
- Weekday/weekend different behaviors

---

## Prerequisites

**Required:**
- Motion sensor integrated with HA
- Camera feed accessible
- Notification service configured

**Optional:**
- Face detection integration (Frigate, Double-Take, Doods)
- Trained face models for known persons
- High-priority notification service

**Estimated Time:** 45-60 minutes (without face detection), 2-3 hours (with face detection training)

---

## Quick Start (Motion Only)

### Basic Motion Alert Automation

```yaml
- id: motion_outside_alert
  alias: "Security - Outside Motion Alert"
  trigger:
    - platform: state
      entity_id: binary_sensor.outside_motion
      to: "on"
  condition:
    # Debounce: Only trigger if motion stayed on for 2 seconds
    - condition: state
      entity_id: binary_sensor.outside_motion
      to: "on"
      for:
        seconds: 2
    # Night mode only (8 PM - 6 AM)
    - condition: or
      conditions:
        - condition: time
          after: "20:00:00"
          before: "23:59:59"
        - condition: time
          after: "00:00:00"
          before: "06:00:00"
  action:
    - service: notify.mobile_app_your_phone
      data:
        title: "Motion Detected"
        message: "Outside motion detected at {{ now().strftime('%I:%M %p') }}"
        data:
          image: /api/camera_proxy/camera.outside
  mode: single
```

---

## Advanced: Face Recognition Integration

### With Frigate

**Prerequisites:**
1. Frigate add-on installed
2. Camera configured in Frigate
3. Face recognition enabled

**Automation:**
```yaml
- id: motion_with_face_detection
  alias: "Security - Motion with Face Detection"
  trigger:
    - platform: state
      entity_id: binary_sensor.frigate_person_detected
      to: "on"
  action:
    - choose:
        # Known person
        - conditions:
            - condition: template
              value_template: "{{ trigger.to_state.attributes.person_name != 'unknown' }}"
          sequence:
            - service: notify.persistent_notification
              data:
                title: "Person Detected"
                message: "{{ trigger.to_state.attributes.person_name }} detected"
        # Unknown person - high priority
        - conditions:
            - condition: template
              value_template: "{{ trigger.to_state.attributes.person_name == 'unknown' }}"
          sequence:
            - service: notify.mobile_app_your_phone
              data:
                title: "⚠️ Unknown Person!"
                message: "Unrecognized person detected outside"
                data:
                  priority: high
                  image: /api/frigate/notifications/snapshot.jpg
  mode: single
```

---

## Time-Based Filtering

### Weekday vs Weekend

```yaml
- choose:
    # Weekdays: Alert during work hours (unusual)
    - conditions:
        - condition: time
          weekday: [mon, tue, wed, thu, fri]
        - condition: time
          after: "08:00:00"
          before: "18:00:00"
      sequence:
        - service: notify.mobile_app_your_phone
          data:
            title: "Unexpected Daytime Motion"
            message: "Motion detected while you're usually at work"
            data:
              priority: high

    # Weekends: Standard notification
    - conditions:
        - condition: time
          weekday: [sat, sun]
      sequence:
        - service: notify.persistent_notification
          data:
            title: "Weekend Motion"
            message: "Outside motion detected"
```

---

## Troubleshooting

### Too Many Alerts (Motion Spam)

**Solution:** Increase debounce time

```yaml
condition:
  - condition: state
    entity_id: binary_sensor.motion
    to: "on"
    for:
      seconds: 10  # Increase to 10 seconds
```

### Face Detection Not Working

**Common Issues:**
1. Integration not configured correctly
2. Camera quality too low
3. Face models not trained
4. Lighting conditions poor

**Debug:**
- Check integration logs
- Test face detection in integration UI
- Verify camera feed quality
- Adjust detection sensitivity

---

## Related Documentation

- Template automation: `automations/99_motion_detection_template.yaml`
- Face recognition template: `automations/99_face_recognition_response_template.yaml`
- Frigate integration: https://docs.frigate.video/

---

**Status:** Template ready, requires face detection integration for full features
**Last Updated:** 2025-11-17
