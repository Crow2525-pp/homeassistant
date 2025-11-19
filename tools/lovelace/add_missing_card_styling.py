#!/usr/bin/env python3
"""
Add card_mod styling to cards that don't have any.
Applies the modern Navy gradient style as default.
"""

import re
from pathlib import Path

try:
    from .constants import DEFAULT_CARD_MOD
except ImportError:  # Allow running as a standalone script
    from constants import DEFAULT_CARD_MOD  # type: ignore

def add_styling_to_file(file_path: Path) -> bool:
    """Add card_mod styling to file if it doesn't have any. Returns True if modified."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has card_mod
    if 'card_mod:' in content:
        return False

    # Skip if it's not a card file
    if 'type:' not in content:
        return False

    original_content = content
    lines = content.split('\n')
    new_lines = []
    modified = False

    # Look for card definitions to add styling to
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # Check if this is a card type that needs styling
        # For custom:auto-entities, add to the main card
        if re.match(r'\s*card:', line):
            # Get indentation
            indent = len(line) - len(line.lstrip())
            # Check the next few lines for type
            j = i + 1
            while j < len(lines) and j < i + 5:
                if 'type:' in lines[j]:
                    # Found a type, add card_mod after the card properties
                    # First, collect all card properties
                    k = j + 1
                    while k < len(lines) and lines[k].strip() and not lines[k].strip().startswith('-'):
                        new_lines.append(lines[k])
                        k += 1

                    # Add card_mod with proper indentation
                    card_mod_lines = DEFAULT_CARD_MOD.split('\n')
                    for cmd_line in card_mod_lines:
                        if cmd_line:
                            new_lines.append(' ' * (indent + 2) + cmd_line)
                        else:
                            new_lines.append('')

                    modified = True
                    i = k - 1
                    break
                j += 1

        i += 1

    if modified:
        new_content = '\n'.join(new_lines)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Added styling to: {file_path.name}")
        return True

    return False

def main():
    lovelace_path = Path('./lovelace')

    # Cards that need styling
    cards_to_style = [
        'cards/automations/automations.yaml',
        'cards/media/media_recent_played.yaml',
        'cards/media/sonarr_all_shows.yaml',
        'cards/media/sonarr_missing.yaml',
        'cards/media/sonarr_queue.yaml',
        'cards/media/sonarr_upcoming.yaml',
        'cards/network/network_portainer.yaml',
        'cards/network/network_services.yaml',
        'cards/switches/powerpoints.yaml',
    ]

    print("Adding card_mod styling to cards without it...\n")

    modified_count = 0
    for card_path in cards_to_style:
        full_path = lovelace_path / card_path
        if full_path.exists():
            if add_styling_to_file(full_path):
                modified_count += 1

    print(f"\n{'='*60}")
    print(f"Modified {modified_count} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
