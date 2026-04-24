#!/usr/bin/env python3
"""
Home Assistant Entity Reference Validator

This script validates that all entity references in YAML files actually exist
in the Home Assistant entity registry.

Usage:
    python validate_entities.py [--verbose] [--report FILE] [targets ...]

Exit codes:
    0 - All entities valid
    1 - One or more entity references not found
    2 - Configuration error
"""

import json
import re
import sys
from pathlib import Path
from typing import Iterable, List, Set, Tuple

import yaml


DEFAULT_PATTERNS = [
    "automations/**/*.yaml",
    "automations/**/*.yml",
    "config/**/*.yaml",
    "config/**/*.yml",
]

YAML_SUFFIXES = {".yaml", ".yml"}
TEMPLATE_MARKERS = ("{{", "{%", "{#")

# Set UTF-8 encoding for Windows compatibility
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class EntityValidator:
    """Validates entity references in Home Assistant YAML files."""

    def __init__(self, ha_config_dir: str = "."):
        self.ha_config_dir = Path(ha_config_dir)
        self.entity_registry = self._load_entity_registry()
        self.errors = []
        self.warnings = []
        self.valid_refs = 0

    def _load_entity_registry(self) -> Set[str]:
        """Load all valid entity IDs from Home Assistant entity registry."""
        registry_path = self.ha_config_dir / ".storage" / "core.entity_registry"

        valid_entities = set()

        if not registry_path.exists():
            print(f"⚠️  Entity registry not found at {registry_path}")
            print("   Will validate entity ID format only")
            return valid_entities

        try:
            with open(registry_path, "r") as f:
                data = json.load(f)

            # Extract all entity IDs from the registry
            for entity in data.get("entities", []):
                entity_id = entity.get("entity_id")
                if entity_id:
                    valid_entities.add(entity_id)

            print(f"✅ Loaded {len(valid_entities)} valid entities from registry")
            return valid_entities

        except Exception as e:
            print(f"⚠️  Failed to load entity registry: {e}")
            return valid_entities

    def _extract_entity_references(self, content: str, file_path: str) -> List[Tuple[str, int]]:
        """Extract all entity ID references from YAML content.

        Returns list of (entity_id, line_number) tuples.
        """
        references: List[Tuple[str, int]] = []
        lines = content.split("\n")

        # Fast path for common single-line cases
        patterns = [
            r"entity_id:\s*([a-z_]+\.[a-z0-9_]+)",
            r"entity_id:\s*-\s*([a-z_]+\.[a-z0-9_]+)",
            r"entity_id:\s*\[\s*([a-z_,\s.0-9_]+)\s*\]",
            r"target:\s*\{?\s*entity_id:\s*([a-z_]+\.[a-z0-9_]+)",
            r"service_entity_id:\s*([a-z_]+\.[a-z0-9_]+)",
        ]

        for line_num, line in enumerate(lines, 1):
            for pattern in patterns:
                for match in re.finditer(pattern, line, re.IGNORECASE):
                    entity_str = match.group(1)
                    for entity_id in entity_str.split(","):
                        entity_id = entity_id.strip()
                        if entity_id and "." in entity_id:
                            references.append((entity_id.lower(), line_num))

        seen = {(entity_id, line_num) for entity_id, line_num in references}

        def add_reference(value: str, line_number: int) -> None:
            if self._is_dynamic_entity_reference(value):
                return

            entity_id = value.strip().lower()
            key = (entity_id, line_number)
            if "." in entity_id and key not in seen:
                seen.add(key)
                references.append(key)

        def walk(node: object) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    if key in {"entity_id", "service_entity_id", "entity"}:
                        line_number = getattr(value, "_yaml_line", 1)
                        if isinstance(value, str):
                            for entity_id in value.split(","):
                                add_reference(entity_id, line_number)
                        elif isinstance(value, list):
                            for item in value:
                                if isinstance(item, str):
                                    add_reference(item, getattr(item, "_yaml_line", line_number))
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        class LineLoader(yaml.SafeLoader):
            pass

        def construct_str(loader: LineLoader, node: yaml.nodes.ScalarNode):
            value = yaml.SafeLoader.construct_scalar(loader, node)
            wrapped = type("LineTrackedStr", (str,), {})(value)
            wrapped._yaml_line = node.start_mark.line + 1
            return wrapped

        LineLoader.add_constructor("tag:yaml.org,2002:str", construct_str)

        try:
            parsed = yaml.load(content, Loader=LineLoader)
        except yaml.YAMLError:
            return references

        walk(parsed)
        return references

    def _is_dynamic_entity_reference(self, entity_id: str) -> bool:
        """Return True for template-driven entity references that cannot be statically validated."""
        stripped = entity_id.strip()
        return any(marker in stripped for marker in TEMPLATE_MARKERS)

    def _is_valid_entity_id_format(self, entity_id: str) -> bool:
        """Check if entity ID follows valid format."""
        # Must be domain.name with lowercase letters, numbers, underscores
        return bool(re.match(r"^[a-z_][a-z0-9_]*\.[a-z_][a-z0-9_]*$", entity_id))

    def validate_file(self, file_path: Path) -> None:
        """Validate all entity references in a YAML file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            self.warnings.append(f"{file_path}: Could not read file: {e}")
            return

        references = self._extract_entity_references(content, str(file_path))

        for entity_id, line_num in references:
            # Check format first
            if not self._is_valid_entity_id_format(entity_id):
                self.errors.append({
                    "file": str(file_path),
                    "line": line_num,
                    "entity": entity_id,
                    "reason": "Invalid entity ID format (must be domain.name)"
                })
                continue

            # Check if entity exists (if registry available)
            if self.entity_registry:
                if entity_id not in self.entity_registry:
                    self.errors.append({
                        "file": str(file_path),
                        "line": line_num,
                        "entity": entity_id,
                        "reason": "Entity not found in registry"
                    })
                else:
                    self.valid_refs += 1
            else:
                # No registry - just count valid format entities
                self.valid_refs += 1

    def _iter_yaml_files(self, targets: List[str] = None, patterns: List[str] = None) -> Iterable[Path]:
        """Yield YAML files selected via explicit targets or default glob patterns."""
        yaml_files = set()

        if targets:
            for target in targets:
                target_path = Path(target)
                if not target_path.is_absolute():
                    target_path = self.ha_config_dir / target_path

                if not target_path.exists():
                    self.warnings.append(f"{target}: Path not found")
                    continue

                if target_path.is_dir():
                    yaml_files.update(
                        file_path
                        for suffix in sorted(YAML_SUFFIXES)
                        for file_path in target_path.rglob(f"*{suffix}")
                        if file_path.is_file()
                    )
                    continue

                if target_path.suffix.lower() in YAML_SUFFIXES:
                    yaml_files.add(target_path)
                else:
                    self.warnings.append(f"{target}: Skipping non-YAML file")
        else:
            if patterns is None:
                patterns = DEFAULT_PATTERNS

            for pattern in patterns:
                yaml_files.update(
                    file_path
                    for file_path in self.ha_config_dir.glob(pattern)
                    if file_path.is_file()
                )

        return sorted(yaml_files)

    def validate_directory(self, directory: str = ".", patterns: List[str] = None, targets: List[str] = None) -> None:
        """Validate YAML files selected by targets or default repository patterns."""
        yaml_files = self._iter_yaml_files(targets=targets, patterns=patterns)

        if not yaml_files:
            print("⚠️  No YAML files found")
            return

        print(f"📄 Checking {len(yaml_files)} YAML files...")
        for file_path in yaml_files:
            self.validate_file(file_path)

    def report(self, verbose: bool = False, output_file: str = None) -> int:
        """Print validation report and return exit code."""
        print("\n" + "="*70)
        print("ENTITY REFERENCE VALIDATION REPORT")
        print("="*70)

        # Summary
        print(f"\n📊 Summary:")
        print(f"   Valid entity references: {self.valid_refs}")
        print(f"   Invalid references found: {len(self.errors)}")
        print(f"   Warnings: {len(self.warnings)}")

        # Errors
        if self.errors:
            print(f"\n❌ Errors ({len(self.errors)}):")
            for error in sorted(self.errors, key=lambda x: (x["file"], x["line"])):
                print(f"\n   File: {error['file']}")
                print(f"   Line: {error['line']}")
                print(f"   Entity: {error['entity']}")
                print(f"   Reason: {error['reason']}")

        # Warnings
        if self.warnings:
            print(f"\n⚠️  Warnings ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"   {warning}")

        # Status
        print("\n" + "-"*70)
        if self.errors:
            print("❌ VALIDATION FAILED")
            exit_code = 1
        else:
            print("✅ VALIDATION PASSED")
            exit_code = 0

        # Save report to file if requested
        if output_file:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            self._save_report(str(output_path))
            print(f"📄 Report saved to: {output_file}")

        print("="*70 + "\n")
        return exit_code

    def _save_report(self, output_file: str) -> None:
        """Save detailed report to file."""
        with open(output_file, "w") as f:
            f.write("# Entity Reference Validation Report\n\n")
            f.write(f"**Valid references:** {self.valid_refs}\n")
            f.write(f"**Invalid references:** {len(self.errors)}\n")
            f.write(f"**Warnings:** {len(self.warnings)}\n\n")

            if self.errors:
                f.write("## Invalid Entity References\n\n")
                for error in sorted(self.errors, key=lambda x: (x["file"], x["line"])):
                    f.write(f"### {error['file']}:{error['line']}\n")
                    f.write(f"- **Entity:** `{error['entity']}`\n")
                    f.write(f"- **Reason:** {error['reason']}\n\n")

            if self.warnings:
                f.write("## Warnings\n\n")
                for warning in self.warnings:
                    f.write(f"- {warning}\n")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate Home Assistant entity references in YAML files"
    )
    parser.add_argument(
        "--config-dir",
        default=".",
        help="Path to Home Assistant config directory (default: current dir)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print verbose output"
    )
    parser.add_argument(
        "--report",
        help="Save detailed report to this file"
    )
    parser.add_argument(
        "targets",
        nargs="*",
        help=(
            "Optional YAML files or directories to validate relative to --config-dir. "
            "If omitted, validate the default automations/ and config/ scope."
        )
    )

    args = parser.parse_args()

    # Validate paths exist
    config_path = Path(args.config_dir)
    if not config_path.exists():
        print(f"❌ Config directory not found: {args.config_dir}")
        sys.exit(2)

    # Run validation
    validator = EntityValidator(args.config_dir)
    validator.validate_directory(targets=args.targets)
    exit_code = validator.report(verbose=args.verbose, output_file=args.report)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
