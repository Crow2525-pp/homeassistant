# YAML Linting Guide

**Created:** 2025-11-17
**Purpose:** Guide to YAML code quality and style enforcement
**Complexity:** Low
**Category:** Code Quality

---

## Overview

This guide explains how to use yamllint to maintain consistent, error-free YAML configuration files in your Home Assistant setup.

**Benefits:**
- Catch syntax errors before deployment
- Consistent code style across all files
- Easier collaboration with standardized formatting
- Automated quality checks in CI/CD

---

## Quick Start

### Installation

**Option A: Via pip**
```bash
pip install yamllint
```

**Option B: Via package manager (Debian/Ubuntu)**
```bash
sudo apt-get install yamllint
```

### Run Linting

```bash
# Lint all config files
yamllint config/ automations/ lovelace/

# Lint specific file
yamllint automations/06_living_room_climate_split.yaml

# Show only errors (ignore warnings)
yamllint -f parsable config/
```

---

## Configuration

Your `.yamllint` file is already configured with Home Assistant-specific rules:

### Key Rules

| Rule | Setting | Reason |
|------|---------|--------|
| **line-length** | 200 chars (warning) | HA templates can be long |
| **indentation** | Disabled | Legacy files use mixed spacing |
| **truthy** | Allow yes/no/on/off | Common in HA configs |
| **comments** | Require space after # | Readability |
| **document-start** | Disabled | Optional `---` header |
| **trailing-spaces** | Disabled | Gradual cleanup |

### Files Excluded

- `.storage/` - Internal HA storage
- `secrets.yaml` - Contains sensitive data
- `deps/` - Downloaded dependencies
- `www/` - Web resources
- `*.backup` - Backup files

---

## Common Issues and Fixes

### 1. Line Too Long

**Error:**
```
automations/example.yaml
  42:81  warning  line too long (220 > 200 characters)
```

**Fix:**
Break long lines using YAML multiline strings:

**Before:**
```yaml
message: "Temperature is {{ states('sensor.temperature') }} and humidity is {{ states('sensor.humidity') }}"
```

**After:**
```yaml
message: >
  Temperature is {{ states('sensor.temperature') }}
  and humidity is {{ states('sensor.humidity') }}
```

### 2. Trailing Spaces

**Error:**
```
config.yaml
  15:23  error  trailing spaces
```

**Fix:**
Remove spaces at end of lines (most editors have "trim trailing whitespace" feature).

### 3. Inconsistent Indentation

**Error:**
```
automations.yaml
  10:5  error  wrong indentation: expected 2 but found 4
```

**Fix:**
Use 2-space indentation consistently:

**Before:**
```yaml
automation:
    - id: example
      alias: Example
```

**After:**
```yaml
automation:
  - id: example
    alias: Example
```

### 4. Truthy Value

**Error:**
```
config.yaml
  20:15  error  truthy value should be one of [true, false]
```

**Fix:**
Home Assistant allows `yes/no`, `on/off`. Update `.yamllint` to allow these (already done in your config).

---

## Running in CI/CD

Your GitHub Actions already include YAML linting:

### Workflow: `.github/workflows/yaml-lint.yml`

Runs automatically on:
- Every push to repository
- Every pull request
- Manual trigger

### Trigger Manually

```bash
# Trigger workflow
gh workflow run yaml-lint.yml

# Check status
gh run list --workflow=yaml-lint.yml

# View logs
gh run view <run-id> --log
```

---

## Integration with Pre-commit

Your `.pre-commit-config.yaml` includes yamllint:

### Usage

```bash
# Run on all files
pre-commit run --all-files

# Run only yamllint
pre-commit run yamllint

# Skip yamllint (emergency)
SKIP=yamllint git commit
```

---

## Best Practices

### DO

✓ Use 2-space indentation
✓ Add comments explaining complex logic
✓ Use multiline strings for long templates
✓ Keep line length under 200 characters
✓ Run yamllint before committing
✓ Fix errors before pushing to repository

### DON'T

✗ Mix tabs and spaces
✗ Use 4-space or other indentation
✗ Commit files with linting errors
✗ Ignore warnings long-term
✗ Disable rules without documenting why

---

## Suppressing Warnings

### Disable Rule for Single Line

```yaml
# yamllint disable-line rule:line-length
very_long_line: "This line exceeds 200 characters but needs to be this way because..."
```

### Disable Rule for Block

```yaml
# yamllint disable rule:line-length
automation:
  - alias: "Example with very long templates"
    # ... long content ...
# yamllint enable rule:line-length
```

### Disable Rule for Entire File

Add to top of file:
```yaml
# yamllint disable rule:line-length
---
# Rest of file...
```

**Use sparingly** - only when absolutely necessary.

---

## Editor Integration

### Visual Studio Code

Install extension: **YAML** by Red Hat

Add to `.vscode/settings.json`:
```json
{
  "yaml.validate": true,
  "yaml.format.enable": true,
  "yaml.customTags": [
    "!secret scalar",
    "!include scalar",
    "!include_dir_list scalar",
    "!include_dir_named scalar",
    "!include_dir_merge_list scalar",
    "!include_dir_merge_named scalar"
  ]
}
```

### Vim

Install plugin: **ale** (Asynchronous Lint Engine)

Add to `.vimrc`:
```vim
let g:ale_linters = {'yaml': ['yamllint']}
let g:ale_yaml_yamllint_options = '-c .yamllint'
```

---

## Maintenance

### Weekly
- [ ] Review linting warnings in pull requests
- [ ] Fix new violations before they accumulate

### Monthly
- [ ] Run `yamllint --strict` to catch all warnings
- [ ] Update `.yamllint` config if rules need adjustment
- [ ] Review and clean up suppressed warnings

### Quarterly
- [ ] Update yamllint: `pip install --upgrade yamllint`
- [ ] Review `.yamllint` config against latest best practices

---

## Related Documentation

- `.yamllint` - Linting configuration file
- `.pre-commit-config.yaml` - Pre-commit hook configuration
- `.github/workflows/yaml-lint.yml` - CI/CD linting workflow
- `docs/GIT_WORKFLOW_SETUP.md` - Git workflow guide

---

**Status:** Ready for use
**Last Updated:** 2025-11-17
