#!/usr/bin/env python3
"""
Home Assistant API Testing Tool

This script provides easy access to the Home Assistant REST API for testing
and validating entity states.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

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

DEFAULT_TIMEOUT = 10.0


def positive_timeout(value: str) -> float:
    """Argparse type for positive timeout values."""
    timeout = float(value)
    if timeout <= 0:
        raise argparse.ArgumentTypeError("timeout must be greater than 0")
    return timeout


class HomeAssistantAPIError(RuntimeError):
    """Base error for Home Assistant API failures."""


class HomeAssistantConfigError(HomeAssistantAPIError):
    """Raised when local configuration is missing or invalid."""


class HomeAssistantRequestError(HomeAssistantAPIError):
    """Raised when an API request fails."""


class HomeAssistantAuthError(HomeAssistantRequestError):
    """Raised when Home Assistant rejects authentication."""


class HomeAssistantNotFoundError(HomeAssistantRequestError):
    """Raised when a requested resource does not exist."""


class HomeAssistantTimeoutError(HomeAssistantRequestError):
    """Raised when an API request times out."""


class HomeAssistantAPI:
    """Simple Home Assistant REST API client."""

    def __init__(self, url: str, token: str, timeout: float = DEFAULT_TIMEOUT):
        self.url = url.rstrip("/")
        self.timeout = timeout
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        self.session = requests.Session()

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.url}/api/{endpoint}"
        timeout = kwargs.pop("timeout", self.timeout)
        try:
            response = self.session.request(
                method,
                url,
                headers=self.headers,
                timeout=timeout,
                **kwargs,
            )
        except requests.exceptions.Timeout as exc:
            raise HomeAssistantTimeoutError(
                f"Request to {url} timed out after {timeout:g}s"
            ) from exc
        except requests.exceptions.RequestException as exc:
            raise HomeAssistantRequestError(f"API request failed: {exc}") from exc

        if response.status_code == 401:
            raise HomeAssistantAuthError(
                "Authentication failed. Check ha_api_token in secrets.yaml."
            )
        if response.status_code == 404:
            raise HomeAssistantNotFoundError(f"Home Assistant endpoint not found: {endpoint}")

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            detail = response.text.strip()
            message = f"API request failed with HTTP {response.status_code}"
            if detail:
                message = f"{message}: {detail}"
            raise HomeAssistantRequestError(message) from exc

        if not response.content:
            return None

        try:
            return response.json()
        except ValueError as exc:
            raise HomeAssistantRequestError(
                f"Home Assistant returned invalid JSON for {endpoint}"
            ) from exc

    def get_config(self) -> dict:
        return self._request("GET", "config")

    def get_states(self) -> list[dict]:
        return self._request("GET", "states")

    def get_state(self, entity_id: str) -> dict | None:
        try:
            return self._request("GET", f"states/{entity_id}")
        except HomeAssistantNotFoundError:
            return None

    def check_entities(self, entity_ids: list[str]) -> dict[str, bool]:
        states = self.get_states()
        existing_ids = {state["entity_id"] for state in states}
        return {entity_id: entity_id in existing_ids for entity_id in entity_ids}

    def list_entities(self, domain: str | None = None) -> list[str]:
        states = self.get_states()
        entity_ids = [state["entity_id"] for state in states]
        if domain:
            entity_ids = [eid for eid in entity_ids if eid.startswith(f"{domain}.")]
        return sorted(entity_ids)


def load_config() -> tuple[str, str]:
    config_dir = Path(__file__).parent.parent
    secrets_file = config_dir / "secrets.yaml"

    if not secrets_file.exists():
        raise HomeAssistantConfigError(
            f"secrets.yaml not found at {secrets_file}. "
            "Please create secrets.yaml from secrets.yaml.example."
        )

    with open(secrets_file, encoding="utf-8") as f:
        secrets = yaml.safe_load(f)

    url = secrets.get("internal_url") or secrets.get("external_url")
    if not url:
        raise HomeAssistantConfigError(
            "No Home Assistant URL found in secrets.yaml. "
            "Please set 'internal_url' or 'external_url'."
        )

    token = secrets.get("ha_api_token")
    if not token:
        raise HomeAssistantConfigError(
            "No API token found in secrets.yaml. "
            "Please set 'ha_api_token' with a long-lived access token. "
            "Create one in Home Assistant under Profile > Security."
        )

    return url, token


def print_json(data: Any, indent: int = 2) -> None:
    print(json.dumps(data, indent=indent, default=str))


def cmd_get(api: HomeAssistantAPI, entity_id: str) -> None:
    state = api.get_state(entity_id)
    if state:
        print(f"Entity: {entity_id}")
        print(f"State: {state['state']}")
        print(f"Last changed: {state.get('last_changed')}")
        print(f"Last updated: {state.get('last_updated')}")
        if state.get("attributes"):
            print("\nAttributes:")
            print_json(state["attributes"])
    else:
        print(f"Entity not found: {entity_id}")
        sys.exit(1)


def cmd_states(api: HomeAssistantAPI, domain: str | None = None) -> None:
    states = api.get_states()
    if domain:
        states = [s for s in states if s["entity_id"].startswith(f"{domain}.")]
        print(f"States for domain '{domain}':")
    else:
        print(f"All entity states ({len(states)} total):")

    for state in sorted(states, key=lambda x: x["entity_id"]):
        print(f"  {state['entity_id']}: {state['state']}")


def cmd_list(api: HomeAssistantAPI, domain: str | None = None) -> None:
    entities = api.list_entities(domain)
    if domain:
        print(f"Entities in domain '{domain}' ({len(entities)} total):")
    else:
        print(f"All entities ({len(entities)} total):")

    for entity_id in entities:
        print(f"  {entity_id}")


def cmd_check(api: HomeAssistantAPI, entity_ids: list[str]) -> None:
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
    config = api.get_config()
    print("Home Assistant Configuration:")
    print_json(config)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Home Assistant API testing tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s get switch.living_room_light
  %(prog)s states
  %(prog)s list light
  %(prog)s check switch.living_room_light light.bedroom
  %(prog)s config
        """,
    )
    parser.add_argument(
        "--timeout",
        type=positive_timeout,
        default=DEFAULT_TIMEOUT,
        help=f"HTTP timeout in seconds (default: {DEFAULT_TIMEOUT:g})",
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    get_parser = subparsers.add_parser("get", help="Get state of a specific entity")
    get_parser.add_argument("entity_id", help="Entity ID to query")

    states_parser = subparsers.add_parser("states", help="List all entity states")
    states_parser.add_argument("--domain", help="Filter by domain (e.g., light, switch)")

    list_parser = subparsers.add_parser("list", help="List entity IDs")
    list_parser.add_argument("domain", nargs="?", help="Optional domain to filter")

    check_parser = subparsers.add_parser("check", help="Check if entities exist")
    check_parser.add_argument("entity_ids", nargs="+", help="Entity IDs to check")

    subparsers.add_parser("config", help="Get Home Assistant configuration")
    return parser


def run_command(api: HomeAssistantAPI, args: argparse.Namespace) -> None:
    if args.command == "get":
        cmd_get(api, args.entity_id)
    elif args.command == "states":
        cmd_states(api, args.domain)
    elif args.command == "list":
        cmd_list(api, args.domain)
    elif args.command == "check":
        cmd_check(api, args.entity_ids)
    elif args.command == "config":
        cmd_config(api)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 1

    try:
        url, token = load_config()
        api = HomeAssistantAPI(url, token, timeout=args.timeout)
        run_command(api, args)
    except HomeAssistantAPIError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
