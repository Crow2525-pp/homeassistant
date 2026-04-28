import json
from pathlib import Path

from tools.validate_entities import EntityValidator


def write_registry(tmp_path: Path, *entity_ids: str) -> None:
    storage = tmp_path / ".storage"
    storage.mkdir()
    registry = {
        "entities": [{"entity_id": entity_id} for entity_id in entity_ids],
    }
    (storage / "core.entity_registry").write_text(json.dumps(registry), encoding="utf-8")


def test_validate_directory_uses_default_scope_only(tmp_path: Path) -> None:
    write_registry(tmp_path, "light.kitchen")
    (tmp_path / "automations").mkdir()
    (tmp_path / "ui_lovelace_minimalist" / "dashboard").mkdir(parents=True)
    (tmp_path / "lovelace").mkdir()
    (tmp_path / "automations" / "lights.yaml").write_text(
        "entity_id: light.kitchen\n", encoding="utf-8"
    )
    (tmp_path / "lovelace" / "legacy.yaml").write_text(
        "entity_id: light.kitchen\n", encoding="utf-8"
    )
    (tmp_path / "ui_lovelace_minimalist" / "dashboard" / "ui-lovelace.yaml").write_text(
        "entity_id: light.kitchen\n", encoding="utf-8"
    )

    validator = EntityValidator(str(tmp_path))
    validator.validate_directory()

    assert validator.valid_refs == 2
    assert validator.errors == []


def test_extracts_multiline_entity_id_lists(tmp_path: Path) -> None:
    write_registry(tmp_path, "light.kitchen", "light.hallway")
    (tmp_path / "automations").mkdir()
    (tmp_path / "automations" / "lights.yaml").write_text(
        "target:\n"
        "  entity_id:\n"
        "    - light.kitchen\n"
        "    - light.hallway\n",
        encoding="utf-8",
    )

    validator = EntityValidator(str(tmp_path))
    validator.validate_directory()

    assert validator.valid_refs == 2
    assert validator.errors == []


def test_validate_directory_can_target_specific_file(tmp_path: Path) -> None:
    write_registry(tmp_path, "light.kitchen")
    (tmp_path / "automations").mkdir()
    (tmp_path / "config").mkdir()
    (tmp_path / "automations" / "lights.yaml").write_text(
        "entity_id: light.kitchen\n", encoding="utf-8"
    )
    (tmp_path / "config" / "bad.yaml").write_text(
        "entity_id: switch.missing\n", encoding="utf-8"
    )

    validator = EntityValidator(str(tmp_path))
    validator.validate_directory(targets=["automations/lights.yaml"])

    assert validator.valid_refs == 1
    assert validator.errors == []


def test_validate_directory_warns_for_missing_or_non_yaml_targets(tmp_path: Path) -> None:
    write_registry(tmp_path, "light.kitchen")
    (tmp_path / "automations").mkdir()
    (tmp_path / "automations" / "lights.yaml").write_text(
        "entity_id: light.kitchen\n", encoding="utf-8"
    )
    (tmp_path / "README.md").write_text("not yaml\n", encoding="utf-8")

    validator = EntityValidator(str(tmp_path))
    validator.validate_directory(targets=["README.md", "missing.yaml", "automations"])

    assert validator.valid_refs == 1
    assert validator.errors == []
    assert "README.md: Skipping non-YAML file" in validator.warnings
    assert "missing.yaml: Path not found" in validator.warnings


def test_save_report_creates_output_when_validation_passes(tmp_path: Path) -> None:
    write_registry(tmp_path, "light.kitchen")
    (tmp_path / "automations").mkdir()
    (tmp_path / "automations" / "lights.yaml").write_text(
        "entity_id: light.kitchen\n", encoding="utf-8"
    )
    report_path = tmp_path / "entity-validation-report.md"

    validator = EntityValidator(str(tmp_path))
    validator.validate_directory()
    exit_code = validator.report(output_file=str(report_path))

    assert exit_code == 0
    assert report_path.exists()
    contents = report_path.read_text(encoding="utf-8")
    assert "**Valid references:** 1" in contents
    assert "**Invalid references:** 0" in contents


def test_ignores_templated_entity_ids_but_keeps_static_references(tmp_path: Path) -> None:
    write_registry(tmp_path, "input_boolean.kitchen_override", "timer.kitchen_override")
    (tmp_path / "automations").mkdir()
    (tmp_path / "automations" / "templated.yaml").write_text(
        "trigger:\n"
        "  - trigger: state\n"
        "    entity_id: input_boolean.kitchen_override\n"
        "action:\n"
        "  - action: timer.start\n"
        "    target:\n"
        "      entity_id: \"{{ timer_map[trigger.entity_id] }}\"\n",
        encoding="utf-8",
    )

    validator = EntityValidator(str(tmp_path))
    validator.validate_directory()

    assert validator.valid_refs == 1
    assert validator.errors == []
