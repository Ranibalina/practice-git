# Git Commands: Basic to Advanced

A comprehensive guide to Git commands organized by skill level and use case.

---

## Table of Contents
- [Getting Started](#getting-started)
- [Basic Commands](#basic-commands)
- [Branching & Merging](#branching--merging)
- [Remote Repositories](#remote-repositories)
- [Intermediate Commands](#intermediate-commands)
- [Advanced Commands](#advanced-commands)
- [Troubleshooting & Recovery](#troubleshooting--recovery)
- [Advanced Workflows](#advanced-workflows)

---

## Getting Started

### Initial Configuration
```bash
# Set your identity
git config --global user.name "Ranibalina"
git config --global user.email "ranibalina1@gmail.com"

# Set default branch name
git config --global init.defaultBranch jansi

# Set default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim

# View all configuration
git config --list
git config --global --list
```

### Create a Repository
```bash
# Initialize a new Git repository
git init

# Clone an existing repository
git clone <repository-url>
git clone <repository-url> <directory-name>

# Clone with specific branch
git clone -b <branch-name> <repository-url>

# Shallow clone (limited history)
git clone --depth 1 <repository-url>
```

---

## Basic Commands

### Checking Status & History
```bash
# Check repository status
git status
git status -s  # Short format

# View commit history
git log
git log --oneline
git log --oneline --graph --all
git log --author="Name"
git log --since="2 weeks ago"
git log --until="2024-01-01"
git log -n 5  # Last 5 commits
git log --stat  # With file statistics
git log -p  # With diff

# Show specific commit
git show <commit-hash>
git show HEAD
git show HEAD~2  # 2 commits before HEAD
```

### Making Changes
```bash
# Add files to staging area
git add <file>
git add .  # Add all changes
git add *.js  # Add all .js files
git add -A  # Add all (including deletions)
git add -p  # Interactive staging (choose hunks)

# Commit changes
git commit -m "Commit message"
git commit -am "Message"  # Add and commit tracked files
git commit --amend  # Modify last commit
git commit --amend --no-edit  # Amend without changing message

# Remove files
git rm <file>  # Delete and stage
git rm --cached <file>  # Unstage but keep file
git rm -r <directory>  # Remove directory

# Move/rename files
git mv <old-name> <new-name>
```

### Viewing Differences
```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged
git diff --cached

# Compare branches
git diff <branch1> <branch2>

# Compare commits
git diff <commit1> <commit2>

# Show changes in specific file
git diff <file>
```

### Undoing Changes
```bash
# Discard changes in working directory
git checkout -- <file>
git restore <file>  # Modern alternative

# Unstage files
git reset HEAD <file>
git restore --staged <file>  # Modern alternative

# Discard all local changes
git reset --hard HEAD
```

---

## Branching & Merging

### Branch Basics
```bash
# List branches
git branch
git branch -a  # All branches (local + remote)
git branch -r  # Remote branches only
git branch -v  # With last commit info

# Create branch
git branch <branch-name>
git branch <branch-name> <commit-hash>  # From specific commit

# Switch branches
git checkout <branch-name>
git switch <branch-name>  # Modern alternative

# Create and switch to new branch
git checkout -b <branch-name>
git switch -c <branch-name>  # Modern alternative

# Delete branch
git branch -d <branch-name>  # Safe delete
git branch -D <branch-name>  # Force delete

# Rename branch
git branch -m <old-name> <new-name>
git branch -m <new-name>  # Rename current branch
```

### Merging
```bash
# Merge branch into current branch
git merge <branch-name>

# Merge with no fast-forward
git merge --no-ff <branch-name>

# Merge and create merge commit message
git merge <branch-name> -m "Merge message"

# Abort merge
git merge --abort

# Continue merge after resolving conflicts
git merge --continue
```

### Rebasing
```bash
# Rebase current branch onto another
git rebase <branch-name>

# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# Continue rebase after resolving conflicts
git rebase --continue

# Skip current commit
git rebase --skip

# Abort rebase
git rebase --abort
```

---

## Remote Repositories

### Remote Management
```bash
# View remotes
git remote
git remote -v  # With URLs

# Add remote
git remote add <name> <url>
git remote add origin https://github.com/user/repo.git

# Remove remote
git remote remove <name>

# Rename remote
git remote rename <old-name> <new-name>

# Change remote URL
git remote set-url <name> <new-url>

# Show remote info
git remote show <name>
```

### Fetching & Pulling
```bash
# Fetch from remote
git fetch
git fetch <remote>
git fetch <remote> <branch>
git fetch --all  # All remotes

# Pull (fetch + merge)
git pull
git pull <remote> <branch>
git pull --rebase  # Fetch and rebase instead of merge
git pull --no-rebase  # Ensure merge
```

### Pushing
```bash
# Push to remote
git push
git push <remote> <branch>
git push origin main

# Push and set upstream
git push -u origin <branch>
git push --set-upstream origin <branch>

# Push all branches
git push --all

# Push tags
git push --tags

# Force push (dangerous!)
git push --force
git push --force-with-lease  # Safer force push

# Delete remote branch
git push <remote> --delete <branch>
git push origin --delete feature-branch
```

---

## Intermediate Commands

### Stashing
```bash
# Stash changes
git stash
git stash save "Message"
git stash -u  # Include untracked files
git stash -a  # Include all files (even ignored)

# List stashes
git stash list

# Apply stash
git stash apply
git stash apply stash@{2}

# Apply and remove stash
git stash pop

# Show stash contents
git stash show
git stash show -p  # With diff

# Drop stash
git stash drop stash@{0}

# Clear all stashes
git stash clear

# Create branch from stash
git stash branch <branch-name>
```

### Tagging
```bash
# List tags
git tag
git tag -l "v1.*"  # Pattern matching

# Create lightweight tag
git tag <tag-name>

# Create annotated tag
git tag -a <tag-name> -m "Message"
git tag -a v1.0.0 -m "Release version 1.0.0"

# Tag specific commit
git tag <tag-name> <commit-hash>

# Show tag info
git show <tag-name>

# Delete tag
git tag -d <tag-name>

# Delete remote tag
git push origin --delete <tag-name>

# Push tag to remote
git push origin <tag-name>
git push origin --tags  # All tags

# Checkout tag
git checkout <tag-name>
```

### Cherry-picking
```bash
# Apply commit from another branch
git cherry-pick <commit-hash>

# Cherry-pick multiple commits
git cherry-pick <commit1> <commit2>

# Cherry-pick range
git cherry-pick <commit1>..<commit2>

# Cherry-pick without committing
git cherry-pick -n <commit-hash>
git cherry-pick --no-commit <commit-hash>

# Continue/abort
git cherry-pick --continue
git cherry-pick --abort
```

---

## Advanced Commands

### Advanced Rebase
```bash
# Interactive rebase options:
# p, pick = use commit
# r, reword = use commit, but edit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, meld into previous
# f, fixup = like squash, discard log message
# d, drop = remove commit

# Rebase onto another base
git rebase --onto <new-base> <old-base> <branch>

# Autosquash commits (with fixup!/squash! prefixes)
git rebase -i --autosquash <base>
```

### Reset Types
```bash
# Soft reset (keep changes staged)
git reset --soft HEAD~1

# Mixed reset (keep changes unstaged) - default
git reset HEAD~1
git reset --mixed HEAD~1

# Hard reset (discard changes)
git reset --hard HEAD~1
git reset --hard <commit-hash>

# Reset specific file
git reset HEAD <file>
```

### Reflog
```bash
# View reflog (reference log)
git reflog
git reflog show HEAD
git reflog show <branch>

# Recover lost commits
git reflog
git reset --hard HEAD@{2}
git checkout -b recovery HEAD@{5}

# Expire reflog entries
git reflog expire --expire=90.days.ago --all
```

### Bisect (Find Bug Introduction)
```bash
# Start bisect
git bisect start

# Mark current as bad
git bisect bad

# Mark known good commit
git bisect good <commit-hash>

# Git will checkout middle commit - test and mark
git bisect good  # If working
git bisect bad   # If broken

# Show bisect log
git bisect log

# Finish bisect
git bisect reset

# Automated bisect with script
git bisect start HEAD v1.0
git bisect run ./test-script.sh
```

### Worktrees
```bash
# List worktrees
git worktree list

# Add new worktree
git worktree add <path> <branch>
git worktree add ../project-feature feature-branch

# Add worktree with new branch
git worktree add -b <new-branch> <path>

# Remove worktree
git worktree remove <path>

# Prune worktrees
git worktree prune
```

### Submodules
```bash
# Add submodule
git submodule add <repository-url> <path>

# Initialize submodules
git submodule init

# Update submodules
git submodule update
git submodule update --init --recursive

# Clone with submodules
git clone --recursive <repository-url>

# Pull with submodule updates
git pull --recurse-submodules

# Remove submodule
git submodule deinit <path>
git rm <path>
rm -rf .git/modules/<path>
```

### Advanced Searching
```bash
# Search in files
git grep "search-term"
git grep -n "search-term"  # With line numbers
git grep --count "search-term"  # Count matches

# Search in specific commit
git grep "search-term" <commit-hash>

# Search commit messages
git log --grep="search-term"

# Search for code changes
git log -S "function-name"  # Pickaxe
git log -G "regex-pattern"

# Search for file
git log --all --full-history -- <file>
```

### Blame & History
```bash
# Show who changed each line
git blame <file>
git blame -L 10,20 <file>  # Specific lines

# Show file history
git log --follow <file>
git log -p <file>  # With changes

# Find when file was deleted
git log --all --full-history -- <file>
```

### Archive
```bash
# Create archive of repository
git archive --format=zip HEAD > project.zip
git archive --format=tar HEAD > project.tar

# Archive specific branch
git archive --format=zip <branch> > branch.zip

# Archive with prefix
git archive --prefix=project/ HEAD > project.tar
```

---

## Troubleshooting & Recovery

### Fixing Mistakes
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert a commit (create new commit)
git revert <commit-hash>
git revert HEAD

# Recover deleted branch
git reflog
git checkout -b <branch-name> HEAD@{n}

# Recover deleted file
git checkout HEAD -- <file>
git checkout <commit-hash> -- <file>

# Fix wrong commit message
git commit --amend -m "New message"

# Remove file from last commit
git reset HEAD~ <file>
git commit --amend --no-edit
```

### Cleaning
```bash
# Show what would be deleted
git clean -n
git clean --dry-run

# Remove untracked files
git clean -f

# Remove untracked files and directories
git clean -fd

# Remove ignored files too
git clean -fdx

# Interactive clean
git clean -i
```

### Resolving Conflicts
```bash
# When conflicts occur during merge/rebase:

# 1. Check status
git status

# 2. Open conflicted files and resolve
# Look for conflict markers:
# <<<<<<< HEAD
# your changes
# =======
# incoming changes
# >>>>>>> branch-name

# 3. Stage resolved files
git add <file>

# 4. Continue operation
git merge --continue
# or
git rebase --continue

# Accept theirs/ours
git checkout --theirs <file>
git checkout --ours <file>

# Use merge tool
git mergetool
```

---

## Advanced Workflows

### Git Flow Commands
```bash
# Feature branches
git checkout -b feature/new-feature develop
git checkout develop
git merge --no-ff feature/new-feature
git branch -d feature/new-feature

# Release branches
git checkout -b release/1.0.0 develop
git checkout main
git merge --no-ff release/1.0.0
git tag -a v1.0.0
git checkout develop
git merge --no-ff release/1.0.0
git branch -d release/1.0.0

# Hotfix branches
git checkout -b hotfix/1.0.1 main
git checkout main
git merge --no-ff hotfix/1.0.1
git tag -a v1.0.1
git checkout develop
git merge --no-ff hotfix/1.0.1
git branch -d hotfix/1.0.1
```

### Aliases (Time Savers)
```bash
# Set up useful aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --oneline --graph --all'
git config --global alias.amend 'commit --amend --no-edit'
git config --global alias.undo 'reset HEAD~1 --mixed'
```

### Hooks
```bash
# Hooks are scripts in .git/hooks/
# Common hooks:
# - pre-commit: run before commit
# - post-commit: run after commit
# - pre-push: run before push
# - commit-msg: validate commit message

# Example pre-commit hook
#!/bin/sh
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed, commit denied"
    exit 1
fi

# Make hook executable
chmod +x .git/hooks/pre-commit
```

### Advanced Git Configuration
```bash
# Set up diff tool
git config --global diff.tool vimdiff
git config --global difftool.prompt false

# Set up merge tool
git config --global merge.tool vimdiff
git config --global mergetool.prompt false

# Auto-correct commands
git config --global help.autocorrect 1

# Reuse recorded conflict resolutions
git config --global rerere.enabled true

# Default push behavior
git config --global push.default current

# Pull rebase by default
git config --global pull.rebase true

# Colorize output
git config --global color.ui auto
```

---

## Best Practices

### Commit Messages
```bash
# Good commit message structure:
# <type>: <subject>
# 
# <body>
# 
# <footer>

# Types: feat, fix, docs, style, refactor, test, chore

# Example:
git commit -m "feat: add user authentication

Implemented JWT-based authentication system with
login, logout, and token refresh functionality.

Closes #123"
```

### Branch Naming
```bash
# Common conventions:
feature/description    # New features
bugfix/description     # Bug fixes
hotfix/description     # Production hotfixes
release/version        # Release preparation
docs/description       # Documentation updates

# Examples:
feature/user-profile
bugfix/login-error
hotfix/security-patch
release/v1.2.0
```

### Workflow Tips
```bash
# Commit often, push regularly
git add -p  # Review changes before staging
git diff --staged  # Review before committing
git log --oneline --graph  # Visualize history

# Keep commits atomic (one logical change)
# Write meaningful commit messages
# Use branches for features
# Rebase before merging to clean history
# Tag releases
# Use .gitignore effectively
```

---

## Quick Reference Card

### Most Used Commands
```bash
git status                    # Check status
git add .                     # Stage all
git commit -m "message"       # Commit
git push                      # Push to remote
git pull                      # Pull from remote
git checkout -b <branch>      # Create and switch branch
git merge <branch>            # Merge branch
git log --oneline            # View history
git diff                      # View changes
git stash                     # Stash changes
```

### Emergency Commands
```bash
git reflog                    # View all changes
git reset --hard HEAD~1       # Undo last commit
git revert <commit>           # Revert commit safely
git clean -fd                 # Remove untracked files
git checkout -- <file>        # Discard file changes
git merge --abort             # Cancel merge
git rebase --abort            # Cancel rebase
```

---

## Resources

- **Official Documentation**: https://git-scm.com/doc
- **Git Book**: https://git-scm.com/book/en/v2
- **Interactive Tutorial**: https://learngitbranching.js.org/
- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf

---

*Remember: Git is powerful but can be dangerous. Always make sure you understand a command before running it, especially with `--force` or `--hard` flags.*

