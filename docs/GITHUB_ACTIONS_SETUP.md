# GitHub Actions CI/CD Setup

## Overview
Automated validation and testing for Home Assistant configuration using GitHub Actions.

---

## Workflows Created

### 1. YAML Linting (`yaml-lint.yml`)

**Purpose:** Validates YAML syntax and style across all configuration files.

**Triggers:**
- Pull requests to `master`, `main`, or `development`
- Pushes to `master`, `main`, or `development`
- Only when `.yaml` or `.yml` files change

**What it does:**
1. Checks out code
2. Installs yamllint
3. Runs yamllint against all YAML files
4. Reports errors/warnings

**Configuration:** `.yamllint` file in repository root

### 2. Home Assistant Validation (`ha-validate.yml`)

**Purpose:** Validates Home Assistant configuration for errors.

**Triggers:**
- Pull requests to `master`, `main`, or `development`
- Pushes to `master`, `main`, or `development`
- Only when YAML files change

**What it does:**
1. Checks out code
2. Creates dummy `secrets.yaml` from `secrets.yaml.example`
3. Runs Home Assistant config validation
4. Reports configuration errors
5. Cleans up dummy secrets

**Requirements:** `secrets.yaml.example` must exist and contain all secret keys

---

## Initial Setup

### Step 1: Update .gitignore

Ensure secrets are never committed:

```bash
# Add to .gitignore if not already there
echo "secrets.yaml" >> .gitignore
echo "*.db" >> .gitignore
echo "*.db-shm" >> .gitignore
echo "*.db-wal" >> .gitignore
```

### Step 2: Create secrets.yaml.example

**Already created!** File: `secrets.yaml.example`

**Update it with your actual secret keys (but dummy values):**
```yaml
# Good - Shows what secrets are needed
wifi_ssid: "YourNetworkName"
spotify_client_id: "your_spotify_client_id"

# Bad - Real values (NEVER commit these)
wifi_ssid: "MyActualWiFiName"  # ❌ Don't do this!
spotify_client_id: "real_id_12345"  # ❌ Don't do this!
```

### Step 3: Commit and Push Workflows

```bash
# Add new files
git add .github/workflows/yaml-lint.yml
git add .github/workflows/ha-validate.yml
git add .yamllint
git add secrets.yaml.example
git add docs/GITHUB_ACTIONS_SETUP.md

# Verify secrets.yaml is NOT staged
git status | grep secrets.yaml
# Should only show secrets.yaml.example, not secrets.yaml

# Commit
git commit -m "ci: add GitHub Actions for YAML linting and HA validation"

# Push to GitHub
git push origin master
```

### Step 4: Enable GitHub Actions

1. Go to your GitHub repository
2. Click "Actions" tab
3. If prompted, enable GitHub Actions
4. Workflows will now run automatically on PRs and pushes

---

## Using the Workflows

### Testing on Pull Requests

**Standard workflow:**

```bash
# 1. Create feature branch
git checkout -b feature/new-automation

# 2. Make changes to automations
vim automations/new_automation.yaml

# 3. Commit changes
git add automations/new_automation.yaml
git commit -m "feat(automation): add new automation"

# 4. Push to GitHub
git push origin feature/new-automation

# 5. Create Pull Request on GitHub
# - Go to repository → Pull Requests → New Pull Request
# - Select: base: master ← compare: feature/new-automation
# - Click "Create Pull Request"

# 6. GitHub Actions will automatically run
# - YAML Lint workflow
# - Home Assistant Validation workflow

# 7. Check workflow results
# - Green checkmark ✅ = All checks passed
# - Red X ❌ = Errors found, click to see details

# 8. Fix any errors
# - Make fixes in your branch
# - Commit and push
# - Workflows run again automatically

# 9. Merge when all checks pass
# - Click "Merge Pull Request" on GitHub
# - Delete feature branch
```

### Local Testing Before Push

