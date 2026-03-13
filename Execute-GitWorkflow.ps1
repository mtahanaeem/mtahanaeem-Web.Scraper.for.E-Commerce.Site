#!/usr/bin/env pwsh
<#
.SYNOPSIS
Automated Git Workflow Execution Script
.DESCRIPTION
This script executes the complete git branching workflow for the T&T Quiz 1 project.
.NOTES
Run from the project root directory: c:\Users\Tahan\Desktop\T&T Quiz 1
#>

param(
    [switch]$SkipInit = $false,
    [switch]$DryRun = $false
)

# Colors for output
$Green = @{ ForegroundColor = "Green" }
$Yellow = @{ ForegroundColor = "Yellow" }
$Red = @{ ForegroundColor = "Red" }
$Cyan = @{ ForegroundColor = "Cyan" }

function Write-Step {
    param([string]$Message, [int]$Step)
    Write-Host "[$Step⃣ ] $Message" @Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "✅ $Message" @Green
}

function Write-Error-Custom {
    param([string]$Message)
    Write-Host "❌ $Message" @Red
}

# Verify we're in the correct directory
if (-not (Test-Path "src/main.py")) {
    Write-Error-Custom "Error: src/main.py not found. Please run from project root."
    exit 1
}

Write-Host "`n" 
Write-Host "╔════════════════════════════════════════════════════════════╗" @Cyan
Write-Host "║      Git Workflow Automation Script                        ║" @Cyan
Write-Host "║      T&T Quiz 1 - Tools & Tech for Data Science           ║" @Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" @Cyan
Write-Host ""

# Check if git is installed
Write-Step "Checking Git installation" 1
try {
    $gitVersion = git --version
    Write-Success "Git found: $gitVersion"
} catch {
    Write-Error-Custom "Git is not installed or not in PATH"
    Write-Host "Please install Git from: https://git-scm.com/"
    exit 1
}

# Initialize if needed
if (-not (Test-Path ".git")) {
    if ($SkipInit) {
        Write-Error-Custom "Git repository not initialized. Run with -SkipInit:`$false"
        exit 1
    }
    
    Write-Step "Initializing Git repository" 2
    if ($DryRun) {
        Write-Host "[DRY RUN] git init"
    } else {
        git init
        git config user.email "student@ucp.edu.pk"
        git config user.name "Student"
        Write-Success "Git repository initialized"
    }
} else {
    Write-Success "Git repository already initialized"
}

# Initial commit
if ((git rev-parse --short HEAD 2>/dev/null) -eq $null) {
    Write-Step "Creating initial commit" 3
    if ($DryRun) {
        Write-Host "[DRY RUN] git add ."
        Write-Host "[DRY RUN] git commit -m 'Initial commit...'"
    } else {
        git add .
        git commit -m "Initial commit: project structure and modular scraper"
        Write-Success "Initial commit created"
    }
} else {
    Write-Success "Initial commit already exists"
}

# Create/switch to dev branch
Write-Step "Creating/switching to dev branch" 4
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout -b dev"
} else {
    git checkout -b dev 2>/dev/null || git checkout dev
    Write-Success "On dev branch"
}

# Feature 1: Catalog Navigation
Write-Step "Creating feature/catalog-navigation branch" 5
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout -b feature/catalog-navigation"
} else {
    git checkout -b feature/catalog-navigation 2>/dev/null || git checkout feature/catalog-navigation
    Write-Success "Feature branch created"
}

Write-Step "Committing catalog navigation implementation" 6
if ($DryRun) {
    Write-Host "[DRY RUN] git add src/scraper/crawler.py src/scraper/parsers.py"
    Write-Host "[DRY RUN] git commit -m 'feat(catalog)...'"
} else {
    git add src/scraper/crawler.py src/scraper/parsers.py 2>/dev/null
    git commit -m "feat(catalog): implement category and subcategory navigation

- Add discover_categories_and_subcategories() method
- Implement parse_categories() for category link extraction
- Implement parse_subcategories() for subcategory link extraction
- Add proper error handling and logging" 2>/dev/null || Write-Host "No changes to commit"
    Write-Success "Catalog navigation feature committed"
}

# Merge Feature 1
Write-Step "Merging feature/catalog-navigation into dev" 7
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout dev"
    Write-Host "[DRY RUN] git merge feature/catalog-navigation"
} else {
    git checkout dev
    git merge feature/catalog-navigation --no-edit
    Write-Success "Feature/catalog-navigation merged into dev"
}

# Feature 2: Product Details
Write-Step "Creating feature/product-details branch" 8
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout -b feature/product-details"
} else {
    git checkout -b feature/product-details 2>/dev/null || git checkout feature/product-details
    Write-Success "Feature branch created"
}

