# Complete Entity Inventory

**Generated:** 2025-11-17

This document provides a comprehensive list of all Home Assistant entities.

## Summary

| Domain | Total | Enabled | Disabled |
|--------|-------|---------|----------|
| `alarm_control_panel` | 1 | 1 | 0 |
| `automation` | 157 | 154 | 3 |
| `binary_sensor` | 246 | 174 | 72 |
| `button` | 103 | 86 | 17 |
| `calendar` | 14 | 13 | 1 |
| `camera` | 17 | 9 | 8 |
| `climate` | 8 | 8 | 0 |
| `counter` | 1 | 1 | 0 |
| `cover` | 4 | 4 | 0 |
| `device_tracker` | 142 | 96 | 46 |
| `event` | 4 | 4 | 0 |
| `fan` | 1 | 1 | 0 |
| `image` | 2 | 0 | 2 |
| `input_boolean` | 46 | 46 | 0 |
| `input_button` | 4 | 4 | 0 |
| `input_datetime` | 35 | 35 | 0 |
| `input_number` | 42 | 42 | 0 |
| `input_select` | 5 | 5 | 0 |
| `input_text` | 3 | 3 | 0 |
| `light` | 16 | 13 | 3 |
| `media_player` | 37 | 36 | 1 |
| `number` | 86 | 71 | 15 |
| `person` | 6 | 5 | 1 |
| `remote` | 7 | 6 | 1 |
| `scene` | 8 | 8 | 0 |
| `schedule` | 3 | 3 | 0 |
| `script` | 53 | 53 | 0 |
| `select` | 42 | 31 | 11 |
| `sensor` | 2542 | 1760 | 782 |
| `switch` | 168 | 87 | 81 |
| `tag` | 11 | 11 | 0 |
| `timer` | 1 | 1 | 0 |
| `update` | 105 | 102 | 3 |
| `weather` | 3 | 3 | 0 |
| `zone` | 1 | 1 | 0 |
| **TOTAL** | **3924** | **2877** | **1047** |

---

## Lights

Physical and virtual light entities.

