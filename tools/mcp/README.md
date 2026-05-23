# Home Assistant MCP Launcher

Launches `mcp-remote` pointed at the HA MCP integration, probing LAN first then Tailscale.

## Setup

The MCP endpoint path contains a private token and must be set as an environment variable — do not hard-code it in the script.

```bash
export HA_MCP_PATH="/private_<your-token-here>"
```

Store this in your shell env, a local `.envrc` (direnv), or your Claude Code `settings.local.json` via an `env` block.

## Variables

| Variable | Default | Description |
|---|---|---|
| `HA_MCP_PATH` | *required* | Private path component of the HA MCP URL |
| `HA_MCP_PORT` | `9583` | Port the HA MCP integration listens on |
| `HA_MCP_LOCAL_HOST` | `192.168.1.98` | LAN IP of Home Assistant |
| `HA_MCP_TAILSCALE_HOST` | `homeassistant` | Tailscale hostname of Home Assistant |
| `HA_MCP_REMOTE_PACKAGE` | `mcp-remote@0.1.38` | npx package to use |
| `HA_MCP_PROBE_TIMEOUT` | `2` | Seconds to wait when probing each URL |
