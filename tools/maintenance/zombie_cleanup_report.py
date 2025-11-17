#!/usr/bin/env python3
"""
Home Assistant Zombie Device and Entity Cleanup Report
Analyzes registry files to identify entities and devices that can be cleaned up.
"""

import json
from collections import defaultdict
from datetime import datetime

def load_json(filepath):
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_report():
    """Generate cleanup report."""

    print("=" * 80)
    print("HOME ASSISTANT ZOMBIE CLEANUP REPORT")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Load registries
    print("\nLoading registries...")
    devices = load_json('.storage/core.device_registry')
    entities = load_json('.storage/core.entity_registry')

    device_list = devices['data']['devices']
    entity_list = entities['data']['entities']

    print(f"[OK] Loaded {len(device_list)} devices")
    print(f"[OK] Loaded {len(entity_list)} entities")

    # Build device to entity mapping
    device_entities = defaultdict(list)
    for entity in entity_list:
        if entity.get('device_id'):
            device_entities[entity['device_id']].append(entity['entity_id'])

    # 1. DISABLED ENTITIES
    print("\n" + "=" * 80)
    print("1. DISABLED ENTITIES (can be safely removed)")
    print("=" * 80)
    disabled = [e for e in entity_list if e.get('disabled_by')]
    disabled.sort(key=lambda x: x.get('platform', ''))

    print(f"\nFound {len(disabled)} disabled entities:\n")

    by_platform = defaultdict(list)
    for e in disabled:
        platform = e.get('platform', 'unknown')
        by_platform[platform].append(e)

    for platform, ents in sorted(by_platform.items()):
        print(f"\n  [{platform.upper()}] - {len(ents)} entities")
        for e in ents[:10]:  # Show first 10
            print(f"    - {e['entity_id']} (disabled by: {e.get('disabled_by')})")
        if len(ents) > 10:
            print(f"    ... and {len(ents) - 10} more")

    # 2. HIDDEN ENTITIES
    print("\n" + "=" * 80)
    print("2. HIDDEN ENTITIES (review if still needed)")
    print("=" * 80)
    hidden = [e for e in entity_list if e.get('hidden_by')]
    print(f"\nFound {len(hidden)} hidden entities:\n")

    for e in hidden:
        print(f"  - {e['entity_id']} (hidden by: {e.get('hidden_by')})")

    # 3. ORPHANED ENTITIES
    print("\n" + "=" * 80)
    print("3. ORPHANED ENTITIES (no device association)")
    print("=" * 80)
    orphaned = [e for e in entity_list
                if not e.get('device_id')
                and e.get('platform') not in ['group', 'template', 'input_boolean',
                                               'input_number', 'input_datetime',
                                               'input_text', 'input_select',
                                               'timer', 'counter', 'automation',
                                               'script', 'scene', 'zone']
                and not e.get('disabled_by')]

    print(f"\nFound {len(orphaned)} orphaned entities (active, no device):\n")

    by_platform = defaultdict(list)
    for e in orphaned:
        platform = e.get('platform', 'unknown')
        by_platform[platform].append(e)

    for platform, ents in sorted(by_platform.items()):
        print(f"\n  [{platform.upper()}] - {len(ents)} entities")
        for e in ents[:5]:  # Show first 5
            print(f"    - {e['entity_id']}")
        if len(ents) > 5:
            print(f"    ... and {len(ents) - 5} more")

    # 4. DEVICES WITH NO ENTITIES
    print("\n" + "=" * 80)
    print("4. DEVICES WITH NO ENTITIES (can likely be removed)")
    print("=" * 80)

    device_id_map = {d['id']: d for d in device_list}
    empty_devices = []

    for device in device_list:
        device_id = device['id']
        if device_id not in device_entities:
            empty_devices.append(device)

    print(f"\nFound {len(empty_devices)} devices with no entities:\n")

    by_manufacturer = defaultdict(list)
    for d in empty_devices:
        mfg = d.get('manufacturer') or 'Unknown'
        by_manufacturer[mfg].append(d)

    for mfg, devs in sorted(by_manufacturer.items(), key=lambda x: x[0] or 'Unknown'):
        print(f"\n  [{mfg}] - {len(devs)} devices")
        for d in devs[:5]:
            name = d.get('name_by_user') or d.get('name', 'Unnamed')
            print(f"    - {name}")
        if len(devs) > 5:
            print(f"    ... and {len(devs) - 5} more")

    # 5. DISABLED DEVICES
    print("\n" + "=" * 80)
    print("5. DISABLED DEVICES")
    print("=" * 80)
    disabled_devs = [d for d in device_list if d.get('disabled_by')]
    print(f"\nFound {len(disabled_devs)} disabled devices:\n")

    for d in disabled_devs[:20]:
        name = d.get('name_by_user') or d.get('name', 'Unnamed')
        print(f"  - {name} (disabled by: {d.get('disabled_by')})")
    if len(disabled_devs) > 20:
        print(f"  ... and {len(disabled_devs) - 20} more")

    # SUMMARY
    print("\n" + "=" * 80)
    print("CLEANUP SUMMARY")
    print("=" * 80)
    print(f"""
Total Entities:           {len(entity_list)}
  - Disabled:             {len(disabled)} [CAN REMOVE]
  - Hidden:               {len(hidden)} [REVIEW]
  - Orphaned (active):    {len(orphaned)} [REVIEW]

Total Devices:            {len(device_list)}
  - With no entities:     {len(empty_devices)} [CAN REMOVE]
  - Disabled:             {len(disabled_devs)} [CAN REMOVE]

RECOMMENDATION:
  1. Start by removing disabled entities through UI (Settings -> Entities)
  2. Remove devices with no entities (Settings -> Devices)
  3. Review and remove orphaned entities
  4. Consider unhiding or removing hidden entities
""")

    print("\n" + "=" * 80)
    print("To clean up via UI:")
    print("  Settings -> Devices & Services -> Entities (filter: disabled)")
    print("  Settings -> Devices & Services -> Devices")
    print("=" * 80)

    # Generate entity lists for easy removal
    print("\n\nGenerating entity ID lists for bulk operations...")

    with open('disabled_entities.txt', 'w') as f:
        f.write("# Disabled entities - can be removed\n")
        for e in disabled:
            f.write(f"{e['entity_id']}\n")
    print("[OK] disabled_entities.txt")

    with open('orphaned_entities.txt', 'w') as f:
        f.write("# Orphaned entities (no device) - review before removing\n")
        for e in orphaned:
            f.write(f"{e['entity_id']}\n")
    print("[OK] orphaned_entities.txt")

    with open('empty_devices.txt', 'w') as f:
        f.write("# Devices with no entities - can be removed\n")
        for d in empty_devices:
            name = d.get('name_by_user') or d.get('name', 'Unnamed')
            f.write(f"{d['id']}\t{name}\n")
    print("[OK] empty_devices.txt")

    print("\n[OK] Report complete!")

if __name__ == '__main__':
    try:
        generate_report()
    except FileNotFoundError as e:
        print(f"Error: Could not find registry file: {e}")
        print("Make sure you're running this script from your Home Assistant config directory.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
