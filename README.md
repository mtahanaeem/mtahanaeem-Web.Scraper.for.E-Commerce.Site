# E-Commerce Web Scraper

A modular Python web scraper for the e-commerce demo site using **Beautiful Soup** and **Requests**. Follows industry best practices with proper project structure, error handling, and data processing.

## Project Information

- **University**: University of Central Punjab
- **Course**: Tools & Tech for Data Science
- **Target**: https://webscraper.io/test-sites/e-commerce/static

## Features

✅ **Automatic Navigation**: Programmatically discovers categories and subcategories  
✅ **Pagination Support**: Follows "Next" links to scrape all pages  
✅ **Product Details**: Extracts detailed information from product pages  
✅ **Data Cleaning**: Normalizes prices, handles missing values, removes duplicates  
✅ **CSV Export**: Generates both product and category summary reports  
✅ **Error Handling**: Robust error handling with informative logging  
✅ **Rate Limiting**: Built-in delay between requests for ethical scraping  

## Architecture

```
T&T Quiz 1/
├── pyproject.toml          # Project configuration (uv)
├── uv.lock                 # Dependency lock file
├── README.md               # This file
├── .gitignore              # Git ignore rules
├── src/
│   ├── main.py             # Entry point
│   └── scraper/
│       ├── __init__.py     # Package marker
│       ├── crawler.py      # Navigation and pagination logic
│       ├── parsers.py      # HTML parsing and data extraction
│       ├── exporters.py    # CSV generation and statistics
│       └── utils.py        # Utility functions (cleaning, URL resolution)
└── output/
    ├── products.csv        # All scraped products
    └── category_summary.csv # Category statistics
```

## Data Fields Collected

The scraper collects the following fields for each product:

| Field | Description |
|-------|-------------|
| **Category** | Product category |
| **Subcategory** | Product subcategory |
| **Title** | Product name |
| **Price** | Normalized numeric price |
| **URL** | Product page URL |
| **Description** | Product description (from detail page) |
| **Review Count** | Number of reviews |
| **Availability** | Stock status (In Stock/Out of Stock/Unknown) |

## Environment Setup