**Total:** 16 (13 enabled, 3 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `light.computer_desk_light_socket_1` | Computer Desk Lamp | switch_as_x |
| `light.dishwasher_smart_plug_dndmode` | Switch | meross_lan |
| `light.led_strip_office_light` | Office Led Strip | zha |
| `light.living_room_light_socket_1` | Living Room Lamp | switch_as_x |
| `light.lounge` | Lounge | group |
| `light.masterbed_lights` | Masterbed Lights | group |
| `light.outdoor_switch_socket_1` | Backyard Lights | switch_as_x |
| `light.reading_light` | Reading Light | tuya |
| `light.sleeping_light_2` | Sleeping Light | tuya |
| `light.study_nook_lamp_socket_1` | Study Nook Lamp | switch_as_x |
| `light.tv_backlight` | TV Lightstrip | template |
| `light.xmas_lights_plug_socket_1` | Heated Blanket | switch_as_x |
| `light.yeelight_color_0x7e3b638` | Floor Lamp | yeelight |

## Switches

Smart switches, outlets, and power control.

**Total:** 168 (87 enabled, 81 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `switch.adguard_home_filtering` | Filtering | adguard |
| `switch.adguard_home_parental_control` | Parental control | adguard |
| `switch.adguard_home_protection` | Protection | adguard |
| `switch.adguard_home_query_log` | Query log | adguard |
| `switch.adguard_home_safe_browsing` | Safe browsing | adguard |
| `switch.adguard_home_safe_search` | Safe search | adguard |
| `switch.better_thermostat_ui_pre_release` | Pre-release | hacs |
| `switch.bi_profile_active` | BI Profile Active | blueiris |
| `switch.bi_profile_inactive` | BI Profile Inactive | blueiris |
| `switch.bi_profile_profile_3` | BI Profile Profile 3 | blueiris |
| `switch.bi_profile_profile_4` | BI Profile Profile 4 | blueiris |
| `switch.bi_profile_profile_5` | BI Profile Profile 5 | blueiris |
| `switch.bi_profile_profile_6` | BI Profile Profile 6 | blueiris |
| `switch.bi_profile_profile_7` | BI Profile Profile 7 | blueiris |
| `switch.bi_profile_work_hours` | BI Profile Work hours | blueiris |
| `switch.bi_schedule_default` | BI Schedule Default | blueiris |
| `switch.cloud_alexa` | Alexa | spook |
| `switch.cloud_alexa_report_state` | Alexa state reporting | spook |
| `switch.cloud_google` | Google Assistant | spook |
| `switch.cloud_google_report_state` | Google Assistant state reporting | spook |
| `switch.cloud_remote` | Remote | spook |
| `switch.computer_desk_light_child_lock` | Child lock | tuya |
| `switch.computer_desk_light_socket_1` | Socket 1 | tuya |
| `switch.computer_desk_light_socket_2` | Socket 2 | tuya |
| `switch.computer_plug_child_lock` | Computer Plug Child lock | zha |
| `switch.computer_plug_switch` | Computer | zha |
| `switch.dinner_table_plug_child_lock` | Dinner Table Plug Child lock | zha |
| `switch.dinner_table_plug_switch` | Dinner Table | zha |
| `switch.dishwasher_smart_plug_config_overtemp_enable` | Config overtemp enable | meross_lan |
| `switch.dishwasher_smart_plug_outlet` | Plug | meross_lan |
| `switch.driveway_cam_email_on_event` | Email on event | reolink |
| `switch.driveway_cam_ftp_upload` | FTP upload | reolink |
| `switch.driveway_cam_infra_red_lights_in_night_mode` | Infrared lights in night mode | reolink |
| `switch.driveway_cam_push_notifications` | Push notifications | reolink |
| `switch.driveway_cam_record` | Record | reolink |
| `switch.driveway_cam_record_audio` | Record audio | reolink |
| `switch.dryer_power_plug_child_lock` | Dryer Power Plug Child lock | zha |
| `switch.dryer_power_plug_switch` | Dryer | zha |
| `switch.espresense_livingroom_arduino_ota` | Arduino OTA | mqtt |
| `switch.espresense_livingroom_auto_update` | Auto Update | mqtt |
| `switch.espresense_livingroom_prerelease` | Prerelease | mqtt |
| `switch.front_door_cam_email_on_event` | Email on event | reolink |
| `switch.front_door_cam_ftp_upload` | FTP upload | reolink |
| `switch.front_door_cam_infra_red_lights_in_night_mode` | Infrared lights in night mode | reolink |
| `switch.front_door_cam_push_notifications_2` | Push notifications | reolink |
| `switch.front_door_cam_record` | Record | reolink |
| `switch.front_door_cam_record_audio_2` | Record audio | reolink |
| `switch.henrys_room_enable_auto_start_stop` | Enable auto start/stop | versatile_thermostat |
| `switch.henrys_room_follow_underlying_temp_change` | Follow underlying temp change | versatile_thermostat |
| `switch.kitchen_smart_plug_child_lock` | Kitchen smart plug Child lock | zha |
| `switch.kitchen_smart_plug_switch` | Kitchen smart plug Switch | zha |
| `switch.living_room_ac_enable_auto_start_stop` | Enable auto start/stop | versatile_thermostat |
| `switch.living_room_ac_follow_underlying_temp_change` | Follow underlying temp change | versatile_thermostat |
| `switch.living_room_light_child_lock` | Child lock | tuya |
| `switch.living_room_light_socket_1` | Socket 1 | tuya |
| `switch.living_room_light_socket_2` | Socket 2 | tuya |
| `switch.masterbed_ac_enable_auto_start_stop` | Enable auto start/stop | versatile_thermostat |
| `switch.masterbed_ac_follow_underlying_temp_change` | Follow underlying temp change | versatile_thermostat |
| `switch.motion_sensor_led_trigger_indicator` | LED trigger indicator | zha |
| `switch.ottos_room_ac_enable_auto_start_stop` | Enable auto start/stop | versatile_thermostat |
| `switch.ottos_room_ac_follow_underlying_temp_change` | Follow underlying temp change | versatile_thermostat |
| `switch.outdoor_switch_socket_1` | Socket 1 | tuya |
| `switch.security_cameras_profile_active` | Security-Cameras Profile Active | blueiris |
| `switch.security_cameras_profile_inactive` | Security-Cameras Profile Inactive | blueiris |
| `switch.security_cameras_profile_profile_3` | Security-Cameras Profile Profile 3 | blueiris |
| `switch.security_cameras_profile_profile_4` | Security-Cameras Profile Profile 4 | blueiris |
| `switch.security_cameras_profile_profile_5` | Security-Cameras Profile Profile 5 | blueiris |
| `switch.security_cameras_profile_profile_6` | Security-Cameras Profile Profile 6 | blueiris |
| `switch.security_cameras_profile_profile_7` | Security-Cameras Profile Profile 7 | blueiris |
| `switch.security_cameras_profile_work_hours` | Security-Cameras Profile Work hours | blueiris |
| `switch.security_cameras_schedule_default` | Security-Cameras Schedule Default | blueiris |
| `switch.server_power_switch_child_lock` | Server power switch Child lock | zha |
| `switch.server_power_switch_switch` | Server | zha |
| `switch.study_nook_lamp_socket_1` | Socket 1 | tuya |
| `switch.usw_16_poe_port_2_poe` | Port 2 PoE | unifi |
| `switch.usw_16_poe_port_3_poe` | Port 3 PoE | unifi |
| `switch.usw_16_poe_port_4_poe` | Port 4 PoE | unifi |
| `switch.usw_16_poe_port_5_poe` | Port 5 PoE | unifi |
| `switch.usw_16_poe_port_6_poe` | Port 6 PoE | unifi |
| `switch.usw_16_poe_port_7_poe` | Port 7 PoE | unifi |
| `switch.usw_16_poe_port_8_poe` | Port 8 PoE | unifi |
| `switch.washing_machine_power_plug_child_lock` | Child lock | zha |
| `switch.washing_machine_power_plug_switch` | Washing Machine | zha |
| `switch.water_switch_switch` | None | zha |
| `switch.water_switch_water_shortage_auto_close` | Water shortage auto-close | zha |
| `switch.xmas_lights_plug_child_lock` | Child lock | tuya |
| `switch.xmas_lights_plug_socket_1` | Socket 1 | tuya |

## Climate Control

HVAC, air conditioning, and heating.

**Total:** 8 (8 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `climate.henry_s_room_versatile_thermostat` | Henrys Room | versatile_thermostat |
| `climate.living_room_ac` | Living Room AC | smartir |
| `climate.living_room_versatile_thermastat` | Living Room AC | versatile_thermostat |
| `climate.masterbed_ac` | Masterbed AC | smartir |
| `climate.masterbed_versatile_thermostat` | Masterbed AC | versatile_thermostat |
| `climate.otto_s_ac` | Otto's AC | smartir |
| `climate.otto_s_room` | Ottos Room AC | versatile_thermostat |
| `climate.study_ac` | Study AC | smartir |

## Covers

Blinds, curtains, shades, and garage doors.

**Total:** 4 (4 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `cover.curtain_3_b3bb` | None | switchbot |
| `cover.roller_blinds_chan1` | Roller blinds (MasterBedroom) | template |
| `cover.smart_garage_door_garage` | Smart Garage Door garage | meross_lan |
| `cover.windowcovering_cover` | None | matter |

## Fans

Ceiling fans and ventilation.

**Total:** 1 (1 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `fan.masterbedroom_fan` | MasterBedroom fan | smartir |

## Automations

All automation entities.

**Total:** 157 (154 enabled, 3 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `automation.530am_living_room_heater_if_cold` | Living Room - Preheat at 5 30 AM if Cold | automation |
| `automation.adjust_floorlamp_based_on_solar_production` | Living Room - Adjust Floor Lamp for Solar Output | automation |
| `automation.amp_backlight_on_off` | Media - Toggle Amp and Backlight | automation |
| `automation.appliance_notifications_actions` | Laundry - Washing Machine Notifications & Actions | automation |
| `automation.appliances_timeout_failsafe` | Appliances - Timeout Failsafe | automation |
| `automation.arm_night_alarm` | Alarmo - Arm Night Routine | automation |
| `automation.automation_33` | Master Bedroom - Bedside Lights at 1 Percent | automation |
| `automation.automation_48` | Alarmo - Follow Occupancy Modes | automation |
| `automation.automation_analytics_anomaly_detection_daily` | Automation Analytics - Anomaly Detection (Daily) | automation |
| `automation.away` | Set Occupancy to Away | automation |
| `automation.bedrooms_overnight_ac_on_hot_days` | Bedrooms - Overnight AC on Hot Days | automation |
| `automation.bedrooms_overnight_frost_protection_no_hot_days` | Bedrooms - Overnight Frost Protection (No Hot Days) | automation |
| `automation.bedrooms_turn_off_overnight_ac_in_morning` | Bedrooms - Turn Off Overnight AC in Morning | automation |
| `automation.blinds_up_if_windy` | Master Bedroom - Raise Blinds When Windy | automation |
| `automation.camera_test_door` | Front Door Camera - Consolidated Motion Detection | automation |
| `automation.change_occupancy_to_holiday_if_alarmo_is` | Occupancy - Set Holiday Mode from Alarmo | automation |
| `automation.climate_auto_detect_season` | Climate - Auto Detect Season | automation |
| `automation.climate_flags_afternoon_re_check_3_4pm` | Climate Flags - Afternoon Re-check (3-4pm) | automation |
| `automation.close_blinds_at_night` | Master Bedroom - Close Blinds for Night Mode | automation |
| `automation.close_master_blinds_and_curtains_if_hot` | Master Bedroom - Close Blinds When Hot | automation |
| `automation.correct_roller_blind_state_on_reset` | Correct Roller Blind State On Reset | automation |
| `automation.cover_control_automation_cca` | Outdoor Blinds - Cover Control Automation | automation |
| `automation.covers_roller_blind_partial_position_stop` | Covers - Roller Blind Partial Position Stop | automation |
| `automation.covers_roller_blind_position_debug_logger` | Covers - Roller Blind Position Debug Logger | automation |
| `automation.covers_roller_blind_timer_finished_full_close` | Covers - Roller Blind Timer Finished (Full Close) | automation |
| `automation.covers_roller_blind_timer_finished_full_open` | Covers - Roller Blind Timer Finished (Full Open) | automation |
| `automation.curtains_cover_automations` | Curtains - Cover Control Automation | automation |
| `automation.dim_the_lights_at_8pm` | Master Bedroom - Dim Lights at 8 PM | automation |
| `automation.disarm_alarm_if_someone_up` | Alarmo - Disarm When Household Awake | automation |
| `automation.dishwasher_appliance_notification` | Laundry - Dishwasher Notifications & Actions | automation |
| `automation.downstairs_doors_group` | Climate - Track Downstairs Door State | automation |
| `automation.driveway_camera_motion_detection` | Driveway Camera - Motion Detection | automation |
| `automation.driveway_motion_detected` | Driveway - Motion Notification | automation |
| `automation.dryer_appliance_notifications_actions` | Laundry - Dryer Notifications & Actions | automation |
| `automation.dryer_v2` | Dryer v2 | automation |
| `automation.energy_high_power_usage_warning` | Energy - High Power Usage Warning | automation |
| `automation.fan_helper` | Master Bedroom - Fan On When AC Starts | automation |
| `automation.fish_not_fed_reminder_dinner` | Aquarium - Dinner Feed Reminder | automation |
| `automation.fish_not_fed_reminder_morning` | Aquarium - Morning Feed Reminder | automation |
| `automation.fishy_are_fed` | Aquarium NFC - Log Feeding Time | automation |
| `automation.fishy_are_fed_2` | Fishy are fed | automation |
| `automation.front_door_camera_motion_detection` | Front Door Camera - Motion Detection | automation |
| `automation.garage_door_cast_front_door_camera_on_open` | Garage Door - Cast Front Door Camera on Open | automation |
| `automation.garage_door_stop_kitchen_stream_on_close` | Garage Door - Stop Kitchen Stream on Close | automation |
| `automation.handle_climate_notification_action_living_room` | Handle Climate Notification Action - Living Room | automation |
| `automation.handle_climate_notification_action_master_bedroom` | Handle Climate Notification Action - Master Bedroom | automation |
| `automation.handle_close_garage_action` | Garage - Handle Close Notification Action | automation |
| `automation.henry_s_room_cooling_night_routine` | Henry's Room - Cooling Night Routine | automation |
| `automation.home` | Set Occupancy to Home | automation |
| `automation.hot_today` | Climate Flags - Mark Hot Day | automation |
| `automation.hvac_kids_room_otto_versatile_climate_manager` | HVAC - Kids Room (Otto) Versatile Climate Manager | automation |
| `automation.hvac_living_room_versatile_climate_manager` | HVAC - Living Room Versatile Climate Manager | automation |
| `automation.hvac_master_bedroom_blinds_temperature_control` | HVAC - Master Bedroom Blinds Temperature Control | automation |
| `automation.hvac_master_bedroom_fan_sync_with_climate` | HVAC - Master Bedroom Fan Sync with Climate | automation |
| `automation.hvac_master_bedroom_versatile_climate_manager` | HVAC - Master Bedroom Versatile Climate Manager | automation |
| `automation.hvac_study_versatile_climate_manager` | HVAC - Study Versatile Climate Manager | automation |
| `automation.ios_actionable_notifications` | iOS Action Button Dispatcher | automation |
| `automation.keep_computer_desk_light_socket_2_always_on` | Keep Computer Desk Light Socket 2 Always On | automation |
| `automation.keep_on` | Living Room - Keep IR Controller Powered | automation |
| `automation.lights_off_if_on_in_morning` | Morning Shutdown for Stray Lights | automation |
| `automation.living_heater_off_at_night` | Living Room - Heater Off Overnight | automation |
| `automation.living_room_away_mode` | Living Room - Away Mode | automation |
| `automation.living_room_away_mode_cool_hot_day` | Living Room - Away Mode Cool (Hot Day) | automation |
| `automation.living_room_daytime_cool_summer` | Living Room - Daytime Cool (Summer) | automation |
| `automation.living_room_daytime_heat_winter` | Living Room - Daytime Heat (Winter) | automation |
| `automation.living_room_dehumidify_high_humidity` | Living Room - Dehumidify (High Humidity) | automation |
| `automation.living_room_morning_heat_winter` | Living Room - Morning Heat (Winter) | automation |
| `automation.living_room_nighttime_frost_protection_winter` | Living Room - Nighttime Frost Protection (Winter) | automation |
| `automation.living_room_shutdown_door_open` | Living Room - Shutdown (Door Open) | automation |
| `automation.living_room_shutdown_manual_override_active` | Living Room - Shutdown (Manual Override Active) | automation |
| `automation.living_room_shutdown_target_temperature_reached` | Living Room - Shutdown (Target Temperature Reached) | automation |
| `automation.lounge_lights_off_at_night` | Living Areas - Lights Off for Night Routine | automation |
| `automation.low_battery_level_detection_notification_for_all_battery_sensors_2` | Battery Alerts - All Sensors | automation |
| `automation.maintenance_ac_filter_change_reminder` | Maintenance - AC Filter Change Reminder | automation |
| `automation.maintenance_clean_toilet` | Maintenance - Clean Master Toilets | automation |
| `automation.maintenance_consolidated_daily_check` | Maintenance - Consolidated Daily Check | automation |
| `automation.maintenance_living_room_ac_filter_changed_nfc` | Maintenance - Living Room AC Filter Changed (NFC) | automation |
| `automation.maintenance_living_room_ac_filter_reminder` | Maintenance - Living Room AC Filter Reminder | automation |
| `automation.maintenance_master_bedroom_ac_filter_changed_nfc` | Maintenance - Master Bedroom AC Filter Changed (NFC) | automation |
| `automation.maintenance_master_bedroom_ac_filter_reminder` | Maintenance - Master Bedroom AC Filter Reminder | automation |
| `automation.maintenance_otto_s_room_ac_filter_changed_nfc` | Maintenance - Otto's Room AC Filter Changed (NFC) | automation |
| `automation.maintenance_otto_s_room_ac_filter_reminder` | Maintenance - Otto's Room AC Filter Reminder | automation |
| `automation.maintenance_study_henry_s_room_ac_filter_changed_nfc` | Maintenance - Study/Henry's Room AC Filter Changed (NFC) | automation |
| `automation.maintenance_study_henry_s_room_ac_filter_reminder` | Maintenance - Study/Henry's Room AC Filter Reminder | automation |
| `automation.master_ac_off_when_wake_up` | Master Bedroom - Turn Off AC on Wake | automation |
| `automation.master_bedroom_cooling_night_assist` | Master Bedroom - Cooling Night Assist | automation |
| `automation.master_bedroom_progressive_heat_management` | Master Bedroom - Solar Assisted Climate Control | automation |
| `automation.master_bedroom_seasonal_climate_manager` | Master Bedroom - Seasonal Climate Manager | automation |
| `automation.masterbed_heater_on_at_night_if_cold` | Master Bedroom - Heater Night Assist | automation |
| `automation.masters_are_sleeping_2` | Master Bedroom - Update Sleeping Status | automation |
| `automation.morning_energy_climate_summary` | Morning - Energy & Climate Summary | automation |
| `automation.morning_open_blinds` | Master Bedroom - Close Blinds on High Humidity | automation |
| `automation.motion_activated_light_2` | Front Entrance - Motion-Activated Light | automation |
| `automation.motion_living_room` | Living Room - Motion Lighting | automation |
| `automation.music_on_in_am` | Morning - Start Music Routine | automation |
| `automation.new_automation` | Driveway Camera - Consolidated Motion Detection | automation |
| `automation.new_automation_2` | Notify Steph When Phil Leaves Work | automation |
| `automation.new_automation_3` | Open Garage When Phil or Steph Arrive Home | automation |
| `automation.new_automation_4` | Morning Wake-Up Lighting Routine | automation |
| `automation.new_automation_5` | Master Bedroom - Keep Lights Dim After Sunrise | automation |
| `automation.new_automation_6` | Living Room - Lights Off When Watching TV | automation |
| `automation.night_bedtime_security_checklist` | Night - Bedtime Security Checklist | automation |
| `automation.night_setback_for_living_room` | Living Room - Night Temperature Setback | automation |
| `automation.nightly_garage_door_check_2` | Nightly Garage Door Check | automation |
| `automation.open_blinds_in_the_morning` | Master Bedroom - Open Blinds for Morning Routine | automation |
| `automation.otto_awake` | Otto's Room - Night Door Alert | automation |
| `automation.otto_s_room_cooling_night_routine` | Otto's Room - Cooling Night Routine | automation |
| `automation.otto_s_room_hvac_if_cold` | Otto's Room - Heater Night Routine | automation |
| `automation.people_home` | Sync People Home Helper | automation |
| `automation.phil_s_left_work` | Phil Leaves Work Alert | automation |
| `automation.presence` | Occupancy - Sync Presence Helper | automation |
| `automation.reading_light_switch` | Master Bedroom Remote - Control Reading Light | automation |
| `automation.reset_daily_automation_trigger_counters_midnight` | Reset Daily Automation Trigger Counters (Midnight) | automation |
| `automation.send_a_camera_snapshot_when_motion_is_detected` | Send Phil a Door Camera Snapshot on Motion | automation |
| `automation.send_a_notification_with_camera_snapshot_when_motion_is_detected_with_blocking_state_and_url_or_lovelace_view_on_click_critical_or_not_collapse_or_not` | Driveway Motion Snapshot for Phil | automation |
| `automation.send_actionable_notifications_for_alarmo` | Alarmo Arming Prompt | automation |
| `automation.send_actionable_notifications_for_workday` | Workday Desk Power Prompt | automation |
| `automation.send_front_door_notification_to_steph` | Front Door - Snapshot Notification for Steph | automation |
| `automation.set_datetime_on_rfid_scan` | Maintenance - Update Cleaning Timestamp via NFC | automation |
| `automation.sleeping_light_seitch` | Master Bedroom Remote - Control Sleeping Light | automation |
| `automation.smart_climate_notification_living_room` | Smart Climate Notification - Living Room | automation |
| `automation.smart_climate_notification_master_bedroom` | Smart Climate Notification - Master Bedroom | automation |
| `automation.solar_available_hide_dashboard_on_kitchen_hub` | Solar Available - Hide Dashboard on Kitchen Hub | automation |
| `automation.solar_available_kitchen_chime` | Solar Available - Kitchen Chime | automation |
| `automation.solar_available_show_dashboard_on_kitchen_hub` | Solar Available - Show Dashboard on Kitchen Hub | automation |
| `automation.sprinkler_on_at_sunrise_if_superhot` | Garden - Run Sprinklers at Sunrise if Hot | automation |
| `automation.stream_cam_to_home_nest` | Kitchen Display - Stream Front Door Camera | automation |
| `automation.study_heater_on_at_night` | Henry's Room - Heater Night Routine | automation |
| `automation.switch_toggle_of_computer_desk` | Study Remote - Toggle Computer Desk | automation |
| `automation.tag_blinds_is_scanned` | Master Bedroom NFC - Control Blinds | automation |
| `automation.tag_masterbed_desk_left_cnr_is_scanned` | Master Bedroom NFC - Heat and Lift Desk Corner | automation |
| `automation.tag_masterbed_desk_left_cnr_is_scanned_2` | Tag Masterbed - Close Blinds Halfway | automation |
| `automation.tag_study_desk_is_scanned` | Study Desk NFC - Toggle Desk Switch | automation |
| `automation.test` | test | automation |
| `automation.theme_set_default_theme` | Theme - Apply Waves on Startup | automation |
| `automation.too_cold_blinds_up_fan_off` | Master Bedroom - Reopen Blinds When Room Cools | automation |
| `automation.track_manual_blind_control` | Automation Tracker - Manual Blind Control | automation |
| `automation.track_manual_climate_control_living_room` | Automation Tracker - Manual Climate Control (Living Room) | automation |
| `automation.track_manual_climate_control_master_bedroom` | Automation Tracker - Manual Climate Control (Master Bedroom) | automation |
| `automation.track_manual_climate_control_otto_s_room` | Automation Tracker - Manual Climate Control (Otto's Room) | automation |
| `automation.track_manual_climate_control_study_henry_s_room` | Automation Tracker - Manual Climate Control (Study / Henry's Room) | automation |
| `automation.turn_off_living_rm_heater_if_hot_enough` | Living Room - Turn Off Heater When Warm | automation |
| `automation.turn_off_study_light` | Reset Occupancy to Home After Wake-Up | automation |
| `automation.turn_on_lights_in_master_bedroom` | Master Bedroom Remote - Toggle Room Lighting | automation |
| `automation.turn_on_lounge_lights_at_20_min_before_sunset` | Living Areas - Lights On Before Sunset | automation |
| `automation.turn_on_xmas_lights_in_am` | Holiday Lights - Turn On Morning Routine | automation |
| `automation.tv_on_off` | Living Room - Sync TV Power and Lighting | automation |
| `automation.update_roller_blind_state_after_movement` | Covers - Refresh Roller Blind Positions | automation |
| `automation.volume_control_wiimamp` | Living Room Audio - Control WiiM Amp Volume | automation |
| `automation.water_10min_only` | Irrigation - Limit Watering to 10 Minutes | automation |
| `automation.water_detected` | Leak Sensors - Notify on Water Detection | automation |
| `automation.workday` | Study - Start Workday Desk Routine | automation |
| `automation.working_from_home` | Detect Working From Home | automation |
| `automation.zha_mijia_wireless_remote_switch_wxkg01lm` | Living Room Remote - Mijia Switch Actions | automation |

## Scripts

Reusable action sequences.

**Total:** 53 (53 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `script.1686171686731` | Master Slow On | script |
| `script.1693262268843` | Blinds Halfway (from any position) | script |
| `script.activate_cooling` | Activate Cooling | script |
| `script.activate_dry_mode` | Activate Dry Mode | script |
| `script.activate_fan_only` | Activate Fan Only | script |
| `script.activate_heating` | Activate Heating | script |
| `script.arriving_home` | Arriving Home | script |
| `script.computer_power_off` | Computer - Power Off | script |
| `script.computer_power_on` | Computer - Power On | script |
| `script.curtains_half_way` | Curtains half way | script |
| `script.deactivate_climate` | Deactivate Climate | script |
| `script.fan_off` | Fan - Off | script |
| `script.fan_speed_1` | Fan - Speed 1 | script |
| `script.fan_speed_3` | Fan - Speed 3 | script |
| `script.fan_speed_6` | Fan - Speed 6 | script |
| `script.garage_door_toggle` | Garage door toggle | script |
| `script.good_morning` | Good Morning | script |
| `script.good_night` | Good Night | script |
| `script.holiday_mode` | Holiday Mode | script |
| `script.leaving_home` | Leaving Home | script |
| `script.led_off_henry` | LED Off - Henry | script |
| `script.morning_news_briefing` | Morning News Briefing | script |
| `script.naptime` | Naptime | script |
| `script.new_roller_blind_down` | New Roller Blind Down | script |
| `script.new_roller_blind_stop` | New Roller Blind Stop | script |
| `script.new_roller_blind_up` | New Roller Blind Up | script |
| `script.new_script` | YouTube | script |
| `script.open_garage` | Open Garage | script |
| `script.play_music` | Play Music | script |
| `script.read_news` | Read the News | script |
| `script.record_climate_trigger` | Record Climate Trigger | script |
| `script.roller_blinds_close_simple` | Roller Blinds Close (Simple) | script |
| `script.roller_blinds_down` | Roller Blinds Down | script |
| `script.roller_blinds_open_simple` | Roller Blinds Open (Simple) | script |
| `script.roller_blinds_set_position_simple` | Roller Blinds Set Position (Simple) | script |
| `script.roller_blinds_stop` | Roller Blinds Stop | script |
| `script.roller_blinds_up` | Roller Blinds Up | script |
| `script.set_climate_mode` | Set Climate Mode | script |
| `script.set_climate_mode_and_preset` | Set Climate Mode and Preset | script |
| `script.set_climate_preset` | Set Climate Preset | script |
| `script.spotify` | Spotify Shortcut | script |
| `script.spotify_music_tv` | Spotify_channel | script |
| `script.spotify_off` | Stop Spotify | script |
| `script.spotify_tv` | Spotify - WiiM Amp | script |
| `script.tv_lights_off` | Tv lights off | script |
| `script.tv_lights_on` | Tv lights on | script |
| `script.tvbrightup` | Tvbrightup | script |
| `script.tvlightbrightdown` | TVlightbrightdown | script |
| `script.volume_high` | Volume High | script |
| `script.volume_medium` | Volume Medium | script |
| `script.volume_quiet` | Volume Quiet | script |
| `script.volume_talking` | Volume Talking | script |
| `script.water_plants` | Water Plants | script |

## Scenes

Preset device configurations.

**Total:** 8 (8 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `scene.blinds_up` | blinds up | homeassistant |
| `scene.living_room_evening` | Living Room Evening | homeassistant |
| `scene.low_brightness_lights` | Low Brightness Lights  | homeassistant |
| `scene.master_bedroom_dimming` | Master Bedroom Dimming | homeassistant |
| `scene.master_bedroom_lights_on` | Master bedroom lights on | homeassistant |
| `scene.new_scene` | Spotify | homeassistant |
| `scene.ottosleep_cool` | OttoSleep(Cool) | homeassistant |
| `scene.ottosleep_heat` | OttoSleep(heat) | homeassistant |

## Input Helpers

### Input Select

**Total:** 5

| Entity ID | Name | Options |
|-----------|------|---------|
| `input_select.climate_season` | Climate Season | summer, autumn, winter, spring |
| `input_select.news_room_selector` | News Room | Kitchen, Study, Master Bedroom, All Rooms |
| `input_select.occupancy` | Occupancy Mode | Home, Away, Holiday, Sleeping |
| `input_select.roller_blind_state` | Roller Blind State |  |
| `input_select.roller_blind_state_simple` | Roller Blind State | closed, partial, open |

### Input Number

**Total:** 42

| Entity ID | Name | Range | Unit |
|-----------|------|-------|------|
| `input_number.afternoon_recheck_triggers_today` | Afternoon Re-check Triggers Today | 0 - 100 | triggers |
| `input_number.children_cooling_night_triggers_today` | Children's Rooms Cooling Night Triggers Today | 0 - 100 | triggers |
| `input_number.climate_flags_mark_hot_day_triggers_today` | Climate Flags - Mark Hot Day Triggers Today | 0 - 100 | triggers |
| `input_number.dishwasher_power_tracker_end` | Dishwasher Power Tracker End |  |  |
| `input_number.dishwasher_power_tracker_start` | Dishwasher Power Tracker Start |  |  |
| `input_number.end_dryer_power_tracker_kwh` | Dryer Power Tracker End |  |  |
| `input_number.evening_cooling_triggers_today` | Evening Cooling Triggers Today | 0 - 100 | triggers |
| `input_number.frost_protection_triggers_today` | Frost Protection Triggers Today | 0 - 100 | triggers |
| `input_number.henrys_room_temp_comfort_high` | Henry's Room Comfort High | 22 - 25 | "°C" |
| `input_number.henrys_room_temp_comfort_low` | Henry's Room Comfort Low | 20 - 23 | "°C" |
| `input_number.henrys_room_temp_heating` | Henry's Room Winter Heating Threshold | 16 - 21 | "°C" |
| `input_number.henrys_room_temp_hot` | Henry's Room Hot Threshold | 23 - 26 | "°C" |
| `input_number.henrys_room_temp_warm` | Henry's Room Warm Threshold | 21 - 25 | "°C" |
| `input_number.living_room_heat_comfort_minutes` | Living Room Heat Comfort Window | 10 - 120 | min |
| `input_number.living_room_heat_lead_minutes` | Living Room Heat Lead Minutes | 0 - 120 | min |
| `input_number.living_room_temp_comfort` | Living Room Comfort Temperature | 18 - 24 | "°C" |
| `input_number.living_room_temp_summer_cool` | Living Room Summer Cooling Threshold | 24 - 32 | "°C" |
| `input_number.living_room_temp_winter_heat` | Living Room Winter Heating Threshold | 16 - 22 | "°C" |
| `input_number.living_room_temp_winter_morning` | Living Room Winter Morning Preheat Threshold | 16 - 21 | "°C" |
| `input_number.master_bedroom_blinds_morning_triggers_today` | Master Bedroom Blinds Morning Triggers Today | 0 - 100 | triggers |
| `input_number.master_bedroom_blinds_night_triggers_today` | Master Bedroom Blinds Night Triggers Today | 0 - 100 | triggers |
| `input_number.master_bedroom_cooling_night_triggers_today` | Master Bedroom Cooling Night Triggers Today | 0 - 100 | triggers |
| `input_number.master_bedroom_temp_comfort_high` | Master Bedroom Comfort High | 20 - 28 | "°C" |
| `input_number.master_bedroom_temp_comfort_low` | Master Bedroom Comfort Low | 16 - 22 | "°C" |
| `input_number.master_bedroom_temp_summer_cool` | Master Bedroom Summer Cooling Threshold | 22 - 28 | "°C" |
| `input_number.master_bedroom_temp_winter_heat` | Master Bedroom Winter Heating Threshold | 14 - 20 | "°C" |
| `input_number.masterbed_temperature` | Masterbed Temperature |  |  |
| `input_number.morning_blinds_triggers_today` | Morning Blinds Triggers Today | 0 - 100 | triggers |
| `input_number.ottos_room_temp_comfort_high` | Otto's Room Comfort High | 19 - 24 | "°C" |
| `input_number.ottos_room_temp_comfort_low` | Otto's Room Comfort Low | 17 - 21 | "°C" |
| `input_number.ottos_room_temp_heating` | Otto's Room Winter Heating Threshold | 16 - 21 | "°C" |
| `input_number.ottos_room_temp_hot` | Otto's Room Hot Threshold | 22 - 26 | "°C" |
| `input_number.ottos_room_temp_very_hot` | Otto's Room Very Hot Threshold | 23 - 28 | "°C" |
| `input_number.ottos_room_temp_warm` | Otto's Room Warm Threshold | 21 - 25 | "°C" |
| `input_number.preheat_triggers_today` | Preheat (5:30am) Triggers Today | 0 - 100 | triggers |
| `input_number.roller_blind_position` | Roller blind position  |  |  |
| `input_number.roller_blind_target_position` | Roller Blind Target Position | 0 - 100 | '%' |
| `input_number.seasonal_climate_triggers_today` | Seasonal Climate Manager Triggers Today | 0 - 100 | triggers |
| `input_number.start_dryer_power_tracker` | Dryer Power Tracker Start |  |  |
| `input_number.temperature_threshold_low` | Temperature_threshold_low |  |  |
| `input_number.washing_power_tracker_end_kwh` | Washing Power Tracker End |  |  |
| `input_number.washing_power_tracker_kwh` | Washing Power Tracker Start |  |  |

### Input Boolean

**Total:** 46

| Entity ID | Name |
|-----------|------|
| `input_boolean.alarmo_actionable_notification` | Alarmo Actionable Notification |
| `input_boolean.anybody_up` | Anybody up |
| `input_boolean.auto_lights` | Auto Lights |
| `input_boolean.blind_manual_control` | Blinds Manual Control Override |
| `input_boolean.camera_notification_cooldown` | Camera notification cooldown |
| `input_boolean.climate_manual_control_living` | Living Room Climate Manual Override |
| `input_boolean.climate_manual_control_master` | Master Bedroom Climate Manual Override |
| `input_boolean.climate_manual_control_otto` | Otto's Room Climate Manual Override |
| `input_boolean.climate_manual_control_study` | Study Climate Manual Override |
| `input_boolean.cold_today_flag` | Cold Day Flag |
| `input_boolean.computer_switch` | Workday Today |
| `input_boolean.cool_only` | Cool only |
| `input_boolean.cool_today_flag` | Cool Day Flag |
| `input_boolean.cooler_sleep_night_auto` | Cooler Sleep Night Auto |
| `input_boolean.dishwasher_on` | Dishwasher On |
| `input_boolean.downstairs_doors_open` | Downstairs Doors Open |
| `input_boolean.dryer_on` | Dryer On |
| `input_boolean.garage_door_notify` | Garage Door Notify |
| `input_boolean.heat_only` | Heat only |
| `input_boolean.henry_automation_killswitch` | Henry Automation Killswitch |
| `input_boolean.home_presence` | Home Presence  |
| `input_boolean.hot_today_flag` | Hot Day Flag |
| `input_boolean.hvac_kids_room_should_be_on` | Kids Room HVAC Should Be On |
| `input_boolean.hvac_living_room_should_be_on` | Living Room HVAC Should Be On |
| `input_boolean.hvac_master_bedroom_should_be_on` | Master Bedroom HVAC Should Be On |
| `input_boolean.hvac_study_should_be_on` | Study HVAC Should Be On |
| `input_boolean.local_network_access` | Local Network Access Mode |
| `input_boolean.manual_adjustment_master_heater` | Manual Adjustment - Master Heater |
| `input_boolean.master_automation_killswitch` | Master Automation Killswitch |
| `input_boolean.masterbed_a_c_sleep_day_setback` | Heater Sleep Day Auto |
| `input_boolean.masterbed_automation_killswitch` | Masterbed Automation Killswitch |
| `input_boolean.masterbed_sleeping` | Masterbed Sleeping |
| `input_boolean.masterbed_thermostat` | Masterbed A/C Sleep Night Setback |
| `input_boolean.network_device_down_notify` | Network Device Down Notify |
| `input_boolean.otto_automation_killswitch` | Otto Automation Killswitch |
| `input_boolean.otto_door_alarm_active` | Otto door alarm active |
| `input_boolean.otto_s_thermostat` | Otto's Thermostat |
| `input_boolean.ottos_door_open` | Ottos Door Open |
| `input_boolean.people_home` | People home |
| `input_boolean.sleep_night_setback` | Heater Sleep Night Auto |
| `input_boolean.study_occupied` | Study_Occupied |
| `input_boolean.super_cold_today` | Super Cold Day Flag |
| `input_boolean.super_hot_today` | Super Hot Day Flag |
| `input_boolean.wan_down_notify` | WAN Down Notify |
| `input_boolean.warm_today_flag` | Warm Day Flag |
| `input_boolean.washing_machine_on` | Washing On |

### Input Datetime

**Total:** 35

| Entity ID | Name |
|-----------|------|
| `input_datetime.ac_filter_living_room` | AC Filter Last Changed - Living Room |
| `input_datetime.ac_filter_master_bedroom` | AC Filter Last Changed - Master Bedroom |
| `input_datetime.ac_filter_otto_room` | AC Filter Last Changed - Otto's Room |
| `input_datetime.ac_filter_study_henry` | AC Filter Last Changed - Study/Henry's Room |
| `input_datetime.bedtime_henry` | Bedtime Henry |
| `input_datetime.bedtime_henry_2` | Bedtime Otto |
| `input_datetime.bedtime_phil_steph` | Bedtime - Phil/Steph |
| `input_datetime.downstairs_toilet_last_cleaned` | Downstairs Toilet Last Cleaned |
| `input_datetime.fish_last_fed` | Fish Last Fed |
| `input_datetime.henry_wake_up` | Wake Up Henry |
| `input_datetime.kids_toilet_last_cleaned` | Kids Toilet |
| `input_datetime.kids_toilet_last_cleaned_2` | Kids Toilet Last Cleaned |
| `input_datetime.last_climate_notification_living` | Last Climate Notification - Living Room |
| `input_datetime.last_climate_notification_master` | Last Climate Notification - Master Bedroom |
| `input_datetime.last_trigger_afternoon_recheck` | Last Trigger - Afternoon Hot Flag Re-check |
| `input_datetime.last_trigger_children_cooling_night` | Last Trigger - Children's Rooms Cooling Night |
| `input_datetime.last_trigger_climate_flags_mark_hot_day` | Last Trigger - Climate Flags Mark Hot Day |
| `input_datetime.last_trigger_evening_cooling` | Last Trigger - Evening Cooling Night |
| `input_datetime.last_trigger_frost_protection` | Last Trigger - Frost Protection Night |
| `input_datetime.last_trigger_master_bedroom_blinds_morning` | Last Trigger - Master Bedroom Blinds Morning |
| `input_datetime.last_trigger_master_bedroom_blinds_night` | Last Trigger - Master Bedroom Blinds Night |
| `input_datetime.last_trigger_master_bedroom_cooling_night` | Last Trigger - Master Bedroom Cooling Night |
| `input_datetime.last_trigger_morning_blinds` | Last Trigger - Morning Blinds Controller |
| `input_datetime.last_trigger_preheat_530am` | Last Trigger - Living Room Preheat 5:30am |
| `input_datetime.last_trigger_seasonal_climate_manager` | Last Trigger - Seasonal Climate Manager |
| `input_datetime.living_room_last_seen_datetime` | living room last seen datetime |
| `input_datetime.main_toilet_last_cleaned` | Main Toilet |
| `input_datetime.masterbed_last_update_datetime` | Masterbed last update datetime |
| `input_datetime.masterbed_toilet_last_cleaned` | Master bed Toilet |
| `input_datetime.masterbed_toilet_last_cleaned_2` | Master Toilet Last Cleaned |
| `input_datetime.omas_toilet_last_cleaned` | Omas Toilet |
| `input_datetime.omas_toilet_last_cleaned_2` | Oma's Toilet Last Cleaned |
| `input_datetime.otto_s_wake_up` | Wake Up Otto |
| `input_datetime.wakeup_time_phil_steph` | Wake Up Phil/Steph |
| `input_datetime.workday_end` | Workday End |

### Input Text

**Total:** 3

| Entity ID | Name |
|-----------|------|
| `input_text.cover_status_helper` | Roller Blinds Cover Status Helper |
| `input_text.cover_status_helper_curtains` | Curtains Cover Status Helper |
| `input_text.cover_status_last_used` | Cover status last used |

### Input Button

**Total:** 4

| Entity ID | Name |
|-----------|------|
| `input_button.bedtime_phil_steph` | Bedtime - Phil/Steph |
| `input_button.iphone_notification` | IPhone Notification |
| `input_button.wake_up_phil_steph` | Wake Up Phil/Steph |
| `input_button.wake_up_start` | Wake up start |

## Sensors

Temperature, humidity, power, and monitoring sensors.

**Total:** 2542 (1760 enabled, 782 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `sensor.240601571_sva_rx` | RX | unifi |
| `sensor.240601571_sva_tx` | TX | unifi |
| `sensor.a4c138f1205c_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.a4c138f1205c_battery_plus` | Battery+ | battery_notes |
| `sensor.a4c138f1205c_battery_type` | Battery type | battery_notes |
| `sensor.active_issues` | Active | spook |
| `sensor.adguard_home_average_processing_speed` | Average processing speed | adguard |
| `sensor.adguard_home_dns_queries` | DNS queries | adguard |
| `sensor.adguard_home_dns_queries_blocked` | DNS queries blocked | adguard |
| `sensor.adguard_home_dns_queries_blocked_ratio` | DNS queries blocked ratio | adguard |
| `sensor.adguard_home_parental_control_blocked` | Parental control blocked | adguard |
| `sensor.adguard_home_safe_browsing_blocked` | Safe browsing blocked | adguard |
| `sensor.adguard_home_safe_searches_enforced` | Safe searches enforced | adguard |
| `sensor.air_quality` | Air quality | spook |
| `sensor.alarm_control_panels` | Alarm control panels | spook |
| `sensor.amplifier_rx` | RX | unifi |
| `sensor.amplifier_tx` | TX | unifi |
| `sensor.aolt002068_rx` | RX | unifi |
| `sensor.aolt002068_rx_2` | RX | unifi |
| `sensor.aolt002068_tx` | TX | unifi |
| `sensor.aolt002068_tx_2` | TX | unifi |
| `sensor.appliance_recommendation` | Appliance Recommendation | template |
| `sensor.aqara_motion_and_light_sensor_p2_battery` | Battery | matter |
| `sensor.aqara_motion_and_light_sensor_p2_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.aqara_motion_and_light_sensor_p2_battery_plus` | Battery+ | battery_notes |
| `sensor.aqara_motion_and_light_sensor_p2_battery_type` | Battery type | matter |
| `sensor.aqara_motion_and_light_sensor_p2_battery_type_2` | Battery type | battery_notes |
| `sensor.aqara_motion_and_light_sensor_p2_battery_voltage` | Battery voltage | matter |
| `sensor.aqara_motion_and_light_sensor_p2_illuminance` | Illuminance | matter |
| `sensor.areas` | Areas | spook |
| `sensor.automations` | Automations | spook |
| `sensor.backup_backup_manager_state` | Backup Manager state | backup |
| `sensor.backup_last_attempted_automatic_backup` | Last attempted automatic backup | backup |
| `sensor.backup_last_successful_automatic_backup` | Last successful automatic backup | backup |
| `sensor.backup_next_scheduled_automatic_backup` | Next scheduled automatic backup | backup |
| `sensor.balcony_door_sensor_magnet_battery_2` | balcony door sensor magnet Battery | zha |
| `sensor.balcony_door_sensor_magnet_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.balcony_door_sensor_magnet_battery_plus` | Battery+ | battery_notes |
| `sensor.balcony_door_sensor_magnet_battery_type` | Battery type | battery_notes |
| `sensor.balcony_door_sensor_magnet_device_temperature_2` | balcony door sensor magnet Device temperature | zha |
| `sensor.bermuda_0c_7e_24_58_96_65_area` | Area | bermuda |
| `sensor.bermuda_0c_7e_24_58_96_65_distance` | Distance | bermuda |
| `sensor.bermuda_0c_7e_24_58_96_65_floor` | Floor | bermuda |
| `sensor.bermuda_14_13_0b_23_80_9c_area` | Area | bermuda |
| `sensor.bermuda_14_13_0b_23_80_9c_distance` | Distance | bermuda |
| `sensor.bermuda_14_13_0b_23_80_9c_floor` | Floor | bermuda |
| `sensor.bermuda_14_13_0b_39_e8_a9_area` | Area | bermuda |
| `sensor.bermuda_14_13_0b_39_e8_a9_distance` | Distance | bermuda |
| `sensor.bermuda_14_13_0b_39_e8_a9_floor` | Floor | bermuda |
| `sensor.bermuda_14_13_0b_f9_cd_25_area` | Area | bermuda |
| `sensor.bermuda_14_13_0b_f9_cd_25_distance` | Distance | bermuda |
| `sensor.bermuda_14_13_0b_f9_cd_25_floor` | Floor | bermuda |
| `sensor.bermuda_global_active_proxy_count` | Active proxy count | bermuda |
| `sensor.bermuda_global_total_device_count` | Total device count | bermuda |
| `sensor.bermuda_global_total_proxy_count` | Total proxy count | bermuda |
| `sensor.bermuda_global_visible_device_count` | Visible device count | bermuda |
| `sensor.bibi_air_rx` | RX | unifi |
| `sensor.bibi_air_tx` | TX | unifi |
| `sensor.binary_sensors` | Binary sensors | spook |
| `sensor.ble_battery_a4c138a817fd` | ble battery A4C138A817FD | ble_monitor |
| `sensor.ble_battery_a4c138f1205c` | ble battery A4C138F1205C | ble_monitor |
| `sensor.ble_battery_front_door` | ble battery Front Door | ble_monitor |
| `sensor.ble_battery_kitchen_temp_humidity_sensor` | ble battery Kitchen Temp/Humidity Sensor | ble_monitor |
| `sensor.ble_battery_masterbed_temp_humidity_sensor` | ble battery Masterbed Temp/Humidity Sensor | ble_monitor |
| `sensor.ble_battery_wendys_room` | ble battery Wendy's Room | ble_monitor |
| `sensor.ble_humidity_a4c138a817fd` | ble humidity A4C138A817FD | ble_monitor |
| `sensor.ble_humidity_a4c138f1205c` | ble humidity A4C138F1205C | ble_monitor |
| `sensor.ble_humidity_front_door` | ble humidity Front Door | ble_monitor |
| `sensor.ble_humidity_kitchen_temp_humidity_sensor` | Kitchen Humidity Sensor | ble_monitor |
| `sensor.ble_humidity_masterbed_temp_humidity_sensor` | Masterbed Humidity Sensor | ble_monitor |
| `sensor.ble_humidity_wendys_room` | Wendy's Room Humidity Sensor | ble_monitor |
| `sensor.ble_mac_49df4b50b1fd4acf99bc980f834d86dd` | ble mac 49DF4B50B1FD4ACF99BC980F834D86DD | ble_monitor |
| `sensor.ble_mac_e2c56db5dffb48d2b060d0f5a71096e0` | ble mac E2C56DB5DFFB48D2B060D0F5A71096E0 | ble_monitor |
| `sensor.ble_major_49df4b50b1fd4acf99bc980f834d86dd` | ble major 49DF4B50B1FD4ACF99BC980F834D86DD | ble_monitor |
| `sensor.ble_major_e2c56db5dffb48d2b060d0f5a71096e0` | ble major E2C56DB5DFFB48D2B060D0F5A71096E0 | ble_monitor |
| `sensor.ble_measured_power_49df4b50b1fd4acf99bc980f834d86dd` | ble measured power 49DF4B50B1FD4ACF99BC980F834D86DD | ble_monitor |
| `sensor.ble_measured_power_e2c56db5dffb48d2b060d0f5a71096e0` | ble measured power E2C56DB5DFFB48D2B060D0F5A71096E0 | ble_monitor |
| `sensor.ble_minor_49df4b50b1fd4acf99bc980f834d86dd` | ble minor 49DF4B50B1FD4ACF99BC980F834D86DD | ble_monitor |
| `sensor.ble_minor_e2c56db5dffb48d2b060d0f5a71096e0` | ble minor E2C56DB5DFFB48D2B060D0F5A71096E0 | ble_monitor |
| `sensor.ble_rssi_49df4b50b1fd4acf99bc980f834d86dd` | ble rssi 49DF4B50B1FD4ACF99BC980F834D86DD | ble_monitor |
| `sensor.ble_rssi_a4c138a817fd` | ble rssi A4C138A817FD | ble_monitor |
| `sensor.ble_rssi_a4c138f1205c` | ble rssi A4C138F1205C | ble_monitor |
| `sensor.ble_rssi_e2c56db5dffb48d2b060d0f5a71096e0` | ble rssi E2C56DB5DFFB48D2B060D0F5A71096E0 | ble_monitor |
| `sensor.ble_rssi_front_door` | ble rssi Front Door | ble_monitor |
| `sensor.ble_rssi_kitchen_temp_humidity_sensor` | ble rssi Kitchen Temp/Humidity Sensor | ble_monitor |
| `sensor.ble_rssi_masterbed_temp_humidity_sensor` | ble rssi Masterbed Temp/Humidity Sensor | ble_monitor |
| `sensor.ble_rssi_wendys_room` | ble rssi Wendy's Room | ble_monitor |
| `sensor.ble_temperature_a4c138a817fd` | ble temperature A4C138A817FD | ble_monitor |
| `sensor.ble_temperature_a4c138f1205c` | ble temperature A4C138F1205C | ble_monitor |
| `sensor.ble_temperature_front_door` | ble temperature Front Door | ble_monitor |
| `sensor.ble_temperature_kitchen_temp_humidity_sensor` | Kitchen Temperature Sensor | ble_monitor |
| `sensor.ble_temperature_masterbed_temp_humidity_sensor` | Masterbed Temperature Sensor | ble_monitor |
| `sensor.ble_temperature_wendys_room` | Wendy's Room Temperature Sensor | ble_monitor |
| `sensor.ble_voltage_a4c138a817fd` | ble voltage A4C138A817FD | ble_monitor |
| `sensor.ble_voltage_a4c138f1205c` | ble voltage A4C138F1205C | ble_monitor |
| `sensor.ble_voltage_front_door` | ble voltage Front Door | ble_monitor |
| `sensor.ble_voltage_kitchen_temp_humidity_sensor` | ble voltage Kitchen Temp/Humidity Sensor | ble_monitor |
| `sensor.ble_voltage_masterbed_temp_humidity_sensor` | ble voltage Masterbed Temp/Humidity Sensor | ble_monitor |
| `sensor.ble_voltage_wendys_room` | ble voltage Wendy's Room | ble_monitor |
| `sensor.braybrook_temp_max_0` | Braybrook Temp Max 0 | bureau_of_meteorology |
| `sensor.braybrook_temp_max_0_2` | Braybrook Temp Max 0 | template |
| `sensor.braybrook_temp_max_1` | Braybrook Temp Max 1 | bureau_of_meteorology |
| `sensor.braybrook_temp_max_2` | Braybrook Temp Max 2 | bureau_of_meteorology |
| `sensor.braybrook_temp_max_3` | Braybrook Temp Max 3 | bureau_of_meteorology |
| `sensor.braybrook_temp_min_0` | Braybrook Temp Min 0 | bureau_of_meteorology |
| `sensor.braybrook_temp_min_0_2` | Braybrook Temp Min 0 | template |
| `sensor.braybrook_temp_min_1` | Braybrook Temp Min 1 | bureau_of_meteorology |
| `sensor.braybrook_temp_min_2` | Braybrook Temp Min 2 | bureau_of_meteorology |
| `sensor.braybrook_temp_min_3` | Braybrook Temp Min 3 | bureau_of_meteorology |
| `sensor.braybrook_uv_category_0` | Braybrook Uv Category 0 | bureau_of_meteorology |
| `sensor.braybrook_uv_category_1` | Braybrook Uv Category 1 | bureau_of_meteorology |
| `sensor.braybrook_uv_category_2` | Braybrook Uv Category 2 | bureau_of_meteorology |
| `sensor.braybrook_uv_category_3` | Braybrook Uv Category 3 | bureau_of_meteorology |
| `sensor.braybrook_warnings` | Braybrook Warnings | bureau_of_meteorology |
| `sensor.buttons` | Buttons | spook |
| `sensor.calendars` | Calendars | spook |
| `sensor.cameras` | Cameras | spook |
| `sensor.chips_air_rx` | RX | unifi |
| `sensor.chips_air_tx` | TX | unifi |
| `sensor.climate` | Climate | spook |
| `sensor.cold_weather_alert` | Cold Weather Alert | template |
| `sensor.colin_s_s24_rx` | RX | unifi |
| `sensor.colin_s_s24_tx` | TX | unifi |
| `sensor.computer_plug_current` | Computer Plug Current | zha |
| `sensor.computer_plug_power` | Computer Plug Power | zha |
| `sensor.computer_plug_summation_delivered_2` | Computer Plug Summation delivered | zha |
| `sensor.computer_plug_voltage` | Computer Plug Voltage | zha |
| `sensor.computer_switch_rx` | RX | unifi |
| `sensor.computer_switch_tx` | TX | unifi |
| `sensor.computer_switch_uptime` | Uptime | unifi |
| `sensor.covers` | Covers | spook |
| `sensor.curtain_3_b3bb_battery` | Battery | switchbot |
| `sensor.curtain_3_b3bb_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.curtain_3_b3bb_battery_plus` | Battery+ | battery_notes |
| `sensor.curtain_3_b3bb_battery_type` | Battery type | battery_notes |
| `sensor.curtain_3_b3bb_light_level` | Light level | switchbot |
| `sensor.curtain_brightness_status` | Curtain Brightness Status | template |
| `sensor.curtain_close_decision` | Curtain Close Decision | template |
| `sensor.custom_integrations` | Custom integrations | spook |
| `sensor.dates` | Dates | spook |
| `sensor.datetimes` | Date/times | spook |
| `sensor.debian_rx` | RX | unifi |
| `sensor.debian_tx` | TX | unifi |
| `sensor.desktop_9viu335_rx` | RX | unifi |
| `sensor.desktop_9viu335_tx` | TX | unifi |
| `sensor.device_trackers` | Device trackers | spook |
| `sensor.devices` | Devices | spook |
| `sensor.dinner_table_plug_current` | Dinner Table Plug Current | zha |
| `sensor.dinner_table_plug_power` | Dinner Table Plug Power | zha |
| `sensor.dinner_table_plug_summation_delivered` | Dinner Table Plug Summation delivered | zha |
| `sensor.dinner_table_plug_voltage` | Dinner Table Plug Voltage | zha |
| `sensor.dishwasher_estimated_remaining` | Dishwasher Estimated Remaining | template |
| `sensor.dishwasher_last_changed` | Dishwasher last changed | template |
| `sensor.dishwasher_random_message` | Dishwasher Random Message | template |
| `sensor.dishwasher_smart_plug_config_overtemp_type` | Config overtemp type | meross_lan |
| `sensor.dishwasher_smart_plug_consumption` | Consumption | meross_lan |
| `sensor.dishwasher_smart_plug_energy_estimate` | Energy estimate | meross_lan |
| `sensor.dishwasher_smart_plug_rx` | RX | unifi |
| `sensor.dishwasher_smart_plug_signal_strength` | Dishwasher Smart Plug signal_strength | meross_lan |
| `sensor.dishwasher_smart_plug_tx` | TX | unifi |
| `sensor.disk_pve_001_1e6164_dev_sdb_airflow_temperature` | Airflow temperature | proxmoxve |
| `sensor.disk_pve_001_1e6164_dev_sdb_node` | Node | proxmoxve |
| `sensor.disk_pve_001_1e6164_dev_sdb_power_cycles` | Power cycles | proxmoxve |
| `sensor.disk_pve_001_1e6164_dev_sdb_power_on_hours` | Power-on hours | proxmoxve |
| `sensor.disk_pve_001_1e6164_dev_sdb_size` | Size | proxmoxve |
| `sensor.disk_pve_001_1e6164_dev_sdb_temperature` | Temperature | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdc_airflow_temperature` | Airflow temperature | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdc_node` | Node | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdc_power_cycles` | Power cycles | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdc_power_on_hours` | Power-on hours | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdc_size` | Size | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdc_temperature` | Temperature | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdd_airflow_temperature` | Airflow temperature | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdd_node` | Node | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdd_power_cycles` | Power cycles | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdd_power_on_hours` | Power-on hours | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdd_size` | Size | proxmoxve |
| `sensor.disk_pve_003_2cy186_dev_sdd_temperature` | Temperature | proxmoxve |
| `sensor.disk_pve_004_2cv104_dev_sda_airflow_temperature` | Airflow temperature | proxmoxve |
| `sensor.disk_pve_004_2cv104_dev_sda_node` | Node | proxmoxve |
| `sensor.disk_pve_004_2cv104_dev_sda_power_cycles` | Power cycles | proxmoxve |
| `sensor.disk_pve_004_2cv104_dev_sda_power_on_hours` | Power-on hours | proxmoxve |
| `sensor.disk_pve_004_2cv104_dev_sda_size` | Size | proxmoxve |
| `sensor.disk_pve_004_2cv104_dev_sda_temperature` | Temperature | proxmoxve |
| `sensor.disk_pve_samsung_ssd_980_500gb_dev_nvme0n1_node` | Node | proxmoxve |
| `sensor.disk_pve_samsung_ssd_980_500gb_dev_nvme0n1_power_cycles` | Power cycles | proxmoxve |
| `sensor.disk_pve_samsung_ssd_980_500gb_dev_nvme0n1_power_on_hours` | Power-on hours | proxmoxve |
| `sensor.disk_pve_samsung_ssd_980_500gb_dev_nvme0n1_size` | Size | proxmoxve |
| `sensor.disk_pve_samsung_ssd_980_500gb_dev_nvme0n1_temperature` | Temperature | proxmoxve |
| `sensor.disk_pve_samsung_ssd_980_500gb_dev_nvme0n1_wearout` | Wearout | proxmoxve |
| `sensor.docker_rx` | RX | unifi |
| `sensor.docker_tx` | TX | unifi |
| `sensor.downstairs_toilet_last_cleaned_date` | Downstairs Toilet Last Cleaned Date | template |
| `sensor.driveway_cam_day_night_state` | Day night state | reolink |
| `sensor.driveway_cam_rx` | RX | unifi |
| `sensor.driveway_cam_tx` | TX | unifi |
| `sensor.dryer_estimated_remaining` | Dryer Estimated Remaining | template |
| `sensor.dryer_last_changed` | Dryer Last Changed | template |
| `sensor.dryer_power_plug_current` | Dryer Power Plug Current | zha |
| `sensor.dryer_power_plug_power` | Dryer Power Plug Power | zha |
| `sensor.dryer_power_plug_summation_delivered` | Dryer Power Plug Summation delivered | zha |
| `sensor.dryer_power_plug_voltage` | Dryer Power Plug Voltage | zha |
| `sensor.dryer_random_message` | Dryer Random Message | template |
| `sensor.entities` | Entities | spook |
| `sensor.esphome_web_286c10_rx` | RX | unifi |
| `sensor.esphome_web_286c10_tx` | TX | unifi |
| `sensor.esphome_web_f57460_henrysroom_temperature_last_seen` | HenrysRoom Temperature Last Seen | esphome |
| `sensor.esphome_web_f57460_ottosroom_temperature_last_seen` | OttosRoom Temperature Last Seen | esphome |
| `sensor.espresense_livingroom_free_mem` | Free Mem | mqtt |
| `sensor.espresense_livingroom_rx` | RX | unifi |
| `sensor.espresense_livingroom_tx` | TX | unifi |
| `sensor.espresense_livingroom_uptime` | Uptime | mqtt |
| `sensor.espressif_rx` | RX | unifi |
| `sensor.espressif_tx` | TX | unifi |
| `sensor.essendon_airport_gust_speed_kilometre` | Essendon Airport Gust Speed Kilometre | bureau_of_meteorology |
| `sensor.essendon_airport_humidity` | Essendon Airport Humidity | bureau_of_meteorology |
| `sensor.essendon_airport_max_temp` | Essendon Airport Max Temp | bureau_of_meteorology |
| `sensor.essendon_airport_min_temp` | Essendon Airport Min Temp | bureau_of_meteorology |
| `sensor.essendon_airport_rain_since_9am` | Essendon Airport Rain Since 9Am | bureau_of_meteorology |
| `sensor.essendon_airport_temp` | Essendon Airport Temp | bureau_of_meteorology |
| `sensor.essendon_airport_temp_feels_like` | Essendon Airport Temp Feels Like | bureau_of_meteorology |
| `sensor.essendon_airport_wind_direction` | Essendon Airport Wind Direction | bureau_of_meteorology |
| `sensor.essendon_airport_wind_speed_kilometre` | Essendon Airport Wind Speed Kilometre | bureau_of_meteorology |
| `sensor.fans` | Fans | spook |
| `sensor.foxtel_mx6505nf_021018135030754_rx` | RX | unifi |
| `sensor.foxtel_mx6505nf_021018135030754_tx` | TX | unifi |
| `sensor.front_door_button_switch_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.front_door_button_switch_battery_plus` | Battery+ | battery_notes |
| `sensor.front_door_button_switch_battery_type` | Battery type | battery_notes |
| `sensor.front_door_cam_day_night_state` | Day night state | reolink |
| `sensor.front_door_cam_rx` | RX | unifi |
| `sensor.front_door_cam_tx` | TX | unifi |
| `sensor.front_door_water_sensor_battery` | Front door water sensor Battery | zha |
| `sensor.front_door_water_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.front_door_water_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.front_door_water_sensor_battery_type` | Battery type | battery_notes |
| `sensor.front_door_water_sensor_device_temperature` | Front door water sensor Device temperature | zha |
| `sensor.galaxy_s23_rx` | RX | unifi |
| `sensor.galaxy_s23_tx` | TX | unifi |
| `sensor.galaxy_tab_a_rx` | RX | unifi |
| `sensor.galaxy_tab_a_tx` | TX | unifi |
| `sensor.galaxy_tab_s2_rx` | RX | unifi |
| `sensor.galaxy_tab_s2_tx` | TX | unifi |
| `sensor.gateway_base_url` | Gateway Base URL | template |
| `sensor.genericswitch_current_switch_position` | Current switch position | matter |
| `sensor.genericswitch_current_switch_position_2` | Current switch position | matter |
| `sensor.google_home_mini_rx` | RX | unifi |
| `sensor.google_home_mini_rx_2` | RX | unifi |
| `sensor.google_home_mini_tx` | TX | unifi |
| `sensor.google_home_mini_tx_2` | TX | unifi |
| `sensor.gosungrow` | GoSungrow | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_0` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_1` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_10` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_11` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_2` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_3` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_4` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_5` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_6` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_7` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_8` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_actual_energy_9` | GoSungrow 1205796 - actual_energy - ActualEnergy - Actual Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_alarm_count` | GoSungrow getPsDetail.1205796.alarm_count | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_area_type` | GoSungrow getPsDetail.1205796.area_type | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_build_date` | GoSungrow getPsDetail.1205796.build_date | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_co2_reduce` | GoSungrow getPsDetail.1205796.co2_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_co2_reduce_total` | GoSungrow getPsDetail.1205796.co2_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_coal_reduce` | GoSungrow getPsDetail.1205796.coal_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_coal_reduce_total` | GoSungrow getPsDetail.1205796.coal_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_connect_type` | GoSungrow getPsDetail.1205796.connect_type | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_curr_power` | GoSungrow getPsDetail.1205796.curr_power | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_data_last_update_time` | GoSungrow getPsDetail.1205796.data_last_update_time | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_day_eq_hours` | GoSungrow getPsDetail.1205796.day_eq_hours | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_design_capacity` | GoSungrow getPsDetail.1205796.design_capacity | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_diagram_url` | GoSungrow getPsDetail.1205796.diagram_url | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_expect_install_date` | GoSungrow getPsDetail.1205796.expect_install_date | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_fault_count` | GoSungrow getPsDetail.1205796.fault_count | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_gcj_latitude` | GoSungrow getPsDetail.1205796.gcj_latitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_gcj_longitude` | GoSungrow getPsDetail.1205796.gcj_longitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_gprs_latitude` | GoSungrow getPsDetail.1205796.gprs_latitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_gprs_longitude` | GoSungrow getPsDetail.1205796.gprs_longitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_has_ammeter` | GoSungrow getPsDetail.1205796.has_ammeter | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_images_0_file_id` | GoSungrow getPsDetail.1205796.images.0.file_id | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_images_0_id` | GoSungrow getPsDetail.1205796.images.0.id | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_images_0_pic_language` | GoSungrow getPsDetail.1205796.images.0.pic_language | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_images_0_pic_type` | GoSungrow getPsDetail.1205796.images.0.pic_type | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_images_0_picture_name` | GoSungrow getPsDetail.1205796.images.0.picture_name | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_images_0_picture_url` | GoSungrow getPsDetail.1205796.images.0.picture_url | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_images_0_ps_id` | GoSungrow getPsDetail.1205796.images.0.ps_id | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_install_date` | GoSungrow getPsDetail.1205796.install_date | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_installer_ps_fault_status` | GoSungrow getPsDetail.1205796.installer_ps_fault_status | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_is_have_es_inverter` | GoSungrow getPsDetail.1205796.is_have_es_inverter | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_is_transform_system` | GoSungrow getPsDetail.1205796.is_transform_system | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_is_tuv` | GoSungrow getPsDetail.1205796.is_tuv | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_latitude` | GoSungrow getPsDetail.1205796.latitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_longitude` | GoSungrow getPsDetail.1205796.longitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_map_latitude` | GoSungrow getPsDetail.1205796.map_latitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_map_longitude` | GoSungrow getPsDetail.1205796.map_longitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_meter_reduce` | GoSungrow getPsDetail.1205796.meter_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_meter_reduce_total` | GoSungrow getPsDetail.1205796.meter_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_month_energy` | GoSungrow getPsDetail.1205796.month_energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_month_eq_hours` | GoSungrow getPsDetail.1205796.month_eq_hours | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_month_income` | GoSungrow getPsDetail.1205796.month_income | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_nox_reduce` | GoSungrow getPsDetail.1205796.nox_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_nox_reduce_total` | GoSungrow getPsDetail.1205796.nox_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_owner_ps_fault_status` | GoSungrow getPsDetail.1205796.owner_ps_fault_status | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83012` | GoSungrow 1205796 - p83012 - Other Information - P-radiation-H | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83013` | GoSungrow 1205796 - p83013 - Other Information - Daily irradiation | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83016` | GoSungrow 1205796 - p83016 - Other Information - Plant ambient temperature | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83017` | GoSungrow 1205796 - p83017 - Other Information - Plant module temperature | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83023` | GoSungrow 1205796 - p83023 - Other Information - Plant PR | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83023y_valid` | GoSungrow getPsDetail.1205796.p83023y.valid | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83036` | GoSungrow getPsDetail.1205796.p83036 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83043` | GoSungrow getPsDetail.1205796.p83043 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83044` | GoSungrow getPsDetail.1205796.p83044 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83045` | GoSungrow getPsDetail.1205796.p83045 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83072` | GoSungrow 1205796 - p83072 - Grid Information - Feed-in energy today | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83102` | GoSungrow 1205796 - p83102 - Grid Information - Energy purchased today | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83102_percent` | GoSungrow getPsDetail.1205796.p83102_percent | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83106` | GoSungrow 1205796 - p83106 - Load Information - Load power | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83118` | GoSungrow 1205796 - p83118 - Other Information - Daily load consumption | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83119` | GoSungrow 1205796 - p83119 - Other Information - Daily feed-in energy (PV) | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83121` | GoSungrow getPsDetail.1205796.p83121 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83122` | GoSungrow getPsDetail.1205796.p83122 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83123` | GoSungrow getPsDetail.1205796.p83123 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83124` | GoSungrow 1205796 - p83124 - Load Information - Total load consumption | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83125` | GoSungrow getPsDetail.1205796.p83125 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83126` | GoSungrow getPsDetail.1205796.p83126 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_p83202` | GoSungrow getPsDetail.1205796.p83202 | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_percent_plan_year` | GoSungrow getPsDetail.1205796.percent_plan_year | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_0` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_1` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_10` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_11` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_2` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_3` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_4` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_5` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_6` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_7` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_8` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_plan_energy_9` | GoSungrow 1205796 - plan_energy - PlanEnergy - Plan Energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_powder_reduce` | GoSungrow getPsDetail.1205796.powder_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_powder_reduce_total` | GoSungrow getPsDetail.1205796.powder_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_power_charge_set` | GoSungrow getPsDetail.1205796.power_charge_set | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_country_id` | GoSungrow getPsDetail.1205796.ps_country_id | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_fault_status` | GoSungrow getPsDetail.1205796.ps_fault_status | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_health_status` | GoSungrow getPsDetail.1205796.ps_health_status | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_holder` | GoSungrow getPsDetail.1205796.ps_holder | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_location` | GoSungrow getPsDetail.1205796.ps_location | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_short_name` | GoSungrow getPsDetail.1205796.ps_short_name | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_state` | GoSungrow getPsDetail.1205796.ps_state | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_type` | GoSungrow getPsDetail.1205796.ps_type | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_ps_type_name` | GoSungrow getPsDetail.1205796.ps_type_name | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_record_create_time` | GoSungrow getPsDetail.1205796.record_create_time | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_report_type` | GoSungrow getPsDetail.1205796.report_type | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_robot_num_sweep_capacity_num` | GoSungrow getPsDetail.1205796.robot_num_sweep_capacity.num | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_robot_num_sweep_capacity_sweep_capacity` | GoSungrow getPsDetail.1205796.robot_num_sweep_capacity.sweep_capacity | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_safe_start_date` | GoSungrow getPsDetail.1205796.safe_start_date | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_self_consumption_offset_reminder` | GoSungrow getPsDetail.1205796.self_consumption_offset_reminder | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_so2_reduce` | GoSungrow getPsDetail.1205796.so2_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_so2_reduce_total` | GoSungrow getPsDetail.1205796.so2_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_sys_scheme` | GoSungrow getPsDetail.1205796.sys_scheme | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_time_zone_id` | GoSungrow getPsDetail.1205796.time_zone_id | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_timezone` | GoSungrow getPsDetail.1205796.timezone | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_today_energy` | GoSungrow getPsDetail.1205796.today_energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_today_income` | GoSungrow getPsDetail.1205796.today_income | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_total_energy` | GoSungrow getPsDetail.1205796.total_energy | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_total_energy_year` | GoSungrow getPsDetail.1205796.total_energy_year | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_total_income` | GoSungrow getPsDetail.1205796.total_income | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_tree_reduce` | GoSungrow getPsDetail.1205796.tree_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_tree_reduce_total` | GoSungrow getPsDetail.1205796.tree_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_valid_flag` | GoSungrow getPsDetail.1205796.valid_flag | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_wait_assign_order_count` | GoSungrow getPsDetail.1205796.wait_assign_order_count | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_water_reduce` | GoSungrow getPsDetail.1205796.water_reduce | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_water_reduce_total` | GoSungrow getPsDetail.1205796.water_reduce_total | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_wgs_latitude` | GoSungrow getPsDetail.1205796.wgs_latitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_wgs_longitude` | GoSungrow getPsDetail.1205796.wgs_longitude | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_year` | GoSungrow getPsDetail.1205796.year | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_zfzy_map` | GoSungrow getPsDetail.1205796.zfzy_map | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_zip_code` | GoSungrow getPsDetail.1205796.zip_code | mqtt |
| `sensor.gosungrow_getpsdetail_1205796_zjzz_map` | GoSungrow getPsDetail.1205796.zjzz_map | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_alarm_count` | GoSungrow getPsList.devices.1205796.alarm_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_alarm_dev_count` | GoSungrow getPsList.devices.1205796.alarm_dev_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_area_id` | GoSungrow getPsList.devices.1205796.area_id | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_area_type` | GoSungrow getPsList.devices.1205796.area_type | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_arrears_status` | GoSungrow getPsList.devices.1205796.arrears_status | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_build_date` | GoSungrow getPsList.devices.1205796.build_date | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_build_status` | GoSungrow getPsList.devices.1205796.build_status | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_channel_id` | GoSungrow getPsList.devices.1205796.channel_id | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_co2_reduce` | GoSungrow getPsList.devices.1205796.co2_reduce | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_co2_reduce_total` | GoSungrow getPsList.devices.1205796.co2_reduce_total | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_curr_power` | GoSungrow getPsList.devices.1205796.curr_power | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_description` | GoSungrow getPsList.devices.1205796.description | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_design_capacity` | GoSungrow getPsList.devices.1205796.design_capacity | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_device_code` | GoSungrow getPsList.devices.1205796.device_code | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_device_type` | GoSungrow getPsList.devices.1205796.device_type | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_equivalent_hour` | GoSungrow getPsList.devices.1205796.equivalent_hour | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_expect_install_date` | GoSungrow getPsList.devices.1205796.expect_install_date | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_fault_alarm_offline_dev_count` | GoSungrow getPsList.devices.1205796.fault_alarm_offline_dev_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_fault_count` | GoSungrow getPsList.devices.1205796.fault_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_fault_dev_count` | GoSungrow getPsList.devices.1205796.fault_dev_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_gcj_latitude` | GoSungrow getPsList.devices.1205796.gcj_latitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_gcj_longitude` | GoSungrow getPsList.devices.1205796.gcj_longitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_gprs_latitude` | GoSungrow getPsList.devices.1205796.gprs_latitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_gprs_longitude` | GoSungrow getPsList.devices.1205796.gprs_longitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_images_1205796_file_id` | GoSungrow getPsList.devices.1205796.images.1205796.file_id | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_images_1205796_id` | GoSungrow getPsList.devices.1205796.images.1205796.id | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_images_1205796_pic_language` | GoSungrow getPsList.devices.1205796.images.1205796.pic_language | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_images_1205796_pic_type` | GoSungrow getPsList.devices.1205796.images.1205796.pic_type | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_images_1205796_picture_name` | GoSungrow getPsList.devices.1205796.images.1205796.picture_name | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_images_1205796_picture_url` | GoSungrow getPsList.devices.1205796.images.1205796.picture_url | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_images_1205796_ps_id` | GoSungrow getPsList.devices.1205796.images.1205796.ps_id | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_install_date` | GoSungrow getPsList.devices.1205796.install_date | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_installed_power_map` | GoSungrow getPsList.devices.1205796.installed_power_map | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_installer_alarm_count` | GoSungrow getPsList.devices.1205796.installer_alarm_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_installer_fault_count` | GoSungrow getPsList.devices.1205796.installer_fault_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_installer_ps_fault_status` | GoSungrow getPsList.devices.1205796.installer_ps_fault_status | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_is_bank_ps` | GoSungrow getPsList.devices.1205796.is_bank_ps | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_is_tuv` | GoSungrow getPsList.devices.1205796.is_tuv | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_join_year_init_elec` | GoSungrow getPsList.devices.1205796.join_year_init_elec | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_latitude` | GoSungrow getPsList.devices.1205796.latitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_location` | GoSungrow getPsList.devices.1205796.location | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_longitude` | GoSungrow getPsList.devices.1205796.longitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_map_latitude` | GoSungrow getPsList.devices.1205796.map_latitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_map_longitude` | GoSungrow getPsList.devices.1205796.map_longitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_mlpe_flag` | GoSungrow getPsList.devices.1205796.mlpe_flag | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_nmi` | GoSungrow getPsList.devices.1205796.nmi | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_offline_dev_count` | GoSungrow getPsList.devices.1205796.offline_dev_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_operate_year` | GoSungrow getPsList.devices.1205796.operate_year | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_operation_bus_name` | GoSungrow getPsList.devices.1205796.operation_bus_name | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_owner_alarm_count` | GoSungrow getPsList.devices.1205796.owner_alarm_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_owner_fault_count` | GoSungrow getPsList.devices.1205796.owner_fault_count | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_owner_ps_fault_status` | GoSungrow getPsList.devices.1205796.owner_ps_fault_status | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83022` | GoSungrow getPsList - p83022 - Other Information - Plant daily yield | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83046` | GoSungrow getPsList - p83046 - Other Information - PCS total active power | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83048` | GoSungrow getPsList.devices.1205796.p83048 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83049` | GoSungrow getPsList.devices.1205796.p83049 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83050` | GoSungrow getPsList.devices.1205796.p83050 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83051` | GoSungrow getPsList.devices.1205796.p83051 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83054` | GoSungrow getPsList.devices.1205796.p83054 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83055` | GoSungrow getPsList.devices.1205796.p83055 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83067` | GoSungrow getPsList - p83067 - Other Information - Total active power of PV | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83070` | GoSungrow getPsList.devices.1205796.p83070 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83076` | GoSungrow getPsList.devices.1205796.p83076 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83077` | GoSungrow getPsList.devices.1205796.p83077 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83081` | GoSungrow getPsList.devices.1205796.p83081 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83089` | GoSungrow getPsList.devices.1205796.p83089 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83095` | GoSungrow getPsList.devices.1205796.p83095 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83120` | GoSungrow getPsList.devices.1205796.p83120 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_p83127` | GoSungrow getPsList.devices.1205796.p83127 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_co2` | GoSungrow getPsList.devices.1205796.param_co2 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_coal` | GoSungrow getPsList.devices.1205796.param_coal | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_income` | GoSungrow getPsList.devices.1205796.param_income | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_meter` | GoSungrow getPsList.devices.1205796.param_meter | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_nox` | GoSungrow getPsList.devices.1205796.param_nox | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_powder` | GoSungrow getPsList.devices.1205796.param_powder | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_so2` | GoSungrow getPsList.devices.1205796.param_so2 | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_tree` | GoSungrow getPsList.devices.1205796.param_tree | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_param_water` | GoSungrow getPsList.devices.1205796.param_water | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_producer` | GoSungrow getPsList.devices.1205796.producer | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_code` | GoSungrow getPsList.devices.1205796.ps_code | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_country_id` | GoSungrow getPsList.devices.1205796.ps_country_id | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_fault_status` | GoSungrow getPsList.devices.1205796.ps_fault_status | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_health_status` | GoSungrow getPsList.devices.1205796.ps_health_status | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_holder` | GoSungrow getPsList.devices.1205796.ps_holder | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_id` | GoSungrow getPsList.devices.1205796.ps_id | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_is_not_init` | GoSungrow getPsList.devices.1205796.ps_is_not_init | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_key` | GoSungrow getPsList.devices.1205796.ps_key | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_name` | GoSungrow getPsList.devices.1205796.ps_name | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_short_name` | GoSungrow getPsList.devices.1205796.ps_short_name | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_status` | GoSungrow getPsList.devices.1205796.ps_status | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_timezone` | GoSungrow getPsList.devices.1205796.ps_timezone | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_ps_type` | GoSungrow getPsList.devices.1205796.ps_type | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_record_create_time` | GoSungrow getPsList.devices.1205796.record_create_time | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_safe_start_date` | GoSungrow getPsList.devices.1205796.safe_start_date | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_share_type` | GoSungrow getPsList.devices.1205796.share_type | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_shipping_address` | GoSungrow getPsList.devices.1205796.shipping_address | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_shipping_zip_code` | GoSungrow getPsList.devices.1205796.shipping_zip_code | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_sys_scheme` | GoSungrow getPsList.devices.1205796.sys_scheme | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_today_energy` | Solar Yield Today | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_today_income` | GoSungrow getPsList.devices.1205796.today_income | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_total_capacity` | GoSungrow getPsList.devices.1205796.total_capacity | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_total_energy` | GoSungrow getPsList.devices.1205796.total_energy | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_total_income` | GoSungrow getPsList.devices.1205796.total_income | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_total_init_co2_accelerate` | GoSungrow getPsList.devices.1205796.total_init_co2_accelerate | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_total_init_elec` | GoSungrow getPsList.devices.1205796.total_init_elec | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_total_init_profit` | GoSungrow getPsList.devices.1205796.total_init_profit | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_wgs_latitude` | GoSungrow getPsList.devices.1205796.wgs_latitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_wgs_longitude` | GoSungrow getPsList.devices.1205796.wgs_longitude | mqtt |
| `sensor.gosungrow_getpslist_devices_1205796_zip_code` | GoSungrow getPsList.devices.1205796.zip_code | mqtt |
| `sensor.gosungrow_getpslist_row_count` | GoSungrow getPsList.row_count | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_device_status_count_fault_count` | GoSungrow queryDeviceList.1205796.device_status_count.fault_count | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_device_status_count_offline_count` | GoSungrow queryDeviceList.1205796.device_status_count.offline_count | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_device_status_count_run_count` | GoSungrow queryDeviceList.1205796.device_status_count.run_count | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_device_status_count_warning_count` | GoSungrow queryDeviceList.1205796.device_status_count.warning_count | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_device_type_count_1` | GoSungrow queryDeviceList.1205796.device_type_count.1 | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_device_type_count_22` | GoSungrow queryDeviceList.1205796.device_type_count.22 | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_device_type_count_7` | GoSungrow queryDeviceList.1205796.device_type_count.7 | mqtt |
| `sensor.gosungrow_querydevicelist_1205796_row_count` | GoSungrow queryDeviceList.1205796.row_count | mqtt |
| `sensor.gosungrow_virtual_1205796_1_1_1_p1` | Solar Production | mqtt |
| `sensor.gosungrow_virtual_1205796_1_1_1_p24` | Solar Yield Now | mqtt |
| `sensor.gosungrow_virtual_1205796_22_247_1_p23011` | GoSungrow 1205796_22_247_1 - p23011 - Other Information - Work Status | mqtt |
| `sensor.gosungrow_virtual_1205796_22_247_1_p23014` | GoSungrow 1205796_22_247_1 - p23014 - Other information - WLAN signal strength | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8000` | GoSungrow 1205796_7_1_1 - p8000 - Overview - Phase A voltage | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8001` | GoSungrow 1205796_7_1_1 - p8001 - Overview - Phase B voltage | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8002` | GoSungrow 1205796_7_1_1 - p8002 - Overview - Phase C voltage | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8006` | GoSungrow 1205796_7_1_1 - p8006 - Overview - Phase A current | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8007` | GoSungrow 1205796_7_1_1 - p8007 - Overview - Phase B current | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8008` | GoSungrow 1205796_7_1_1 - p8008 - Overview - Phase C current | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8014` | GoSungrow 1205796_7_1_1 - p8014 - Overview - PF | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8018` | Grid or Net Energy | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8030` | GoSungrow 1205796_7_1_1 - p8030 - Grid information - Forward active energy | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8031` | GoSungrow 1205796_7_1_1 - p8031 - Grid information - Reverse active energy | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8062` | Purchased Energy | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8063` | Feed-in Energy from PV | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8075` | GoSungrow 1205796_7_1_1 - p8075 - Overview - Feed-in Power | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8076` | GoSungrow 1205796_7_1_1 - p8076 - Other information - Meter phase A active power | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8077` | GoSungrow 1205796_7_1_1 - p8077 - Other information - Meter phase B active power | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8078` | GoSungrow 1205796_7_1_1 - p8078 - Other information - Meter phase C active power | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8084` | GoSungrow 1205796_7_1_1 - p8084 - Load information - Daily load energy consumption from PV | mqtt |
| `sensor.gosungrow_virtual_1205796_7_1_1_p8085` | GoSungrow 1205796_7_1_1 - p8085 - Load information - Total load energy consumption from PV | mqtt |
| `sensor.gosungrow_virtual_1205796_p83012` | GoSungrow 1205796 - p83012 - Other Information - P-radiation-H | mqtt |
| `sensor.gosungrow_virtual_1205796_p83013` | GoSungrow 1205796 - p83013 - Other Information - Daily irradiation | mqtt |
| `sensor.gosungrow_virtual_1205796_p83016` | GoSungrow 1205796 - p83016 - Other Information - Plant ambient temperature | mqtt |
| `sensor.gosungrow_virtual_1205796_p83017` | GoSungrow 1205796 - p83017 - Other Information - Plant module temperature | mqtt |
| `sensor.gosungrow_virtual_1205796_p83023` | GoSungrow 1205796 - p83023 - Other Information - Plant PR | mqtt |
| `sensor.gosungrow_virtual_1205796_p83036` | GoSungrow virtual.1205796.p83036 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83043` | GoSungrow virtual.1205796.p83043 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83044` | GoSungrow virtual.1205796.p83044 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83045` | GoSungrow virtual.1205796.p83045 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83072` | GoSungrow 1205796 - p83072 - Grid Information - Feed-in energy today | mqtt |
| `sensor.gosungrow_virtual_1205796_p83102` | GoSungrow 1205796 - p83102 - Grid Information - Energy purchased today | mqtt |
| `sensor.gosungrow_virtual_1205796_p83102_percent` | GoSungrow virtual.1205796.p83102_percent | mqtt |
| `sensor.gosungrow_virtual_1205796_p83106` | GoSungrow 1205796 - p83106 - Load Information - Load power | mqtt |
| `sensor.gosungrow_virtual_1205796_p83118` | GoSungrow 1205796 - p83118 - Other Information - Daily load consumption | mqtt |
| `sensor.gosungrow_virtual_1205796_p83119` | GoSungrow 1205796 - p83119 - Other Information - Daily feed-in energy (PV) | mqtt |
| `sensor.gosungrow_virtual_1205796_p83121` | GoSungrow virtual.1205796.p83121 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83122` | GoSungrow virtual.1205796.p83122 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83123` | GoSungrow virtual.1205796.p83123 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83124` | GoSungrow 1205796 - p83124 - Load Information - Total load consumption | mqtt |
| `sensor.gosungrow_virtual_1205796_p83125` | GoSungrow virtual.1205796.p83125 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83126` | GoSungrow virtual.1205796.p83126 | mqtt |
| `sensor.gosungrow_virtual_1205796_p83202` | GoSungrow virtual.1205796.p83202 | mqtt |
| `sensor.gosungrow_virtual_1205796_zfzy_map` | GoSungrow virtual.1205796.zfzy_map | mqtt |
| `sensor.gosungrow_virtual_1205796_zjzz_map` | GoSungrow virtual.1205796.zjzz_map | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_co2_reduce` | GoSungrow virtual.devices.1205796.co2_reduce | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_co2_reduce_total` | GoSungrow virtual.devices.1205796.co2_reduce_total | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_curr_power` | GoSungrow virtual.devices.1205796.curr_power | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83022` | GoSungrow getPsList - p83022 - Other Information - Plant daily yield | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83046` | GoSungrow getPsList - p83046 - Other Information - PCS total active power | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83048` | GoSungrow virtual.devices.1205796.p83048 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83049` | GoSungrow virtual.devices.1205796.p83049 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83050` | GoSungrow virtual.devices.1205796.p83050 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83051` | GoSungrow virtual.devices.1205796.p83051 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83054` | GoSungrow virtual.devices.1205796.p83054 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83055` | GoSungrow virtual.devices.1205796.p83055 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83067` | GoSungrow getPsList - p83067 - Other Information - Total active power of PV | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83070` | GoSungrow virtual.devices.1205796.p83070 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83076` | GoSungrow virtual.devices.1205796.p83076 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83077` | GoSungrow virtual.devices.1205796.p83077 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83081` | GoSungrow virtual.devices.1205796.p83081 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83089` | GoSungrow virtual.devices.1205796.p83089 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83095` | GoSungrow virtual.devices.1205796.p83095 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83120` | GoSungrow virtual.devices.1205796.p83120 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_p83127` | GoSungrow virtual.devices.1205796.p83127 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_co2` | GoSungrow virtual.devices.1205796.param_co2 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_coal` | GoSungrow virtual.devices.1205796.param_coal | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_income` | GoSungrow virtual.devices.1205796.param_income | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_meter` | GoSungrow virtual.devices.1205796.param_meter | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_nox` | GoSungrow virtual.devices.1205796.param_nox | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_powder` | GoSungrow virtual.devices.1205796.param_powder | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_so2` | GoSungrow virtual.devices.1205796.param_so2 | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_tree` | GoSungrow virtual.devices.1205796.param_tree | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_param_water` | GoSungrow virtual.devices.1205796.param_water | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_today_energy` | GoSungrow virtual.devices.1205796.today_energy | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_today_income` | GoSungrow virtual.devices.1205796.today_income | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_total_capacity` | GoSungrow virtual.devices.1205796.total_capacity | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_total_energy` | GoSungrow virtual.devices.1205796.total_energy | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_total_income` | GoSungrow virtual.devices.1205796.total_income | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_total_init_co2_accelerate` | GoSungrow virtual.devices.1205796.total_init_co2_accelerate | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_total_init_elec` | GoSungrow virtual.devices.1205796.total_init_elec | mqtt |
| `sensor.gosungrow_virtual_devices_1205796_total_init_profit` | GoSungrow virtual.devices.1205796.total_init_profit | mqtt |
| `sensor.henry_s_door_battery` | Henry's Door Battery | zha |
| `sensor.henry_s_door_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.henry_s_door_battery_plus` | Battery+ | battery_notes |
| `sensor.henry_s_door_battery_type` | Battery type | battery_notes |
| `sensor.henry_s_door_device_temperature` | Henry's Door Device temperature | zha |
| `sensor.henry_s_room_climate_suggestion` | Henry's Room Climate Suggestion | template |
| `sensor.henry_s_room_ir_blaster_rx` | RX | unifi |
| `sensor.henry_s_room_ir_blaster_tx` | TX | unifi |
| `sensor.henry_s_room_temp_humidity_sensor_battery` | Battery | xiaomi_ble |
| `sensor.henry_s_room_temp_humidity_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.henry_s_room_temp_humidity_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.henry_s_room_temp_humidity_sensor_battery_type` | Battery type | battery_notes |
| `sensor.henry_s_room_temp_humidity_sensor_voltage` | Voltage | xiaomi_ble |
| `sensor.henry_s_room_temp_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.henry_s_room_temp_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.henry_s_room_temp_sensor_battery_type` | Battery type | battery_notes |
| `sensor.henrys_room_ema_temperature` | EMA temperature | versatile_thermostat |
| `sensor.henrys_room_energy` | Energy | versatile_thermostat |
| `sensor.henrys_room_ir_blaster_humidity` | Henry's Room IR Blaster Humidity | broadlink |
| `sensor.henrys_room_ir_blaster_temperature` | Henry's Room IR Blaster Temperature | broadlink |
| `sensor.henrys_room_last_external_temperature_date` | Last external temperature date | versatile_thermostat |
| `sensor.henrys_room_last_temperature_date` | Last temperature date | versatile_thermostat |
| `sensor.henrys_room_regulated_temperature` | Regulated temperature | versatile_thermostat |
| `sensor.henrys_room_temp_humidity_sensor_humidity` | Henry's Room Temp/Humidity Sensor Humidity | xiaomi_ble |
| `sensor.henrys_room_temp_humidity_sensor_temperature` | Henry's Room Temp/Humidity Sensor Temperature | xiaomi_ble |
| `sensor.henrys_room_temperature_slope` | Temperature slope | versatile_thermostat |
| `sensor.homeassistant_rx` | RX | unifi |
| `sensor.homeassistant_tx` | TX | unifi |
| `sensor.homenetwork` | None | unifi |
| `sensor.homenetworkiot` | None | unifi |
| `sensor.hot_weather_alert` | Hot Weather Alert | template |
| `sensor.huawei_p30_lite_1cf5181c8_rx` | RX | unifi |
| `sensor.huawei_p30_lite_1cf5181c8_tx` | TX | unifi |
| `sensor.hub_2_0be5` | Temperature | switchbot |
| `sensor.hub_2_0be5_humidity` | Humidity | switchbot |
| `sensor.hub_2_0be5_illuminance` | Illuminance | switchbot |
| `sensor.hub_2_0be5_light_level` | Light level | switchbot |
| `sensor.humidifiers` | Humidifiers | spook |
| `sensor.humiditysensor_humidity` | Humidity | matter |
| `sensor.hvac_door_open_summary` | HVAC Door Open Summary | template |
| `sensor.ignored_issues` | Ignored | spook |
| `sensor.images` | Images | spook |
| `sensor.input_booleans` | Input booleans | spook |
| `sensor.input_buttons` | Input buttons | spook |
| `sensor.input_datetimes` | Input date/times | spook |
| `sensor.input_numbers` | Input numbers | spook |
| `sensor.input_selects` | Input selects | spook |
| `sensor.input_texts` | Input texts | spook |
| `sensor.integrations` | Integrations | spook |
| `sensor.interior_garage_door_sensor_magnet_battery` | interior garage door sensor magnet Battery | zha |
| `sensor.interior_garage_door_sensor_magnet_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.interior_garage_door_sensor_magnet_battery_plus` | Battery+ | battery_notes |
| `sensor.interior_garage_door_sensor_magnet_battery_type` | Battery type | battery_notes |
| `sensor.interior_garage_door_sensor_magnet_device_temperature` | interior garage door sensor magnet Device temperature | zha |
| `sensor.ipad_rx` | RX | unifi |
| `sensor.ipad_rx_2` | RX | unifi |
| `sensor.ipad_tx` | TX | unifi |
| `sensor.ipad_tx_2` | TX | unifi |
| `sensor.iphone_rx` | RX | unifi |
| `sensor.iphone_rx_2` | RX | unifi |
| `sensor.iphone_rx_3` | RX | unifi |
| `sensor.iphone_rx_4` | RX | unifi |
| `sensor.iphone_rx_5` | RX | unifi |
| `sensor.iphone_rx_6` | RX | unifi |
| `sensor.iphone_tx` | TX | unifi |
| `sensor.iphone_tx_2` | TX | unifi |
| `sensor.iphone_tx_3` | TX | unifi |
| `sensor.iphone_tx_4` | TX | unifi |
| `sensor.iphone_tx_5` | TX | unifi |
| `sensor.iphone_tx_6` | TX | unifi |
| `sensor.issues` | Total | spook |
| `sensor.julies_imac_rx` | RX | unifi |
| `sensor.julies_imac_tx` | TX | unifi |
| `sensor.kids_toilet_last_cleaned_date` | Kids Toilet Last Cleaned Date | template |
| `sensor.kitchen_light_rx` | RX | unifi |
| `sensor.kitchen_light_tx` | TX | unifi |
| `sensor.kitchen_smart_plug_current` | Kitchen smart plug Current | zha |
| `sensor.kitchen_smart_plug_power` | Kitchen smart plug Power | zha |
| `sensor.kitchen_smart_plug_summation_delivered` | Kitchen smart plug Summation delivered | zha |
| `sensor.kitchen_smart_plug_voltage` | Kitchen smart plug Voltage | zha |
| `sensor.kobo_rx` | RX | unifi |
| `sensor.kobo_tx` | TX | unifi |
| `sensor.lights` | Lights | spook |
| `sensor.liling_s_s23_rx` | RX | unifi |
| `sensor.liling_s_s23_tx` | TX | unifi |
| `sensor.living_room_ac_ema_temperature` | EMA temperature | versatile_thermostat |
| `sensor.living_room_ac_energy` | Energy | versatile_thermostat |
| `sensor.living_room_ac_filter_last_changed_date` | Living Room AC Filter Last Changed Date | template |
| `sensor.living_room_ac_last_external_temperature_date` | Last external temperature date | versatile_thermostat |
| `sensor.living_room_ac_last_temperature_date` | Last temperature date | versatile_thermostat |
| `sensor.living_room_ac_regulated_temperature` | Regulated temperature | versatile_thermostat |
| `sensor.living_room_ac_temperature_slope` | Temperature slope | versatile_thermostat |
| `sensor.living_room_climate_suggestion` | Living Room Climate Suggestion | template |
| `sensor.living_room_comfort_delta` | Living Room Comfort Delta | template |
| `sensor.living_room_door_sensor_battery` | Living Room Door Sensor Battery | zha |
| `sensor.living_room_door_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.living_room_door_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.living_room_door_sensor_battery_type` | Battery type | battery_notes |
| `sensor.living_room_door_sensor_device_temperature` | Living Room Door Sensor Device temperature | zha |
| `sensor.living_room_humidity_diff_from_master` | Living Room Humidity Diff from Master | template |
| `sensor.living_room_ir_blaster_rx` | RX | unifi |
| `sensor.living_room_ir_blaster_tx` | TX | unifi |
| `sensor.living_room_temp_diff_from_master` | Living Room Temp Diff from Master | template |
| `sensor.living_room_temperature_offset` | Living Room Temperature (Offset) | template |
| `sensor.living_room_tv_rx` | RX | unifi |
| `sensor.living_room_tv_tx` | TX | unifi |
| `sensor.livingroom_irblaster_humidity` | Living Room Humidity Sensor | broadlink |
| `sensor.livingroom_irblaster_temperature` | Living Room Temperature Sensor | broadlink |
| `sensor.locks` | Locks | spook |
| `sensor.lounge_cpu_utilization` | CPU utilization | unifi |
| `sensor.lounge_memory_utilization` | Memory utilization | unifi |
| `sensor.lounge_state` | State | unifi |
| `sensor.lounge_uplink_mac` | Uplink MAC | unifi |
| `sensor.lounge_uptime` | Uptime | unifi |
| `sensor.lucas_room_comfort_delta` | Lucas Room Comfort Delta | template |
| `sensor.lucas_room_humidity_diff_from_master` | Lucas Room Humidity Diff from Master | template |
| `sensor.lucas_room_temp_diff_from_master` | Lucas Room Temp Diff from Master | template |
| `sensor.lumi_lumi_sensor_magnet_battery` | Battery | zha |
| `sensor.lumi_lumi_sensor_magnet_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.lumi_lumi_sensor_magnet_battery_plus` | Battery+ | battery_notes |
| `sensor.lumi_lumi_sensor_magnet_battery_type` | Battery type | battery_notes |
| `sensor.lumi_lumi_sensor_magnet_device_temperature` | Device temperature | zha |
| `sensor.lumi_lumi_sensor_wleak_aq1_battery` | Battery | zha |
| `sensor.lumi_lumi_sensor_wleak_aq1_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.lumi_lumi_sensor_wleak_aq1_battery_plus` | Battery+ | battery_notes |
| `sensor.lumi_lumi_sensor_wleak_aq1_battery_type` | Battery type | battery_notes |
| `sensor.lumi_lumi_sensor_wleak_aq1_device_temperature` | Device temperature | zha |
| `sensor.master_bed_switch_4_battery` | Master Bed Switch 4 Battery | zha |
| `sensor.master_bed_switch_4_battery_last_replaced` | Master Bed Switch 4 Battery last replaced | battery_notes |
| `sensor.master_bed_switch_4_battery_plus` | Master Bed Switch 4 Battery+ | battery_notes |
| `sensor.master_bed_switch_4_battery_type` | Master Bed Switch 4 Battery type | battery_notes |
| `sensor.master_bedroom_ac_filter_last_changed_date` | Master Bedroom AC Filter Last Changed Date | template |
| `sensor.master_bedroom_climate_suggestion` | Master Bedroom Climate Suggestion | template |
| `sensor.master_bedroom_comfort_delta` | Master Bedroom Comfort Delta | template |
| `sensor.master_bedroom_door_sensor_battery` | Master Bedroom Door Sensor Battery | zha |
| `sensor.master_bedroom_door_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.master_bedroom_door_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.master_bedroom_door_sensor_battery_type` | Battery type | battery_notes |
| `sensor.master_bedroom_door_sensor_device_temperature` | Master Bedroom Door Sensor Device temperature | zha |
| `sensor.master_bedroom_ir_blaster_rx` | RX | unifi |
| `sensor.master_bedroom_ir_blaster_tx` | TX | unifi |
| `sensor.master_switch_3_battery` | Master Switch 3 Battery | zha |
| `sensor.master_switch_3_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.master_switch_3_battery_plus` | Battery+ | battery_notes |
| `sensor.master_switch_3_battery_type` | Battery type | battery_notes |
| `sensor.master_toilet_last_cleaned_date` | Master Toilet Last Cleaned Date | template |
| `sensor.masterbed_7989_battery` | Battery | bthome |
| `sensor.masterbed_7989_humidity` | Humidity | bthome |
| `sensor.masterbed_7989_temperature` | Temperature | bthome |
| `sensor.masterbed_7989_voltage` | Voltage | bthome |
| `sensor.masterbed_ac_ema_temperature` | EMA temperature | versatile_thermostat |
| `sensor.masterbed_ac_energy` | Energy | versatile_thermostat |
| `sensor.masterbed_ac_last_external_temperature_date` | Last external temperature date | versatile_thermostat |
| `sensor.masterbed_ac_last_temperature_date` | Last temperature date | versatile_thermostat |
| `sensor.masterbed_ac_regulated_temperature` | Regulated temperature | versatile_thermostat |
| `sensor.masterbed_ac_temperature_slope` | Temperature slope | versatile_thermostat |
| `sensor.masterbed_sink_leak_detector_battery_2` | Masterbed Sink Leak Detector Battery | zha |
| `sensor.masterbed_sink_leak_detector_battery_last_replaced` | Masterbed Sink Leak Detector Battery last replaced | battery_notes |
| `sensor.masterbed_sink_leak_detector_battery_plus` | Masterbed Sink Leak Detector Battery+ | battery_notes |
| `sensor.masterbed_sink_leak_detector_battery_type` | Masterbed Sink Leak Detector Battery type | battery_notes |
| `sensor.masterbed_switch_1_battery` | Masterbed Switch 1 Battery | zha |
| `sensor.masterbed_switch_1_battery_last_replaced` | Masterbed Switch 1 Battery last replaced | battery_notes |
| `sensor.masterbed_switch_1_battery_plus` | Masterbed Switch 1 Battery+ | battery_notes |
| `sensor.masterbed_switch_1_battery_type` | Masterbed Switch 1 Battery type | battery_notes |
| `sensor.masterbed_switch_2_battery` | Masterbed Switch 2 Battery | zha |
| `sensor.masterbed_switch_2_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.masterbed_switch_2_battery_plus` | Battery+ | battery_notes |
| `sensor.masterbed_switch_2_battery_type` | Battery type | battery_notes |
| `sensor.media_players` | Media players | spook |
| `sensor.media_server` | None | plex |
| `sensor.media_server_base_url` | Media Server Base URL | template |
| `sensor.media_server_rx` | RX | unifi |
| `sensor.media_server_tx` | TX | unifi |
| `sensor.minimum_temperature_forecast_today` | Minimum Temperature forecast today | template |
| `sensor.motion_sensor_battery` | motion sensor Battery | zha |
| `sensor.motion_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.motion_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.motion_sensor_battery_type` | Battery type | battery_notes |
| `sensor.motion_sensor_illuminance` | motion sensor Illuminance | zha |
| `sensor.node_pve_containers_running` | Containers running | proxmoxve |
| `sensor.node_pve_cpu_used` | CPU used | proxmoxve |
| `sensor.node_pve_disk_used_percentage` | Disk used percentage | proxmoxve |
| `sensor.node_pve_last_boot` | Last boot | proxmoxve |
| `sensor.node_pve_memory_free` | Memory free | proxmoxve |
| `sensor.node_pve_memory_used` | Memory used | proxmoxve |
| `sensor.node_pve_memory_used_percentage` | Memory used percentage | proxmoxve |
| `sensor.node_pve_total_updates` | Total updates | proxmoxve |
| `sensor.node_pve_virtual_machines_running` | Virtual machines running | proxmoxve |
| `sensor.numbers` | Numbers | spook |
| `sensor.office_zone_debug` | Office Zone Debug | template |
| `sensor.offline_security_entities` | Offline Security Entities | template |
| `sensor.oma_s_toilet_last_cleaned_date` | Oma's Toilet Last Cleaned Date | template |
| `sensor.otto_room_comfort_delta` | Otto Room Comfort Delta | template |
| `sensor.otto_room_door_sensor_battery` | otto room door sensor Battery | zha |
| `sensor.otto_room_door_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.otto_room_door_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.otto_room_door_sensor_battery_type` | Battery type | battery_notes |
| `sensor.otto_room_door_sensor_device_temperature` | otto room door sensor Device temperature | zha |
| `sensor.otto_room_humidity_diff_from_master` | Otto Room Humidity Diff from Master | template |
| `sensor.otto_room_temp_diff_from_master` | Otto Room Temp Diff from Master | template |
| `sensor.otto_s_rm_ir_blaster_rx` | RX | unifi |
| `sensor.otto_s_rm_ir_blaster_tx` | TX | unifi |
| `sensor.otto_s_room_ac_filter_last_changed_date` | Otto's Room AC Filter Last Changed Date | template |
| `sensor.otto_s_room_climate_suggestion` | Otto's Room Climate Suggestion | template |
| `sensor.otto_s_room_temp_humidity_sensor_battery` | Battery | xiaomi_ble |
| `sensor.otto_s_room_temp_humidity_sensor_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.otto_s_room_temp_humidity_sensor_battery_plus` | Battery+ | battery_notes |
| `sensor.otto_s_room_temp_humidity_sensor_battery_type` | Battery type | battery_notes |
| `sensor.otto_s_room_temp_humidity_sensor_voltage` | Voltage | xiaomi_ble |
| `sensor.ottos_room_ac_ema_temperature` | EMA temperature | versatile_thermostat |
| `sensor.ottos_room_ac_energy` | Energy | versatile_thermostat |
| `sensor.ottos_room_ac_last_external_temperature_date` | Last external temperature date | versatile_thermostat |
| `sensor.ottos_room_ac_last_temperature_date` | Last temperature date | versatile_thermostat |
| `sensor.ottos_room_ac_regulated_temperature` | Regulated temperature | versatile_thermostat |
| `sensor.ottos_room_ac_temperature_slope` | Temperature slope | versatile_thermostat |
| `sensor.ottos_room_temp_humidity_sensor_humidity` | Otto's Room Temp/Humidity Sensor Humidity | xiaomi_ble |
| `sensor.ottos_room_temp_humidity_sensor_temperature` | Otto's Room Temp/Humidity Sensor Temperature | xiaomi_ble |
| `sensor.outdoor_switch_total_energy` | Total energy | tuya |
| `sensor.papercut` | None | ipp |
| `sensor.persistent_notifications` | Persistent notifications | spook |
| `sensor.persons` | Persons | spook |
| `sensor.phil_s_phone_area` | Area | bermuda |
| `sensor.phil_s_phone_distance` | Distance | bermuda |
| `sensor.phil_s_phone_floor` | Floor | bermuda |
| `sensor.phils_phone_area` | Area | bermuda |
| `sensor.phils_phone_distance` | Distance | bermuda |
| `sensor.phils_phone_estimated_distance` | Estimated distance | private_ble_device |
| `sensor.phils_phone_floor` | Floor | bermuda |
| `sensor.phils_phone_rx` | RX | unifi |
| `sensor.phils_phone_rx_2` | RX | unifi |
| `sensor.phils_phone_tx` | TX | unifi |
| `sensor.phils_phone_tx_2` | TX | unifi |
| `sensor.phils_work_pc_rx` | RX | unifi |
| `sensor.phils_work_pc_tx` | TX | unifi |
| `sensor.philslaptop_rx` | RX | unifi |
| `sensor.philslaptop_tx` | TX | unifi |
| `sensor.pixel_10_pro_rx` | RX | unifi |
| `sensor.pixel_10_pro_tx` | TX | unifi |
| `sensor.pixel_7_rx` | RX | unifi |
| `sensor.pixel_7_tx` | TX | unifi |
| `sensor.portainer_endpoints_local` | local | portainer |
| `sensor.portainer_local_107b203db8b7_dagster_webserver` | 107b203db8b7_dagster_webserver | portainer |
| `sensor.portainer_local_53ada761d61f_dagster_daemon` | 53ada761d61f_dagster_daemon | portainer |
| `sensor.portainer_local_54f7e6e4b8c5_dagster_daemon` | 54f7e6e4b8c5_dagster_daemon | portainer |
| `sensor.portainer_local_59c5915e71e7_pipeline_personal_finance` | 59c5915e71e7_pipeline_personal_finance | portainer |
| `sensor.portainer_local_62ee075823cd_dagster_daemon` | 62ee075823cd_dagster_daemon | portainer |
| `sensor.portainer_local_802a38efd952_qif_personal_finance_dagster_daemon_1` | 802a38efd952_qif_personal_finance-dagster_daemon-1 | portainer |
| `sensor.portainer_local_a122ef9feecb_dagster_webserver` | a122ef9feecb_dagster_webserver | portainer |
| `sensor.portainer_local_a532a529939c_qif_personal_finance_pipeline_personal_finance_1` | a532a529939c_qif_personal_finance-pipeline_personal_finance-1 | portainer |
| `sensor.portainer_local_admiring_bose` | admiring_bose | portainer |
| `sensor.portainer_local_audiobookshelf` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_10` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_11` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_12` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_13` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_14` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_15` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_16` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_2` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_3` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_4` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_5` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_6` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_7` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_8` | audiobookshelf | portainer |
| `sensor.portainer_local_audiobookshelf_9` | audiobookshelf | portainer |
| `sensor.portainer_local_bazarr` | bazarr | portainer |
| `sensor.portainer_local_bazarr_10` | bazarr | portainer |
| `sensor.portainer_local_bazarr_11` | bazarr | portainer |
| `sensor.portainer_local_bazarr_12` | bazarr | portainer |
| `sensor.portainer_local_bazarr_13` | bazarr | portainer |
| `sensor.portainer_local_bazarr_2` | bazarr | portainer |
| `sensor.portainer_local_bazarr_3` | bazarr | portainer |
| `sensor.portainer_local_bazarr_4` | bazarr | portainer |
| `sensor.portainer_local_bazarr_5` | bazarr | portainer |
| `sensor.portainer_local_bazarr_6` | bazarr | portainer |
| `sensor.portainer_local_bazarr_7` | bazarr | portainer |
| `sensor.portainer_local_bazarr_8` | bazarr | portainer |
| `sensor.portainer_local_bazarr_9` | bazarr | portainer |
| `sensor.portainer_local_bf1e22625826_dagster_daemon` | bf1e22625826_dagster_daemon | portainer |
| `sensor.portainer_local_brave_heyrovsky` | brave_heyrovsky | portainer |
| `sensor.portainer_local_calibre` | calibre | portainer |
| `sensor.portainer_local_calibre_10` | calibre | portainer |
| `sensor.portainer_local_calibre_11` | calibre | portainer |
| `sensor.portainer_local_calibre_12` | calibre | portainer |
| `sensor.portainer_local_calibre_13` | calibre | portainer |
| `sensor.portainer_local_calibre_14` | calibre | portainer |
| `sensor.portainer_local_calibre_2` | calibre | portainer |
| `sensor.portainer_local_calibre_3` | calibre | portainer |
| `sensor.portainer_local_calibre_4` | calibre | portainer |
| `sensor.portainer_local_calibre_5` | calibre | portainer |
| `sensor.portainer_local_calibre_6` | calibre | portainer |
| `sensor.portainer_local_calibre_7` | calibre | portainer |
| `sensor.portainer_local_calibre_8` | calibre | portainer |
| `sensor.portainer_local_calibre_9` | calibre | portainer |
| `sensor.portainer_local_calibre_web` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_10` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_11` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_12` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_13` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_14` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_15` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_16` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_17` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_2` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_3` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_4` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_5` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_6` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_7` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_8` | calibre-web | portainer |
| `sensor.portainer_local_calibre_web_9` | calibre-web | portainer |
| `sensor.portainer_local_charming_boyd` | charming_boyd | portainer |
| `sensor.portainer_local_cloudflared_tunnel` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_10` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_11` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_12` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_13` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_14` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_15` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_16` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_17` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_2` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_3` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_4` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_5` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_6` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_7` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_8` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_cloudflared_tunnel_9` | cloudflared-tunnel | portainer |
| `sensor.portainer_local_compassionate_gauss` | compassionate_gauss | portainer |
| `sensor.portainer_local_competent_tu` | competent_tu | portainer |
| `sensor.portainer_local_confident_kowalevski` | confident_kowalevski | portainer |
| `sensor.portainer_local_cool_chebyshev` | cool_chebyshev | portainer |
| `sensor.portainer_local_cranky_newton` | cranky_newton | portainer |
| `sensor.portainer_local_dagster_daemon` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_10` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_11` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_12` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_13` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_14` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_15` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_16` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_17` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_18` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_19` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_2` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_20` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_21` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_22` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_23` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_24` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_25` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_26` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_27` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_28` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_29` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_3` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_30` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_31` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_32` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_33` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_4` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_5` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_6` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_7` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_8` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_daemon_9` | dagster_daemon | portainer |
| `sensor.portainer_local_dagster_postgres` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_10` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_11` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_12` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_13` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_14` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_15` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_16` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_17` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_18` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_19` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_2` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_20` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_21` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_22` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_23` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_24` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_25` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_3` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_4` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_5` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_6` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_7` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_8` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_postgres_9` | dagster_postgres | portainer |
| `sensor.portainer_local_dagster_webserver` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_10` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_11` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_12` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_13` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_14` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_15` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_16` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_17` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_18` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_19` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_2` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_20` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_21` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_22` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_23` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_24` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_25` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_26` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_27` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_28` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_29` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_3` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_30` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_31` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_32` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_33` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_34` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_35` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_36` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_4` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_5` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_6` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_7` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_8` | dagster_webserver | portainer |
| `sensor.portainer_local_dagster_webserver_9` | dagster_webserver | portainer |
| `sensor.portainer_local_distracted_rubin` | distracted_rubin | portainer |
| `sensor.portainer_local_distracted_sanderson` | distracted_sanderson | portainer |
| `sensor.portainer_local_dreamy_feynman` | dreamy_feynman | portainer |
| `sensor.portainer_local_dreamy_pike` | dreamy_pike | portainer |
| `sensor.portainer_local_e8b417e98329_readarr` | readarr | portainer |
| `sensor.portainer_local_eager_leavitt` | eager_leavitt | portainer |
| `sensor.portainer_local_ee6601eee022_pipeline_personal_finance` | ee6601eee022_pipeline_personal_finance | portainer |
| `sensor.portainer_local_elastic_bardeen` | elastic_bardeen | portainer |
| `sensor.portainer_local_elastic_sutherland` | elastic_sutherland | portainer |
| `sensor.portainer_local_elegant_lovelace` | elegant_lovelace | portainer |
| `sensor.portainer_local_eloquent_grothendieck` | eloquent_grothendieck | portainer |
| `sensor.portainer_local_exciting_diffie` | exciting_diffie | portainer |
| `sensor.portainer_local_exciting_lewin` | exciting_lewin | portainer |
| `sensor.portainer_local_f08d485e2d17_pipeline_personal_finance` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_festive_goldstine` | festive_goldstine | portainer |
| `sensor.portainer_local_flamboyant_hopper` | flamboyant_hopper | portainer |
| `sensor.portainer_local_friendly_aryabhata` | friendly_aryabhata | portainer |
| `sensor.portainer_local_frosty_kirch` | frosty_kirch | portainer |
| `sensor.portainer_local_gifted_chaplygin` | gifted_chaplygin | portainer |
| `sensor.portainer_local_grafana` | grafana | portainer |
| `sensor.portainer_local_grafana_10` | grafana | portainer |
| `sensor.portainer_local_grafana_11` | grafana | portainer |
| `sensor.portainer_local_grafana_12` | grafana | portainer |
| `sensor.portainer_local_grafana_13` | grafana | portainer |
| `sensor.portainer_local_grafana_14` | grafana | portainer |
| `sensor.portainer_local_grafana_2` | grafana | portainer |
| `sensor.portainer_local_grafana_3` | grafana | portainer |
| `sensor.portainer_local_grafana_4` | grafana | portainer |
| `sensor.portainer_local_grafana_5` | grafana | portainer |
| `sensor.portainer_local_grafana_6` | grafana | portainer |
| `sensor.portainer_local_grafana_7` | grafana | portainer |
| `sensor.portainer_local_grafana_8` | grafana | portainer |
| `sensor.portainer_local_grafana_9` | grafana | portainer |
| `sensor.portainer_local_happy_gagarin` | happy_gagarin | portainer |
| `sensor.portainer_local_homebox` | homebox | portainer |
| `sensor.portainer_local_homebox_10` | homebox | portainer |
| `sensor.portainer_local_homebox_11` | homebox | portainer |
| `sensor.portainer_local_homebox_12` | homebox | portainer |
| `sensor.portainer_local_homebox_13` | homebox | portainer |
| `sensor.portainer_local_homebox_14` | homebox | portainer |
| `sensor.portainer_local_homebox_15` | homebox | portainer |
| `sensor.portainer_local_homebox_16` | homebox | portainer |
| `sensor.portainer_local_homebox_17` | homebox | portainer |
| `sensor.portainer_local_homebox_18` | homebox | portainer |
| `sensor.portainer_local_homebox_19` | homebox | portainer |
| `sensor.portainer_local_homebox_2` | homebox | portainer |
| `sensor.portainer_local_homebox_3` | homebox | portainer |
| `sensor.portainer_local_homebox_4` | homebox | portainer |
| `sensor.portainer_local_homebox_5` | homebox | portainer |
| `sensor.portainer_local_homebox_6` | homebox | portainer |
| `sensor.portainer_local_homebox_7` | homebox | portainer |
| `sensor.portainer_local_homebox_8` | homebox | portainer |
| `sensor.portainer_local_homebox_9` | homebox | portainer |
| `sensor.portainer_local_hopeful_taussig` | hopeful_taussig | portainer |
| `sensor.portainer_local_inspiring_swirles` | inspiring_swirles | portainer |
| `sensor.portainer_local_inspiring_wing` | inspiring_wing | portainer |
| `sensor.portainer_local_intelligent_yalow` | intelligent_yalow | portainer |
| `sensor.portainer_local_laughing_allen` | laughing_allen | portainer |
| `sensor.portainer_local_lidarr` | lidarr | portainer |
| `sensor.portainer_local_lidarr_10` | lidarr | portainer |
| `sensor.portainer_local_lidarr_11` | lidarr | portainer |
| `sensor.portainer_local_lidarr_12` | lidarr | portainer |
| `sensor.portainer_local_lidarr_13` | lidarr | portainer |
| `sensor.portainer_local_lidarr_2` | lidarr | portainer |
| `sensor.portainer_local_lidarr_3` | lidarr | portainer |
| `sensor.portainer_local_lidarr_4` | lidarr | portainer |
| `sensor.portainer_local_lidarr_5` | lidarr | portainer |
| `sensor.portainer_local_lidarr_6` | lidarr | portainer |
| `sensor.portainer_local_lidarr_7` | lidarr | portainer |
| `sensor.portainer_local_lidarr_8` | lidarr | portainer |
| `sensor.portainer_local_lidarr_9` | lidarr | portainer |
| `sensor.portainer_local_magical_lamarr` | magical_lamarr | portainer |
| `sensor.portainer_local_magical_lewin` | magical_lewin | portainer |
| `sensor.portainer_local_maria_db_photoprism` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_10` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_11` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_12` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_13` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_14` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_15` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_16` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_2` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_3` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_4` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_5` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_6` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_7` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_8` | maria_db_photoprism | portainer |
| `sensor.portainer_local_maria_db_photoprism_9` | maria_db_photoprism | portainer |
| `sensor.portainer_local_modest_carver` | modest_carver | portainer |
| `sensor.portainer_local_musing_ptolemy` | musing_ptolemy | portainer |
| `sensor.portainer_local_nextcloud` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_10` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_11` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_12` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_13` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_14` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_2` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_3` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_4` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_5` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_6` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_7` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_8` | nextcloud | portainer |
| `sensor.portainer_local_nextcloud_9` | nextcloud | portainer |
| `sensor.portainer_local_nginxproxymanager` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_10` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_11` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_12` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_13` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_14` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_15` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_16` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_17` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_18` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_19` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_2` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_20` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_21` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_3` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_4` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_5` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_6` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_7` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_8` | nginxproxymanager | portainer |
| `sensor.portainer_local_nginxproxymanager_9` | nginxproxymanager | portainer |
| `sensor.portainer_local_nostalgic_jackson` | nostalgic_jackson | portainer |
| `sensor.portainer_local_nostalgic_mahavira` | nostalgic_mahavira | portainer |
| `sensor.portainer_local_nostalgic_ritchie` | nostalgic_ritchie | portainer |
| `sensor.portainer_local_ofelia` | ofelia | portainer |
| `sensor.portainer_local_ofelia_10` | ofelia | portainer |
| `sensor.portainer_local_ofelia_11` | ofelia | portainer |
| `sensor.portainer_local_ofelia_12` | ofelia | portainer |
| `sensor.portainer_local_ofelia_13` | ofelia | portainer |
| `sensor.portainer_local_ofelia_2` | ofelia | portainer |
| `sensor.portainer_local_ofelia_3` | ofelia | portainer |
| `sensor.portainer_local_ofelia_4` | ofelia | portainer |
| `sensor.portainer_local_ofelia_5` | ofelia | portainer |
| `sensor.portainer_local_ofelia_6` | ofelia | portainer |
| `sensor.portainer_local_ofelia_7` | ofelia | portainer |
| `sensor.portainer_local_ofelia_8` | ofelia | portainer |
| `sensor.portainer_local_ofelia_9` | ofelia | portainer |
| `sensor.portainer_local_peaceful_ritchie` | peaceful_ritchie | portainer |
| `sensor.portainer_local_pedantic_mestorf` | pedantic_mestorf | portainer |
| `sensor.portainer_local_pensive_wright` | pensive_wright | portainer |
| `sensor.portainer_local_photoprism` | photoprism | portainer |
| `sensor.portainer_local_photoprism_10` | photoprism | portainer |
| `sensor.portainer_local_photoprism_11` | photoprism | portainer |
| `sensor.portainer_local_photoprism_12` | photoprism | portainer |
| `sensor.portainer_local_photoprism_13` | photoprism | portainer |
| `sensor.portainer_local_photoprism_2` | photoprism | portainer |
| `sensor.portainer_local_photoprism_3` | photoprism | portainer |
| `sensor.portainer_local_photoprism_4` | photoprism | portainer |
| `sensor.portainer_local_photoprism_5` | photoprism | portainer |
| `sensor.portainer_local_photoprism_6` | photoprism | portainer |
| `sensor.portainer_local_photoprism_7` | photoprism | portainer |
| `sensor.portainer_local_photoprism_8` | photoprism | portainer |
| `sensor.portainer_local_photoprism_9` | photoprism | portainer |
| `sensor.portainer_local_pipeline_personal_finance` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_10` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_11` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_12` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_13` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_14` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_15` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_16` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_17` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_18` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_19` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_2` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_20` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_21` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_22` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_23` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_24` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_25` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_26` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_27` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_28` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_29` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_3` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_30` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_31` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_32` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_33` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_34` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_35` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_36` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_37` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_38` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_39` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_4` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_40` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_41` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_42` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_43` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_44` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_45` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_46` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_47` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_48` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_49` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_5` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_50` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_51` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_52` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_53` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_54` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_55` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_56` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_57` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_58` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_59` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_6` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_60` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_61` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_62` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_63` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_64` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_65` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_66` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_67` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_7` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_8` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_9` | pipeline_personal_finance | portainer |
| `sensor.portainer_local_pipeline_personal_finance_dagster_daemon_1` | pipeline_personal_finance-dagster_daemon-1 | portainer |
| `sensor.portainer_local_pipeline_personal_finance_dagster_postgres_1` | pipeline_personal_finance-dagster_postgres-1 | portainer |
| `sensor.portainer_local_pipeline_personal_finance_dagster_webserver_1` | pipeline_personal_finance-dagster_webserver-1 | portainer |
| `sensor.portainer_local_pipeline_personal_finance_grafana_1` | pipeline_personal_finance-grafana-1 | portainer |
| `sensor.portainer_local_pipeline_personal_finance_pipeline_personal_finance_1` | pipeline_personal_finance-pipeline_personal_finance-1 | portainer |
| `sensor.portainer_local_plex` | plex | portainer |
| `sensor.portainer_local_plex_10` | plex | portainer |
| `sensor.portainer_local_plex_11` | plex | portainer |
| `sensor.portainer_local_plex_12` | plex | portainer |
| `sensor.portainer_local_plex_13` | plex | portainer |
| `sensor.portainer_local_plex_14` | plex | portainer |
| `sensor.portainer_local_plex_15` | plex | portainer |
| `sensor.portainer_local_plex_2` | plex | portainer |
| `sensor.portainer_local_plex_3` | plex | portainer |
| `sensor.portainer_local_plex_4` | plex | portainer |
| `sensor.portainer_local_plex_5` | plex | portainer |
| `sensor.portainer_local_plex_6` | plex | portainer |
| `sensor.portainer_local_plex_7` | plex | portainer |
| `sensor.portainer_local_plex_8` | plex | portainer |
| `sensor.portainer_local_plex_9` | plex | portainer |
| `sensor.portainer_local_portainer` | portainer | portainer |
| `sensor.portainer_local_portainer_2` | portainer | portainer |
| `sensor.portainer_local_postgres_nextcloud` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_10` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_2` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_3` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_4` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_5` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_6` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_7` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_8` | postgres_nextcloud | portainer |
| `sensor.portainer_local_postgres_nextcloud_9` | postgres_nextcloud | portainer |
| `sensor.portainer_local_prowlarr` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_10` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_11` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_12` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_13` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_14` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_15` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_2` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_3` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_4` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_5` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_6` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_7` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_8` | prowlarr | portainer |
| `sensor.portainer_local_prowlarr_9` | prowlarr | portainer |
| `sensor.portainer_local_qbittorrent` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_10` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_11` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_12` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_13` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_14` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_15` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_16` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_2` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_3` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_4` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_5` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_6` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_7` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_8` | qbittorrent | portainer |
| `sensor.portainer_local_qbittorrent_9` | qbittorrent | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_daemon_1` | qif_personal_finance_dagster_daemon_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_daemon_1_2` | qif_personal_finance_dagster_daemon_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_daemon_1_3` | qif_personal_finance-dagster_daemon-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_daemon_1_4` | qif_personal_finance-dagster_daemon-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_daemon_1_5` | qif_personal_finance-dagster_daemon-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_postgres_1` | qif_personal_finance_dagster_postgres_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_postgres_1_2` | qif_personal_finance-dagster_postgres-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_postgres_1_3` | qif_personal_finance_dagster_postgres_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_postgres_1_4` | qif_personal_finance-dagster_postgres-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_postgres_1_5` | qif_personal_finance-dagster_postgres-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_webserver_1` | qif_personal_finance_dagster_webserver_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_webserver_1_2` | qif_personal_finance-dagster_webserver-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_webserver_1_3` | qif_personal_finance_dagster_webserver_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_webserver_1_4` | qif_personal_finance-dagster_webserver-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_webserver_1_5` | qif_personal_finance-dagster_webserver-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_dagster_webserver_1_6` | qif_personal_finance-dagster_webserver-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_grafana_1` | qif_personal_finance_grafana_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_grafana_1_2` | qif_personal_finance-grafana-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_grafana_1_3` | qif_personal_finance_grafana_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_grafana_1_4` | qif_personal_finance-grafana-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_pipeline_personal_finance_1` | qif_personal_finance_pipeline_personal_finance_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_pipeline_personal_finance_1_2` | qif_personal_finance-pipeline_personal_finance-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_pipeline_personal_finance_1_3` | qif_personal_finance-pipeline_personal_finance-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_pipeline_personal_finance_1_4` | qif_personal_finance_pipeline_personal_finance_1 | portainer |
| `sensor.portainer_local_qif_personal_finance_pipeline_personal_finance_1_5` | qif_personal_finance-pipeline_personal_finance-1 | portainer |
| `sensor.portainer_local_qif_personal_finance_pipeline_personal_finance_1_6` | qif_personal_finance-pipeline_personal_finance-1 | portainer |
| `sensor.portainer_local_quirky_wing` | quirky_wing | portainer |
| `sensor.portainer_local_radarr` | radarr | portainer |
| `sensor.portainer_local_radarr_10` | radarr | portainer |
| `sensor.portainer_local_radarr_11` | radarr | portainer |
| `sensor.portainer_local_radarr_12` | radarr | portainer |
| `sensor.portainer_local_radarr_2` | radarr | portainer |
| `sensor.portainer_local_radarr_3` | radarr | portainer |
| `sensor.portainer_local_radarr_4` | radarr | portainer |
| `sensor.portainer_local_radarr_5` | radarr | portainer |
| `sensor.portainer_local_radarr_6` | radarr | portainer |
| `sensor.portainer_local_radarr_7` | radarr | portainer |
| `sensor.portainer_local_radarr_8` | radarr | portainer |
| `sensor.portainer_local_radarr_9` | radarr | portainer |
| `sensor.portainer_local_readarr` | readarr | portainer |
| `sensor.portainer_local_readarr_10` | readarr | portainer |
| `sensor.portainer_local_readarr_11` | readarr | portainer |
| `sensor.portainer_local_readarr_2` | readarr | portainer |
| `sensor.portainer_local_readarr_3` | readarr | portainer |
| `sensor.portainer_local_readarr_4` | readarr | portainer |
| `sensor.portainer_local_readarr_5` | readarr | portainer |
| `sensor.portainer_local_readarr_6` | readarr | portainer |
| `sensor.portainer_local_readarr_7` | readarr | portainer |
| `sensor.portainer_local_readarr_8` | readarr | portainer |
| `sensor.portainer_local_readarr_9` | readarr | portainer |
| `sensor.portainer_local_readarr_ab` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_10` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_11` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_12` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_2` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_3` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_4` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_5` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_6` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_7` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_8` | readarr_ab | portainer |
| `sensor.portainer_local_readarr_ab_9` | readarr_ab | portainer |
| `sensor.portainer_local_recursing_greider` | recursing_greider | portainer |
| `sensor.portainer_local_relaxed_shtern` | relaxed_shtern | portainer |
| `sensor.portainer_local_reverent_tu` | reverent_tu | portainer |
| `sensor.portainer_local_sabnzbd` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_10` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_11` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_12` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_13` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_14` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_2` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_3` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_4` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_5` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_6` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_7` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_8` | sabnzbd | portainer |
| `sensor.portainer_local_sabnzbd_9` | sabnzbd | portainer |
| `sensor.portainer_local_serene_antonelli` | serene_antonelli | portainer |
| `sensor.portainer_local_serene_khayyam` | serene_khayyam | portainer |
| `sensor.portainer_local_sleepy_dirac` | sleepy_dirac | portainer |
| `sensor.portainer_local_sonarr` | sonarr | portainer |
| `sensor.portainer_local_sonarr_10` | sonarr | portainer |
| `sensor.portainer_local_sonarr_11` | sonarr | portainer |
| `sensor.portainer_local_sonarr_12` | sonarr | portainer |
| `sensor.portainer_local_sonarr_13` | sonarr | portainer |
| `sensor.portainer_local_sonarr_2` | sonarr | portainer |
| `sensor.portainer_local_sonarr_3` | sonarr | portainer |
| `sensor.portainer_local_sonarr_4` | sonarr | portainer |
| `sensor.portainer_local_sonarr_5` | sonarr | portainer |
| `sensor.portainer_local_sonarr_6` | sonarr | portainer |
| `sensor.portainer_local_sonarr_7` | sonarr | portainer |
| `sensor.portainer_local_sonarr_8` | sonarr | portainer |
| `sensor.portainer_local_sonarr_9` | sonarr | portainer |
| `sensor.portainer_local_stupefied_yalow` | stupefied_yalow | portainer |
| `sensor.portainer_local_sweet_volhard` | sweet_volhard | portainer |
| `sensor.portainer_local_syncthing` | syncthing | portainer |
| `sensor.portainer_local_syncthing_10` | syncthing | portainer |
| `sensor.portainer_local_syncthing_11` | syncthing | portainer |
| `sensor.portainer_local_syncthing_12` | syncthing | portainer |
| `sensor.portainer_local_syncthing_13` | syncthing | portainer |
| `sensor.portainer_local_syncthing_14` | syncthing | portainer |
| `sensor.portainer_local_syncthing_2` | syncthing | portainer |
| `sensor.portainer_local_syncthing_3` | syncthing | portainer |
| `sensor.portainer_local_syncthing_4` | syncthing | portainer |
| `sensor.portainer_local_syncthing_5` | syncthing | portainer |
| `sensor.portainer_local_syncthing_6` | syncthing | portainer |
| `sensor.portainer_local_syncthing_7` | syncthing | portainer |
| `sensor.portainer_local_syncthing_8` | syncthing | portainer |
| `sensor.portainer_local_syncthing_9` | syncthing | portainer |
| `sensor.portainer_local_tdarr` | tdarr | portainer |
| `sensor.portainer_local_tdarr_10` | tdarr | portainer |
| `sensor.portainer_local_tdarr_11` | tdarr | portainer |
| `sensor.portainer_local_tdarr_12` | tdarr | portainer |
| `sensor.portainer_local_tdarr_2` | tdarr | portainer |
| `sensor.portainer_local_tdarr_3` | tdarr | portainer |
| `sensor.portainer_local_tdarr_4` | tdarr | portainer |
| `sensor.portainer_local_tdarr_5` | tdarr | portainer |
| `sensor.portainer_local_tdarr_6` | tdarr | portainer |
| `sensor.portainer_local_tdarr_7` | tdarr | portainer |
| `sensor.portainer_local_tdarr_8` | tdarr | portainer |
| `sensor.portainer_local_tdarr_9` | tdarr | portainer |
| `sensor.portainer_local_tender_jennings` | tender_jennings | portainer |
| `sensor.portainer_local_tender_wiles` | tender_wiles | portainer |
| `sensor.portainer_local_trusting_swanson` | trusting_swanson | portainer |
| `sensor.portainer_local_trusting_volhard` | trusting_volhard | portainer |
| `sensor.portainer_local_vibrant_chebyshev` | vibrant_chebyshev | portainer |
| `sensor.portainer_local_watchtower` | watchtower | portainer |
| `sensor.portainer_local_watchtower_2` | watchtower | portainer |
| `sensor.portainer_local_watchtower_3` | watchtower | portainer |
| `sensor.portainer_local_watchtower_4` | watchtower | portainer |
| `sensor.portainer_local_watchtower_5` | watchtower | portainer |
| `sensor.portainer_local_watchtower_6` | watchtower | portainer |
| `sensor.portainer_local_watchtower_7` | watchtower | portainer |
| `sensor.portainer_local_watchtower_8` | watchtower | portainer |
| `sensor.portainer_local_wizardly_babbage` | wizardly_babbage | portainer |
| `sensor.portainer_local_wonderful_banach` | wonderful_banach | portainer |
| `sensor.portainer_local_xenodochial_kilby` | xenodochial_kilby | portainer |
| `sensor.portainer_local_xenodochial_ptolemy` | xenodochial_ptolemy | portainer |
| `sensor.portainer_local_youthful_benz` | youthful_benz | portainer |
| `sensor.portainer_local_youthful_mahavira` | youthful_mahavira | portainer |
| `sensor.portainer_local_youthful_raman` | youthful_raman | portainer |
| `sensor.portainer_local_zen_fermi` | zen_fermi | portainer |
| `sensor.proxmox_base_url` | Proxmox Base URL | template |
| `sensor.qca4002_rx` | RX | unifi |
| `sensor.qca4002_tx` | TX | unifi |
| `sensor.qemu_media_server_101_cpu_used` | CPU used | proxmoxve |
| `sensor.qemu_media_server_101_disk_used_percentage` | Disk used percentage | proxmoxve |
| `sensor.qemu_media_server_101_last_boot` | Last boot | proxmoxve |
| `sensor.qemu_media_server_101_memory_free` | Memory free | proxmoxve |
| `sensor.qemu_media_server_101_memory_used` | Memory used | proxmoxve |
| `sensor.qemu_media_server_101_memory_used_percentage` | Memory used percentage | proxmoxve |
| `sensor.qemu_media_server_101_node` | Node | proxmoxve |
| `sensor.qemu_media_server_101_status` | Status | proxmoxve |
| `sensor.rain_alert` | Rain Alert | template |
| `sensor.rain_probability_tomorrow` | Rain Probability Tomorrow | template |
| `sensor.reading_light_rx` | RX | unifi |
| `sensor.reading_light_tx` | TX | unifi |
| `sensor.relevant_weather_warnings_count` | Relevant Weather Warnings Count | template |
| `sensor.remotes` | Remotes | spook |
| `sensor.rx` | RX | unifi |
| `sensor.rx_10` | RX | unifi |
| `sensor.rx_11` | RX | unifi |
| `sensor.rx_12` | RX | unifi |
| `sensor.rx_13` | RX | unifi |
| `sensor.rx_14` | RX | unifi |
| `sensor.rx_15` | RX | unifi |
| `sensor.rx_16` | RX | unifi |
| `sensor.rx_17` | RX | unifi |
| `sensor.rx_18` | RX | unifi |
| `sensor.rx_19` | RX | unifi |
| `sensor.rx_2` | RX | unifi |
| `sensor.rx_20` | RX | unifi |
| `sensor.rx_21` | RX | unifi |
| `sensor.rx_22` | RX | unifi |
| `sensor.rx_23` | RX | unifi |
| `sensor.rx_24` | RX | unifi |
| `sensor.rx_25` | RX | unifi |
| `sensor.rx_26` | RX | unifi |
| `sensor.rx_27` | RX | unifi |
| `sensor.rx_28` | RX | unifi |
| `sensor.rx_3` | RX | unifi |
| `sensor.rx_30` | RX | unifi |
| `sensor.rx_36` | RX | unifi |
| `sensor.rx_38` | RX | unifi |
| `sensor.rx_39` | RX | unifi |
| `sensor.rx_4` | RX | unifi |
| `sensor.rx_44` | RX | unifi |
| `sensor.rx_45` | RX | unifi |
| `sensor.rx_49` | RX | unifi |
| `sensor.rx_5` | RX | unifi |
| `sensor.rx_57` | RX | unifi |
| `sensor.rx_6` | RX | unifi |
| `sensor.rx_64` | RX | unifi |
| `sensor.rx_7` | RX | unifi |
| `sensor.rx_8` | RX | unifi |
| `sensor.rx_9` | RX | unifi |
| `sensor.s14e81868ae650f9fc_203d_estimated_distance` | Estimated distance | ibeacon |
| `sensor.s52b8e5d99d047c0ec_56cc_estimated_distance` | Estimated distance | ibeacon |
| `sensor.s9d6ec136dd860422c_58f1_estimated_distance` | Estimated distance | ibeacon |
| `sensor.sa6e2be45dc723626c_16ea_estimated_distance` | Estimated distance | ibeacon |
| `sensor.samsung_galaxy_s22_ultra_app_rx_gb` | Samsung Galaxy S22 Ultra App Rx GB | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_app_tx_gb` | Samsung Galaxy S22 Ultra App Tx GB | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.samsung_galaxy_s22_ultra_battery_level` | Samsung Galaxy S22 Ultra Battery level | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_battery_plus` | Battery+ | battery_notes |
| `sensor.samsung_galaxy_s22_ultra_battery_state` | Samsung Galaxy S22 Ultra Battery state | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_battery_type` | Battery type | battery_notes |
| `sensor.samsung_galaxy_s22_ultra_ble_transmitter` | Samsung Galaxy S22 Ultra BLE transmitter | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_bluetooth_connection` | Samsung Galaxy S22 Ultra Bluetooth connection | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_charger_type` | Samsung Galaxy S22 Ultra Charger type | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_detected_activity` | Samsung Galaxy S22 Ultra Detected activity | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_geocoded_location` | Samsung Galaxy S22 Ultra Geocoded location | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_high_accuracy_update_interval` | Samsung Galaxy S22 Ultra High accuracy update interval | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_network_type` | Samsung Galaxy S22 Ultra Network type | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_sleep_confidence` | Samsung Galaxy S22 Ultra Sleep confidence | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_sleep_segment` | Samsung Galaxy S22 Ultra Sleep segment | mobile_app |
| `sensor.samsung_galaxy_s22_ultra_wifi_connection` | Samsung Galaxy S22 Ultra Wi-Fi connection | mobile_app |
| `sensor.scenes` | Scenes | spook |
| `sensor.scripts` | Scripts | spook |
| `sensor.selects` | Selects | spook |
| `sensor.sensors` | Sensors | spook |
| `sensor.server_power_switch_current` | Server power switch Current | zha |
| `sensor.server_power_switch_power` | Server power switch Power | zha |
| `sensor.server_power_switch_summation_delivered` | Server power switch Summation delivered | zha |
| `sensor.server_power_switch_voltage` | Server power switch Voltage | zha |
| `sensor.server_rx` | RX | unifi |
| `sensor.server_switch_rx` | RX | unifi |
| `sensor.server_switch_tx` | TX | unifi |
| `sensor.server_switch_uptime` | Uptime | unifi |
| `sensor.server_tx` | TX | unifi |
| `sensor.sf41225f64c0af8edc_a202_estimated_distance` | Estimated distance | ibeacon |
| `sensor.side_garage_door_sensor_magnet_battery` | side garage door sensor magnet Battery | zha |
| `sensor.side_garage_door_sensor_magnet_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.side_garage_door_sensor_magnet_battery_plus` | Battery+ | battery_notes |
| `sensor.side_garage_door_sensor_magnet_battery_type` | Battery type | battery_notes |
| `sensor.side_garage_door_sensor_magnet_device_temperature` | side garage door sensor magnet Device temperature | zha |
| `sensor.silent_bob_rx` | RX | unifi |
| `sensor.silent_bob_tx` | TX | unifi |
| `sensor.sink_leak_detection_battery` | Sink leak detection Battery | zha |
| `sensor.sink_leak_detection_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.sink_leak_detection_battery_plus` | Battery+ | battery_notes |
| `sensor.sink_leak_detection_battery_type` | Battery type | battery_notes |
| `sensor.sirens` | Sirens | spook |
| `sensor.sleeping_light_rx` | RX | unifi |
| `sensor.sleeping_light_tx` | TX | unifi |
| `sensor.slvdh_activity` | slvdh Activity | mobile_app |
| `sensor.slvdh_app_version` | slvdh App Version | mobile_app |
| `sensor.slvdh_audio_output` | slvdh Audio Output | mobile_app |
| `sensor.slvdh_average_active_pace` | slvdh Average Active Pace | mobile_app |
| `sensor.slvdh_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.slvdh_battery_level` | slvdh Battery Level | mobile_app |
| `sensor.slvdh_battery_plus` | Battery+ | battery_notes |
| `sensor.slvdh_battery_state` | slvdh Battery State | mobile_app |
| `sensor.slvdh_battery_type` | Battery type | battery_notes |
| `sensor.slvdh_bssid` | slvdh BSSID | mobile_app |
| `sensor.slvdh_connection_type` | slvdh Connection Type | mobile_app |
| `sensor.slvdh_distance` | slvdh Distance | mobile_app |
| `sensor.slvdh_floors_ascended` | slvdh Floors Ascended | mobile_app |
| `sensor.slvdh_floors_descended` | slvdh Floors Descended | mobile_app |
| `sensor.slvdh_geocoded_location` | slvdh Geocoded Location | mobile_app |
| `sensor.slvdh_last_update_trigger` | slvdh Last Update Trigger | mobile_app |
| `sensor.slvdh_location_permission` | slvdh Location permission | mobile_app |
| `sensor.slvdh_rx` | RX | unifi |
| `sensor.slvdh_sim_1` | slvdh SIM 1 | mobile_app |
| `sensor.slvdh_sim_2` | slvdh SIM 2 | mobile_app |
| `sensor.slvdh_ssid` | slvdh SSID | mobile_app |
| `sensor.slvdh_steps` | slvdh Steps | mobile_app |
| `sensor.slvdh_storage` | slvdh Storage | mobile_app |
| `sensor.slvdh_tx` | TX | unifi |
| `sensor.smart_garage_door_rx` | RX | unifi |
| `sensor.smart_garage_door_signal_strength` | Smart Garage Door signal_strength | meross_lan |
| `sensor.smart_garage_door_tx` | TX | unifi |
| `sensor.smart_garage_door_uptime` | Uptime | unifi |
| `sensor.smart_plug_current` | Current | meross_lan |
| `sensor.smart_plug_energy` | Volts | meross_lan |
| `sensor.smart_plug_power` | Watt | meross_lan |
| `sensor.smart_plug_voltage` | Dishwasher Smart Plug voltage | meross_lan |
| `sensor.sonarr_disk_space` | Disk space | sonarr |
| `sensor.sonarr_queue` | Queue | sonarr |
| `sensor.sonarr_shows` | Shows | sonarr |
| `sensor.sonarr_upcoming` | Upcoming | sonarr |
| `sensor.sonnar_upcoming_media_sonarr_upcoming_media` | Sonnar upcoming media Sonarr Upcoming Media | sonarr_upcoming_media |
| `sensor.sonoff_snzb_05p_battery` | Battery | zha |
| `sensor.stephanies_ipad_activity` | Stephanie’s iPad Activity | mobile_app |
| `sensor.stephanies_ipad_app_version` | Stephanie’s iPad App Version | mobile_app |
| `sensor.stephanies_ipad_audio_output` | Stephanie’s iPad Audio Output | mobile_app |
| `sensor.stephanies_ipad_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.stephanies_ipad_battery_level` | Stephanie’s iPad Battery Level | mobile_app |
| `sensor.stephanies_ipad_battery_plus` | Battery+ | battery_notes |
| `sensor.stephanies_ipad_battery_state` | Stephanie’s iPad Battery State | mobile_app |
| `sensor.stephanies_ipad_battery_type` | Battery type | battery_notes |
| `sensor.stephanies_ipad_bssid` | Stephanie’s iPad BSSID | mobile_app |
| `sensor.stephanies_ipad_connection_type` | Stephanie’s iPad Connection Type | mobile_app |
| `sensor.stephanies_ipad_geocoded_location` | Stephanie’s iPad Geocoded Location | mobile_app |
| `sensor.stephanies_ipad_last_update_trigger` | Stephanie’s iPad Last Update Trigger | mobile_app |
| `sensor.stephanies_ipad_location_permission` | Stephanie’s iPad Location permission | mobile_app |
| `sensor.stephanies_ipad_ssid` | Stephanie’s iPad SSID | mobile_app |
| `sensor.stephanies_ipad_storage` | Stephanie’s iPad Storage | mobile_app |
| `sensor.stephen_s_s22_rx` | RX | unifi |
| `sensor.stephen_s_s22_tx` | TX | unifi |
| `sensor.steve_s_phone_rx` | RX | unifi |
| `sensor.steve_s_phone_tx` | TX | unifi |
| `sensor.stt` | Speech-to-text | spook |
| `sensor.study_esp32_henrysroom_battery_level` | HenrysRoom Battery Level | esphome |
| `sensor.study_esp32_henrysroom_humidity` | HenrysRoom Humidity | esphome |
| `sensor.study_esp32_henrysroom_temperature` | HenrysRoom Temperature | esphome |
| `sensor.study_esp32_ottosroom_battery_level` | OttosRoom Battery Level | esphome |
| `sensor.study_esp32_ottosroom_humidity` | OttosRoom Humidity | esphome |
| `sensor.study_esp32_ottosroom_temperature` | OttosRoom Temperature | esphome |
| `sensor.study_esp32_rx` | RX | unifi |
| `sensor.study_esp32_tx` | TX | unifi |
| `sensor.study_henry_s_room_ac_filter_last_changed_date` | Study/Henry's Room AC Filter Last Changed Date | template |
| `sensor.study_rx` | RX | unifi |
| `sensor.study_rx_2` | RX | unifi |
| `sensor.study_tx` | TX | unifi |
| `sensor.study_tx_2` | TX | unifi |
| `sensor.sun_next_dawn` | Next dawn | sun |
| `sensor.sun_next_dusk` | Next dusk | sun |
| `sensor.sun_next_midnight` | Next midnight | sun |
| `sensor.sun_next_noon` | Next noon | sun |
| `sensor.sun_next_rising` | Next rising | sun |
| `sensor.sun_next_setting` | Next setting | sun |
| `sensor.suns` | Suns | spook |
| `sensor.switch_battery` | Front door Button Switch Battery | zha |
| `sensor.switchbot_hub_2_rx` | RX | unifi |
| `sensor.switchbot_hub_2_tx` | TX | unifi |
| `sensor.switchbot_hub_2_uptime` | Uptime | unifi |
| `sensor.switches` | Switches | spook |
| `sensor.tablet_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.tablet_battery_level` | tablet Battery level | mobile_app |
| `sensor.tablet_battery_plus` | Battery+ | battery_notes |
| `sensor.tablet_battery_state` | tablet Battery state | mobile_app |
| `sensor.tablet_battery_type` | Battery type | battery_notes |
| `sensor.tablet_charger_type` | tablet Charger type | mobile_app |
| `sensor.temperature_forecast_next_hour` | Temperature forecast next hour | template |
| `sensor.temperaturesensor_temperature` | Temperature | matter |
| `sensor.test_forecast_today` | Test forecast today | template |
| `sensor.texts` | Texts | spook |
| `sensor.times` | Times | spook |
| `sensor.tnb_09412323_rx` | RX | unifi |
| `sensor.tnb_09412323_tx` | TX | unifi |
| `sensor.total_security_entities` | Total Security Entities | template |
| `sensor.tts` | Text-to-speech | spook |
| `sensor.tx` | TX | unifi |
| `sensor.tx_10` | TX | unifi |
| `sensor.tx_11` | TX | unifi |
| `sensor.tx_12` | TX | unifi |
| `sensor.tx_13` | TX | unifi |
| `sensor.tx_14` | TX | unifi |
| `sensor.tx_15` | TX | unifi |
| `sensor.tx_16` | TX | unifi |
| `sensor.tx_17` | TX | unifi |
| `sensor.tx_18` | TX | unifi |
| `sensor.tx_19` | TX | unifi |
| `sensor.tx_2` | TX | unifi |
| `sensor.tx_20` | TX | unifi |
| `sensor.tx_21` | TX | unifi |
| `sensor.tx_22` | TX | unifi |
| `sensor.tx_23` | TX | unifi |
| `sensor.tx_24` | TX | unifi |
| `sensor.tx_25` | TX | unifi |
| `sensor.tx_26` | TX | unifi |
| `sensor.tx_27` | TX | unifi |
| `sensor.tx_28` | TX | unifi |
| `sensor.tx_3` | TX | unifi |
| `sensor.tx_30` | TX | unifi |
| `sensor.tx_36` | TX | unifi |
| `sensor.tx_38` | TX | unifi |
| `sensor.tx_39` | TX | unifi |
| `sensor.tx_4` | TX | unifi |
| `sensor.tx_44` | TX | unifi |
| `sensor.tx_45` | TX | unifi |
| `sensor.tx_49` | TX | unifi |
| `sensor.tx_5` | TX | unifi |
| `sensor.tx_57` | TX | unifi |
| `sensor.tx_6` | TX | unifi |
| `sensor.tx_64` | TX | unifi |
| `sensor.tx_7` | TX | unifi |
| `sensor.tx_8` | TX | unifi |
| `sensor.tx_9` | TX | unifi |
| `sensor.ubuntu_server_rx` | RX | unifi |
| `sensor.ubuntu_server_tx` | TX | unifi |
| `sensor.ucg_ultra_clients` | Clients | unifi |
| `sensor.ucg_ultra_cloudflare_wan_latency` | Cloudflare WAN latency | unifi |
| `sensor.ucg_ultra_cpu_utilization` | CPU utilization | unifi |
| `sensor.ucg_ultra_google_wan_latency` | Google WAN latency | unifi |
| `sensor.ucg_ultra_memory_utilization` | Memory utilization | unifi |
| `sensor.ucg_ultra_microsoft_wan_latency` | Microsoft WAN latency | unifi |
| `sensor.ucg_ultra_port_1_rx` | Port 1 RX | unifi |
| `sensor.ucg_ultra_port_1_tx` | Port 1 TX | unifi |
| `sensor.ucg_ultra_port_2_rx` | Port 2 RX | unifi |
| `sensor.ucg_ultra_port_2_tx` | Port 2 TX | unifi |
| `sensor.ucg_ultra_port_3_rx` | Port 3 RX | unifi |
| `sensor.ucg_ultra_port_3_tx` | Port 3 TX | unifi |
| `sensor.ucg_ultra_port_4_rx` | Port 4 RX | unifi |
| `sensor.ucg_ultra_port_4_tx` | Port 4 TX | unifi |
| `sensor.ucg_ultra_port_5_rx` | Port 5 RX | unifi |
| `sensor.ucg_ultra_port_5_tx` | Port 5 TX | unifi |
| `sensor.ucg_ultra_state` | State | unifi |
| `sensor.ucg_ultra_ucg_ultra_cpu_temperature` | UCG Ultra CPU Temperature | unifi |
| `sensor.ucg_ultra_uptime` | Uptime | unifi |
| `sensor.update` | Update | spook |
| `sensor.upstairs_cpu_utilization` | CPU utilization | unifi |
| `sensor.upstairs_memory_utilization` | Memory utilization | unifi |
| `sensor.upstairs_state` | State | unifi |
| `sensor.upstairs_uplink_mac` | Uplink MAC | unifi |
| `sensor.upstairs_uptime` | Uptime | unifi |
| `sensor.usw_16_poe_cpu_utilization` | CPU utilization | unifi |
| `sensor.usw_16_poe_memory_utilization` | Memory utilization | unifi |
| `sensor.usw_16_poe_state` | State | unifi |
| `sensor.usw_16_poe_uplink_mac` | Uplink MAC | unifi |
| `sensor.usw_16_poe_uptime` | Uptime | unifi |
| `sensor.vacuums` | Vacuums | spook |
| `sensor.washing_machine_estimated_remaining` | Washing Machine Estimated Remaining | template |
| `sensor.washing_machine_last_changed` | Laundry Last Changed | template |
| `sensor.washing_machine_power_plug_current` | Current | zha |
| `sensor.washing_machine_power_plug_power` | Power | zha |
| `sensor.washing_machine_power_plug_summation_delivered` | Summation delivered | zha |
| `sensor.washing_machine_power_plug_voltage` | Voltage | zha |
| `sensor.washing_machine_random_message` | Washing Machine Random Message | template |
| `sensor.water_heaters` | Water heaters | spook |
| `sensor.water_leak_detection_battery` | Battery | zha |
| `sensor.water_leak_detection_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.water_leak_detection_battery_plus` | Battery+ | battery_notes |
| `sensor.water_leak_detection_battery_type` | Battery type | battery_notes |
| `sensor.water_leak_detector_battery` | Water leak detector Battery | zha |
| `sensor.water_leak_detector_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.water_leak_detector_battery_last_replaced_2` | Battery last replaced | battery_notes |
| `sensor.water_leak_detector_battery_plus` | Battery+ | battery_notes |
| `sensor.water_leak_detector_battery_plus_2` | Battery+ | battery_notes |
| `sensor.water_leak_detector_battery_type` | Battery type | battery_notes |
| `sensor.water_leak_detector_battery_type_2` | Battery type | battery_notes |
| `sensor.water_switch_battery` | Battery | zha |
| `sensor.water_switch_battery_last_replaced` | Battery last replaced | battery_notes |
| `sensor.water_switch_battery_plus` | Battery+ | battery_notes |
| `sensor.water_switch_battery_type` | Battery type | battery_notes |
| `sensor.water_switch_volume_flow_rate` | Volume flow rate | zha |
| `sensor.weather` | Weather | spook |
| `sensor.wilc_rx` | RX | unifi |
| `sensor.wilc_rx_2` | RX | unifi |
| `sensor.wilc_tx` | TX | unifi |
| `sensor.wilc_tx_2` | TX | unifi |
| `sensor.win_server_base_url` | Win Server Base URL | template |
| `sensor.win_server_rx` | RX | unifi |
| `sensor.win_server_tx` | TX | unifi |
| `sensor.wlan0_rx` | RX | unifi |
| `sensor.wlan0_rx_2` | RX | unifi |
| `sensor.wlan0_tx` | TX | unifi |
| `sensor.wlan0_tx_2` | TX | unifi |
| `sensor.work_calendar_this_week` | Work Calendar This Week | template |
| `sensor.xmas_lights_plug_current` | Current | tuya |
| `sensor.xmas_lights_plug_power` | Power | tuya |
| `sensor.xmas_lights_plug_total_energy` | Total energy | tuya |
| `sensor.xmas_lights_plug_voltage` | Voltage | tuya |
| `sensor.yeelink_light_color2_miap2566_rx` | RX | unifi |
| `sensor.yeelink_light_color2_miap2566_tx` | TX | unifi |
| `sensor.zones` | Zones | spook |

## Binary Sensors

Motion, door, window, and connectivity sensors.

**Total:** 246 (174 enabled, 72 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `binary_sensor.a4c138f1205c_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.aqara_motion_and_light_sensor_p2_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.aqara_motion_and_light_sensor_p2_occupancy` | Occupancy | matter |
| `binary_sensor.at_work_zone_only` | At Work Zone Only | template |
| `binary_sensor.balcony_door_sensor_magnet_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.balcony_door_sensor_magnet_opening_2` | Balcony Door | zha |
| `binary_sensor.bi_alerts` | BI Alerts | blueiris |
| `binary_sensor.bi_door_camera_audio` | BI Door Camera Audio | blueiris |
| `binary_sensor.bi_door_camera_connectivity` | BI Door Camera Connectivity | blueiris |
| `binary_sensor.bi_door_camera_dio` | BI Door Camera DIO | blueiris |
| `binary_sensor.bi_door_camera_external` | BI Door Camera External | blueiris |
| `binary_sensor.bi_door_camera_motion` | BI Door Camera Motion | blueiris |
| `binary_sensor.bi_driveway_audio` | BI Driveway Audio | blueiris |
| `binary_sensor.bi_driveway_connectivity` | BI Driveway Connectivity | blueiris |
| `binary_sensor.bi_driveway_dio` | BI Driveway DIO | blueiris |
| `binary_sensor.bi_driveway_external` | BI Driveway External | blueiris |
| `binary_sensor.bi_driveway_motion` | BI Driveway Motion | blueiris |
| `binary_sensor.bi_front_door_camera_audio` | BI Front Door Camera Audio | blueiris |
| `binary_sensor.bi_front_door_camera_connectivity` | BI Front Door Camera Connectivity | blueiris |
| `binary_sensor.bi_front_door_camera_dio` | BI Front Door Camera DIO | blueiris |
| `binary_sensor.bi_front_door_camera_external` | BI Front Door Camera External | blueiris |
| `binary_sensor.bi_front_door_camera_motion` | BI Front Door Camera Motion | blueiris |
| `binary_sensor.blue_iris_cam_driveway` | Blue Iris Cam Driveway | mqtt |
| `binary_sensor.blue_iris_cam_front_door` | Blue Iris Cam Front Door | mqtt |
| `binary_sensor.cold_weather_alert` | Cold Weather Alert | template |
| `binary_sensor.curtain_3_b3bb_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.curtain_3_b3bb_calibration` | Calibration | switchbot |
| `binary_sensor.curtain_should_close_brightness` | Curtain - Should Close (Brightness) | template |
| `binary_sensor.dishwasher_suggestion` | Dishwasher Suggestion | template |
| `binary_sensor.disk_pve_001_1e6164_dev_sdb_health` | Health | proxmoxve |
| `binary_sensor.disk_pve_003_2cy186_dev_sdc_health` | Health | proxmoxve |
| `binary_sensor.disk_pve_003_2cy186_dev_sdd_health` | Health | proxmoxve |
| `binary_sensor.disk_pve_004_2cv104_dev_sda_health` | Health | proxmoxve |
| `binary_sensor.disk_pve_samsung_ssd_980_500gb_dev_nvme0n1_health` | Health | proxmoxve |
| `binary_sensor.downstairs_doors` | Downstairs Doors | group |
| `binary_sensor.driveway_cam_motion` | Motion | reolink |
| `binary_sensor.dryer_estimated_remaining` | Dryer Estimated Remaining | template |
| `binary_sensor.dryer_suggestion` | Dryer Suggestion | template |
| `binary_sensor.espresense_livingroom` | Connectivity | mqtt |
| `binary_sensor.external_door_open_at_night` | External Door Open at Night | template |
| `binary_sensor.front_door_button_switch_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.front_door_cam_motion_2` | Motion | reolink |
| `binary_sensor.front_door_sensor_opening` | Front Door | zha |
| `binary_sensor.front_door_water_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.front_door_water_sensor_moisture` | Front Door Roof Moisture | zha |
| `binary_sensor.garage_door_alert` | Garage door alert | template |
| `binary_sensor.gosungrow_getpsdetail_1205796_has_ammeter` | GoSungrow getPsDetail.1205796.has_ammeter | mqtt |
| `binary_sensor.gosungrow_getpsdetail_1205796_is_have_es_inverter` | GoSungrow getPsDetail.1205796.is_have_es_inverter | mqtt |
| `binary_sensor.gosungrow_getpsdetail_1205796_is_transform_system` | GoSungrow getPsDetail.1205796.is_transform_system | mqtt |
| `binary_sensor.gosungrow_getpsdetail_1205796_is_tuv` | GoSungrow getPsDetail.1205796.is_tuv | mqtt |
| `binary_sensor.gosungrow_getpsdetail_1205796_p83023y_valid` | GoSungrow getPsDetail.1205796.p83023y.valid | mqtt |
| `binary_sensor.gosungrow_getpsdetail_1205796_power_charge_set` | GoSungrow getPsDetail.1205796.power_charge_set | mqtt |
| `binary_sensor.gosungrow_getpsdetail_1205796_valid_flag` | GoSungrow getPsDetail.1205796.valid_flag | mqtt |
| `binary_sensor.gosungrow_getpslist_devices_1205796_is_bank_ps` | GoSungrow getPsList.devices.1205796.is_bank_ps | mqtt |
| `binary_sensor.gosungrow_getpslist_devices_1205796_is_tuv` | GoSungrow getPsList.devices.1205796.is_tuv | mqtt |
| `binary_sensor.gosungrow_getpslist_devices_1205796_mlpe_flag` | GoSungrow getPsList.devices.1205796.mlpe_flag | mqtt |
| `binary_sensor.gosungrow_getpslist_devices_1205796_ps_is_not_init` | GoSungrow getPsList.devices.1205796.ps_is_not_init | mqtt |
| `binary_sensor.gosungrow_getpslist_devices_1205796_ps_status` | GoSungrow getPsList.devices.1205796.ps_status | mqtt |
| `binary_sensor.gosungrow_getpslist_devices_1205796_valid_flag` | GoSungrow getPsList.devices.1205796.valid_flag | mqtt |
| `binary_sensor.henry_door_sensor_magnet_opening` | Henry's Door | zha |
| `binary_sensor.henry_s_door_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.henry_s_room_temp_humidity_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.henry_s_room_temp_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.henrys_room_overpowering_state` | Overpowering state | versatile_thermostat |
| `binary_sensor.henrys_room_presence_state` | Presence state | versatile_thermostat |
| `binary_sensor.henrys_room_security_state` | Security state | versatile_thermostat |
| `binary_sensor.henrys_room_window_bypass` | Window bypass | versatile_thermostat |
| `binary_sensor.henrys_room_window_state` | Window state | versatile_thermostat |
| `binary_sensor.henrys_thermometer` | Henrys thermometer  | threshold |
| `binary_sensor.holiday_season` | Holiday Season | template |
| `binary_sensor.hot_weather_alert` | Hot Weather Alert | template |
| `binary_sensor.hvac_door_open_alert` | HVAC Door Open Alert | template |
| `binary_sensor.interior_garage_door_sensor_magnet_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.interior_garage_door_sensor_magnet_opening` | interior garage door sensor magnet Opening | zha |
| `binary_sensor.living_room_ac_overpowering_state` | Overpowering state | versatile_thermostat |
| `binary_sensor.living_room_ac_presence_state` | Presence state | versatile_thermostat |
| `binary_sensor.living_room_ac_security_state` | Security state | versatile_thermostat |
| `binary_sensor.living_room_ac_window_bypass` | Window bypass | versatile_thermostat |
| `binary_sensor.living_room_ac_window_state` | Window state | versatile_thermostat |
| `binary_sensor.living_room_door_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.living_room_door_sensor_opening` | Living Room Door | zha |
| `binary_sensor.lumi_lumi_sensor_magnet_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.lumi_lumi_sensor_wleak_aq1_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.lumi_lumi_sensor_wleak_aq1_moisture` | Laundry Moisture | zha |
| `binary_sensor.master_bed_switch_4_battery_plus_low` | Master Bed Switch 4 Battery low | battery_notes |
| `binary_sensor.master_bedroom_door_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.master_bedroom_door_sensor_opening` | Master Bedroom Door | zha |
| `binary_sensor.master_switch_3_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.masterbed_7989_power` | Power | bthome |
| `binary_sensor.masterbed_ac_presence_state` | Presence state | versatile_thermostat |
| `binary_sensor.masterbed_ac_security_state` | Security state | versatile_thermostat |
| `binary_sensor.masterbed_ac_window_bypass` | Window bypass | versatile_thermostat |
| `binary_sensor.masterbed_ac_window_state` | Window state | versatile_thermostat |
| `binary_sensor.masterbed_sink_leak_detector_2` | Masterbed Sink Leak Detector | zha |
| `binary_sensor.masterbed_sink_leak_detector_battery_plus_low` | Masterbed Sink Leak Detector Battery low | battery_notes |
| `binary_sensor.masterbed_switch_1_battery_plus_low` | Masterbed Switch 1 Battery low | battery_notes |
| `binary_sensor.masterbed_switch_2_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.motion_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.motion_sensor_motion` | Hallway Motion | zha |
| `binary_sensor.motion_sensor_occupancy` | Occupancy | zha |
| `binary_sensor.node_pve_status` | Status | proxmoxve |
| `binary_sensor.node_pve_updates_packages` | Updates packages | proxmoxve |
| `binary_sensor.otto_room_door_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.otto_room_door_sensor_opening` | Otto's Door | zha |
| `binary_sensor.otto_s_room_temp_humidity_sensor_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.ottos_room_ac_overpowering_state` | Overpowering state | versatile_thermostat |
| `binary_sensor.ottos_room_ac_presence_state` | Presence state | versatile_thermostat |
| `binary_sensor.ottos_room_ac_security_state` | Security state | versatile_thermostat |
| `binary_sensor.ottos_room_ac_window_bypass` | Window bypass | versatile_thermostat |
| `binary_sensor.ottos_room_ac_window_state` | Window state | versatile_thermostat |
| `binary_sensor.ping_firewalla` | None | ping |
| `binary_sensor.ping_pve1` | None | ping |
| `binary_sensor.pingext_google_dns` | None | ping |
| `binary_sensor.pingext_opendns` | None | ping |
| `binary_sensor.qemu_media_server_101_health` | Health | proxmoxve |
| `binary_sensor.qemu_media_server_101_status` | Status | proxmoxve |
| `binary_sensor.rain_alert` | Rain Alert | template |
| `binary_sensor.room_climate_alert` | Room Climate Alert | template |
| `binary_sensor.rpi_power_status` | RPi Power status | rpi_power |
| `binary_sensor.samsung_galaxy_s22_ultra_android_auto` | Samsung Galaxy S22 Ultra Android Auto | mobile_app |
| `binary_sensor.samsung_galaxy_s22_ultra_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.samsung_galaxy_s22_ultra_high_accuracy_mode` | Samsung Galaxy S22 Ultra High accuracy mode | mobile_app |
| `binary_sensor.samsung_galaxy_s22_ultra_is_charging` | Samsung Galaxy S22 Ultra Is charging | mobile_app |
| `binary_sensor.samsung_galaxy_s22_ultra_work_profile` | Samsung Galaxy S22 Ultra Work profile | mobile_app |
| `binary_sensor.security_cameras_alerts` | Security-Cameras Alerts | blueiris |
| `binary_sensor.security_cameras_driveway_audio` | Security-Cameras Driveway Audio | blueiris |
| `binary_sensor.security_cameras_driveway_connectivity` | Security-Cameras Driveway Connectivity | blueiris |
| `binary_sensor.security_cameras_driveway_dio` | Security-Cameras Driveway DIO | blueiris |
| `binary_sensor.security_cameras_driveway_external` | Security-Cameras Driveway External | blueiris |
| `binary_sensor.security_cameras_driveway_motion` | Security-Cameras Driveway Motion | blueiris |
| `binary_sensor.security_cameras_front_door_camera_audio` | Security-Cameras Front Door Camera Audio | blueiris |
| `binary_sensor.security_cameras_front_door_camera_connectivity` | Security-Cameras Front Door Camera Connectivity | blueiris |
| `binary_sensor.security_cameras_front_door_camera_dio` | Security-Cameras Front Door Camera DIO | blueiris |
| `binary_sensor.security_cameras_front_door_camera_external` | Security-Cameras Front Door Camera External | blueiris |
| `binary_sensor.security_cameras_front_door_camera_motion` | Security-Cameras Front Door Camera Motion | blueiris |
| `binary_sensor.show_arriving_home_button` | Show Arriving Home Button | template |
| `binary_sensor.show_arriving_home_button_filtered` | Show Arriving Home Button Filtered | template |
| `binary_sensor.show_good_morning_button` | Show Good Morning Button | template |
| `binary_sensor.show_good_morning_button_filtered` | Show Good Morning Button Filtered | template |
| `binary_sensor.show_good_night_button` | Show Good Night Button | template |
| `binary_sensor.show_good_night_button_filtered` | Show Good Night Button Filtered | template |
| `binary_sensor.show_leaving_home_button` | Show Leaving Home Button | template |
| `binary_sensor.show_leaving_home_button_filtered` | Show Leaving Home Button Filtered | template |
| `binary_sensor.show_naptime_button` | Show Naptime Button | template |
| `binary_sensor.show_naptime_button_filtered` | Show Naptime Button Filtered | template |
| `binary_sensor.show_play_music_button_filtered` | Show Play Music Button Filtered | template |
| `binary_sensor.show_read_news_button_filtered` | Show Read News Button Filtered | template |
| `binary_sensor.show_water_plants_button` | Show Water Plants Button | template |
| `binary_sensor.show_water_plants_button_filtered` | Show Water Plants Button Filtered | template |
| `binary_sensor.side_garage_door_sensor_magnet_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.side_garage_door_sensor_magnet_opening` | Side Garage Door | zha |
| `binary_sensor.sink_leak_detection` | Sink leak detection | zha |
| `binary_sensor.sink_leak_detection_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.slvdh_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.slvdh_focus` | slvdh Focus | mobile_app |
| `binary_sensor.smart_garage_door_problem` | Smart Garage Door problem | meross_lan |
| `binary_sensor.smoke_alarm_smoke` | Garage Smoke Alarm | zha |
| `binary_sensor.solar_excess_available` | Solar Excess Available | template |
| `binary_sensor.someone_home` | Someone Home | template |
| `binary_sensor.sonoff_snzb_05p` | None | zha |
| `binary_sensor.stephanies_ipad_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.stephanies_ipad_focus` | Stephanie’s iPad Focus | mobile_app |
| `binary_sensor.tablet_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.washing_machine_estimated_remaining` | Washing Machine Estimated Remaining | template |
| `binary_sensor.washing_machine_suggestion` | Washing Machine Suggestion | template |
| `binary_sensor.water_leak_detection` | None | zha |
| `binary_sensor.water_leak_detection_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.water_leak_detector` | Water leak detector | zha |
| `binary_sensor.water_leak_detector_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.water_leak_detector_battery_plus_low_2` | Battery low | battery_notes |
| `binary_sensor.water_switch_battery_plus_low` | Battery low | battery_notes |
| `binary_sensor.water_switch_water_leak` | Water leak | zha |
| `binary_sensor.water_switch_water_supply` | Water supply | zha |
| `binary_sensor.workday_sensor` | None | workday |

## Media Players

TVs, speakers, and media devices.

**Total:** 37 (36 enabled, 1 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `media_player.downstairs` | None | cast |
| `media_player.googletv0235` | None | cast |
| `media_player.gtv_living_room_2` | None | cast |
| `media_player.kitchen` | None | cast |
| `media_player.kitchen_1` | None | cast |
| `media_player.living_room_tv` | None | cast |
| `media_player.living_room_tv_2` | Living Room TV | dlna_dmr |
| `media_player.living_room_wiimamp` | None | linkplay |
| `media_player.master_bedroom_speaker` | Masterbed | cast |
| `media_player.plex_otto_plex_for_android_tv_google_tv_streamer` | Plex (Steph - Plex for Android (TV) - Google TV Streamer) | plex |
| `media_player.plex_otto_plex_web_chrome_android` | Plex (Plex Web - Chrome - Android) | plex |
| `media_player.plex_otto_plex_web_firefox_android` | Plex (Otto - Plex Web - Firefox - Android) | plex |
| `media_player.plex_otto_plex_web_firefox_linux` | Plex (Plex Web - Firefox - Linux) | plex |
| `media_player.plex_plex_for_android_mobile_phils_phone` | Plex (Plex for Android (Mobile) - Phils phone) | plex |
| `media_player.plex_plex_for_ios_ipad` | Plex (Steph - Plex for iOS - iPad) | plex |
| `media_player.plex_plex_web_chrome_linux` | Plex (Plex Web - Chrome - Linux) | plex |
| `media_player.plex_plex_web_chrome_windows` | Plex (Plex Web - Chrome - Windows) | plex |
| `media_player.plex_plex_web_chrome_windows_2` | Plex (Plex Web - Chrome - Windows) | plex |
| `media_player.plex_plex_web_firefox_windows` | Plex (Plex Web - Firefox - Windows) | plex |
| `media_player.plex_plex_web_firefox_windows_2` | Plex (Plex Web - Firefox - Windows) | plex |
| `media_player.plex_plex_web_safari_osx` | Plex (Plex Web - Safari - OSX) | plex |
| `media_player.plex_plexamp_android` | Plex (Plexamp - Android) | plex |
| `media_player.plex_steph_plex_for_android_tv_chromecast_google_tv` | Plex (Plex for Android (TV) - Chromecast Google TV) | plex |
| `media_player.plex_steph_plex_web_safari_ios` | Plex (Steph - Plex Web - Safari - iOS) | plex |
| `media_player.plex_steph_plex_web_safari_ios_2` | Plex (Steph - Plex Web - Safari - iOS) | plex |
| `media_player.plex_steph_plex_web_safari_ios_3` | Plex (Steph - Plex Web - Safari - iOS) | plex |
| `media_player.plex_steph_plex_web_safari_osx` | Plex (Steph - Plex Web - Safari - OSX) | plex |
| `media_player.sony_bravia` | Sony Bravia | universal |
| `media_player.sony_kd_55x8500c` | None | braviatv |
| `media_player.spotify_philip_patterson` | Spotify | spotify |
| `media_player.study_speaker` | None | cast |
| `media_player.tv` | None | cast |
| `media_player.tv_2` | None | androidtv_remote |
| `media_player.upstairs` | None | cast |
| `media_player.wiim_amp_1739` | None | cast |
| `media_player.wiim_amp_pro_ebe4` | WiiM Amp Pro-EBE4 | dlna_dmr |

## Remotes

IR blasters and remote controls.

**Total:** 7 (6 enabled, 1 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `remote.henrys_room_ir_blaster_remote` | Henry's Room IR Blaster | broadlink |
| `remote.ir_blaster_master_bedroom_remote` | Masterbed IR Blaster | broadlink |
| `remote.livingroom_irblaster_remote` | None | broadlink |
| `remote.otto_s_room_remote_control_remote` | Otto's Room IR Blaster | broadlink |
| `remote.sony_kd_55x8500c` | None | braviatv |
| `remote.tv` | None | androidtv_remote |

## Cameras

Security cameras.

**Total:** 17 (9 enabled, 8 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `camera.bi_all_cameras` | BI +All cameras | blueiris |
| `camera.bi_all_cameras_cycle` | BI +All cameras cycle | blueiris |
| `camera.bi_driveway` | BI Driveway | blueiris |
| `camera.bi_front_door_camera` | BI Front Door Camera | blueiris |
| `camera.driveway_cam_fluent` | Fluent | reolink |
| `camera.front_door_cam_sub` | Fluent | reolink |
| `camera.security_cameras_all_cameras` | Security-Cameras +All cameras | blueiris |
| `camera.security_cameras_driveway` | Security-Cameras Driveway | blueiris |
| `camera.security_cameras_front_door_camera` | Security-Cameras Front Door Camera | blueiris |

## Alarm Control

Security alarm panels.

**Total:** 1 (1 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `alarm_control_panel.alarmo` | Alarmo | alarmo |

## Other Domains

## Button

**Total:** 103 (86 enabled, 17 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `button.a4c138f1205c_battery_replaced` | Battery replaced | battery_notes |
| `button.aqara_motion_and_light_sensor_p2_battery_replaced` | Battery replaced | battery_notes |
| `button.aqara_motion_and_light_sensor_p2_identify_1` | Identify (1) | matter |
| `button.aqara_motion_and_light_sensor_p2_identify_2` | Identify (2) | matter |
| `button.balcony_door_sensor_magnet_battery_replaced` | Battery replaced | battery_notes |
| `button.balcony_door_sensor_magnet_identify_2` | balcony door sensor magnet Identify | zha |
| `button.computer_plug_identify` | Computer Plug Identify | zha |
| `button.curtain_3_b3bb_battery_replaced` | Battery replaced | battery_notes |
| `button.dinner_table_plug_identify` | Dinner Table Plug Identify | zha |
| `button.dishwasher_smart_plug_refresh` | Refresh | meross_lan |
| `button.dishwasher_smart_plug_reload` | Reload | meross_lan |
| `button.dryer_power_plug_identify` | Dryer Power Plug Identify | zha |
| `button.espresense_livingroom_enroll` | Enroll | mqtt |
| `button.espresense_livingroom_restart` | Restart | mqtt |
| `button.espresense_livingroom_update` | Update | mqtt |
| `button.front_door_button_switch_battery_replaced` | Battery replaced | battery_notes |
| `button.front_door_water_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.front_door_water_sensor_identify` | Front door water sensor Identify | zha |
| `button.genericswitch_identify` | Identify | matter |
| `button.genericswitch_identify_2` | Identify | matter |
| `button.henry_s_door_battery_replaced` | Battery replaced | battery_notes |
| `button.henry_s_door_identify` | Henry's Door Identify | zha |
| `button.henry_s_room_temp_humidity_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.henry_s_room_temp_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.homeassistant_reload` | Reload | spook |
| `button.homeassistant_restart` | Restart | spook |
| `button.hub_2_button_identify` | Identify | matter |
| `button.humiditysensor_identify` | Identify | matter |
| `button.ignore_all_issues` | Ignore all | spook |
| `button.interior_garage_door_sensor_magnet_battery_replaced` | Battery replaced | battery_notes |
| `button.interior_garage_door_sensor_magnet_identify` | interior garage door sensor magnet Identify | zha |
| `button.kitchen_smart_plug_identify` | Kitchen smart plug Identify | zha |
| `button.led_strip_office_identify` | Led Strip Office Identify | zha |
| `button.living_room_door_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.living_room_door_sensor_identify` | Living Room Door Sensor Identify | zha |
| `button.living_room_wiimamp_restart` | Restart | linkplay |
| `button.living_room_wiimamp_sync_time` | Sync time | linkplay |
| `button.lumi_lumi_sensor_magnet_battery_replaced` | Battery replaced | battery_notes |
| `button.lumi_lumi_sensor_magnet_identify` | Identify | zha |
| `button.lumi_lumi_sensor_wleak_aq1_battery_replaced` | Battery replaced | battery_notes |
| `button.lumi_lumi_sensor_wleak_aq1_identify` | Identify | zha |
| `button.master_bed_switch_4_battery_replaced` | Master Bed Switch 4 Battery replaced | battery_notes |
| `button.master_bed_switch_4_identify` | Master Bed Switch 4 Identify | zha |
| `button.master_bedroom_door_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.master_bedroom_door_sensor_identify` | Master Bedroom Door Sensor Identify | zha |
| `button.master_switch_3_battery_replaced` | Battery replaced | battery_notes |
| `button.master_switch_3_identify` | Master Switch 3 Identify | zha |
| `button.masterbed_sink_leak_detector_battery_replaced` | Masterbed Sink Leak Detector Battery replaced | battery_notes |
| `button.masterbed_sink_leak_detector_identify_2` | Masterbed Sink Leak Detector Identify | zha |
| `button.masterbed_switch_1_battery_replaced` | Masterbed Switch 1 Battery replaced | battery_notes |
| `button.masterbed_switch_1_identify` | Masterbed Switch 1 Identify | zha |
| `button.masterbed_switch_2_battery_replaced` | Battery replaced | battery_notes |
| `button.masterbed_switch_2_identify` | Masterbed Switch 2 Identify | zha |
| `button.media_server_scan_clients` | Scan clients | plex |
| `button.motion_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.motion_sensor_identify` | motion sensor Identify | zha |
| `button.otto_room_door_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.otto_room_door_sensor_identify` | otto room door sensor Identify | zha |
| `button.otto_s_room_temp_humidity_sensor_battery_replaced` | Battery replaced | battery_notes |
| `button.samsung_galaxy_s22_ultra_battery_replaced` | Battery replaced | battery_notes |
| `button.server_power_switch_identify` | Server power switch Identify | zha |
| `button.side_garage_door_sensor_magnet_battery_replaced` | Battery replaced | battery_notes |
| `button.side_garage_door_sensor_magnet_identify` | side garage door sensor magnet Identify | zha |
| `button.sink_leak_detection_battery_replaced` | Battery replaced | battery_notes |
| `button.sink_leak_detection_identify` | Sink leak detection Identify | zha |
| `button.slvdh_battery_replaced` | Battery replaced | battery_notes |
| `button.smart_garage_door_refresh` | Refresh | meross_lan |
| `button.smart_garage_door_reload` | Reload | meross_lan |
| `button.sonoff_snzb_05p_identify` | Identify | zha |
| `button.sony_kd_55x8500c_restart` | Restart | braviatv |
| `button.sony_kd_55x8500c_terminate_apps` | Terminate apps | braviatv |
| `button.stephanies_ipad_battery_replaced` | Battery replaced | battery_notes |
| `button.switch_identify` | Front door Button Switch Identify | zha |
| `button.switchbot_hub_2_identify` | Identify | matter |
| `button.tablet_battery_replaced` | Battery replaced | battery_notes |
| `button.temperaturesensor_identify` | Identify | matter |
| `button.unignore_all_issues` | Unignore all | spook |
| `button.washing_machine_power_plug_identify` | Identify | zha |
| `button.water_leak_detection_battery_replaced` | Battery replaced | battery_notes |
| `button.water_leak_detection_identify` | Identify | zha |
| `button.water_leak_detector_battery_replaced` | Battery replaced | battery_notes |
| `button.water_leak_detector_battery_replaced_2` | Battery replaced | battery_notes |
| `button.water_leak_detector_identify` | Water leak detector Identify | zha |
| `button.water_switch_battery_replaced` | Battery replaced | battery_notes |
| `button.water_switch_identify` | Identify | zha |
| `button.windowcovering_identify` | Identify | matter |

## Calendar

**Total:** 14 (13 enabled, 1 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `calendar.birthdays` | Birthdays | google |
| `calendar.early_to_bed` | Early to Bed | local_calendar |
| `calendar.family` | Family | local_calendar |
| `calendar.family_2` | Family | google |
| `calendar.holidays_in_australia` | Holidays in australia | google |
| `calendar.ideal_week` | Ideal week | google |
| `calendar.patterson_babysitting_calendar` | Patterson babysitting calendar | google |
| `calendar.philip_james_patterson_gmail_com` | Philip.james.patterson@gmail.com | google |
| `calendar.slvandenhoff_gmail_com` | Slvandenhoff@gmail.com | google |
| `calendar.stephanie_louise_patterson_gmail_com` | Stephanie.louise.patterson@gmail.com | google |
| `calendar.weather` | Weather | google |
| `calendar.workday_sensor_calendar` | Calendar | workday |
| `calendar.working_from_home` | Working from home | local_calendar |

## Counter

**Total:** 1 (1 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `counter.dishwasher_counter` | Dishwasher Counter | counter |

## Device Tracker

**Total:** 142 (96 enabled, 46 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `device_tracker.240601571_sva` | 240601571-SVA | unifi |
| `device_tracker.aolt002068_2` | AOLT002068 | unifi |
| `device_tracker.aolt002068_3` | AOLT002068 | unifi |
| `device_tracker.bermuda_0c_7e_24_58_96_65_bermuda_tracker` | Bermuda Tracker | bermuda |
| `device_tracker.bermuda_14_13_0b_23_80_9c_bermuda_tracker` | Bermuda Tracker | bermuda |
| `device_tracker.bermuda_14_13_0b_39_e8_a9_bermuda_tracker` | Bermuda Tracker | bermuda |
| `device_tracker.bermuda_14_13_0b_f9_cd_25_bermuda_tracker` | Bermuda Tracker | bermuda |
| `device_tracker.colin_s_s23` | colin-s-S23 | unifi |
| `device_tracker.colin_s_s24` | colin-s-S24 | unifi |
| `device_tracker.computer_switch` | Computer Switch | unifi |
| `device_tracker.driveway` | Driveway | unifi |
| `device_tracker.esp32_27d9d4` | esp32-27D9D4 | unifi |
| `device_tracker.esphome_web_286c10` | masterbedroom | unifi |
| `device_tracker.front` | Front | unifi |
| `device_tracker.galaxy_tab_a` | Galaxy-Tab-A | unifi |
| `device_tracker.galaxy_tab_s2_2` | Galaxy-Tab-S2 | unifi |
| `device_tracker.google_home_mini` | Google-Home-Mini | unifi |
| `device_tracker.google_tv` | Google-TV | unifi |
| `device_tracker.homeassistant` | homeassistant | unifi |
| `device_tracker.huawei_p30_lite_1cf5181c8` | HUAWEI_P30_lite-1cf5181c8 | unifi |
| `device_tracker.ipad` | iPad | unifi |
| `device_tracker.ipad_2` | iPad | unifi |
| `device_tracker.iphone` | iPhone | unifi |
| `device_tracker.iphone_2` | iPhone | unifi |
| `device_tracker.iphone_3` | iPhone | unifi |
| `device_tracker.iphone_4` | iPhone | unifi |
| `device_tracker.iphone_5` | iPhone | unifi |
| `device_tracker.iphone_6` | iPhone | unifi |
| `device_tracker.kobo` | kobo | unifi |
| `device_tracker.liling_s_s23` | Liling-s-S23 | unifi |
| `device_tracker.livingroom` | livingroom | unifi |
| `device_tracker.lounge` | Lounge | unifi |
| `device_tracker.nixos` | DESKTOP-9VIU335 | unifi |
| `device_tracker.phil_s_phone_bermuda_tracker` | Bermuda Tracker | bermuda |
| `device_tracker.phil_t100ta` | phil-T100TA | unifi |
| `device_tracker.phils_phone` | Phils-phone | unifi |
| `device_tracker.phils_phone_2` | None | private_ble_device |
| `device_tracker.phils_phone_bermuda_tracker` | Bermuda Tracker | bermuda |
| `device_tracker.phils_work_pc` | Phils Work PC | unifi |
| `device_tracker.pixel_10_pro` | Pixel-10-Pro | unifi |
| `device_tracker.pixel_7_2` | Pixel-7 | unifi |
| `device_tracker.s14e81868ae650f9fc_203d` | None | ibeacon |
| `device_tracker.s52b8e5d99d047c0ec_56cc` | None | ibeacon |
| `device_tracker.s9d6ec136dd860422c_58f1` | None | ibeacon |
| `device_tracker.sa6e2be45dc723626c_16ea` | None | ibeacon |
| `device_tracker.server` | SERVER | unifi |
| `device_tracker.server_switch` | Server Switch | unifi |
| `device_tracker.sf41225f64c0af8edc_a202` | None | ibeacon |
| `device_tracker.silent_bob` | Silent-Bob | unifi |
| `device_tracker.slvdh` | iPhone | unifi |
| `device_tracker.slvdh_2` | slvdh | mobile_app |
| `device_tracker.sm_s908e` | Samsung Galaxy S22 Ultra | mobile_app |
| `device_tracker.stephanies_ipad` | Stephanie’s iPad | mobile_app |
| `device_tracker.stephen_s_s22` | Stephen-s-S22 | unifi |
| `device_tracker.steve_s_phone` | Steve-s-Phone | unifi |
| `device_tracker.study` | AOLT002068 | unifi |
| `device_tracker.study_2` | STUDY | unifi |
| `device_tracker.study_3` | STUDY | unifi |
| `device_tracker.switchbot_hub_2_f1dbd8` | SwitchBot-Hub-2-F1DBD8 | unifi |
| `device_tracker.tablet` | tablet | mobile_app |
| `device_tracker.ucg_ultra` | UCG Ultra | unifi |
| `device_tracker.unifi_1e_09_78_81_ae_70_default` | media-server | unifi |
| `device_tracker.unifi_default_00_22_6c_33_96_09` | WiiM Amp Pro-EBE4 | unifi |
| `device_tracker.unifi_default_06_cf_aa_f6_fb_17` |  | unifi |
| `device_tracker.unifi_default_0c_7e_24_58_96_67` | garmin-Forerunner965-10dbd6d65e7a | unifi |
| `device_tracker.unifi_default_1a_42_49_ba_86_7d` |  | unifi |
| `device_tracker.unifi_default_1c_f2_9a_0b_34_9e` |  | unifi |
| `device_tracker.unifi_default_2e_0d_2c_65_84_9c` |  | unifi |
| `device_tracker.unifi_default_32_46_d5_26_7a_9c` |  | unifi |
| `device_tracker.unifi_default_62_ea_08_38_e8_c0` |  | unifi |
| `device_tracker.unifi_default_66_82_48_f9_f1_35` |  | unifi |
| `device_tracker.unifi_default_66_e0_82_9e_f2_6a` |  | unifi |
| `device_tracker.unifi_default_66_f4_d0_b5_4d_77` |  | unifi |
| `device_tracker.unifi_default_6a_ef_34_ce_df_f5` |  | unifi |
| `device_tracker.unifi_default_6e_c7_a2_63_2b_95` |  | unifi |
| `device_tracker.unifi_default_76_23_a6_ee_d2_0c` | docker | unifi |
| `device_tracker.unifi_default_84_8c_8d_cb_fd_7b` |  | unifi |
| `device_tracker.unifi_default_8c_8c_aa_9d_77_b5` | DESKTOP-9VIU335 | unifi |
| `device_tracker.unifi_default_8e_1e_20_55_3c_c6` |  | unifi |
| `device_tracker.unifi_default_9a_9d_d5_5e_1a_27` |  | unifi |
| `device_tracker.unifi_default_aa_aa_03_00_00_00` |  | unifi |
| `device_tracker.unifi_default_b6_da_62_bb_de_a2` |  | unifi |
| `device_tracker.unifi_default_b8_7b_d4_f8_8a_31` |  | unifi |
| `device_tracker.unifi_default_c2_67_ad_4a_16_a5` |  | unifi |
| `device_tracker.unifi_default_c2_83_02_21_69_5f` |  | unifi |
| `device_tracker.unifi_default_d6_86_53_34_7f_44` |  | unifi |
| `device_tracker.unifi_default_da_ae_5a_bd_59_b8` |  | unifi |
| `device_tracker.unifi_default_e6_67_54_ab_6e_ab` |  | unifi |
| `device_tracker.unifi_default_ea_1f_cb_a6_f9_53` |  | unifi |
| `device_tracker.upstairs` | Upstairs | unifi |
| `device_tracker.usw_16_poe` | USW 16 PoE | unifi |
| `device_tracker.wilc` | WILC | unifi |
| `device_tracker.win_server` | Win-Server | unifi |
| `device_tracker.wlan0` | wlan0 | unifi |
| `device_tracker.wlan0_2` | wlan0 | unifi |
| `device_tracker.yeelink_light_color2_miap2566` | yeelink-light-color2_miap2566 | unifi |

## Event

**Total:** 4 (4 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `event.backup_automatic_backup` | Automatic backup | backup |
| `event.genericswitch_button` | Button | matter |
| `event.genericswitch_button_2` | Button | matter |
| `event.repair` | None | spook |

## Image

**Total:** 2 (0 enabled, 2 disabled)

## Number

**Total:** 86 (71 enabled, 15 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `number.aqara_motion_and_light_sensor_p2_hold_time` | Hold time | matter |
| `number.bermuda_0c_7e_24_58_96_65_calibration_ref_power_at_1m_0_for_default` | Calibration Ref Power at 1m. 0 for default. | bermuda |
| `number.bermuda_14_13_0b_23_80_9c_calibration_ref_power_at_1m_0_for_default` | Calibration Ref Power at 1m. 0 for default. | bermuda |
| `number.bermuda_14_13_0b_39_e8_a9_calibration_ref_power_at_1m_0_for_default` | Calibration Ref Power at 1m. 0 for default. | bermuda |
| `number.bermuda_14_13_0b_f9_cd_25_calibration_ref_power_at_1m_0_for_default` | Calibration Ref Power at 1m. 0 for default. | bermuda |
| `number.central_configuration_preset_boost_ac_away_temp` | Boost ac away | versatile_thermostat |
| `number.central_configuration_preset_boost_ac_temp` | Boost ac | versatile_thermostat |
| `number.central_configuration_preset_boost_away_temp` | Boost away | versatile_thermostat |
| `number.central_configuration_preset_boost_temp` | Boost | versatile_thermostat |
| `number.central_configuration_preset_comfort_ac_away_temp` | Comfort ac away | versatile_thermostat |
| `number.central_configuration_preset_comfort_ac_temp` | Comfort ac | versatile_thermostat |
| `number.central_configuration_preset_comfort_away_temp` | Comfort away | versatile_thermostat |
| `number.central_configuration_preset_comfort_temp` | Comfort | versatile_thermostat |
| `number.central_configuration_preset_eco_ac_away_temp` | Eco ac away | versatile_thermostat |
| `number.central_configuration_preset_eco_ac_temp` | Eco ac | versatile_thermostat |
| `number.central_configuration_preset_eco_away_temp` | Eco away | versatile_thermostat |
| `number.central_configuration_preset_eco_temp` | Eco | versatile_thermostat |
| `number.central_configuration_preset_frost_away_temp` | Frost away | versatile_thermostat |
| `number.central_configuration_preset_frost_temp` | Frost | versatile_thermostat |
| `number.driveway_cam_motion_sensitivity` | Motion sensitivity | reolink |
| `number.espresense_livingroom_absorption` | Absorption | mqtt |
| `number.espresense_livingroom_max_distance` | Max Distance | mqtt |
| `number.front_door_cam_motion_sensitivity` | Motion sensitivity | reolink |
| `number.henrys_room_preset_boost_ac_away_temp` | Boost ac away | versatile_thermostat |
| `number.henrys_room_preset_boost_ac_temp` | Boost ac | versatile_thermostat |
| `number.henrys_room_preset_boost_away_temp` | Boost away | versatile_thermostat |
| `number.henrys_room_preset_boost_temp` | Boost | versatile_thermostat |
| `number.henrys_room_preset_comfort_ac_away_temp` | Comfort ac away | versatile_thermostat |
| `number.henrys_room_preset_comfort_ac_temp` | Comfort ac | versatile_thermostat |
| `number.henrys_room_preset_comfort_away_temp` | Comfort away | versatile_thermostat |
| `number.henrys_room_preset_comfort_temp` | Comfort | versatile_thermostat |
| `number.henrys_room_preset_eco_ac_away_temp` | Eco ac away | versatile_thermostat |
| `number.henrys_room_preset_eco_ac_temp` | Eco ac | versatile_thermostat |
| `number.henrys_room_preset_eco_away_temp` | Eco away | versatile_thermostat |
| `number.henrys_room_preset_eco_temp` | Eco | versatile_thermostat |
| `number.henrys_room_preset_frost_away_temp` | Frost away | versatile_thermostat |
| `number.henrys_room_preset_frost_temp` | Frost | versatile_thermostat |
| `number.led_strip_office_start_up_color_temperature` | Led Strip Office Start-up color temperature | zha |
| `number.masterbed_ac_preset_boost_ac_away_temp` | Boost ac away | versatile_thermostat |
| `number.masterbed_ac_preset_boost_ac_temp` | Boost ac | versatile_thermostat |
| `number.masterbed_ac_preset_boost_away_temp` | Boost away | versatile_thermostat |
| `number.masterbed_ac_preset_boost_temp` | Boost | versatile_thermostat |
| `number.masterbed_ac_preset_comfort_ac_away_temp` | Comfort ac away | versatile_thermostat |
| `number.masterbed_ac_preset_comfort_ac_temp` | Comfort ac | versatile_thermostat |
| `number.masterbed_ac_preset_comfort_away_temp` | Comfort away | versatile_thermostat |
| `number.masterbed_ac_preset_comfort_temp` | Comfort | versatile_thermostat |
| `number.masterbed_ac_preset_eco_ac_away_temp` | Eco ac away | versatile_thermostat |
| `number.masterbed_ac_preset_eco_ac_temp` | Eco ac | versatile_thermostat |
| `number.masterbed_ac_preset_eco_away_temp` | Eco away | versatile_thermostat |
| `number.masterbed_ac_preset_eco_temp` | Eco | versatile_thermostat |
| `number.masterbed_ac_preset_frost_away_temp` | Frost away | versatile_thermostat |
| `number.masterbed_ac_preset_frost_temp` | Frost | versatile_thermostat |
| `number.motion_sensor_detection_interval` | Detection interval | zha |
| `number.ottos_room_ac_preset_boost_ac_away_temp` | Boost ac away | versatile_thermostat |
| `number.ottos_room_ac_preset_boost_ac_temp` | Boost ac | versatile_thermostat |
| `number.ottos_room_ac_preset_boost_away_temp` | Boost away | versatile_thermostat |
| `number.ottos_room_ac_preset_boost_temp` | Boost | versatile_thermostat |
| `number.ottos_room_ac_preset_comfort_ac_away_temp` | Comfort ac away | versatile_thermostat |
| `number.ottos_room_ac_preset_comfort_ac_temp` | Comfort ac | versatile_thermostat |
| `number.ottos_room_ac_preset_comfort_away_temp` | Comfort away | versatile_thermostat |
| `number.ottos_room_ac_preset_comfort_temp` | Comfort | versatile_thermostat |
| `number.ottos_room_ac_preset_eco_ac_away_temp` | Eco ac away | versatile_thermostat |
| `number.ottos_room_ac_preset_eco_ac_temp` | Eco ac | versatile_thermostat |
| `number.ottos_room_ac_preset_eco_away_temp` | Eco away | versatile_thermostat |
| `number.ottos_room_ac_preset_eco_temp` | Eco | versatile_thermostat |
| `number.ottos_room_ac_preset_frost_away_temp` | Frost away | versatile_thermostat |
| `number.ottos_room_ac_preset_frost_temp` | Frost | versatile_thermostat |
| `number.phil_s_phone_calibration_ref_power_at_1m_0_for_default` | Calibration Ref Power at 1m. 0 for default. | bermuda |
| `number.phils_phone_calibration_ref_power_at_1m_0_for_default` | Calibration Ref Power at 1m. 0 for default. | bermuda |
| `number.smart_garage_door_doorcloseduration_2` | Smart Garage Door doorCloseDuration | meross_lan |
| `number.smart_garage_door_dooropenduration_2` | Smart Garage Door doorOpenDuration | meross_lan |

## Person

**Total:** 6 (5 enabled, 1 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `person.mum_or_dad` | Mum Or Dad | person |
| `person.phil_patterson` | Phil Patterson | person |
| `person.stephanie_patterson` | Stephanie Patterson | person |
| `person.tablet` | Tablet | person |
| `person.wendy` | Wendy | person |

## Schedule

**Total:** 3 (3 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `schedule.awake_hours` | Awake Hours | schedule |
| `schedule.cover_time_open` | Cover time open | schedule |
| `schedule.test` | Test  | schedule |

## Select

**Total:** 42 (31 enabled, 11 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `select.central_mode` | Central Mode | versatile_thermostat |
| `select.computer_desk_light_power_on_behavior` | Power on behavior | tuya |
| `select.computer_plug_backlight_mode` | Computer Plug Backlight mode | zha |
| `select.computer_plug_power_on_state` | Computer Plug Power on state | zha |
| `select.dinner_table_plug_backlight_mode` | Dinner Table Plug Backlight mode | zha |
| `select.dinner_table_plug_power_on_state` | Dinner Table Plug Power on state | zha |
| `select.dinner_table_plug_start_up_behavior` | Dinner Table Plug Start-up behavior | zha |
| `select.driveway_cam_day_night_mode` | Day night mode | reolink |
| `select.dryer_power_plug_backlight_mode` | Dryer Power Plug Backlight mode | zha |
| `select.dryer_power_plug_power_on_state` | Dryer Power Plug Power on state | zha |
| `select.dryer_power_plug_start_up_behavior` | Dryer Power Plug Start-up behavior | zha |
| `select.front_door_cam_day_night_mode` | Day night mode | reolink |
| `select.gosungrow_option_fetchschedule` | GoSungrow Option Fetch Schedule | mqtt |
| `select.gosungrow_option_loglevel` | GoSungrow Option Log Level | mqtt |
| `select.gosungrow_option_mqtt_debug` | GoSungrow Option Mqtt Debug | mqtt |
| `select.gosungrow_option_mqtt_loglevel` | GoSungrow Option Mqtt LogLevel | mqtt |
| `select.gosungrow_option_servicestate` | GoSungrow Option Service State | mqtt |
| `select.gosungrow_option_sleepdelay` | GoSungrow Option Sleep Delay After Schedule | mqtt |
| `select.kitchen_smart_plug_backlight_mode` | Kitchen smart plug Backlight mode | zha |
| `select.kitchen_smart_plug_power_on_state` | Kitchen smart plug Power on state | zha |
| `select.kitchen_smart_plug_start_up_behavior` | Kitchen smart plug Start-up behavior | zha |
| `select.living_room_light_power_on_behavior` | Power on behavior | tuya |
| `select.motion_sensor_motion_sensitivity` | Motion sensitivity | zha |
| `select.outdoor_switch_power_on_behavior` | Power on behavior | tuya |
| `select.server_power_switch_backlight_mode` | Server power switch Backlight mode | zha |
| `select.server_power_switch_power_on_state` | Server power switch Power on state | zha |
| `select.server_power_switch_start_up_behavior` | Server power switch Start-up behavior | zha |
| `select.washing_machine_power_plug_backlight_mode` | Backlight mode | zha |
| `select.washing_machine_power_plug_power_on_state` | Power on state | zha |
| `select.xmas_lights_plug_indicator_light_mode` | Indicator light mode | tuya |
| `select.xmas_lights_plug_power_on_behavior` | Power on behavior | tuya |

## Tag

**Total:** 11 (11 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `tag.downstairs_hall_toilet` | Downstairs hall toilet | tag |
| `tag.fed_fishy` | Fed fishy | tag |
| `tag.kids_toilet` | Kids toilet | tag |
| `tag.kitchen_light_switch` | Kitchen light switch | tag |
| `tag.maintenance_ac_filter` | Maintenance - AC Filter | tag |
| `tag.maintenance_toilet_clean` | Maintenance - Toilet Clean | tag |
| `tag.master_light_switch` | Master light switch | tag |
| `tag.masterbed_desk_left_cnr` | Masterbed desk left cnr | tag |
| `tag.masterbed_desk_mid` | Masterbed desk mid | tag |
| `tag.omas_room_toilet` | Omas room toilet | tag |
| `tag.study_desk` | Study Desk | tag |

## Timer

**Total:** 1 (1 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `timer.roller_blind_timer` | Roller Blind Timer | timer |

## Update

**Total:** 105 (102 enabled, 3 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `update.adaptive_lighting_update` | Adaptive Lighting update | hacs |
| `update.adguard_home_update` | Update | hassio |
| `update.advanced_ssh_web_terminal_update` | Update | hassio |
| `update.alarmo_card_update` | Alarmo Card update | hacs |
| `update.alarmo_update` | Alarmo update | hacs |
| `update.aqara_motion_and_light_sensor_p2_firmware` | Firmware | matter |
| `update.auto_entities_update` | auto-entities update | hacs |
| `update.battery_notes_update` | Battery Notes update | hacs |
| `update.bermuda_ble_trilateration_update` | Bermuda BLE Trilateration update | hacs |
| `update.better_thermostat_ui_update` | Better Thermostat UI update | hacs |
| `update.blueiris_nvr_update` | BlueIris NVR update | hacs |
| `update.browser_mod_update` | browser_mod update | hacs |
| `update.bureau_of_meteorology_update` | Bureau of Meteorology update | hacs |
| `update.button_card_update` | button-card update | hacs |
| `update.card_mod_update` | card-mod update | hacs |
| `update.cloudflared_update` | Update | hassio |
| `update.computer_plug_firmware` | Computer Plug Firmware | zha |
| `update.config_template_card_update` | Config Template Card update | hacs |
| `update.digital_clock_update` | Digital Clock update | hacs |
| `update.dinner_table_plug_firmware` | Dinner Table Plug Firmware | zha |
| `update.driveway_cam_firmware` | Firmware | reolink |
| `update.dryer_power_plug_firmware` | Dryer Power Plug Firmware | zha |
| `update.entryway_power_switch_firmware` | Server power switch Firmware | zha |
| `update.esphome_update` | Update | hassio |
| `update.file_editor_update` | Update | hassio |
| `update.front_door_button_switch_firmware` | Firmware | zha |
| `update.front_door_cam_update` | Firmware | reolink |
| `update.front_door_water_sensor_firmware` | Firmware | zha |
| `update.get_hacs_update` | Update | hassio |
| `update.google_home_update` | Google Home update | hacs |
| `update.gosungrow_update` | Update | hassio |
| `update.grafana_update` | Update | hassio |
| `update.hacs_update` | HACS update | hacs |
| `update.home_assistant_core_update` | Update | hassio |
| `update.home_assistant_google_drive_backup_update` | Update | hassio |
| `update.home_assistant_operating_system_update` | Update | hassio |
| `update.home_assistant_skyconnect_28365b02_firmware` | Firmware | homeassistant_sky_connect |
| `update.home_assistant_supervisor_update` | Update | hassio |
| `update.kitchen_smart_plug_firmware` | Kitchen smart plug Firmware | zha |
| `update.layout_card_update` | layout-card update | hacs |
| `update.led_strip_office_firmware` | Led Strip Office Firmware | zha |
| `update.light_entity_card_update` | Light Entity Card update | hacs |
| `update.local_tuya_update` | Local Tuya update | hacs |
| `update.lounge` | None | unifi |
| `update.lumi_lumi_sensor_magnet_firmware` | Firmware | zha |
| `update.lumi_lumi_sensor_wleak_aq1_firmware` | Firmware | zha |
| `update.master_bed_switch_4_firmware` | Master Bed Switch 4 Firmware | zha |
| `update.master_switch_3_firmware` | Master Switch 3 Firmware | zha |
| `update.masterbed_sink_leak_detector_firmware_2` | Masterbed Sink Leak Detector Firmware | zha |
| `update.masterbed_switch_1_firmware` | Masterbed Switch 1 Firmware | zha |
| `update.masterbed_switch_2_firmware` | Masterbed Switch 2 Firmware | zha |
| `update.matter_server_update` | Update | hassio |
| `update.meross_integration_update` | Meross Integration update | hacs |
| `update.meross_lan_update` | Meross LAN update | hacs |
| `update.mini_graph_card_update` | mini-graph-card update | hacs |
| `update.mini_media_player_update` | Mini Media Player update | hacs |
| `update.mosquitto_broker_update` | Update | hassio |
| `update.motion_sensor_firmware` | Firmware | zha |
| `update.mqtt_explorer_update` | Update | hassio |
| `update.my_cards_bundle_update` | My Cards Bundle update | hacs |
| `update.navbar_card_update` | Navbar card update | hacs |
| `update.nginx_proxy_manager_update` | Update | hassio |
| `update.node_red_companion_update` | Node-RED Companion update | hacs |
| `update.passive_ble_monitor_integration_update` | Passive BLE monitor integration update | hacs |
| `update.plex_media_server_media_server` | Update | plex |
| `update.portainer_update` | Portainer update | hacs |
| `update.presence_simulation_update` | Presence Simulation update | hacs |
| `update.proxmox_ve_update` | Proxmox VE update | hacs |
| `update.samba_share_update` | Update | hassio |
| `update.scheduler_card_update` | Scheduler Card update | hacs |
| `update.scheduler_component_update` | Scheduler component update | hacs |
| `update.simple_weather_card_update` | Simple Weather Card update | hacs |
| `update.simpleicons_update` | simpleicons update | hacs |
| `update.sink_leak_detection_firmware` | Sink leak detection Firmware | zha |
| `update.smartir_update` | SmartIR update | hacs |
| `update.smartlife_update` | smartlife update | hacs |
| `update.smartthinq_lge_sensors_update` | SmartThinQ LGE Sensors update | hacs |
| `update.smoke_alarm_firmware` | Smoke Alarm Firmware | zha |
| `update.sonoff_snzb_05p_firmware` | Firmware | zha |
| `update.spook_your_homie_update` | Spook 👻 Your homie update | hacs |
| `update.state_switch_update` | state-switch update | hacs |
| `update.studio_code_server_update` | Update | hassio |
| `update.study_esp32_firmware` | Firmware | esphome |
| `update.tailscale_update` | Update | hassio |
| `update.template_entity_row_update` | template-entity-row update | hacs |
| `update.thermal_comfort_update` | Thermal Comfort update | hacs |
| `update.ucg_ultra` | None | unifi |
| `update.ui_lovelace_minimalist_update` | UI Lovelace Minimalist update | hacs |
| `update.upcoming_media_card_update` | Upcoming Media Card update | hacs |
| `update.upstairs` | None | unifi |
| `update.usw_16_poe` | None | unifi |
| `update.versatile_thermostat_update` | Versatile Thermostat update | hacs |
| `update.washing_machine_power_plug_firmware` | Firmware | zha |
| `update.water_leak_detection_firmware` | Firmware | zha |
| `update.water_leak_detector_firmware` | Water leak detector Firmware | zha |
| `update.water_switch_firmware` | Firmware | zha |
| `update.waves_update` | Waves update | hacs |
| `update.weather_radar_card_update` | Weather Radar Card update | hacs |
| `update.week_planner_card_update` | Week planner card update | hacs |
| `update.wiim_devices_update` | WiiM devices update | hacs |
| `update.wireguard_update` | Update | hassio |
| `update.xiaomi_miot_auto_update` | Xiaomi Miot update | hacs |

## Weather

**Total:** 3 (3 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `weather.braybrook` | Braybrook | bureau_of_meteorology |
| `weather.braybrook_hourly` | Braybrook Hourly | bureau_of_meteorology |
| `weather.home` | Home | met |

## Zone

**Total:** 1 (1 enabled, 0 disabled)

| Entity ID | Name | Platform |
|-----------|------|----------|
| `zone.work` | Phil's Work | zone |
