# Git Workflow Guide

Complete step-by-step instructions for implementing the git branching strategy used in this project.

## Prerequisites

- Git installed and configured
- VS Code or preferred editor with Git integration
- Terminal/PowerShell access

## Initial Setup

### Configure Git (One-time)

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --global --list
```

### Initialize Repository

```bash
cd "T&T Quiz 1"

# Initialize git repository
git init

# Create .gitignore
echo # (create .gitignore file with patterns listed below)

# Stage initial files
git add .

# Make initial commit
git commit -m "Initial commit: project structure and dependencies"
```

## Branching Workflow

### Phase 1: Main and Dev Branches

```bash
# Create and switch to dev branch
git checkout -b dev

# Verify you're on dev
git branch

# Output should show:
#   main
# * dev
```

### Phase 2: Feature Branch 1 - Catalog Navigation

**Purpose**: Implement category and subcategory discovery

```bash
# Create feature branch from dev
git checkout -b feature/catalog-navigation

# Make changes to files:
# - src/scraper/crawler.py (discover_categories_and_subcategories method)
# - src/scraper/parsers.py (parse_categories and parse_subcategories methods)

# Stage changes
git add src/scraper/crawler.py src/scraper/parsers.py

# Commit
git commit -m "feat(catalog): implement category and subcategory navigation

- Add discover_categories_and_subcategories() method
- Implement parse_categories() for category link extraction
- Implement parse_subcategories() for subcategory link extraction
- Add proper error handling and logging"

# Push to remote (if applicable)
git push -u origin feature/catalog-navigation
```

### Phase 3: Merge Feature 1 into Dev

```bash
# Switch to dev
git checkout dev

# Merge feature branch
git merge feature/catalog-navigation

# Output shows:
# Updating xxx...xxx
# Fast-forward
#  src/scraper/crawler.py  | XX changes(+)
#  src/scraper/parsers.py  | XX changes(+)

# Push dev branch
git push origin dev

# (Optional) Delete feature branch
git branch -d feature/catalog-navigation
git push origin --delete feature/catalog-navigation
```

### Phase 4: Feature Branch 2 - Product Details

**Purpose**: Implement product detail page scraping

```bash
# Create feature branch from dev
git checkout -b feature/product-details

# Make changes to files:
# - src/scraper/crawler.py (scrape_product_details method)
# - src/scraper/parsers.py (parse_product_detail method)

# Stage changes
git add src/scraper/crawler.py src/scraper/parsers.py

# Commit
git commit -m "feat(products): implement product detail page scraping

- Add scrape_product_details() method to crawler
- Implement parse_product_detail() for detail extraction
- Extract description, review count, and availability
- Add visited URL tracking for efficiency"

# Push
git push -u origin feature/product-details
```

### Phase 5: Merge Feature 2 into Dev

```bash
git checkout dev
git merge feature/product-details
git push origin dev
git branch -d feature/product-details
```

### Phase 6: Fix Branch 1 - URL Resolution

**Purpose**: Fix and improve URL handling

```bash
# Create fix branch
git checkout -b fix/url-resolution

# Make changes to files:
# - src/scraper/utils.py (resolve_url function improvements)
# - src/scraper/parser.py (URL resolution in parsing)

# Stage changes
git add src/scraper/utils.py src/scraper/parsers.py

# Commit
git commit -m "fix(urls): improve URL resolution and normalization

- Enhance resolve_url() to handle edge cases
- Fix relative URL conversion
- Add URL validation
- Improve error messages"

# Push
git push -u origin fix/url-resolution
```

### Phase 7: Merge Fix 1 into Dev

```bash
git checkout dev
git merge fix/url-resolution
git push origin dev
git branch -d fix/url-resolution
```

### Phase 8: Fix Branch 2 - Deduplication

**Purpose**: Implement product deduplication

```bash
# Create fix branch
git checkout -b fix/deduplication

# Make changes to files:
# - src/scraper/utils.py (remove_duplicates function)
# - src/scraper/crawler.py (integration of deduplication)

# Stage changes
git add src/scraper/utils.py src/scraper/crawler.py

# Commit
git commit -m "fix(data): implement product deduplication logic

- Add remove_duplicates() function in utils
- Implement URL-based tracking in crawler
- Ensure no duplicate products in output
- Add deduplication logging"

# Push
git push -u origin fix/deduplication
```

### Phase 9: Merge Fix 2 into Dev

```bash
git checkout dev
git merge fix/deduplication
git push origin dev
git branch -d fix/deduplication
```

### Phase 10: Final Merge - Dev to Main

**Purpose**: Release version 1.0.0

```bash
# Switch to main
git checkout main

