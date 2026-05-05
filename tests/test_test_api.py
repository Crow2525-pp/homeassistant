from __future__ import annotations

import argparse

import requests

from tools import test_api
from tools.test_api import (
    DEFAULT_TIMEOUT,
    HomeAssistantAPI,
    HomeAssistantAuthError,
    HomeAssistantNotFoundError,
    HomeAssistantRequestError,
    HomeAssistantTimeoutError,
)


class DummyResponse:
    def __init__(
        self,
        status_code: int = 200,
        payload=None,
        text: str = "",
        content: bytes = b"{}",
    ):
        self.status_code = status_code
        self._payload = {} if payload is None else payload
        self.text = text
        self.content = content

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(response=self)

    def json(self):
        return self._payload


def test_request_uses_default_timeout(monkeypatch) -> None:
    recorded: dict[str, object] = {}

    def fake_request(
        method: str,
        url: str,
        headers: dict[str, str],
        timeout: float,
        **kwargs,
    ):
        recorded.update(
            method=method,
            url=url,
            headers=headers,
            timeout=timeout,
            kwargs=kwargs,
        )
        return DummyResponse(payload={"ok": True})

    api = HomeAssistantAPI("http://ha.local:8123", "token")
    monkeypatch.setattr(api.session, "request", fake_request)

    payload = api.get_config()

    assert payload == {"ok": True}
    assert recorded["method"] == "GET"
    assert recorded["url"] == "http://ha.local:8123/api/config"
    assert recorded["timeout"] == DEFAULT_TIMEOUT


def test_get_state_returns_none_for_missing_entity(monkeypatch) -> None:
    def fake_request(*args, **kwargs):
        return DummyResponse(status_code=404, text="missing", content=b'{"message":"missing"}')

    api = HomeAssistantAPI("http://ha.local:8123", "token")
    monkeypatch.setattr(api.session, "request", fake_request)

    assert api.get_state("light.missing") is None


def test_request_raises_auth_error_for_401(monkeypatch) -> None:
    def fake_request(*args, **kwargs):
        return DummyResponse(
            status_code=401,
            text="unauthorized",
            content=b'{"message":"bad token"}',
        )

    api = HomeAssistantAPI("http://ha.local:8123", "token")
    monkeypatch.setattr(api.session, "request", fake_request)

    try:
        api.get_states()
    except HomeAssistantAuthError as exc:
        assert "ha_api_token" in str(exc)
    else:
        raise AssertionError("Expected HomeAssistantAuthError")


def test_request_raises_timeout_error(monkeypatch) -> None:
    def fake_request(*args, **kwargs):
        raise requests.exceptions.Timeout("too slow")

    api = HomeAssistantAPI("http://ha.local:8123", "token", timeout=2.5)
    monkeypatch.setattr(api.session, "request", fake_request)

    try:
        api.get_config()
    except HomeAssistantTimeoutError as exc:
        assert "2.5s" in str(exc)
    else:
        raise AssertionError("Expected HomeAssistantTimeoutError")


def test_request_raises_detailed_http_error(monkeypatch) -> None:
    def fake_request(*args, **kwargs):
        return DummyResponse(
            status_code=500,
            text="server blew up",
            content=b'{"message":"server blew up"}',
        )

    api = HomeAssistantAPI("http://ha.local:8123", "token")
    monkeypatch.setattr(api.session, "request", fake_request)

    try:
        api.get_states()
    except HomeAssistantRequestError as exc:
        assert "HTTP 500" in str(exc)
        assert "server blew up" in str(exc)
    else:
        raise AssertionError("Expected HomeAssistantRequestError")


def test_missing_endpoint_raises_not_found(monkeypatch) -> None:
    def fake_request(*args, **kwargs):
        return DummyResponse(status_code=404, text="missing", content=b'{"message":"missing"}')

    api = HomeAssistantAPI("http://ha.local:8123", "token")
    monkeypatch.setattr(api.session, "request", fake_request)

    try:
        api.get_config()
    except HomeAssistantNotFoundError as exc:
        assert "config" in str(exc)
    else:
        raise AssertionError("Expected HomeAssistantNotFoundError")


def test_positive_timeout_rejects_zero() -> None:
    try:
        test_api.positive_timeout("0")
    except argparse.ArgumentTypeError as exc:
        assert "greater than 0" in str(exc)
    else:
        raise AssertionError("Expected ArgumentTypeError")


class StubAPI:
    def __init__(self) -> None:
        self.called: tuple[str, object] | None = None

    def get_state(self, entity_id: str):
        self.called = ("get", entity_id)
        return None

    def get_states(self):
        self.called = ("states", None)
        return []

    def list_entities(self, domain: str | None = None):
        self.called = ("list", domain)
        return []

    def check_entities(self, entity_ids: list[str]):
        self.called = ("check", entity_ids)
        return dict.fromkeys(entity_ids, True)

    def get_config(self):
        self.called = ("config", None)
        return {"version": "test"}


def test_run_command_routes_to_expected_handler(capsys) -> None:
    api = StubAPI()
    args = argparse.Namespace(command="config")

    test_api.run_command(api, args)

    captured = capsys.readouterr()
    assert api.called == ("config", None)
    assert "Home Assistant Configuration:" in captured.out


def test_main_prints_actionable_errors(monkeypatch, capsys) -> None:
    monkeypatch.setattr(test_api, "load_config", lambda: ("http://ha.local:8123", "token"))

    class FailingAPI:
        def __init__(self, url: str, token: str, timeout: float) -> None:
            self.timeout = timeout

        def get_config(self):
            raise HomeAssistantAuthError("Authentication failed. Check ha_api_token.")

    monkeypatch.setattr(test_api, "HomeAssistantAPI", FailingAPI)

    exit_code = test_api.main(["--timeout", "3", "config"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Error: Authentication failed" in captured.err
