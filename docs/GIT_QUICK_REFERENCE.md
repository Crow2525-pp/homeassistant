# Git Workflow Quick Reference

**For your Home Assistant configuration - quick commands**

---

## 🚀 One-Time Setup

```bash
# Install pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install

# Verify it's working
pre-commit run --all-files
```

---

## 📋 Typical Workflow

### 1️⃣ Start a new feature

```bash
# Get latest changes from main branch
git checkout master
git pull origin master

# Create feature branch (use descriptive name)
git checkout -b feature/my-new-feature
```

**Branch naming:** `feature/`, `bugfix/`, `hotfix/`, `docs/`, `refactor/`, `test/`

Examples:
- `feature/add-rfid-tracking`
- `bugfix/fix-light-entity`
- `docs/update-morning-routine`

---

### 2️⃣ Make your changes

Edit your YAML files as usual.

**Before committing:**
```bash
# Check YAML syntax
yamllint config/ automations/ lovelace/

# Run pre-commit checks
pre-commit run --all-files
```

---

### 3️⃣ Commit your changes

```bash
# Stage your changes
git add .

# Commit with proper message
git commit -m "feat: add morning routine automation

- Add 5:30 AM preheat trigger
- Use climate preset mode
- Create helper input selectors

Closes #12"
```

**Commit types:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`

---

### 4️⃣ Push to GitHub

```bash
# Push your branch
git push -u origin feature/my-new-feature
```

---

### 5️⃣ Create Pull Request

**Option A: Via GitHub web interface**
1. Go to https://github.com/Crow2525-pp/homeassistant
2. Click "Pull Requests" > "New pull request"
3. Set base: `master`, compare: `feature/my-new-feature`
4. Fill in description and submit

**Option B: Via GitHub CLI**
```bash
gh pr create --base master --head feature/my-new-feature \
  --title "feat: add morning routine automation" \
  --body "- Add preheat at 5:30 AM\n- Use climate presets\n- Closes #12"
```

---

### 6️⃣ Automated checks run

GitHub will automatically:
- ✅ Run yamllint (YAML syntax)
- ✅ Run ha-validate (Home Assistant config check)
- ✅ Run entity-validate (entity reference check)

**If checks fail:** Fix the issues, commit, and push again. PR updates automatically.

---

### 7️⃣ Merge and cleanup

Once all checks pass:
```bash
# Merge via GitHub web interface, or use CLI:
gh pr merge feature/my-new-feature --squash

# Delete local branch
git branch -d feature/my-new-feature
```

---

## 📊 Common Commands

```bash
# See what branch you're on
git branch

# See all branches
git branch -a

# Switch branches
git checkout master
git checkout feature/my-feature

# See your changes before committing
git status          # What files changed
git diff            # What lines changed

# Undo uncommitted changes
git checkout -- filename.yaml

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Update your branch with latest master
git fetch origin
git merge origin/master
```

---

## 🚨 Common Mistakes & Fixes

### Committed to master by accident?

```bash
# Create branch from current master
git branch feature/oops-my-feature

# Reset master to before your commit
git checkout master
git reset --soft HEAD~1  # Keep your changes

# Switch to your feature branch
git checkout feature/oops-my-feature
git commit -m "feat: actual commit message"
git push -u origin feature/oops-my-feature
```

### Want to update your branch with latest master?

```bash
git fetch origin
git merge origin/master

# If conflicts, fix them and:
git add .
git commit -m "chore: merge latest master"
git push
```

### Push to wrong branch?

```bash
# If already pushed, create correct branch:
git checkout -b feature/correct-name
git push -u origin feature/correct-name

# Delete wrong branch
git push origin :feature/wrong-name
```

---

## ✅ Checklist Before Pushing

- [ ] Branch created from latest `master`
- [ ] Changes test locally (no HA errors)
- [ ] yamllint passes: `yamllint config/ automations/ lovelace/`
- [ ] No secrets committed: `grep -r "password\|token\|api_key" config/ automations/`
- [ ] Commit message follows format: `type: description`
- [ ] Code follows existing patterns in your config
- [ ] Entity IDs exist (check ENTITY_LIST.md)

---

## 📝 Full Documentation

For more details, see:
- **Full workflow:** `CONTRIBUTING.md`
- **Git setup:** `docs/GIT_WORKFLOW_SETUP.md`
- **YAML style:** `docs/YAML_LINTING_GUIDE.md`

---

## 🎯 For You Right Now

**Next steps:**
1. Install pre-commit hooks (one-time, 2 minutes)
2. Create a test branch: `git checkout -b feature/test-workflow`
3. Make a small change (like updating a comment)
4. Commit and push it
5. Create a PR on GitHub
6. Watch the checks run automatically
7. Merge it

This way you'll see the whole workflow in action with zero risk.
