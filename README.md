# Home Assistant Configuration

My personal Home Assistant setup.

## Structure

- `configuration.yaml` - Main HA config
- `automations/` - Automation YAML files
- `config/` - Additional configuration, including active dashboard YAML under `config/lovelace/`
- `config/lovelace/` - Dashboard YAML used by the main HA config and scanned by the entity validator
- `ui_lovelace_minimalist/` - UI Lovelace Minimalist dashboard source and dashboards
- `custom_components/ui_lovelace_minimalist/lovelace/` - Custom component Lovelace YAML also covered by entity validation
- `esphome/` - ESPHome device configs
- `zigbee2mqtt/` - Zigbee2MQTT config
- `custom_components/` - Custom integrations (HACS)
- `tools/` - Utility scripts
- `docs/` - Notes and reference docs
