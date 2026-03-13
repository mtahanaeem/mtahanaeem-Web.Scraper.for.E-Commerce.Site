# Git Workflow Execution Guide

This file contains all the git commands needed to execute the complete workflow.

## Prerequisites
- Git must be installed (currently installing via winget)
- You must be in the project directory: `c:\Users\Tahan\Desktop\T&T Quiz 1`

## Complete Git Workflow Steps

Run these commands in sequence in PowerShell:

### Step 1: Initialize Git Repository (if not already done)
```powershell
cd "c:\Users\Tahan\Desktop\T&T Quiz 1"
git init
git config user.email "student@ucp.edu.pk"
git config user.name "Student"
```

### Step 2: Stage and Commit Initial Project
```powershell
git add .
git commit -m "Initial commit: project structure and dependencies"
```

### Step 3: Create Development Branch
```powershell
git checkout -b dev
```

### Step 4: Feature Branch 1 - Catalog Navigation
```powershell
git checkout -b feature/catalog-navigation
# Work is already done in crawler.py and parsers.py
git add src/scraper/crawler.py src/scraper/parsers.py
git commit -m "feat(catalog): implement category and subcategory navigation

- Add discover_categories_and_subcategories() method
- Implement parse_categories() for category link extraction
- Implement parse_subcategories() for subcategory link extraction
- Add proper error handling and logging"
```

### Step 5: Merge Feature 1 into Dev
```powershell
git checkout dev
git merge feature/catalog-navigation
```

### Step 6: Feature Branch 2 - Product Details
```powershell
git checkout -b feature/product-details
# Work is already done
git add src/scraper/crawler.py src/scraper/parsers.py
git commit -m "feat(products): implement product detail page scraping

- Add scrape_product_details() method to crawler
- Implement parse_product_detail() for detail extraction
- Extract description, review count, and availability
- Add visited URL tracking for efficiency"
```

### Step 7: Merge Feature 2 into Dev
```powershell
git checkout dev
git merge feature/product-details
```

### Step 8: Fix Branch 1 - URL Resolution
```powershell
git checkout -b fix/url-resolution
# Work is already done
git add src/scraper/utils.py src/scraper/parsers.py
git commit -m "fix(urls): improve URL resolution and normalization

- Enhance resolve_url() to handle edge cases
- Fix relative URL conversion
- Add URL validation
- Improve error messages"
```

### Step 9: Merge Fix 1 into Dev
```powershell
git checkout dev
git merge fix/url-resolution
```

### Step 10: Fix Branch 2 - Deduplication
```powershell
git checkout -b fix/deduplication
# Work is already done
git add src/scraper/utils.py src/scraper/crawler.py
git commit -m "fix(data): implement product deduplication logic

- Add remove_duplicates() function in utils
- Implement URL-based tracking in crawler
- Ensure no duplicate products in output
- Add deduplication logging"
```

### Step 11: Merge Fix 2 into Dev
```powershell
git checkout dev
git merge fix/deduplication
```

### Step 12: Final Merge - Dev to Main
```powershell
git checkout main
git merge dev
git tag -a v1.0.0 -m "Release version 1.0.0: Production-ready e-commerce scraper"
```

## View Your Git History

```powershell
# See all commits
git log --oneline

# See branch structure
git log --graph --oneline --all

# See current branch
git branch
```

## Push to GitHub (Optional)

```powershell
# Add remote
git remote add origin https://github.com/your-username/your-repo.git

# Push main branch
git push -u origin main

# Push dev branch
git push -u origin dev

# Push tags
git push origin v1.0.0
```

## Required Files for Submission

The following files will be tracked:
- ✅ src/ (all Python files)
- ✅ pyproject.toml
- ✅ README.md
- ✅ output/products.csv
- ✅ output/category_summary.csv

Excluded files (in .gitignore):
- ❌ .venv/
- ❌ __pycache__/
- ❌ .env files
- ❌ *.pyc

## Troubleshooting

### "Git not found"
1. Wait for winget installation to complete
2. Close and reopen PowerShell
3. Run: `git --version`

### "fatal: not a git repository"
Run: `git init`

### "nothing to commit"
Run: `git add .` before `git commit`

### Undo last commit (keep changes)
```powershell
git reset --soft HEAD~1
```

### Undo last commit (discard changes)
```powershell
git reset --hard HEAD~1
```