**Run yamllint locally:**

```bash
# Install yamllint (one-time)
pip install yamllint

# Run linting
yamllint .

# Check specific files
yamllint configuration.yaml
yamllint automations/

# Auto-fix some issues (be careful!)
# yamllint doesn't auto-fix, but you can use other tools:
# prettier --write "**/*.yaml"
```

**Run Home Assistant config check:**

```bash
# From Home Assistant CLI
ha core check

# OR via web UI
# Settings → System → Configuration Validation → Check Configuration
```

---

## Workflow Configuration

### YAML Lint Rules (.yamllint)

**Key settings:**

```yaml
line-length:
  max: 200  # Allow longer lines for HA configs

indentation:
  spaces: 2  # HA standard

truthy:
  allowed-values: ['true', 'false', 'yes', 'no', 'on', 'off']
  # Allows HA-style boolean values

document-start:
  present: false  # Don't require --- at start
```

**Customize rules:**
Edit `.yamllint` to adjust strictness.

**Disable rules for specific files:**

```yaml
# In .yamllint, add to ignore:
ignore: |
  .git/
  .storage/
  specific_file.yaml  # Add files to ignore
```

**Disable rules inline:**

```yaml
# In YAML file, disable specific rule
# yamllint disable-line rule:line-length
very_long_line_that_exceeds_limit: "this is okay now"

# Or disable for entire file
# yamllint disable
# ... rest of file
```

### Home Assistant Validation

**What it checks:**
- YAML syntax errors
- Invalid configuration keys
- Missing required fields
- Integration configuration issues
- Template syntax errors

**What it DOESN'T check:**
- Runtime logic errors
- Automation timing issues
- Integration connectivity (no network access)
- Custom component functionality

