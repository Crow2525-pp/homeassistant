# Mobile vs Web YAML Configuration Errors - Debugging Guide

## Issue Summary

Configuration errors appear on mobile but not on web browsers for Home Assistant Lovelace dashboards.

**Root Cause**: Mobile browsers enforce stricter YAML parsing than desktop browsers.

## Why This Happens

- **Desktop browsers** may cache configurations, use fallback mechanisms, or have lenient parsing
- **Mobile browsers** (Safari on iOS, Chrome on Android) enforce strict YAML validation
- **Custom cards** like `auto-entities` have built-in error recovery and work regardless
- **Native Home Assistant cards** fail immediately when YAML is malformed

## Common YAML Indentation Errors Causing This Issue

### 1. Incorrect Nested List Indentation
**Wrong:**
```yaml
cards:
filter:
- domain: switch
  label: Switch
```

**Correct:**
```yaml
cards:
filter:
  include:
    - domain: switch
      label: Switch
```

### 2. Property Order in Tile Cards
**Wrong:**
```yaml
- features:
    - type: fan-speed
  type: tile
  entity: fan.example
```

**Correct:**
```yaml
- type: tile
  entity: fan.example
  features:
    - type: fan-speed
```

The `type:` property must come first.

### 3. Improper CSS Style Indentation in card_mod
**Wrong:**
```yaml
card_mod:
  style: |
  ha-card {
    color: white;
  }
```

**Correct:**
```yaml
card_mod:
  style: |
    ha-card {
      color: white;
    }
```

All CSS content must be indented 2 more spaces than `style: |`.

### 4. Standalone Card Definitions with List Syntax
**Wrong:**
```yaml
- type: markdown
  title: My Card
```

**Correct (if it's a standalone file):**
```yaml
type: markdown
title: My Card
```

Remove the list item dash if the file is meant to be a card definition, not a list item.

### 5. Missing Indentation for Options
**Wrong:**
```yaml
filter:
  include:
  - domain: switch
    options:
    type: tile
```

**Correct:**
```yaml
filter:
  include:
    - domain: switch
      options:
        type: tile
```

Each nesting level should add 2 more spaces.

## Testing for YAML Errors

1. **Check in Home Assistant Developer Tools**:
   - Go to Developer Tools → YAML Editor
   - Load your configuration files to check for syntax errors

2. **Test on Mobile vs Desktop**:
   - If cards work on desktop but fail on mobile, suspect YAML indentation
   - Use browser DevTools to check console errors

3. **Common Error Messages**:
   - "Configuration Error" on card
   - Card not rendering
   - Blank card area (no error message)

## Prevention Tips

1. Use a **YAML linter** in your editor (VS Code extension: YAML)
2. **Ensure consistent spacing**: Use exactly 2 spaces per indent level
3. **Validate includes**: Check that included files have proper structure
4. **Test after changes**: Always refresh mobile browser after config changes
5. **Use auto-entities cautiously**: Just because auto-entities works doesn't mean your YAML is correct elsewhere

## Files Affected (from historical fixes)

- `lovelace/cards/alarm/motion.yaml`
- `lovelace/cards/fans.yaml`
- `lovelace/cards/switches/covers.yaml` (2 instances)
- `lovelace/cards/switches/powerpoints.yaml`
- `lovelace/cards/media/sonarr_all_shows.yaml`
- `lovelace/cards/media/sonarr_missing.yaml`

All issues were resolved by correcting indentation and property ordering.
