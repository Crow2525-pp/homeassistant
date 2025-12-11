# Claude Code Instructions for this Repository

## Git Workflow - MANDATORY

**ALWAYS follow this workflow for ANY code changes:**

1. Create a new branch from master before making changes
2. Make the changes on the new branch
3. Commit with a descriptive message
4. Push the branch to GitHub
5. Create a Pull Request using `gh pr create`

**NEVER commit directly to master.**

Example workflow:
```bash
git checkout -b descriptive-branch-name
# make changes
git add <files>
git commit -m "type: description"
git push -u origin descriptive-branch-name
gh pr create --title "type: description" --body "..."
```
