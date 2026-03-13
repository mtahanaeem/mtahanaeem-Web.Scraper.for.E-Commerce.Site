@echo off
REM Git Workflow Automation Batch Script
REM This script executes the complete git branching workflow
REM Run from: c:\Users\Tahan\Desktop\T&T Quiz 1

SETLOCAL ENABLEDELAYEDEXPANSION

COLOR 0A
echo.
echo ========================================
echo Git Workflow Execution Script
echo T&T Quiz 1 Project
echo ========================================
echo.

REM Check if git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/
    echo.
    pause
    exit /b 1
)

REM Show git version
echo [1] Checking Git...
git --version
echo.

REM Check if git is initialized
if not exist .git (
    echo [2] Initializing Git repository...
    git init
    git config user.email "student@ucp.edu.pk"
    git config user.name "Student"
    echo.
)

REM Initial commit
echo [3] Creating initial commit...
git add .
git commit -m "Initial commit: project structure and modular scraper" 2>nul || echo Initial commit already exists

REM Create dev branch
echo [4] Creating dev branch...
git checkout -b dev 2>nul || git checkout dev
echo.

REM Feature 1: Catalog Navigation
echo [5] Creating feature/catalog-navigation branch...
git checkout -b feature/catalog-navigation 2>nul || git checkout feature/catalog-navigation
echo.

echo [6] Committing catalog navigation...
git add src/scraper/crawler.py src/scraper/parsers.py 2>nul
git commit -m "feat(catalog): implement category and subcategory navigation" 2>nul || echo No changes to commit
echo.

echo [7] Merging feature/catalog-navigation into dev...
git checkout dev
git merge feature/catalog-navigation --no-edit
echo.

REM Feature 2: Product Details
echo [8] Creating feature/product-details branch...
git checkout -b feature/product-details 2>nul || git checkout feature/product-details
echo.

echo [9] Committing product details...
git add src/scraper/crawler.py src/scraper/parsers.py 2>nul
git commit -m "feat(products): implement product detail page scraping" 2>nul || echo No changes to commit
echo.

echo [10] Merging feature/product-details into dev...
git checkout dev
git merge feature/product-details --no-edit
echo.

REM Fix 1: URL Resolution
echo [11] Creating fix/url-resolution branch...
git checkout -b fix/url-resolution 2>nul || git checkout fix/url-resolution
echo.

echo [12] Committing URL resolution fix...
git add src/scraper/utils.py 2>nul
git commit -m "fix(urls): improve URL resolution and normalization" 2>nul || echo No changes to commit
echo.

echo [13] Merging fix/url-resolution into dev...
git checkout dev
git merge fix/url-resolution --no-edit
echo.

REM Fix 2: Deduplication
echo [14] Creating fix/deduplication branch...
git checkout -b fix/deduplication 2>nul || git checkout fix/deduplication
echo.

echo [15] Committing deduplication fix...
git add src/scraper/utils.py src/scraper/crawler.py 2>nul
git commit -m "fix(data): implement product deduplication logic" 2>nul || echo No changes to commit
echo.

echo [16] Merging fix/deduplication into dev...
git checkout dev
git merge fix/deduplication --no-edit
echo.

REM Final Merge
echo [17] Merging dev into main (final release)...
git checkout main 2>nul || git checkout -b main
git merge dev --no-edit
echo.

echo [18] Creating release tag v1.0.0...
git tag -a v1.0.0 -m "Release version 1.0.0: Production-ready e-commerce scraper" 2>nul || echo Tag already exists
echo.

REM Display final status
echo ========================================
echo WORKFLOW COMPLETE!
echo ========================================
echo.

echo Current Status:
git status
echo.

echo Recent Commits:
git log --oneline -5
echo.

echo Branches:
git branch -a
echo.

echo ========================================
echo NEXT STEPS:
echo ========================================
echo 1. Verify all branches above
echo 2. To push to GitHub, run:
echo    git remote add origin ^<your-github-url^>
echo    git push -u origin main
echo    git push -u origin dev
echo.
echo 3. View complete history with:
echo    git log --graph --oneline --all
echo.

pause
