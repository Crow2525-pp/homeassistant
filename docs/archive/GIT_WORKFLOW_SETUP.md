# Git Workflow & Version Control Setup Guide

**Created:** 2025-11-17
**Purpose:** Set up professional git workflow for Home Assistant configuration
**Complexity:** Medium (30-45 minutes)
**Category:** Development Setup

---

## Overview

This guide establishes a professional git workflow for your Home Assistant configuration, including version control, code quality checks, and automated validation. You'll set up pre-commit hooks to catch errors before they reach your production system.

**Benefits:**
- Track all configuration changes with git history
- Automatic YAML validation before commits
- Rollback capability if changes break your system
- Collaboration support (multiple contributors)
- GitHub Actions CI/CD for automated testing
- Professional development workflow

**What you'll set up:**
1. Git repository with proper .gitignore
2. Branch protection and naming conventions
3. Pre-commit hooks for YAML linting
4. GitHub Actions for automated validation
5. Pull request workflow

---

## Prerequisites

- Git installed on your system (`git --version`)
- GitHub account (for remote repository and CI/CD)
- Home Assistant configuration directory access
- Basic command line knowledge
- Terminal/SSH access to HA system

**Estimated Time:** 30-45 minutes

---

## Step 1: Verify .gitignore is Configured

Your repository already has a `.gitignore` file. Verify it excludes sensitive data:

### Check Current .gitignore

```bash
cat .gitignore
```

The file should exclude:
- `secrets.yaml` (contains passwords, API keys)
- `*.db*` (database files)
- `.storage/` (internal HA storage)
- `deps/` (dependencies)
- `*.backup` (backup files)

### Current .gitignore Status

Your `.gitignore` is already properly configured and includes:
- Whitelist approach (ignore everything, then include specific files)
- Secrets protection (`secrets.yaml`, `esphome/secrets.yaml`)
- Database exclusions (`*.db`, `*.db-shm`, `*.db-wal`)
- Proper includes for config, automations, docs, lovelace

**Action:** No changes needed. Your `.gitignore` is properly configured.

---

## Step 2: Initialize Git Repository (if not done)

### Check if Git is Already Initialized

```bash
git status
```

If you see "fatal: not a git repository", initialize:

```bash
cd /config  # or your HA config directory
git init
git branch -M master  # or main, depending on preference
```

**Note:** Based on your git status, your repository is already initialized on the `master` branch.

---

## Step 3: Set Up Branch Strategy

### Branch Naming Convention

Use descriptive branch names following this pattern:

- `feature/description` - New features or enhancements
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `hotfix/description` - Urgent production fixes

### Create Development Branch

```bash
# Ensure you're on master
git checkout master

# Create and switch to development branch
git checkout -b development

# Push to remote (if using GitHub)
git push -u origin development
```

### Example Workflow

```bash
# Create a feature branch from development
git checkout development
git pull origin development
git checkout -b feature/morning-routine-automation

# Make your changes...

# Commit changes
git add automations/morning_routine.yaml
git commit -m "feat: add morning preheat automation"

# Push feature branch
git push -u origin feature/morning-routine-automation

# Create Pull Request on GitHub to merge into development
# After review and approval, merge to development
# Periodically merge development → master for releases
```

---

## Step 4: Install and Configure Pre-commit Hooks

Pre-commit hooks run automated checks before allowing a git commit. This catches errors early.

### Install Pre-commit

**Option A: Via pip (Python)**

```bash
pip install pre-commit
```

**Option B: Via Home Assistant Add-on (if available)**

Some HA installations have pre-commit available via add-ons.

**Option C: Use GitHub Actions only**

If you can't install pre-commit locally, skip to Step 5 for GitHub Actions setup.

### Configure Pre-commit Hooks

The pre-commit configuration is already created at `.pre-commit-config.yaml`. Verify it exists:

```bash
cat .pre-commit-config.yaml
```

### Install Pre-commit Git Hooks

```bash
# Install the git hooks
pre-commit install

# Test the hooks
pre-commit run --all-files
```

This will:
1. Check YAML syntax with yamllint
2. Trim trailing whitespace
3. Fix end-of-file formatting
4. Check for large files
5. Validate YAML formatting

