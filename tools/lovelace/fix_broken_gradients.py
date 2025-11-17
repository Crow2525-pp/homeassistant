#!/usr/bin/env python3
"""
Fix broken gradient syntax from incorrect replacements.
"""

import re
from pathlib import Path

def fix_file(file_path: Path) -> int:
    """Fix broken gradients in a single file. Returns number of fixes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixes = 0

    # Pattern 1: background: linear-gradient(145deg, linear-gradient(145deg, #HEX 0%, #HEX 100%);
    # Should be: background: linear-gradient(145deg, #HEX 0%, #HEX 100%);
    pattern1 = r'background:\s*linear-gradient\(145deg,\s*linear-gradient\(145deg,\s*(#[0-9A-Fa-f]{6})\s*0%,\s*(#[0-9A-Fa-f]{6})\s*100%\);'
    matches1 = re.findall(pattern1, content)
    if matches1:
        fixes += len(matches1)
        content = re.sub(pattern1, r'background: linear-gradient(145deg, \1 0%, \2 100%);', content)

    #Pattern 2: background-color: linear-gradient(...)
    pattern2 = r'background-color:\s*(linear-gradient\([^;]+\));'
    matches2 = re.findall(pattern2, content)
    if matches2:
        fixes += len(matches2)
        content = re.sub(pattern2, r'background: \1;', content)

    if fixes > 0:
        print(f"  {file_path.name}: Fixed {fixes} broken gradients")

    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return fixes

def main():
    lovelace_path = Path('./lovelace')

    # Find all YAML files
    yaml_files = list(lovelace_path.rglob('*.yaml'))

    print(f"Fixing broken gradients in {len(yaml_files)} files...\n")

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
    print(f"Total broken gradients fixed: {total_fixes}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
