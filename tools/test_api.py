#!/usr/bin/env python3
"""
Home Assistant API Testing Tool

This script provides easy access to the Home Assistant REST API for testing
and validating entity states.

Usage:
    # Get state of a specific entity
    python test_api.py get switch.living_room_light

    # Get all entity states
    python test_api.py states

    # List all entities of a specific domain
    python test_api.py list light

    # Check if specific entities exist
    python test_api.py check switch.living_room_light light.bedroom

    # Get full API config
    python test_api.py config

Requirements:
    - Python 3.7+
    - requests library (pip install requests)
    - Home Assistant URL and API token configured in secrets.yaml

Setup:
    1. Create a long-lived access token in Home Assistant:
       Profile > Security > Long-Lived Access Tokens
    2. Add to secrets.yaml:
       ha_api_token: "your_token_here"
    3. Ensure internal_url or external_url is set in secrets.yaml
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import requests
except ImportError:
    print("Error: requests library not found")
    print("Install with: pip install requests")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("Error: PyYAML library not found")
    print("Install with: pip install pyyaml")
    sys.exit(1)


class HomeAssistantAPI:
    """Simple Home Assistant REST API client."""

    def __init__(self, url: str, token: str):
        """Initialize the API client.

        Args:
            url: Home Assistant URL (e.g., http://homeassistant.local:8123)
            token: Long-lived access token
        """
        self.url = url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        """Make an API request.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (without base URL)
            **kwargs: Additional arguments for requests

        Returns:
            JSON response data
        """
        url = f"{self.url}/api/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            sys.exit(1)

    def get_config(self) -> Dict:
        """Get Home Assistant configuration."""
        return self._request('GET', 'config')

    def get_states(self) -> List[Dict]:
        """Get all entity states."""
        return self._request('GET', 'states')

    def get_state(self, entity_id: str) -> Optional[Dict]:
        """Get state of a specific entity.

        Args:
            entity_id: Entity ID to query

        Returns:
            Entity state dict or None if not found
        """
        try:
            return self._request('GET', f'states/{entity_id}')
        except SystemExit:
            return None

    def check_entities(self, entity_ids: List[str]) -> Dict[str, bool]:
        """Check if multiple entities exist.

        Args:
            entity_ids: List of entity IDs to check

        Returns:
            Dict mapping entity_id to exists (bool)
        """
        states = self.get_states()
        existing_ids = {state['entity_id'] for state in states}
        return {entity_id: entity_id in existing_ids for entity_id in entity_ids}

    def list_entities(self, domain: Optional[str] = None) -> List[str]:
        """List all entities, optionally filtered by domain.

        Args:
            domain: Optional domain to filter (e.g., 'light', 'switch')

        Returns:
            List of entity IDs
        """
        states = self.get_states()
        entity_ids = [state['entity_id'] for state in states]

        if domain:
            entity_ids = [eid for eid in entity_ids if eid.startswith(f'{domain}.')]

        return sorted(entity_ids)


def load_config() -> tuple[str, str]:
    """Load Home Assistant URL and API token from secrets.yaml.

    Returns:
        Tuple of (url, token)
    """
    config_dir = Path(__file__).parent.parent
    secrets_file = config_dir / 'secrets.yaml'

    if not secrets_file.exists():
        print(f"Error: secrets.yaml not found at {secrets_file}")
        print("Please create secrets.yaml from secrets.yaml.example")
        sys.exit(1)

    with open(secrets_file) as f:
        secrets = yaml.safe_load(f)

    # Try to get URL from secrets
    url = secrets.get('internal_url') or secrets.get('external_url')
    if not url:
        print("Error: No Home Assistant URL found in secrets.yaml")
        print("Please set 'internal_url' or 'external_url'")
        sys.exit(1)

    token = secrets.get('ha_api_token')
    if not token:
        print("Error: No API token found in secrets.yaml")
        print("Please set 'ha_api_token' with a long-lived access token")
        print("\nTo create a token:")
        print("1. Open Home Assistant web interface")
        print("2. Go to Profile > Security")
        print("3. Create a Long-Lived Access Token")
        print("4. Add to secrets.yaml: ha_api_token: 'your_token'")
        sys.exit(1)

    return url, token


def print_json(data: Any, indent: int = 2) -> None:
    """Pretty print JSON data."""
    print(json.dumps(data, indent=indent, default=str))


def cmd_get(api: HomeAssistantAPI, entity_id: str) -> None:
    """Get state of a specific entity."""
    state = api.get_state(entity_id)
    if state:
        print(f"Entity: {entity_id}")
        print(f"State: {state['state']}")
        print(f"Last changed: {state.get('last_changed')}")
        print(f"Last updated: {state.get('last_updated')}")
        if state.get('attributes'):
            print("\nAttributes:")
            print_json(state['attributes'])
    else:
        print(f"Entity not found: {entity_id}")
        sys.exit(1)


def cmd_states(api: HomeAssistantAPI, domain: Optional[str] = None) -> None:
    """List all entity states."""
    states = api.get_states()

    if domain:
        states = [s for s in states if s['entity_id'].startswith(f'{domain}.')]
        print(f"States for domain '{domain}':")
    else:
        print(f"All entity states ({len(states)} total):")

    for state in sorted(states, key=lambda x: x['entity_id']):
        print(f"  {state['entity_id']}: {state['state']}")


def cmd_list(api: HomeAssistantAPI, domain: Optional[str] = None) -> None:
    """List entity IDs."""
    entities = api.list_entities(domain)

    if domain:
        print(f"Entities in domain '{domain}' ({len(entities)} total):")
    else:
        print(f"All entities ({len(entities)} total):")

    for entity_id in entities:
        print(f"  {entity_id}")


def cmd_check(api: HomeAssistantAPI, entity_ids: List[str]) -> None:
    """Check if entities exist."""
    results = api.check_entities(entity_ids)

    print(f"Checking {len(entity_ids)} entities:")
    all_exist = True

    for entity_id, exists in results.items():
        status = "✓ EXISTS" if exists else "✗ NOT FOUND"
        print(f"  {entity_id}: {status}")
        if not exists:
            all_exist = False

    if not all_exist:
        sys.exit(1)


def cmd_config(api: HomeAssistantAPI) -> None:
    """Get Home Assistant configuration."""
    config = api.get_config()
    print("Home Assistant Configuration:")
    print_json(config)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Home Assistant API testing tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get state of an entity
  %(prog)s get switch.living_room_light

  # List all entity states
  %(prog)s states

  # List all entities in a domain
  %(prog)s list light

  # Check if entities exist
  %(prog)s check switch.living_room_light light.bedroom

  # Get HA configuration
  %(prog)s config
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # get command
    get_parser = subparsers.add_parser('get', help='Get state of a specific entity')
    get_parser.add_argument('entity_id', help='Entity ID to query')

    # states command
    states_parser = subparsers.add_parser('states', help='List all entity states')
    states_parser.add_argument('--domain', help='Filter by domain (e.g., light, switch)')

    # list command
    list_parser = subparsers.add_parser('list', help='List entity IDs')
    list_parser.add_argument('domain', nargs='?', help='Optional domain to filter')

    # check command
    check_parser = subparsers.add_parser('check', help='Check if entities exist')
    check_parser.add_argument('entity_ids', nargs='+', help='Entity IDs to check')

    # config command
    subparsers.add_parser('config', help='Get Home Assistant configuration')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Load configuration
    url, token = load_config()
    api = HomeAssistantAPI(url, token)

    # Execute command
    if args.command == 'get':
        cmd_get(api, args.entity_id)
    elif args.command == 'states':
        cmd_states(api, args.domain)
    elif args.command == 'list':
        cmd_list(api, args.domain)
    elif args.command == 'check':
        cmd_check(api, args.entity_ids)
    elif args.command == 'config':
        cmd_config(api)


if __name__ == '__main__':
    main()