**Limitations:**
- Uses dummy secrets (can't validate actual API connections)
- No access to actual devices
- Some platform-specific checks may fail

**To skip validation for specific changes:**

Add to commit message:
```bash
git commit -m "docs: update README

[skip ci]"
```

This skips ALL workflows for this commit (use sparingly!)

---

## Troubleshooting

### Workflow Fails on YAML Lint

**Common issues:**

1. **Line too long**
   ```
   error: line too long (210 > 200 characters)
   ```
   **Fix:** Break line or increase limit in `.yamllint`

2. **Trailing spaces**
   ```
   error: trailing spaces
   ```
   **Fix:** Remove spaces at end of lines

3. **Indentation error**
   ```
   error: wrong indentation: expected 2 but found 4
   ```
   **Fix:** Use 2 spaces for indentation

4. **Truthy values**
   ```
   error: truthy value should be 'true' or 'false'
   ```
   **Fix:** Already allowed in our config, but can use true/false explicitly

### Workflow Fails on HA Validation

**Common issues:**

1. **Missing secrets**
   ```
   error: Secret 'xyz' not found
   ```
   **Fix:** Add to `secrets.yaml.example`

2. **Invalid entity_id**
   ```
   error: Entity ID 'sensor.invalid..name' is invalid
   ```
   **Fix:** Use valid entity_id format

3. **Unknown integration**
   ```
   error: Integration 'custom_integration' not found
   ```
   **Fix:** May fail for custom components (this is expected)

4. **Template errors**
   ```
   error: Invalid template
   ```
   **Fix:** Check Jinja2 template syntax

### Workflow Doesn't Run

**Check:**

1. **Actions enabled?**
   - GitHub repo → Settings → Actions → Allow all actions

2. **Correct file paths?**
   - Workflows must be in `.github/workflows/`
   - Files must end in `.yml` or `.yaml`

3. **Triggered correctly?**
   - Check `on:` section matches your branch/file changes
   - View "Actions" tab to see if workflow was triggered

4. **Permissions?**
   - Repo → Settings → Actions → Workflow permissions
   - Should be "Read and write permissions"

### View Workflow Logs

1. Go to repository → Actions tab
2. Click on workflow run
3. Click on job (e.g., "YAML Lint Check")
4. Expand steps to see detailed logs
5. Look for errors in red

---

## Advanced Usage

### Add More Checks

**Example: Check for secrets exposure**

Create `.github/workflows/security-check.yml`:

```yaml
name: Security Check

on: [pull_request, push]

jobs:
  check-secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for exposed secrets
        run: |
          if grep -r "password\|token\|api_key" --exclude-dir=.git --exclude="secrets.yaml.example" .; then
            echo "❌ Potential secret exposure detected!"
            exit 1
          else
            echo "✅ No secrets detected"
          fi
```

### Add Status Badge to README

Add to `README.md`:

```markdown
[![YAML Lint](https://github.com/username/repo/workflows/YAML%20Lint/badge.svg)](https://github.com/username/repo/actions)
[![HA Validate](https://github.com/username/repo/workflows/Home%20Assistant%20Config%20Validation/badge.svg)](https://github.com/username/repo/actions)
```

Replace `username/repo` with your actual GitHub username and repository name.

### Run Workflows on Schedule

Add to workflow:

```yaml
on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday at midnight
  pull_request:
    # ... existing triggers
```

### Matrix Testing (Multiple HA Versions)

```yaml
jobs:
  validate:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        ha-version: ['stable', 'beta', 'dev']
    steps:
      # ... existing steps
      - name: Home Assistant Check
        uses: frenck/action-home-assistant@v1.4
        with:
          version: ${{ matrix.ha-version }}
```

---

## Best Practices

### Before Creating PR

```bash
# 1. Run local checks
yamllint .
ha core check

# 2. Fix any errors
# ... make fixes

# 3. Commit and push
git add .
git commit -m "fix: resolve linting errors"
git push

# 4. Create PR (workflows run automatically)
```

### During Code Review

- Don't merge if workflows fail (red X)
- Review workflow logs for errors
- Fix errors in feature branch
- Push fixes (workflows run again)
- Merge when all checks pass (green checkmark)

### After Merge

- Workflows run again on master branch
- Monitor for any issues
- If failures on master, create hotfix branch

---

## Maintenance

### Update yamllint Rules

```bash
# Edit configuration
vim .yamllint

# Test locally
yamllint .

# Commit changes
git add .yamllint
git commit -m "chore: update yamllint rules"
git push
```

### Update Workflows

```bash
# Edit workflow
vim .github/workflows/yaml-lint.yml

# Commit changes
git add .github/workflows/
git commit -m "ci: update GitHub Actions workflow"
git push
```

### Keep Actions Up to Date

**Check for updates:**
- actions/checkout: https://github.com/actions/checkout/releases
- actions/setup-python: https://github.com/actions/setup-python/releases
- frenck/action-home-assistant: https://github.com/frenck/action-home-assistant/releases

**Update in workflows:**
```yaml
- uses: actions/checkout@v4  # Update version number
```

---

## Summary

### What You Now Have

✅ **Automated YAML linting** on every PR
✅ **Home Assistant config validation** before merge
✅ **Prevents broken configs** from reaching production
✅ **Consistent code style** across all files
✅ **Professional CI/CD workflow**

### Typical Workflow

```
1. Create feature branch
2. Make changes
3. Push to GitHub
4. Create Pull Request
   ↓
5. GitHub Actions run automatically
   ├─ YAML Lint ✅
   └─ HA Validate ✅
   ↓
6. All checks pass → Merge PR
7. Deploy to production (manual or automated)
```

### Next Steps

1. ✅ Workflows are created and configured
2. ⏳ Commit and push to GitHub
3. ⏳ Create test PR to verify workflows
4. ⏳ Add status badges to README (optional)
5. ⏳ Train team on workflow (if applicable)

---

**Created:** 2025-11-16
**Status:** Ready to use - Just commit and push!
**Testing:** Create a test PR to verify workflows work correctly
