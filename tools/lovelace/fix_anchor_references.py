#!/usr/bin/env python3
"""
Fix YAML anchor references that don't work across files.
Replaces anchor references with actual color values.
"""

import re
from pathlib import Path

try:
    from .constants import ANCHOR_TO_VALUE
except ImportError:  # Allow running as a standalone script
    from constants import ANCHOR_TO_VALUE  # type: ignore

def fix_file(file_path: Path) -> int:
    """Fix anchor references in a single file. Returns number of replacements."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    replacements = 0

    # Replace each anchor reference with its value
    for anchor, value in ANCHOR_TO_VALUE.items():
        # Count occurrences
        count = content.count(anchor)
        if count > 0:
            # Replace the anchor
            content = content.replace(anchor, value)
            replacements += count
            print(f"  {file_path.name}: Replaced {anchor} ({count} times)")

    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return replacements

def main():
    lovelace_path = Path('./lovelace')

    # Find all YAML files except card_styles.yaml
    yaml_files = [f for f in lovelace_path.rglob('*.yaml') if 'card_styles.yaml' not in str(f)]

    print(f"Fixing anchor references in {len(yaml_files)} files...\n")

    total_replacements = 0
    files_modified = 0

    for yaml_file in sorted(yaml_files):
        replacements = fix_file(yaml_file)
        if replacements > 0:
            files_modified += 1
            total_replacements += replacements

    print(f"\n{'='*60}")
    print(f"SUMMARY:")
    print(f"Files modified: {files_modified}")
    print(f"Total replacements: {total_replacements}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
