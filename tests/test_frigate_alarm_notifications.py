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


def trigger_entities(automation: dict) -> set[str]:
    return {
        trigger["entity_id"]
        for trigger in automation["trigger"]
        if trigger.get("trigger") == "state"
    }


def test_frigate_alarm_alerts_watch_person_and_car_sensors() -> None:
    assert trigger_entities(automation_by_id("front_door_frigate_person_detection")) == {
        "binary_sensor.front_door_person_occupancy",
        "binary_sensor.front_door_car_occupancy",
    }
    assert trigger_entities(automation_by_id("driveway_frigate_person_detection")) == {
        "binary_sensor.driveway_person_occupancy",
        "binary_sensor.driveway_car_occupancy",
    }


def test_frigate_alarm_alerts_are_gated_by_alarmo_armed_state() -> None:
    for automation_id in (
        "front_door_frigate_person_detection",
        "driveway_frigate_person_detection",
    ):
        conditions = automation_by_id(automation_id)["condition"]

        assert conditions == [
            {
                "condition": "state",
                "entity_id": "alarm_control_panel.alarmo",
                "state": sorted(ARMED_ALARMO_STATES),
            }
        ]
