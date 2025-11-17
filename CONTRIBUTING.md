# Contributing to Home Assistant Configuration

Thank you for considering contributing to this Home Assistant configuration! This document provides guidelines and workflows for making contributions.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Branch Naming Convention](#branch-naming-convention)
3. [Commit Message Format](#commit-message-format)
4. [Pull Request Process](#pull-request-process)
5. [Code Style Guidelines](#code-style-guidelines)
6. [Testing Requirements](#testing-requirements)
7. [Documentation Standards](#documentation-standards)

---

## Getting Started

### Prerequisites

- Git installed and configured
- Access to the Home Assistant instance
- Pre-commit hooks installed (optional but recommended)
- Basic understanding of YAML and Home Assistant

### Initial Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install pre-commit hooks (optional):**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

3. **Create a development branch:**
   ```bash
   git checkout -b development
   ```

4. **Stay up to date:**
   ```bash
   git pull origin master
   ```

---

## Branch Naming Convention

All branches must follow this naming pattern:

### Format

```
<type>/<short-description>
```

### Types

| Type | Description | Example |
|------|-------------|---------|
| `feature/` | New functionality or enhancement | `feature/morning-routine` |
| `bugfix/` | Bug fix for non-critical issues | `bugfix/climate-temperature-fix` |
| `hotfix/` | Urgent fix for production issues | `hotfix/automation-loop` |
| `docs/` | Documentation updates only | `docs/setup-guide` |
| `refactor/` | Code restructuring (no functional changes) | `refactor/climate-automation-split` |
| `test/` | Adding or updating tests | `test/automation-validation` |

### Examples

```bash
git checkout -b feature/automated-backup
git checkout -b bugfix/spotify-playback-error
git checkout -b docs/rfid-setup-guide
git checkout -b hotfix/broken-morning-automation
```

### Rules

- Use lowercase and hyphens (kebab-case)
- Keep descriptions short and descriptive (2-4 words)
- One feature/fix per branch
- Delete branch after merging

---

## Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for clear and structured commit history.

### Format

```
<type>: <short description>

[optional body]

[optional footer]
```

### Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature or enhancement | `feat: add morning preheat automation` |
| `fix` | Bug fix | `fix: correct bedroom light entity reference` |
| `docs` | Documentation changes | `docs: add RFID setup guide` |
| `refactor` | Code restructuring | `refactor: split climate automation into modules` |
| `test` | Testing changes | `test: add automation validation checks` |
| `chore` | Maintenance, dependencies | `chore: update pre-commit hooks` |
| `style` | Formatting, whitespace | `style: fix YAML indentation` |
| `perf` | Performance improvements | `perf: optimize template sensor calculations` |

### Rules

1. **Subject line:**
   - Start with type followed by colon
   - Use imperative mood ("add" not "added")
   - Keep under 72 characters
   - Don't end with period
   - Lowercase after type (except proper nouns)

2. **Body (optional):**
   - Explain *what* and *why*, not *how*
   - Wrap at 72 characters
   - Separate from subject with blank line
   - Use bullet points for multiple changes

3. **Footer (optional):**
   - Reference issues: `Closes #42`
   - Breaking changes: `BREAKING CHANGE: description`
   - Co-authors: `Co-Authored-By: Name <email>`

### Examples

**Simple commit:**
```bash
git commit -m "feat: add automated backup at 3 AM"
```

**Commit with body:**
```bash
git commit -m "fix: resolve morning light automation error

The bedroom light was incorrectly referenced as light.bedroom
instead of light.masterbed_lights, causing automation to fail.

Closes #15"
```

**Breaking change:**
```bash
git commit -m "refactor: change climate preset selection logic

BREAKING CHANGE: Climate automations now require input_select.climate_season
to be configured. See migration guide for details.

Closes #28"
```

---

## Pull Request Process

### Creating a Pull Request

1. **Ensure your branch is up to date:**
   ```bash
   git checkout development
   git pull origin development
   git checkout your-branch
   git merge development
   ```

2. **Run validation checks:**
   ```bash
   # YAML linting
   yamllint config/ automations/ lovelace/

   # Home Assistant config check
   ha core check

   # Pre-commit checks
   pre-commit run --all-files
   ```

3. **Push your branch:**
   ```bash
   git push -u origin your-branch
   ```

4. **Create PR via GitHub CLI:**
   ```bash
   gh pr create --base development --head your-branch \
     --title "feat: add morning routine automation" \
     --body "See PULL_REQUEST_TEMPLATE.md for checklist"
   ```

   **Or via GitHub web interface:**
   - Go to repository on GitHub
   - Click "Pull requests" > "New pull request"
   - Select base: `development`, compare: `your-branch`
   - Fill in title and description

### Pull Request Template

Use this template for all pull requests:

```markdown
## Description
[Brief description of changes]

## Type of Change
- [ ] Feature (new functionality)
- [ ] Bug fix
- [ ] Documentation update
- [ ] Refactoring
- [ ] Breaking change

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing Checklist
- [ ] Config check passes (`ha core check`)
- [ ] YAML lint passes (`yamllint`)
- [ ] Tested locally
- [ ] No errors in logs
- [ ] All automations trigger correctly
- [ ] Dashboard displays correctly

## Documentation
- [ ] Updated relevant documentation
- [ ] Added inline comments where needed
- [ ] Updated entity inventory (if applicable)

## Checklist
- [ ] No secrets committed
- [ ] Follows naming conventions
- [ ] Follows commit message convention
- [ ] Branch is up to date with base
- [ ] Pre-commit hooks pass (if installed)
```

### PR Review Process

1. **Automated checks must pass:**
   - YAML Lint
   - Home Assistant Config Check
   - Any other CI/CD workflows

2. **Code review (if required):**
   - At least one approval for major changes
   - Self-merge allowed for minor changes

3. **Merge strategy:**
   - Use "Squash and merge" for feature branches
   - Use "Merge commit" for hotfixes
   - Delete branch after merge

---

## Code Style Guidelines

### YAML Formatting

Follow `.yamllint` configuration:

- **Indentation:** 2 spaces (no tabs)
- **Line length:** Max 200 characters (warnings only)
- **Quotes:** Use single or double quotes consistently within each file
- **Lists:** Use `-` with space, indent 2 spaces
- **Comments:** Use `#` with space after
- **Blank lines:** One blank line between major sections

**Example:**

```yaml
# Good - Proper formatting
automation:
  - id: example_automation
    alias: "Example Automation"
    description: "This is an example"
    trigger:
      - platform: state
        entity_id: binary_sensor.motion
        to: "on"
    action:
      - service: light.turn_on
        target:
          entity_id: light.living_room

# Bad - Mixed indentation, inconsistent quotes
automation:
- id: example_automation
  alias: Example Automation
  description: 'This is an example'
  trigger:
    - platform: state
      entity_id: binary_sensor.motion
      to: 'on'
  action:
  - service: light.turn_on
    target:
      entity_id: light.living_room
```

### Entity Naming Conventions

- **Domains:** Use standard HA domains (`sensor`, `binary_sensor`, `switch`, etc.)
- **Entity IDs:** Use lowercase with underscores (`snake_case`)
- **Friendly names:** Use title case with spaces
- **Prefixes:** Group related entities with common prefix

**Examples:**
```yaml
# Good
sensor.living_room_temperature
input_boolean.climate_manual_control_living
automation.living_room_morning_heat_winter

# Bad
sensor.LivingRoomTemp
input_boolean.ManualControlLiving
automation.Automation_1
```

### Automation Structure

Follow this template structure:

```yaml
- id: unique_automation_id
  alias: "Human Readable Name"
  description: "What this automation does"

  trigger:
    - platform: state
      entity_id: sensor.example
      to: "on"
      id: trigger_id

  condition:
    - condition: state
      entity_id: input_boolean.enable_automation
      state: "on"

  action:
    - service: light.turn_on
      target:
        entity_id: light.example

  mode: single
```

### Comments and Documentation

- **Inline comments:** Explain *why*, not *what*
- **Section headers:** Use for large files
- **Entity references:** Document where entities are defined
- **Complex logic:** Add comments explaining the approach

**Example:**

```yaml
# ============================================================================
# MORNING HEATING AUTOMATION
# ============================================================================
# Purpose: Preheat living room before wake-up time
# Trigger: 5:30 AM on weekdays
# Condition: Winter season, home occupied, temperature below threshold
# ============================================================================

- id: living_room_morning_preheat
  alias: "Living Room - Morning Preheat"
  description: "Warm living room 30 minutes before wake-up"

  trigger:
    - platform: time
      at: "05:30:00"

  condition:
    # Only run in winter when heating is needed
    - condition: state
      entity_id: input_select.climate_season
      state: winter

    # Don't heat if already warm
    - condition: numeric_state
      entity_id: sensor.living_room_temperature
      below: 18

  action:
    # Use comfort preset for morning warmth
    - service: script.activate_heating
      data:
        climate_entity: climate.living_room_versatile_thermastat
        preset_mode: comfort

  mode: single
```

---

## Testing Requirements

### Before Committing

1. **YAML Syntax Validation:**
   ```bash
   yamllint config/ automations/ lovelace/
   ```

2. **Home Assistant Config Check:**
   ```bash
   ha core check
   ```

3. **No Secrets in Code:**
   ```bash
   grep -r "password" config/ automations/
   grep -r "api_key" config/ automations/
   grep -r "token" config/ automations/
   ```

### After Deployment

1. **Restart Home Assistant:**
   ```bash
   ha core restart
   ```

2. **Monitor Logs:**
   ```bash
   ha core logs -f
   ```
   - Watch for errors for 5-10 minutes
   - Verify automations load successfully

3. **Manual Testing:**
   - Trigger automations manually (Developer Tools > Actions)
   - Verify expected behavior
   - Check dashboard displays correctly

4. **Monitoring Period:**
   - Monitor for 24-48 hours after deployment
   - Check automation execution logs
   - Verify no unexpected triggers or errors

---

## Documentation Standards

### Required Documentation

For all new features:

1. **Inline YAML comments:** Explain purpose and behavior
2. **Setup guide:** Step-by-step instructions (if complex)
3. **Entity inventory update:** Add new entities to docs/ENTITY_INVENTORY.md
4. **Troubleshooting section:** Common issues and solutions

### Documentation Format

Use markdown (.md) for all documentation:

- **Headings:** Use `#` for h1, `##` for h2, etc.
- **Code blocks:** Use triple backticks with language identifier
- **Lists:** Use `-` for unordered, `1.` for ordered
- **Links:** Use descriptive text, not "click here"
- **Tables:** Use markdown tables for structured data

**Example:**

```markdown
# Feature Name

## Overview

Brief description of what this feature does.

## Prerequisites

- Requirement 1
- Requirement 2

## Setup Instructions

1. Step 1
   ```yaml
   code: example
   ```

2. Step 2

3. Step 3

## Troubleshooting

### Issue 1

**Symptom:** Description

**Solution:** Steps to resolve

## Related Documentation

- [Link to related guide](path/to/guide.md)
```

---

## Questions or Issues?

- **Documentation:** See `docs/` directory
- **Git workflow:** See `docs/GIT_WORKFLOW_SETUP.md`
- **YAML style:** See `docs/YAML_LINTING_GUIDE.md`
- **Issues:** Open a GitHub issue

---

## License

This configuration is provided as-is for personal use. By contributing, you agree to license your contributions under the same terms as the repository.

---

**Last Updated:** 2025-11-17
