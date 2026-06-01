from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
OCCUPANCY_AUTOMATIONS = REPO_ROOT / "automations" / "01_occupancy.yaml"


def load_occupancy_automations() -> list[dict]:
    return yaml.safe_load(OCCUPANCY_AUTOMATIONS.read_text(encoding="utf-8"))


def automation_by_id(automation_id: str) -> dict:
    automations = load_occupancy_automations()
    return next(item for item in automations if item["id"] == automation_id)


def test_set_occupancy_to_away_uses_short_leave_debounce() -> None:
    automation = automation_by_id("1681337163617")

    zone_home_trigger = next(
        trigger
        for trigger in automation["trigger"]
        if trigger.get("entity_id") == ["zone.home"] and trigger.get("to") == "0"
    )

    assert zone_home_trigger["for"] == {
        "hours": 0,
        "minutes": 2,
        "seconds": 0,
    }
    assert "2 minutes" in automation["description"]
    assert "10 minutes" not in automation["description"]
