#!/usr/bin/env python3
"""
Home Assistant Entity Reference Validator

This script validates that all entity references in YAML files actually exist
in the Home Assistant entity registry.

Usage:
    python validate_entities.py [--verbose] [--report FILE]

Exit codes:
    0 - All entities valid
    1 - One or more entity references not found
    2 - Configuration error
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

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
        references = []

        # Pattern for entity references in YAML
        # Matches: entity_id: light.lounge, target: { entity_id: switch.kitchen }, etc.
        patterns = [
            r"entity_id:\s*([a-z_]+\.[a-z0-9_]+)",  # entity_id: domain.name
            r"entity_id:\s*-\s*([a-z_]+\.[a-z0-9_]+)",  # entity_id: \n  - domain.name
            r"entity_id:\s*\[\s*([a-z_,\s.0-9_]+)\s*\]",  # entity_id: [domain.name, ...]
            r"target:\s*\{?\s*entity_id:\s*([a-z_]+\.[a-z0-9_]+)",  # target: { entity_id: ...
            r"service_entity_id:\s*([a-z_]+\.[a-z0-9_]+)",  # service_entity_id: domain.name
        ]

        lines = content.split("\n")
        for line_num, line in enumerate(lines, 1):
            for pattern in patterns:
                matches = re.finditer(pattern, line, re.IGNORECASE)
                for match in matches:
                    entity_str = match.group(1)
                    # Handle comma-separated lists
                    for entity_id in entity_str.split(","):
                        entity_id = entity_id.strip()
                        if entity_id and "." in entity_id:
                            references.append((entity_id.lower(), line_num))

        return references

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

    def validate_directory(self, directory: str = ".", patterns: List[str] = None) -> None:
        """Recursively validate all YAML files in directory."""
        if patterns is None:
            patterns = ["automations/**/*.yaml", "config/**/*.yaml", "lovelace/**/*.yaml"]

        dir_path = self.ha_config_dir / directory
        yaml_files = []

        for pattern in patterns:
            yaml_files.extend(self.ha_config_dir.glob(pattern))

        if not yaml_files:
            print("⚠️  No YAML files found")
            return

        print(f"📄 Checking {len(yaml_files)} YAML files...")
        for file_path in sorted(yaml_files):
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
            self._save_report(output_file)
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

    args = parser.parse_args()

    # Validate paths exist
    config_path = Path(args.config_dir)
    if not config_path.exists():
        print(f"❌ Config directory not found: {args.config_dir}")
        sys.exit(2)

    # Run validation
    validator = EntityValidator(args.config_dir)
    validator.validate_directory()
    exit_code = validator.report(verbose=args.verbose, output_file=args.report)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