# Merge dev into main
git merge dev

# Create release tag
git tag -a v1.0.0 -m "Release version 1.0.0: Production-ready e-commerce scraper"

# Push changes
git push origin main
git push origin v1.0.0
```

## Viewing Git History

### View all commits
```bash
git log --oneline

# Output:
# abc1234 Release version 1.0.0
# def5678 fix(data): implement product deduplication logic
# ghi9012 fix(urls): improve URL resolution and normalization
# jkl3456 feat(products): implement product detail page scraping
# mno7890 feat(catalog): implement category and subcategory navigation
# pqr1111 Initial commit: project structure and dependencies
```

### View branch structure
```bash
git log --graph --oneline --all

# Output shows visual tree of commits and branches
```

### View branches
```bash
# Show all local branches
git branch

# Show all branches (local and remote)
git branch -a

# Show branch with last commit
git branch -v
```

## Common Git Commands

### Status & Information
```bash
# Current status
git status

# Show staged changes
git diff --staged

# Show unstaged changes
git diff

# Show commit details
git show abc1234
```

### Working with Branches
```bash
# List all branches
git branch

# Create new branch
git branch new-feature

# Switch to branch
git checkout branch-name

# Create and switch in one command
git checkout -b branch-name

# Delete branch (local)
git branch -d branch-name

# Delete branch (remote)
git push origin --delete branch-name

# Rename branch
git branch -m old-name new-name
```

### Undoing Changes
```bash
# Unstage file
git reset HEAD filename.py

# Discard changes in working directory
git checkout -- filename.py

# Undo last commit (keep changes)
git revert HEAD

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

### Stashing
```bash
# Save uncommitted changes
git stash

# List stashed changes
git stash list

# Apply last stash
git stash pop

# Apply specific stash
git stash apply stash@{0}
```

## Conflict Resolution

If you encounter merge conflicts:

```bash
# See conflicting files
git status

# Open conflicting file - you'll see:
# <<<<<<< HEAD
# your changes
# =======
# incoming changes
# >>>>>>> branch-name

# Edit file to resolve conflicts
# Then stage the file
git add conflicting-file.py

# Complete the merge
git commit -m "Resolve merge conflicts"
```

## Best Practices

### Commit Messages
```bash
# Good commit message structure:
# [type]: [subject]
# 
# [body]

# Types:
# feat:  New feature
# fix:   Bug fix
# refactor: Code refactoring
# test: Tests
# docs: Documentation
# style: Code style changes

# Examples:
git commit -m "feat(crawler): add pagination support"
git commit -m "fix(parser): handle missing product descriptions"
git commit -m "refactor(utils): simplify price normalization"
```

### Branch Naming
```
main              - Production releases
dev               - Integration branch
feature/*         - New features
fix/*             - Bug fixes
refactor/*        - Code refactoring
test/*            - Test additions
docs/*            - Documentation updates
```

### Before Pushing
```bash
# Always pull latest changes
git pull origin dev

# Review your commits
git log --oneline -5

# Check status
git status
```

## Advanced: Interactive Rebase

To clean up commit history before merging:

```bash
# On feature branch, rebase on dev
git fetch origin
git rebase -i origin/dev

# In the interactive editor:
# pick = use commit
# reword = use commit, but edit message
# squash = use commit, but meld into previous
# fixup = like squash, but discard log message
# drop = remove commit

# After rebase
git push -f origin feature-branch
```

## Remote Repository (GitHub/GitLab)

If using a remote repository:

```bash
# Add remote
git remote add origin https://github.com/user/repo.git

# Push branch
git push -u origin feature-branch

# Pull latest
git pull origin dev

# Fetch without merging
git fetch origin

# View remotes
git remote -v
```

## Scenario: Working in Parallel

Multiple team members working on different features:

```
Person A:
git checkout -b feature/pagination
# ... work ...
git push -u origin feature/pagination

Person B:
git checkout -b feature/export
# ... work ...
git push -u origin feature/export

# Both merge when ready:
git checkout dev
git pull origin dev
git merge feature/pagination
git push origin dev
```

## Summary

The complete workflow creates a clean git history:

```
main (v1.0.0)
├── Initial commit
└── Merged from dev

dev
├── Feature 1: catalog-navigation
├── Feature 2: product-details
├── Fix 1: url-resolution
├── Fix 2: deduplication
└── Ready for release
```

For more information, see the main [README.md](README.md)
