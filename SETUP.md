# Project Setup & Quick Start Guide

Complete guide for setting up the Data Science Tools & Tech Quiz 1 project on your machine.

## ⚡ Quick Start (5 minutes)

### 1. Verify uv is Installed
```bash
uv --version
# Output: uv 0.x.x (or similar)
```

### 2. Install Dependencies
```bash
cd "T&T Quiz 1"
uv sync
```

### 3. Run the Scraper
```bash
uv run src/main.py
```

### 4. Check Results
```bash
ls output/
# You should see:
# - products.csv
# - category_summary.csv
```

---

## 📦 Full Installation Guide

### Step 1: Install Python & uv

#### Windows
```bash
# Option A: Using Windows Package Manager
winget install astral.uv

# Option B: Using pip (requires Python 3.8+)
pip install uv

# Verify
uv --version
```

#### macOS
```bash
brew install uv

# Or with pip
pip install uv
```

#### Linux
```bash
# Using curl (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

### Step 2: Clone/Navigate to Project
```bash
cd "path/to/T&T Quiz 1"
```

### Step 3: Create Virtual Environment with uv
```bash
# Automatic (recommended)
uv sync

# This will:
# ✓ Create .venv directory
# ✓ Install Python 3.14.3 (if needed)
# ✓ Install all dependencies from pyproject.toml
# ✓ Generate uv.lock file
```

### Step 4: Verify Installation
```bash
# Check Python version
uv run python --version

# Check installed packages
uv run pip list

# You should see:
# - requests
# - beautifulsoup4
# - pandas
# - lxml
```

---

## 🚀 Running the Scraper

### Method 1: Using uv (Recommended)
```bash
uv run src/main.py
```

### Method 2: Activate Virtual Environment First
```bash
# Windows
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# Then run
python src/main.py

# Deactivate when done
deactivate
```

### Method 3: Direct Python Execution
```bash
# Windows
.\.venv\Scripts\python src/main.py

# macOS/Linux
./.venv/bin/python src/main.py
```

---

## 📊 Understanding the Output

### products.csv
Contains all scraped products with these columns:
```
category,subcategory,title,price,url,description,review_count,availability
```

Example:
```
Computers,Laptops,Laptop 1,"449.0",https://example.com/1,"High performance laptop",30,In Stock
```

### category_summary.csv
Contains aggregate statistics:
```
Category,Subcategory,Product_Count,Avg_Price,Min_Price,Max_Price,Avg_Review_Count
```

Example:
```
Computers,Laptops,25,599.50,299.00,999.99,45.2
```

---

## 🔧 Project Structure

```
T&T Quiz 1/
├── src/
│   ├── main.py                    # Entry point - run this!
│   └── scraper/
│       ├── crawler.py             # Website navigation
│       ├── parsers.py             # HTML parsing
│       ├── exporters.py           # CSV export
│       ├── utils.py               # Utility functions
│       └── __init__.py            # Package marker
├── output/                         # Generated files (auto-created)
│   ├── products.csv
│   └── category_summary.csv
├── pyproject.toml                  # Project configuration
├── uv.lock                         # Dependency lock
├── README.md                       # Full documentation
├── GIT_WORKFLOW.md                 # Git branching guide
├── SETUP.md                        # This file
└── .gitignore                      # Git ignore rules
```

---

## 🛠️ Configuration Options

### Adjust Scraping Delay
Edit `src/main.py`:
```python
# Slower (2 second delay between requests)
crawler = WebCrawler(base_url, delay=2.0)

# Faster (0.1 second delay - be careful!)
crawler = WebCrawler(base_url, delay=0.1)
```

### Change Output Directory
Edit `src/main.py`:
```python
exporter = CSVExporter(output_dir="my_output")
```

### Modify Target URL
Edit `src/main.py`:
```python
base_url = "https://another-site.com"
```

---

## 🐛 Troubleshooting

### "uv: command not found"
**Solution**: Install uv or add it to PATH
```bash
# Reinstall uv
pip install --force-reinstall uv

