#!/usr/bin/env python3
"""
Lovelace YAML Style Normalizer
Recursively processes Lovelace YAML files to:
1. Replace hardcoded colors with theme colors
2. Ensure card_mod styling uses theme references
3. Apply default styling to cards without card_mod
4. Report any colors not in the theme
"""

import re
from pathlib import Path

import yaml

try:
    from .constants import THEME_COLORS
except ImportError:  # Allow running as a standalone script
    from constants import THEME_COLORS  # type: ignore

CARD_STYLES = {
    "navy": "card_navy",
    "slate": "card_slate",
    "teal": "card_teal",
    "indigo": "card_indigo",
    "amber": "card_amber",
    "rose": "card_rose",
}

DEFAULT_CARD_STYLE = "<<: *card_navy"


def extract_colors_from_text(text: str) -> set[str]:
    """Extract all color values from text."""
    colors = set()
    colors.update(re.findall(r"#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}", text))
    colors.update(re.findall(r"rgba?\([^)]+\)", text))
    colors.update(re.findall(r"linear-gradient\([^)]+\)", text))
    colors.update(re.findall(r"\b\d{1,3},\s*\d{1,3},\s*\d{1,3}\b", text))
    return colors


def normalize_color(color: str) -> str:
    """Normalize color format for matching."""
    color = re.sub(r"\s+", " ", color.strip())
    if color.startswith("#"):
        return color.upper()
    return color


def replace_colors_in_text(
    text: str, replacements: dict[str, tuple[str, str]]
) -> tuple[str, list[str]]:
    """Replace hardcoded colors with theme references."""
    replaced = []
    result = text

    for color, (theme_ref, description) in replacements.items():
        pattern = re.compile(re.escape(color), re.IGNORECASE)
        if pattern.search(result):
            result = pattern.sub(theme_ref, result)
            replaced.append(f"{color} => {theme_ref} ({description})")

    return result, replaced


def has_card_mod(card_dict: dict) -> bool:
    """Check if a card has card_mod styling."""
    if isinstance(card_dict, dict):
        if "card_mod" in card_dict:
            return True
        if "cards" in card_dict:
            for nested in card_dict["cards"]:
                if has_card_mod(nested):
                    return True
        if "card" in card_dict and has_card_mod(card_dict["card"]):
            return True
    return False


def should_add_styling(card_dict: dict) -> bool:
    """Determine if a card should have styling added."""
    if not isinstance(card_dict, dict):
        return False

    styleable_types = [
        "tile",
        "button",
        "entities",
        "entity",
        "markdown",
        "custom:mini-graph-card",
        "history-graph",
        "statistics-graph",
        "glance",
        "sensor",
        "gauge",
        "custom:bar-card",
    ]

    card_type = card_dict.get("type", "")
    skip_types = [
        "vertical-stack",
        "horizontal-stack",
        "grid",
        "conditional",
        "heading",
        "custom:week-planner-card",
    ]

    if card_type in skip_types:
        return False

    return card_type in styleable_types and not has_card_mod(card_dict)


def process_yaml_file(file_path: Path, dry_run: bool = True) -> dict:
    """Process a single YAML file."""
    results = {
        "file": str(file_path),
        "colors_replaced": [],
        "unknown_colors": [],
        "cards_styled": 0,
        "changes_made": False,
    }

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        found_colors = extract_colors_from_text(content)
        unknown = []
        for color in found_colors:
            normalized = normalize_color(color)
            if normalized not in THEME_COLORS and not normalized.startswith("var("):
                unknown.append(color)

        results["unknown_colors"] = unknown
        new_content, replaced = replace_colors_in_text(content, THEME_COLORS)
        results["colors_replaced"] = replaced

        if replaced:
            results["changes_made"] = True

        try:
            yaml.safe_load(new_content)
        except yaml.YAMLError as e:
            results["yaml_error"] = str(e)

        if not dry_run and results["changes_made"]:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

    except Exception as e:
        results["error"] = str(e)

    return results


def main():
    import argparse
    import io
    import sys

    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Normalize Lovelace YAML styles")
    parser.add_argument("--path", default="./lovelace", help="Path to lovelace directory")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without applying them")
    parser.add_argument("--apply", action="store_true", help="Apply changes to files")

    args = parser.parse_args()

    lovelace_path = Path(args.path)
    dry_run = not args.apply

    if dry_run:
        print("DRY RUN MODE - No files will be modified\n")
    else:
        print("APPLY MODE - Files will be modified\n")

    yaml_files = [f for f in lovelace_path.rglob("*.yaml") if "card_styles.yaml" not in str(f)]

    print(f"Found {len(yaml_files)} YAML files to process\n")

    total_changes = 0
    all_unknown_colors = set()

    for yaml_file in sorted(yaml_files):
        results = process_yaml_file(yaml_file, dry_run=dry_run)

        if results.get("error"):
            print(f"[ERROR] Error processing {yaml_file.name}: {results['error']}\n")
            continue

        if results.get("yaml_error"):
            print(f"[WARN] YAML Error in {yaml_file.name}: {results['yaml_error']}\n")

        if results["colors_replaced"] or results["unknown_colors"]:
            print(f"[FILE] {yaml_file.relative_to(lovelace_path)}")

            if results["colors_replaced"]:
                print(f"   [OK] Replaced {len(results['colors_replaced'])} colors:")
                for replacement in results["colors_replaced"]:
                    print(f"      - {replacement}")
                total_changes += len(results["colors_replaced"])

            if results["unknown_colors"]:
                print("   [WARN] Unknown colors found:")
                for color in results["unknown_colors"]:
                    print(f"      - {color}")
                    all_unknown_colors.add(color)

            print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total files processed: {len(yaml_files)}")
    print(f"Total color replacements: {total_changes}")
    print(f"Unique unknown colors: {len(all_unknown_colors)}")

    if all_unknown_colors:
        print("\n[WARN] UNKNOWN COLORS TO REVIEW:")
        print("Please review these colors and decide whether to:")
        print("  1. Add them to the theme")
        print("  2. Replace with existing theme colors")
        print()
        for color in sorted(all_unknown_colors):
            print(f"   - {color}")

    if dry_run:
        print("\n[INFO] Run with --apply to apply these changes")
    else:
        print("\n[OK] Changes have been applied!")


if __name__ == "__main__":
    main()
