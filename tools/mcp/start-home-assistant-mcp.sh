#!/usr/bin/env bash

set -euo pipefail

# Codex URL transports are static; bridge through mcp-remote so the upstream
# host can be selected at launch time.
MCP_PORT="${HA_MCP_PORT:-9583}"
MCP_PATH="${HA_MCP_PATH:?HA_MCP_PATH must be set (HA MCP private path — do not hard-code in this file)}"
LOCAL_HOST="${HA_MCP_LOCAL_HOST:-192.168.1.98}"
TAILSCALE_HOST="${HA_MCP_TAILSCALE_HOST:-homeassistant}"
MCP_REMOTE_PACKAGE="${HA_MCP_REMOTE_PACKAGE:-mcp-remote@0.1.38}"
PROBE_TIMEOUT="${HA_MCP_PROBE_TIMEOUT:-2}"

local_url="http://${LOCAL_HOST}:${MCP_PORT}${MCP_PATH}"
tailscale_url="http://${TAILSCALE_HOST}:${MCP_PORT}${MCP_PATH}"

tailscale_is_ready() {
  command -v tailscale >/dev/null 2>&1 || return 1
  tailscale status --json 2>/dev/null | grep -q '"BackendState":[[:space:]]*"Running"' || return 1
  getent hosts "${TAILSCALE_HOST}" >/dev/null 2>&1 || return 1
}

url_responds() {
  local url="$1"
  local code

  code="$(curl -sS -o /dev/null -w '%{http_code}' --max-time "${PROBE_TIMEOUT}" "${url}" 2>/dev/null || true)"
  [ -n "${code}" ] && [ "${code}" != "000" ]
}

if ! command -v npx >/dev/null 2>&1; then
  echo "npx is required to launch ${MCP_REMOTE_PACKAGE}" >&2
  exit 1
fi

if ! command -v curl >/dev/null 2>&1; then
  echo "curl is required to probe Home Assistant MCP availability" >&2
  exit 1
fi

selected_url=""
if url_responds "${local_url}"; then
  selected_url="${local_url}"
elif tailscale_is_ready && url_responds "${tailscale_url}"; then
  selected_url="${tailscale_url}"
fi

if [ -z "${selected_url}" ]; then
  echo "Home Assistant MCP endpoint is unreachable." >&2
  echo "Tried local URL: ${local_url}" >&2
  echo "Tried tailscale URL: ${tailscale_url}" >&2
  exit 1
fi

exec npx -y "${MCP_REMOTE_PACKAGE}" \
  "${selected_url}" \
  --transport http-only \
  --allow-http \
  --silent