# Or install curl and use recommended installer
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### "Python not found"
**Solution**: uv will auto-download Python, or specify version
```bash
# Let uv download Python
uv sync

# Or specify manually
uv python install 3.11
```

### ". venv\Scripts\Activate.ps1 cannot be run..."
**Solution**: Update PowerShell execution policy
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "SSL Certificate Error"
**Solution**: This shouldn't happen with uv, but if it does:
1. Update certificates:
   ```bash
   pip install --upgrade certifi
   ```

2. Or ignore SSL (NOT recommended for production):
   Edit crawler.py:
   ```python
   self.session.verify = False
   ```

### "No products found"
**Troubleshooting**:
1. Check target URL is accessible
2. Verify site structure hasn't changed
3. Check CSS selectors in `parsers.py`
4. Manually visit URL in browser
5. Update selectors if site changed

### "Import Error" or "Module not found"
**Solution**: Ensure dependencies are installed
```bash
uv sync
# or
uv add requests beautifulsoup4 pandas lxml
```

### "Permission Denied" (macOS/Linux)
**Solution**: Make file executable
```bash
chmod +x src/main.py
```

---

## 🔄 Virtual Environment Management

### View Current Environment
```bash
uv python list
```

### Use Specific Python Version
```bash
uv python install 3.11
uv python install 3.12
```

### Check Which Python is Active
```bash
uv run which python
# or
uv run python -c "import sys; print(sys.executable)"
```

### Clear Cache
```bash
uv cache clean
```

### Recreate Virtual Environment
```bash
rm -r .venv
uv sync
```

---

## 📝 Common Commands

```bash
# Install dependencies
uv sync

# Add new package
uv add package_name

# Add dev package
uv add --dev package_name

# Remove package
uv remove package_name

# List installed packages
uv pip list

# Run command
uv run python myscript.py

# Run with arguments
uv run python src/main.py --arg value
```

---

## 🌐 Network & Proxy Settings

### If Behind Corporate Proxy
Set environment variables:
```bash
# Windows
$env:HTTP_PROXY = "http://proxy.company.com:8080"
$env:HTTPS_PROXY = "https://proxy.company.com:8080"

# macOS/Linux
export HTTP_PROXY="http://proxy.company.com:8080"
export HTTPS_PROXY="https://proxy.company.com:8080"
```

Then run:
```bash
uv sync
uv run src/main.py
```

---

## 📚 Learn More

- **Python Documentation**: https://docs.python.org/3/
- **uv Documentation**: https://docs.astral.sh/uv/
- **Beautiful Soup**: https://www.crummy.com/software/BeautifulSoup/
- **Requests Library**: https://docs.python-requests.org/
- **Pandas Documentation**: https://pandas.pydata.org/

---

## ✅ Verification Checklist

- [ ] uv is installed (`uv --version`)
- [ ] Project directory is correct
- [ ] Dependencies installed (`uv sync` completed)
- [ ] Python works (`uv run python --version`)
- [ ] source files exist (`ls src/scraper/`)
- [ ] Main script runs (`uv run src/main.py`)
- [ ] Output files created (`ls output/`)
- [ ] CSV files contain data (check with text editor)

---

## 🎓 Next Steps

1. **Read the documentation**:
   - [README.md](README.md) - Full project documentation
   - [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Git branching guide

2. **Understand the code**:
   - Start with [src/main.py](src/main.py)
   - Review [src/scraper/crawler.py](src/scraper/crawler.py)
   - Check [src/scraper/parsers.py](src/scraper/parsers.py)

3. **Modify and extend**:
   - Change target URL in main.py
   - Adjust CSS selectors in parsers.py
   - Add new data fields to parse

4. **Version control**:
   - Follow [GIT_WORKFLOW.md](GIT_WORKFLOW.md)
   - Create feature branches
   - Practice git workflow

---

**Happy Scraping! 🚀**

For issues or questions, check the [README.md](README.md) or [GIT_WORKFLOW.md](GIT_WORKFLOW.md).
