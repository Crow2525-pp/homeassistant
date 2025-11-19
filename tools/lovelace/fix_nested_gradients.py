#!/usr/bin/env python3
"""
Fix nested gradients created by incorrect replacements.
Changes: linear-gradient(145deg, linear-gradient(...) 0%, linear-gradient(...) 100%)
To: linear-gradient(...)
"""

import re
from pathlib import Path

def fix_nested_gradient(match):
    """Extract the inner gradient from a nested pattern."""
    full_match = match.group(0)
    # Extract the inner gradient (first occurrence)
    inner_gradient_match = re.search(r'(linear-gradient\([^)]+\))', full_match)
    if inner_gradient_match:
        return inner_gradient_match.group(1)
    return full_match

def fix_file(file_path: Path) -> int:
    """Fix nested gradients in a single file. Returns number of fixes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match nested gradients
    nested_pattern = r'linear-gradient\(145deg,\s*linear-gradient\([^)]+\)\s*0%,\s*linear-gradient\([^)]+\)\s*100%\)'

    # Find and fix nested gradients
    fixes = len(re.findall(nested_pattern, content))
    if fixes > 0:
        content = re.sub(nested_pattern, fix_nested_gradient, content)
        print(f"  {file_path.name}: Fixed {fixes} nested gradients")

    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return fixes

def main():
    lovelace_path = Path('./lovelace')

    # Find all YAML files
    yaml_files = list(lovelace_path.rglob('*.yaml'))

    print(f"Checking {len(yaml_files)} files for nested gradients...\n")

    total_fixes = 0
    files_fixed = 0

    for yaml_file in sorted(yaml_files):
        fixes = fix_file(yaml_file)
        if fixes > 0:
            files_fixed += 1
            total_fixes += fixes

    print(f"\n{'='*60}")
    print(f"SUMMARY:")
    print(f"Files fixed: {files_fixed}")
    print(f"Total nested gradients fixed: {total_fixes}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
