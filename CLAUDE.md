# Claude Code Instructions for this Repository

## Git Workflow - MANDATORY

**ALWAYS follow this workflow for ANY code changes:**

1. Create a new branch from master before making changes
2. Make the changes on the new branch
3. Commit with a descriptive message
4. Push the branch to GitHub
5. Create a Pull Request using `gh pr create`
6. Merge the Pull Request into `master`
7. Let the Home Assistant Git Pull app pull the merged `master` commit onto the live `/homeassistant` checkout

**NEVER commit directly to master.**

**NEVER edit files directly in the live `/homeassistant` checkout for code/config changes.** Direct live edits dirty the working tree and can block the Git Pull app with `cannot pull with rebase: You have unstaged changes`. Use the PR workflow above, then trigger or wait for the Git Pull app.

Only inspect the live checkout with read-only commands such as `git status`, `git diff`, and entity/config reads unless the explicit task is to recover from a dirty working tree.

Example workflow:
```bash
git checkout -b descriptive-branch-name
# make changes
git add <files>
git commit -m "type: description"
git push -u origin descriptive-branch-name
gh pr create --title "type: description" --body "..."
```
