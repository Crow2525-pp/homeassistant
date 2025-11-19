# Contributing Guidelines

## Git Workflow

This project follows a standard feature-branch workflow with pull requests. All new work must be done in dedicated branches and reviewed via pull requests before merging to the main branch.

### Standard Workflow

1. **Create a new branch** for each feature/fix
   - Branch from `master` (the main branch)
   - Use descriptive branch names: `feat/feature-name` or `fix/bug-description`
   - Example: `fix/computer-plug-automation`, `feat/add-climate-control`

2. **Make your changes** in the feature branch
   - Keep changes focused and related to the branch purpose
   - Write clear commit messages

3. **Commit and push** your changes
   ```bash
   git add .
   git commit -m "description of changes"
   git push -u origin <branch-name>
   ```

4. **Create a Pull Request**
   - Push to GitHub and create a PR (use `gh pr create`)
   - PR should reference any related issues
   - Automated tests run on all PRs

5. **Review tests and merge**
   - Wait for automated tests to pass (GitHub Actions)
   - Once tests pass, squash merge to `master` to keep commit history clean
   - Close the PR automatically on merge

### Example Workflow in Practice

```bash
# Create and switch to a new feature branch from master
git checkout master
git pull origin master
git checkout -b fix/my-bug-fix

# Make changes and commit
git add .
git commit -m "fix: correct entity reference in automation"

# Push to GitHub and create PR
git push -u origin fix/my-bug-fix
gh pr create --title "Fix: Correct entity reference in automation" --body "..."

# Wait for tests to pass, then squash merge
gh pr merge --squash
```

## One Feature/Branch Rule

**Important:** Never mix unrelated changes in the same branch. This ensures:
- Easier code review
- Cleaner commit history
- Simpler rollbacks if needed
- Clear separation of concerns

If you need to work on multiple things, create separate branches for each:
- ❌ Bad: Mix bug fixes, new features, and refactoring in one branch
- ✅ Good: Separate branches for each logical unit of work

## Automated Merge Workflow

Once a PR is created and tests pass, the merge can be automated from Claude Code:
- Tests run automatically via GitHub Actions
- Poll test results using `gh pr view`
- Squash merge once all tests pass using `gh pr merge --squash`
- PR closes automatically

This keeps the workflow streamlined and the commit history clean.

## Commit Message Format

Use clear, descriptive commit messages that explain the "why":
- `feat: add new feature description`
- `fix: correct entity reference in automation`
- `docs: update README with installation steps`
- `refactor: simplify automation logic`
- `test: add tests for X functionality`

## Questions?

If you need help with the git workflow or have questions about branch strategy, ask in your Claude Code session.
