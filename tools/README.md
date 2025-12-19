# Home Assistant Tools

This directory contains various utility scripts for managing and testing your Home Assistant configuration.

## Available Tools

### test_api.py - API Testing Tool

Test and validate Home Assistant entity states using the REST API.

#### Setup

1. **Create a Long-Lived Access Token:**
   - Open Home Assistant web interface
   - Go to your Profile (click your name in bottom left)
   - Navigate to Security tab
   - Scroll to "Long-Lived Access Tokens"
   - Click "Create Token"
   - Give it a name (e.g., "API Testing")
   - Copy the generated token

2. **Configure secrets.yaml:**
   ```yaml
   # Home Assistant API Access
   ha_api_token: "your_long_lived_access_token_here"

   # Ensure you have a URL configured
   internal_url: "http://homeassistant.local:8123"
   # OR
   external_url: "https://your-domain.com"
   ```

3. **Install Python dependencies:**
   ```bash
   pip install requests pyyaml
   ```

#### Usage Examples

```bash
# Get state of a specific entity
python tools/test_api.py get switch.living_room_light

# Get state with full attributes
python tools/test_api.py get climate.master_bedroom

# List all entity IDs
python tools/test_api.py list

# List entities in a specific domain
python tools/test_api.py list light
python tools/test_api.py list climate
python tools/test_api.py list sensor

# Show all entity states
python tools/test_api.py states

# Show entity states for a specific domain
python tools/test_api.py states --domain light

# Check if specific entities exist
python tools/test_api.py check switch.living_room_light climate.master_bedroom

# Get Home Assistant configuration
python tools/test_api.py config
```

#### Common Use Cases

**Verify automation entity references:**
```bash
# Check if entities used in automation exist
python tools/test_api.py check \
  climate.master_bedroom \
  input_boolean.master_bedroom_warm \
  sensor.master_bedroom_temperature
```

**Debug entity states:**
```bash
# Check current state and attributes of a climate entity
python tools/test_api.py get climate.master_bedroom

# See all available lights
python tools/test_api.py list light
```

**Validate configuration changes:**
```bash
# After adding new devices, list them
python tools/test_api.py list switch

# Check that newly configured entities are available
python tools/test_api.py check switch.new_device
```

### validate_entities.py - Entity Reference Validator

Validates that all entity references in YAML configuration files exist in the Home Assistant entity registry.

#### Usage

```bash
# Run validation
python tools/validate_entities.py

# Verbose output
python tools/validate_entities.py --verbose

# Save report to file
python tools/validate_entities.py --report validation_report.md
```

This tool:
- Scans all YAML files in automations/, config/, and lovelace/
- Extracts entity ID references
- Validates against the entity registry (.storage/core.entity_registry)
- Reports any invalid or missing entities

### Maintenance Tools

See `maintenance/` directory for additional maintenance utilities:
- `zombie_cleanup_report.py` - Reports on unused/orphaned entities

## Tips

- Always test API access after creating a new token
- Use `test_api.py config` to verify API connectivity
- Run `validate_entities.py` before committing configuration changes
- Keep your `secrets.yaml` secure and never commit it to git