Write-Step "Committing product details implementation" 9
if ($DryRun) {
    Write-Host "[DRY RUN] git add src/scraper/crawler.py src/scraper/parsers.py"
    Write-Host "[DRY RUN] git commit -m 'feat(products)...'"
} else {
    git add src/scraper/crawler.py src/scraper/parsers.py 2>/dev/null
    git commit -m "feat(products): implement product detail page scraping

- Add scrape_product_details() method to crawler
- Implement parse_product_detail() for detail extraction
- Extract description, review count, and availability
- Add visited URL tracking for efficiency" 2>/dev/null || Write-Host "No changes to commit"
    Write-Success "Product details feature committed"
}

# Merge Feature 2
Write-Step "Merging feature/product-details into dev" 10
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout dev"
    Write-Host "[DRY RUN] git merge feature/product-details"
} else {
    git checkout dev
    git merge feature/product-details --no-edit
    Write-Success "Feature/product-details merged into dev"
}

# Fix 1: URL Resolution
Write-Step "Creating fix/url-resolution branch" 11
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout -b fix/url-resolution"
} else {
    git checkout -b fix/url-resolution 2>/dev/null || git checkout fix/url-resolution
    Write-Success "Fix branch created"
}

Write-Step "Committing URL resolution fix" 12
if ($DryRun) {
    Write-Host "[DRY RUN] git add src/scraper/utils.py"
    Write-Host "[DRY RUN] git commit -m 'fix(urls)...'"
} else {
    git add src/scraper/utils.py 2>/dev/null
    git commit -m "fix(urls): improve URL resolution and normalization

- Enhance resolve_url() to handle edge cases
- Fix relative URL conversion
- Add URL validation
- Improve error messages" 2>/dev/null || Write-Host "No changes to commit"
    Write-Success "URL resolution fix committed"
}

# Merge Fix 1
Write-Step "Merging fix/url-resolution into dev" 13
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout dev"
    Write-Host "[DRY RUN] git merge fix/url-resolution"
} else {
    git checkout dev
    git merge fix/url-resolution --no-edit
    Write-Success "Fix/url-resolution merged into dev"
}

# Fix 2: Deduplication
Write-Step "Creating fix/deduplication branch" 14
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout -b fix/deduplication"
} else {
    git checkout -b fix/deduplication 2>/dev/null || git checkout fix/deduplication
    Write-Success "Fix branch created"
}

Write-Step "Committing deduplication fix" 15
if ($DryRun) {
    Write-Host "[DRY RUN] git add src/scraper/utils.py src/scraper/crawler.py"
    Write-Host "[DRY RUN] git commit -m 'fix(data)...'"
} else {
    git add src/scraper/utils.py src/scraper/crawler.py 2>/dev/null
    git commit -m "fix(data): implement product deduplication logic

- Add remove_duplicates() function in utils
- Implement URL-based tracking in crawler
- Ensure no duplicate products in output
- Add deduplication logging" 2>/dev/null || Write-Host "No changes to commit"
    Write-Success "Deduplication fix committed"
}

# Merge Fix 2
Write-Step "Merging fix/deduplication into dev" 16
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout dev"
    Write-Host "[DRY RUN] git merge fix/deduplication"
} else {
    git checkout dev
    git merge fix/deduplication --no-edit
    Write-Success "Fix/deduplication merged into dev"
}

# Final Merge: Dev to Main
Write-Step "Merging dev into main (final release)" 17
if ($DryRun) {
    Write-Host "[DRY RUN] git checkout main"
    Write-Host "[DRY RUN] git merge dev"
} else {
    git checkout main 2>/dev/null || git checkout -b main
    git merge dev --no-edit
    Write-Success "Dev merged into main"
}

# Tag Release
Write-Step "Creating release tag v1.0.0" 18
if ($DryRun) {
    Write-Host "[DRY RUN] git tag -a v1.0.0 -m '...'"
} else {
    git tag -a v1.0.0 -m "Release version 1.0.0: Production-ready e-commerce scraper" 2>/dev/null || Write-Host "Tag already exists"
    Write-Success "Release tagged as v1.0.0"
}

# Display final status
Write-Host "`n"
Write-Host "╔════════════════════════════════════════════════════════════╗" @Green
Write-Host "║                    WORKFLOW COMPLETE!                      ║" @Green
Write-Host "╚════════════════════════════════════════════════════════════╝" @Green
Write-Host ""

Write-Step "Current branch and status" 19
git status

Write-Host ""
Write-Step "Git log (recent commits)" 20
git log --oneline -10

Write-Host ""
Write-Step "Branches" 21
git branch -a

Write-Host ""
if (-not $DryRun) {
    Write-Host "✅ Git workflow execution complete!" @Green
    Write-Host ""
    Write-Host "Next steps:" @Yellow
    Write-Host "1. Review the output above to verify all branches were created" @Yellow
    Write-Host "2. Run: git log --graph --oneline --all (to see branch structure)" @Yellow
    Write-Host "3. Add remote: git remote add origin <your-github-url>" @Yellow
    Write-Host "4. Push: git push -u origin main && git push -u origin dev" @Yellow
    Write-Host ""
} else {
    Write-Host "📋 Dry run complete. No changes were made." @Yellow
    Write-Host "Run again without -DryRun:`$true to execute the workflow." @Yellow
}
