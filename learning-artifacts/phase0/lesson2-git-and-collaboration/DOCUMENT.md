# Git and Collaboration

## What is a repository?

A repository, or repo, is a folder that Git tracks. It contains project files and their change history.

Git records changes on your computer. GitHub hosts a copy online. Git calls that online copy a remote repository.

## Where your changes go

| Place | What it means |
|---|---|
| Working directory | The files you edit. |
| Staging area | The changes you selected for the next commit. |
| Local repository | The commits saved on your computer. |
| Remote repository | The commits you uploaded to GitHub. |

The usual workflow moves changes from your working directory to the staging area, then to a local commit, and finally to GitHub.

```bash
git status
git add LEARNING.md
git commit -m "Record lesson progress"
git push origin main
```

`git status` lists changed and untracked files. `git add` selects changes for a commit. `git commit` saves those changes in your local repository. `git push` uploads commits to GitHub.

A commit stays on your computer until you push it. Staged changes are not on GitHub until you commit and push them.

## Branches

A branch is a named line of work. Use a branch to make changes without moving `main`.

Create a branch and switch to it with:

```bash
git checkout -b experiment/new-optimizer
```

Commits made on this branch move it forward. They do not move `main`. Switch back to `main` and merge the branch when you want to include its changes:

```bash
git checkout main
git merge experiment/new-optimizer
```

## The `.gitignore` file

The `.gitignore` file tells Git which untracked files to leave out. This keeps generated files, local tools, and large model files out of your commits.

```gitignore
.venv/
__pycache__/
node_modules/
/target/
*.pt
*.pth
*.safetensors
```

Git patterns are case-sensitive. For example, `*.pt` matches `model.pt`, but it does not match `model.PT`.

Use `git check-ignore -v` to see which rule ignores a path:

```bash
git check-ignore -v example.pt example.pth example.safetensors
```

Adding a pattern does not stop Git from tracking a file that is already tracked.

## Read the commit history

Use these commands to inspect project history:

```bash
git log --oneline
git log --oneline -- phases/00-setup-and-tooling
git show --stat 2b62eda33
```

`git log --oneline` lists commits in a compact form. Adding a path limits the list to commits that changed that path. `git show --stat` lists the files changed by one commit.

## What I practiced

- I checked that the `.pt`, `.pth`, and `.safetensors` patterns match example files.
- I read the Phase 0 commit history and inspected the commit that added this lesson.
- I scored 3/3 on the lesson quiz.

Next, create a branch, commit a small change, and push it to your own GitHub repository.