### Manual Validation (Without Pre-commit Installation)

If you can't install pre-commit, manually validate before commits:

```bash
# YAML linting
yamllint config/ automations/ lovelace/

# Home Assistant config check
ha core check
```

---

## Step 5: Set Up GitHub Actions CI/CD

Your repository already has GitHub Actions configured. Let's verify and understand them.

### Current GitHub Actions Workflows

**File 1: `.github/workflows/ha-validate.yml`**
- **Purpose:** Validates Home Assistant configuration
- **Runs:** On every push and pull request
- **What it does:**
  1. Sets up Python environment
  2. Generates dummy `secrets.yaml` for testing
  3. Runs `hass --script check_config`
  4. Fails if configuration is invalid

**File 2: `.github/workflows/yaml-lint.yml`**
- **Purpose:** Validates YAML syntax
- **Runs:** On every push and pull request
- **What it does:**
  1. Sets up yamllint
  2. Checks all YAML files for syntax errors
  3. Fails if linting errors found

### Triggering Workflows Manually (from Claude Code / Remote)

When working from a remote environment (Claude Code, Codex online), trigger workflows manually:

```bash
# Trigger HA validation workflow
gh workflow run ha-validate.yml --ref feature/your-branch

# Trigger YAML linting workflow
gh workflow run yaml-lint.yml --ref feature/your-branch

# Check workflow status
gh run list --workflow=ha-validate.yml
gh run list --workflow=yaml-lint.yml

# View workflow logs
gh run view <run-id> --log
```

### LLM Runbook for CI/CD (Claude Code Reference)

When working from Claude Code or similar hosted LLM:

**Before Pushing Changes:**
1. Ensure all files are saved
2. Run local validation: `ha core check` (if available)
3. Commit and push to feature branch
4. Trigger workflows manually if not auto-triggered

**After Pushing:**
1. Verify workflows triggered: `gh run list`
2. Monitor workflow status: `gh run view <run-id>`
3. If workflow fails, review logs: `gh run view <run-id> --log`
4. Fix errors and push again
5. Once workflows pass, create or update pull request

**Creating Pull Request:**
```bash
gh pr create --title "feat: add morning routine" --body "Description of changes"
```

**Checking PR Status:**
```bash
gh pr status
gh pr checks  # View all required checks
```

---

## Step 6: Configure Branch Protection (Optional but Recommended)

Set up branch protection on GitHub to enforce quality checks.

### Via GitHub Web UI:

1. Go to repository on GitHub
2. **Settings** > **Branches**
3. Click **Add rule** under "Branch protection rules"
4. Branch name pattern: `master` (or `main`)
5. Enable:
   - ✓ Require pull request reviews before merging
   - ✓ Require status checks to pass before merging
     - Select: `YAML Lint`, `Home Assistant Config Check`
   - ✓ Require branches to be up to date before merging
   - ✓ Include administrators (optional)
6. Click **Create**

### Via GitHub CLI:

```bash
# Protect master branch
gh api repos/:owner/:repo/branches/master/protection \
  --method PUT \
  -f required_status_checks[strict]=true \
  -f required_status_checks[contexts][]=YAML\ Lint \
  -f required_status_checks[contexts][]=Home\ Assistant\ Config\ Check \
  -f enforce_admins=false \
  -f required_pull_request_reviews[required_approving_review_count]=0
```

**Result:** Master branch cannot be directly committed to. All changes must go through pull requests with passing CI checks.

---

## Step 7: Commit Message Convention

Use conventional commit format for clarity and automatic changelog generation:

### Format

```
<type>: <short description>

[optional body]

[optional footer]
```

### Types

- `feat:` - New feature or enhancement
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code restructuring (no functional changes)
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks, dependency updates
- `style:` - Formatting, whitespace (no logic changes)

### Examples

```bash
# Feature addition
git commit -m "feat: add morning preheat automation with preset selection"

# Bug fix
git commit -m "fix: correct bedroom light entity in morning routine"

# Documentation
git commit -m "docs: add setup guide for RFID filter tracking"

# Refactoring
git commit -m "refactor: split climate automation into focused modules"

# With body and footer
git commit -m "feat: implement automated backup system

- Daily backups at 3 AM
- Notification on success/failure
- Retention policy: 7 daily, 4 weekly

Closes #42"
```

