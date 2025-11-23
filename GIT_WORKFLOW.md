# Complete Git Workflow with Automated PR & Merge

This document shows the complete workflow for creating, testing, and merging PRs in Claude Code.

## Prerequisites

- `gh` (GitHub CLI) installed: `https://cli.github.com/`
- Authenticated to GitHub: `gh auth login`
- Local repository set up with proper remotes

## Step-by-Step Workflow

### 1. Create Feature Branch and Make Changes

```bash
# Start from master
git checkout master
git pull GitHub master  # Note: remote is "GitHub" not "origin"

# Create feature branch (use descriptive names)
git checkout -b fix/my-bug-fix
# or: git checkout -b feat/new-feature

# Make your changes...
# Edit files as needed
```

### 2. Commit with Clear Message

```bash
# Stage and commit changes
git add .
git commit -m "fix: describe what you fixed

Explain why this change was needed, what problem it solves.

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"

# Verify commit
git log --oneline -1
```

### 3. Push to GitHub and Create PR

```bash
# Push feature branch to GitHub
git push -u GitHub <branch-name>

# Create PR using GitHub CLI
gh pr create --title "Fix: Brief description" \
  --body "## Summary
- What changed
- Why it changed

## Test plan
- [ ] Test item 1
- [ ] Test item 2" \
  --base master
```

**Manual PR Creation** (if `gh` is not available):
1. Go to: `https://github.com/Crow2525-pp/homeassistant/`
2. Click "New pull request"
3. Compare: `fix/my-bug-fix` → `master`
4. Add title and description
5. Create pull request

### 4. Wait for Tests to Pass

Automated tests run on all PRs via GitHub Actions.

**Check test status:**
```bash
# Check PR status and test results
gh pr view

# Watch test results
gh pr checks --watch
```

**Manual check:**
- Go to your PR on GitHub
- Scroll down to see "Checks" section
- Wait for all tests to turn green ✓

### 5. Squash Merge Once Tests Pass

Once tests pass and you're ready to merge:

```bash
# Squash merge closes the PR and cleans up commit history
gh pr merge --squash

# Or specify the merge message
gh pr merge --squash \
  --subject "fix: human-readable commit message" \
  --body "Optional detailed description"
```

**Manual merge:**
1. Go to your PR on GitHub
2. Click "Squash and merge" button
3. Confirm merge
4. Delete branch (optional)

### 6. Clean Up Local Branch

```bash
# Switch back to master
git checkout master

# Pull merged changes
git pull GitHub master

# Delete local feature branch
git branch -d fix/my-bug-fix
```

## Full Example

```bash
# 1. Create branch
git checkout master
git pull GitHub master
git checkout -b fix/automation-entity-reference

# 2. Make changes to automations/05a_lighting.yaml...

# 3. Commit
git add .
git commit -m "fix: correct automation entity reference

Changed the workday desk routine to use the computer
power outlet instead of the desk light."

# 4. Push and create PR
git push -u GitHub fix/automation-entity-reference
gh pr create --title "Fix: Correct automation entity reference" \
  --body "Fixes the workday routine to control the right device" \
  --base master

# 5. Wait for tests (watch on GitHub or use: gh pr checks --watch)

# 6. Merge when ready
gh pr merge --squash

# 7. Clean up
git checkout master
git pull GitHub master
git branch -d fix/automation-entity-reference
```

## Current PR Status

Your recent PR:
- **Branch:** `fix/computer-plug-automation`
- **Base:** `master`
- **Changes:**
  - `automations/05a_lighting.yaml` - Fixed entity reference
  - `CONTRIBUTING.md` - Added workflow documentation

**Next steps:**
1. Create the PR manually at: https://github.com/Crow2525-pp/homeassistant/pull/new/fix/computer-plug-automation
2. Or install `gh` CLI and use: `gh pr create --title "..." --base master`
3. Wait for tests to pass
4. Merge with: `gh pr merge --squash`

## Key Points

- ✅ One feature per branch - keeps history clean
- ✅ Clear commit messages - explain the "why"
- ✅ Squash merge - one commit per feature to master
- ✅ Test before merge - automated checks catch issues
- ✅ Delete old branches - keep repo clean

## Common Commands Reference

```bash
# View current branch status
git status

# List all branches
git branch -a

# Switch branches
git checkout <branch-name>

# Create and switch in one command
git checkout -b <new-branch-name>

# Delete local branch
git branch -d <branch-name>

# View PR details
gh pr view

# Watch test results
gh pr checks --watch

# Merge with squash
gh pr merge --squash

# Merge with rebase
gh pr merge --rebase

# Close PR without merging
gh pr close
```