### Prerequisites
- Python 3.8+
- `uv` package manager ([install here](https://docs.astral.sh/uv/getting-started/installation/))

### Installation with uv

```bash
# Navigate to project directory
cd "T&T Quiz 1"

# Install dependencies (already done if created with this project)
uv sync

# Or manually add packages
uv add requests beautifulsoup4 pandas lxml

# Verify installation
uv run python --version
```

### Python Virtual Environment

The `uv` tool automatically creates and manages a virtual environment in `.venv/`:

```bash
# Activate virtual environment (optional - uv handles this)
# On Windows:
.\.venv\Scripts\Activate.ps1

# On Unix/macOS:
source .venv/bin/activate
```

## Running the Scraper

### Quick Start

```bash
cd "T&T Quiz 1"
uv run src/main.py
```

### Running with Python

```bash
cd "T&T Quiz 1"
.venv\Scripts\python src/main.py
```

### Output

The scraper generates two CSV files in the `output/` directory:

**products.csv** - Contains all product details:
```
category,subcategory,title,price,url,description,review_count,availability
```

**category_summary.csv** - Contains aggregated statistics:
```
Category,Subcategory,Product_Count,Avg_Price,Min_Price,Max_Price,Avg_Review_Count
```

## Code Modules

### `crawler.py` - WebCrawler Class
Handles website navigation, pagination, and product discovery.

**Key Methods:**
- `discover_categories_and_subcategories()` - Finds all category links
- `scrape_products_with_pagination()` - Iterates through pages
- `scrape_product_details()` - Extracts detail page information
- `crawl_all()` - Main method that orchestrates the entire process

```python
crawler = WebCrawler("https://example.com", delay=0.5)
products = crawler.crawl_all()
```

### `parsers.py` - ProductParser Class
Extracts data from HTML using BeautifulSoup.

**Key Methods:**
- `parse_product_listing()` - Extracts products from list pages
- `parse_product_detail()` - Extracts detailed product info
- `parse_categories()` - Finds category links
- `parse_subcategories()` - Finds subcategory links
- `parse_pagination()` - Finds next page link

### `exporters.py` - CSVExporter Class
Handles data export and statistical analysis.

**Key Methods:**
- `export_products()` - Saves all products to CSV
- `export_category_summary()` - Generates category summary statistics
- `get_statistics()` - Returns scraping statistics

### `utils.py` - Utility Functions

| Function | Purpose |
|----------|---------|
| `normalize_price()` | Converts price strings to floats |
| `clean_text()` | Removes extra whitespace |
| `resolve_url()` | Converts relative URLs to absolute |
| `remove_duplicates()` | Removes duplicate products |
| `validate_product_data()` | Validates required fields |

## Git Workflow & Branching Strategy

This project follows a **feature-branch** workflow with dedicated fix branches.

### Complete Git Workflow Commands

#### Step 1: Initialize Repository
```bash
git init
git config user.email "your.email@example.com"
git config user.name "Your Name"
```

#### Step 2: Create Initial Commit on Main
```bash
git add .
git commit -m "Initial project setup with project structure"
```

#### Step 3: Create Development Branch
```bash
git checkout -b dev
git push -u origin dev  # if using remote
```

#### Step 4: Create Feature Branch - Catalog Navigation
```bash
git checkout -b feature/catalog-navigation
# (Make changes to crawler.py and parsers.py for category/subcategory discovery)
git add .
git commit -m "feat(catalog): implement category and subcategory navigation"
git push -u origin feature/catalog-navigation
```

#### Step 5: Merge Feature into Dev
```bash
git checkout dev
git merge feature/catalog-navigation
git push
```

#### Step 6: Create Feature Branch - Product Details
```bash
git checkout -b feature/product-details
# (Make changes to scraper for detail page extraction)
git add .
git commit -m "feat(products): implement product detail page scraping"
git push -u origin feature/product-details
```

#### Step 7: Merge Feature into Dev
```bash
git checkout dev
git merge feature/product-details
git push
```

#### Step 8: Create Fix Branch - URL Resolution
```bash
git checkout -b fix/url-resolution
# (Make changes to utils.py for URL handling)
git add .
git commit -m "fix(urls): improve URL resolution and normalization"
git push -u origin fix/url-resolution
```

#### Step 9: Merge Fix into Dev
```bash
git checkout dev
git merge fix/url-resolution
git push
```

#### Step 10: Create Fix Branch - Deduplication
```bash
git checkout -b fix/deduplication
# (Make changes to utils.py for duplicate removal)
git add .
git commit -m "fix(data): implement product deduplication logic"
git push -u origin fix/deduplication
```

#### Step 11: Merge Fix into Dev
```bash
git checkout dev
git merge fix/deduplication
git push
```

#### Step 12: Merge Dev into Main (Release)
```bash
git checkout main
git merge dev
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin main
git push origin v1.0.0
```

### Branch Summary

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready code, tagged releases |
| `dev` | Integration branch, receives all features/fixes |
| `feature/catalog-navigation` | Category and subcategory discovery |
| `feature/product-details` | Product detail page extraction |
| `fix/url-resolution` | URL handling and normalization |
| `fix/deduplication` | Duplicate product removal |

### Git Configuration

Create a `.gitignore` file:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
.venv
venv/
.env

# Project specific
output/
*.csv

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

## Deduplication Strategy

The scraper removes duplicates through:

1. **URL-based Deduplication** - Tracks visited URLs
2. **Duplicate Removal** - Uses `remove_duplicates()` utility function
3. **Validation** - Ensures all required fields exist

```python
# In crawler.py - self.visited_urls prevents re-scraping
if url in self.visited_urls:
    continue

# After scraping - remove_duplicates function
all_products = remove_duplicates(all_products, key='url')
```

## Data Cleaning

### Price Normalization
- Removes currency symbols
- Handles different decimal separators (. and ,)
- Converts to float

### Text Cleaning
- Removes extra whitespace
- Collapses multiple spaces
- Strips leading/trailing whitespace

### Missing Values Handling
- Returns `None` for unparseable prices
- Uses "No description available" default
- Sets review count to 0 if not found

## Error Handling

All network requests include:
- Try-catch blocks for exception handling
- 10-second timeout per request
- Informative error messages
- Continues on individual failures

```python
try:
    response = self.session.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")
    return None
```

## Rate Limiting

The scraper includes a configurable delay between requests (default 0.5 seconds):

```python
crawler = WebCrawler(base_url, delay=0.5)
# or
crawler = WebCrawler(base_url, delay=2.0)  # 2-second delay
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `requests` | 2.32.5 | HTTP requests |
| `beautifulsoup4` | 4.14.3 | HTML parsing |
| `lxml` | 6.0.2 | XML/HTML parser |
| `pandas` | 3.0.1 | Data processing & CSV |
| `python` | 3.14.3 | Language runtime |

## Extending the Scraper

### Custom CSS Selectors

Modify selectors in `parsers.py`:

```python
# Current
product_elements = soup.find_all('div', class_='product')

# Custom
product_elements = soup.find_all('article', class_='item')
```

### Additional Data Fields

Add to `_extract_product_basic_info()`:

```python
rating_elem = element.find('div', class_='rating')
rating = float(rating_elem.get_text()) if rating_elem else None
```

### Multiple Sites

Extend to other sites:

```python
urls = [
    "https://site1.com",
    "https://site2.com"
]

for url in urls:
    crawler = WebCrawler(url)
    products = crawler.crawl_all()
```

## Troubleshooting

### "Module not found" Error
```bash
# Ensure virtual environment is activated
uv sync
```

### SSL Certificate Error
```python
# In crawler.py, modify:
self.session.verify = False  # Not recommended for production
```

### Timeout Issues
```python
# Increase delay
crawler = WebCrawler(base_url, delay=2.0)
```

### No Products Found
1. Check if target URL is correct
2. Verify CSS selectors match current HTML structure
3. Check HTML manually in browser
4. Update selectors in `parsers.py`

## Project Statistics

- **Total Code Lines**: ~600+ lines
- **Modules**: 5 (crawler, parsers, exporters, utils, main)
- **Key Classes**: WebCrawler, ProductParser, CSVExporter
- **Error Handling**: Comprehensive try-catch blocks
- **Documentation**: Extensive docstrings and comments

## Learning Outcomes

This project demonstrates:

✓ Web scraping with Beautiful Soup & Requests  
✓ Async-like pagination handling  
✓ Data cleaning and normalization  
✓ CSV/data export with Pandas  
✓ Modular Python architecture  
✓ Error handling and logging  
✓ Git version control workflow  
✓ Project documentation best practices  

## Notes

- **Ethical Scraping**: Always check `robots.txt` and site terms
- **Rate Limiting**: Default 0.5s delay prevents server overload
- **Legal**: Educational use only
- **Performance**: First run may take 5-10 minutes

## Author

Created for Tools & Tech for Data Science - University of Central Punjab

## License

Educational Use Only

---

**Last Updated**: March 2026  
**Project Version**: 1.0.0