---

## Step 8: Pull Request Workflow

### Creating a Pull Request

**Via GitHub CLI:**

```bash
# From your feature branch
git checkout feature/morning-routine
git push -u origin feature/morning-routine

# Create PR
gh pr create \
  --title "feat: add morning routine automation" \
  --body "## Changes
- Added morning preheat automation (5:30 AM)
- Added morning lighting automation (5:00 AM)
- Added motion-based kitchen routine
- Created input helpers for configuration

## Testing
- [x] Config check passes
- [x] YAML lint passes
- [x] Tested on development instance
- [ ] Monitored for 1 week (pending)

## Checklist
- [x] Documentation updated
- [x] No secrets committed
- [x] Follows naming conventions
" \
  --base development \
  --head feature/morning-routine
```

**Via GitHub Web UI:**

1. Push your feature branch: `git push -u origin feature/morning-routine`
2. Go to repository on GitHub
3. Click **Pull requests** > **New pull request**
4. Base: `development`, Compare: `feature/morning-routine`
5. Fill in title and description (use template below)
6. Click **Create pull request**

### Pull Request Template

Save as `.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Description
Brief description of changes

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

## Documentation
- [ ] Updated relevant documentation
- [ ] Added inline comments where needed
- [ ] Updated entity inventory (if applicable)

## Checklist
- [ ] No secrets committed
- [ ] Follows naming conventions
- [ ] Follows commit message convention
- [ ] Branch is up to date with base
```

### Auto-merge When Checks Pass

Enable auto-merge for pull requests:

```bash
# Enable auto-merge for a PR
gh pr merge <PR-number> --auto --squash

# PR will merge automatically when:
# 1. All required checks pass
# 2. Required reviews are approved (if configured)
```

---

## Step 9: Handling Merge Conflicts

When your branch conflicts with the base branch:

### Resolve Conflicts

```bash
# Update your feature branch with latest base
git checkout feature/your-branch
git fetch origin
git merge origin/development

# Git will show conflicts - resolve them manually
# Edit conflicting files, keeping desired changes

# Mark as resolved
git add <conflicted-files>
git commit -m "fix: resolve merge conflicts with development"
git push
```

### Avoid Conflicts

- Keep feature branches short-lived (merge within days)
- Pull latest changes frequently
- Coordinate with other contributors on overlapping files

---

## Step 10: Testing & Validation Checklist

Before merging any changes, verify:

### Local Validation

```bash
# 1. YAML syntax check
yamllint config/ automations/ lovelace/

# 2. Home Assistant config check
ha core check

# 3. Check for secrets
grep -r "password" config/ automations/  # Should be empty
grep -r "api_key" config/ automations/   # Should be empty

# 4. Review changes
git diff master...HEAD
```

### Remote Validation (GitHub Actions)

```bash
# Check workflow status
gh run list --limit 5

# View workflow details
gh run view <run-id>

# Download workflow logs
gh run view <run-id> --log > workflow-log.txt
```

### Manual Testing

- [ ] Restart Home Assistant: `ha core restart`
- [ ] Monitor logs: `ha core logs -f`
- [ ] Test affected automations manually
- [ ] Verify dashboard displays correctly
- [ ] Check entities are available

---

## Troubleshooting

### Pre-commit Fails on Every Commit

**Symptom:** Pre-commit hooks reject all commits even after fixing issues.

**Solutions:**
1. Update pre-commit: `pre-commit autoupdate`
2. Clear cache: `pre-commit clean`
3. Re-install hooks: `pre-commit install`
4. Skip hook temporarily (emergency only): `git commit --no-verify`

### GitHub Actions Fails with "secrets.yaml not found"

**Symptom:** HA validation workflow fails because `secrets.yaml` doesn't exist.

**Solution:**
The workflow should auto-generate dummy secrets. Verify `.github/workflows/ha-validate.yml` contains:

```yaml
- name: Create dummy secrets
  run: |
    echo "# Dummy secrets for CI" > secrets.yaml
    echo "http_password: test123" >> secrets.yaml
    # Add other required secrets here
```

