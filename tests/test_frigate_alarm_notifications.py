from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
MOTION_AUTOMATIONS = REPO_ROOT / "automations" / "13_motion_detection.yaml"
ARMED_ALARMO_STATES = {
    "armed_away",
    "armed_home",
    "armed_night",
    "armed_vacation",
    "armed_custom_bypass",
}


def load_motion_automations() -> list[dict]:
    return yaml.safe_load(MOTION_AUTOMATIONS.read_text(encoding="utf-8"))


def automation_by_id(automation_id: str) -> dict:
    automations = load_motion_automations()
    return next(item for item in automations if item["id"] == automation_id)


def automation_ids() -> set[str]:
    return {automation["id"] for automation in load_motion_automations()}


def trigger_entities(automation: dict) -> set[str]:
    return {
        trigger["entity_id"]
        for trigger in automation["trigger"]
        if trigger.get("trigger") == "state"
    }


def test_frigate_alarm_alerts_only_watch_front_door_person_and_car_sensors() -> None:
    automation = automation_by_id("front_door_frigate_person_detection")

    assert trigger_entities(automation) == {
        "binary_sensor.front_door_person_occupancy",
        "binary_sensor.front_door_car_occupancy",
    }
    assert "driveway_frigate_person_detection" not in automation_ids()


def test_front_door_frigate_alarm_alert_is_gated_by_alarmo_armed_state() -> None:
    conditions = automation_by_id("front_door_frigate_person_detection")["condition"]

    assert conditions == [
        {
            "condition": "state",
            "entity_id": "alarm_control_panel.alarmo",
            "state": sorted(ARMED_ALARMO_STATES),
        }
    ]


def test_front_door_frigate_alarm_alert_uses_critical_family_notification() -> None:
    actions = automation_by_id("front_door_frigate_person_detection")["action"]
    notification = next(action for action in actions if action.get("action") == "notify.std_critical")

    assert notification["data"]["title"] == "Front Door {{ detected_object | title }} Detected"
    assert notification["data"]["message"] == (
        "Frigate detected a {{ detected_object }} at the front door while Alarmo is armed."
    )
    assert notification["data"]["data"] == {
        "image": "/api/camera_proxy/camera.front_door",
        "clickAction": "/lovelace/security",
        "tag": "frigate_front_door_{{ detected_object }}",
        "ttl": 0,
        "priority": "high",
    }


def test_front_door_frigate_alarm_alert_maps_car_trigger_to_car_label() -> None:
    actions = automation_by_id("front_door_frigate_person_detection")["action"]
    variables = next(action for action in actions if "variables" in action)

    assert variables["variables"]["detected_object"] == (
        "{{ 'car' if trigger.entity_id == 'binary_sensor.front_door_car_occupancy' else 'person' }}"
    )


def test_front_door_frigate_alarm_alert_has_duplicate_cooldown() -> None:
    automation = automation_by_id("front_door_frigate_person_detection")

    assert {"delay": {"minutes": 15}} in automation["action"]
    assert automation["mode"] == "single"
    assert automation["max_exceeded"] == "silent"