### Merge Conflicts Every Time

**Symptom:** Frequent merge conflicts when merging to development/master.

**Solutions:**
1. Pull often: `git pull origin development` before starting new work
2. Keep branches small and focused
3. Use shorter-lived feature branches
4. Coordinate with team on overlapping files

### CI Passes But Config Fails on Real System

**Symptom:** GitHub Actions shows green checkmark but HA fails on restart.

**Possible causes:**
1. Integration-specific issues (external services, devices)
2. Missing secrets in production
3. Different HA versions (CI vs production)

**Solutions:**
1. Test on development HA instance before production
2. Match HA versions in CI (update workflow)
3. Use staging environment for integration testing

---

## Maintenance

### Weekly Tasks

- [ ] Review open pull requests
- [ ] Merge development → master (release)
- [ ] Clean up merged feature branches: `git branch -d feature/old-branch`
- [ ] Review GitHub Actions logs for warnings

### Monthly Tasks

- [ ] Update pre-commit hooks: `pre-commit autoupdate`
- [ ] Review and clean git history: `git log --oneline --graph`
- [ ] Audit .gitignore (ensure no secrets leaked)
- [ ] Review branch protection rules

### Quarterly Tasks

- [ ] Audit entire repository for sensitive data
- [ ] Update GitHub Actions workflow versions
- [ ] Review and update CONTRIBUTING.md
- [ ] Archive/delete stale branches

---

## Advanced Workflows

### Hotfix Workflow (Emergency Production Fix)

```bash
# Create hotfix branch from master
git checkout master
git checkout -b hotfix/critical-fix

# Make minimal changes
# ... edit files ...

# Commit with descriptive message
git commit -m "hotfix: fix critical automation error causing restart loop"

# Push and create PR to master
git push -u origin hotfix/critical-fix
gh pr create --base master --head hotfix/critical-fix

# After merge, backport to development
git checkout development
git merge master
git push origin development
```

### Release Workflow

```bash
# When ready to release development → master
git checkout master
git pull origin master
git merge development --no-ff -m "release: merge development for v1.2.0"

# Tag release
git tag -a v1.2.0 -m "Release version 1.2.0 - Morning routines & backup"
git push origin master --tags

# Create GitHub release
gh release create v1.2.0 --title "v1.2.0 - Morning Routines" --notes "Release notes here"
```

---

## Next Steps

After completing git setup:

1. **Create first commit:**
   ```bash
   git add .
   git commit -m "docs: add git workflow and automation templates"
   git push origin master
   ```

2. **Set up development workflow:**
   - Create development branch
   - Create first feature branch
   - Make a test change
   - Submit pull request
   - Verify CI/CD runs successfully

3. **Train team members:**
   - Share this guide
   - Review commit message conventions
   - Demonstrate pull request workflow

4. **Monitor and refine:**
   - Review CI/CD logs weekly
   - Adjust yamllint rules if needed
   - Update documentation as workflow evolves

---

## Related Documentation

- `.gitignore` - Repository file exclusions
- `.pre-commit-config.yaml` - Pre-commit hook configuration
- `.github/workflows/ha-validate.yml` - HA validation workflow
- `.github/workflows/yaml-lint.yml` - YAML linting workflow
- `CONTRIBUTING.md` - Contribution guidelines
- `docs/YAML_LINTING_GUIDE.md` - YAML style guide

---

## Rollback Plan

If git workflow causes issues:

1. **Disable pre-commit hooks:**
   ```bash
   pre-commit uninstall
   ```

2. **Bypass GitHub Actions:**
   - Temporarily disable workflows in GitHub settings
   - Or use `[skip ci]` in commit messages

3. **Emergency direct commit to master:**
   ```bash
   git checkout master
   git add <files>
   git commit -m "hotfix: emergency fix [skip ci]"
   git push origin master
   ```

4. **Restore to known good state:**
   ```bash
   git log  # Find last known good commit
   git reset --hard <commit-hash>
   git push --force origin master  # CAUTION: Use only in emergency
   ```

---

**Status:** Template ready for deployment
**Last Updated:** 2025-11-17
