# 🛍️ E-Commerce Web Scraper

A **modular Python web scraper** built using **Requests** and **BeautifulSoup** to collect product information from the WebScraper test e-commerce website.

This project follows **clean architecture, modular code structure, proper Git workflow, and data processing best practices**.

---

## 📋 Project Information



- **University:** University of Central Punjab
- **Course:** Tools & Tech for Data Science (T&T Quiz 1)
- **Target Website:** https://webscraper.io/test-sites/e-commerce/static
- **GitHub Repository:** https://github.com/mtahanaeem/mtahanaeem-Web.Scraper.for.E-Commerce.Site



---

## ✨ Features

✅ Automatic category & subcategory discovery  
✅ Pagination handling across multiple pages  
✅ Detailed product page scraping with error handling  
✅ Data cleaning & price normalization  
✅ Duplicate product removal  
✅ CSV data export with statistics  
✅ Rate limiting for ethical scraping  
✅ Modular architecture for easy extension  

---

## 📁 Project Structure

```
T&T Quiz 1/
├── data/                          # Output data (generated CSV files)
│   ├── products.csv              # All scraped products
│   └── category_summary.csv      # Category statistics
│
├── src/
│   ├── main.py                   # Entry point
│   └── scraper/
│       ├── __init__.py
│       ├── crawler.py            # Website navigation & crawling
│       ├── parsers.py            # HTML parsing & extraction
│       ├── exporters.py          # CSV export functionality
│       └── utils.py              # Utility functions
│
├── pyproject.toml                # uv project configuration
├── uv.lock                       # Dependency lock file
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```



---

## 📊 Data Fields Collected

The scraper collects **11 fields** per product:

| Field | Description |
|-------|-------------|
| `category` | Top-level product category |
| `subcategory` | Product subcategory |
| `product_title` | Product name |
| `price` | Normalized numeric price |
| `product_url` | Link to product page |
| `image_url` | Product image URL |
| `description` | Product description text |
| `rating` | Customer rating |
| `review_count` | Number of reviews |
| `spec` | Product specifications |
| `page_number` | Page where product was found |

### Category Summary Statistics

The scraper generates statistics per subcategory:
- **total_products:** Count of unique products
- **average_price:** Mean product price
- **min_price:** Lowest product price
- **max_price:** Highest product price
- **missing_descriptions:** Count of products without descriptions
- **duplicates_removed:** Count of duplicate entries removed



---

## ⚙️ Environment Setup

### Prerequisites

- **Python 3.8+**
- **uv package manager** (modern Python package manager)

### Install uv

```bash
pip install uv
```

### Install Dependencies with uv

Once uv is installed, run:

```bash
uv sync
```

This will:
- Create a virtual environment (`.venv`)
- Install all packages from `pyproject.toml`
- Use `uv.lock` for reproducible builds

### Alternative: Use pip instead of uv

```bash
pip install requests beautifulsoup4 pandas
```



---

## 🚀 Running the Scraper

### Step 1: Navigate to Project Directory

```bash
cd "T&T Quiz 1"
```

### Step 2: Run with uv (Recommended)

```bash
uv run python src/main.py
```

### Step 3: Check Output

CSV files will be generated in the `data/` folder:
- `products.csv` - All 92 scraped products
- `category_summary.csv` - Statistics by category/subcategory

### Example Output

```
============================================================
Web Scraper for E-Commerce Site
============================================================
Target: https://webscraper.io/test-sites/e-commerce/static

Starting web scraping...

Discovered category: Computers with 5 subcategories
Discovered category: Phones with 4 subcategories

Exported 92 products to data/products.csv
Exported category summary to data/category_summary.csv

============================================================
Scraping Statistics
============================================================
Total Products: 92
Unique Categories: 2
Unique Subcategories: 4
Avg Price: 546.84
Min Price: 24.99
Max Price: 1799.0
Products with Description: 92
Avg Review Count: 7.1
============================================================
```

---

## 📊 Output Files

### `data/products.csv`

Contains all 92 scraped products with 11 columns. Headers:
```csv
category,subcategory,product_title,price,product_url,image_url,description,rating,review_count,spec,page_number
```

Example rows:
```csv
Computers,Home,Dell Latitude 5280,...,1102.66,https://webscraper.io/test-sites/e-commerce/static/product/99,...
Computers,Laptops,Packard 255 G2,...,416.99,https://webscraper.io/test-sites/e-commerce/static/product/31,...
```

### `data/category_summary.csv`

Contains aggregated statistics per subcategory:
```csv
category,subcategory,total_products,average_price,min_price,max_price,missing_descriptions,duplicates_removed
Computers,Home,3,948.63,484.23,1259.0,0,1
Computers,Laptops,59,660.76,295.99,1799.0,0,1
Computers,Tablets,21,232.04,69.99,603.99,0,1
Phones,Touch,9,400.66,24.99,899.99,0,1
```



---

## 🔧 Technical Stack

### Core Dependencies

- **requests** - HTTP library for fetching web pages
- **beautifulsoup4** - HTML parsing and element selection
- **pandas** - Data manipulation and CSV export
- **lxml** (optional) - Fast HTML/XML parser

### Key Technologies

- **Language:** Python 3.8+
- **Package Manager:** uv (or pip)
- **Parsing:** CSS Selectors (BeautifulSoup)
- **Target Site:** Static HTML (no JavaScript)

### CSS Selectors Used

- **Products:** `div.thumbnail`
- **Categories:** `ul.flex-column`
- **Pagination:** `ul.pagination`
- **Prices:** `.float-end`

---

## 🌿 Git Workflow & Branching History

### Branch Strategy

The project uses a **feature branch workflow**:

```
main (production)
  ↑
dev (testing/staging)
  ↑
features/ (individual features)
  ↑
fixes/ (bug fixes)
```

### Merge Flow Completed ✅

**2. Feature Branches Merged:**
1. ✅ `feature/catalog-navigation` → dev (Category & subcategory discovery)
2. ✅ `feature/product-details` → dev (Product detail page scraping)

**Fix Branches Merged:**
1. ✅ `fix/url-resolution` → dev (URL handling & normalization)
2. ✅ `fix/deduplication` → dev (Duplicate removal)

**Final Release:**
```
dev → main (production)
```

**Cleanup:**
- ✅ Deleted 4 local feature/fix branches
- ✅ Pushed main to GitHub
- ✅ Pushed dev to GitHub

### Git Commands Used

#### Create feature branch
```bash
git checkout -b feature/feature-name
```

#### Merge features into dev
```bash
git checkout dev
git merge feature/catalog-navigation -m "Merge feature: catalog navigation"
git merge feature/product-details -m "Merge feature: product details"
git merge fix/url-resolution -m "Merge fix: URL resolution"
git merge fix/deduplication -m "Merge fix: deduplication"
```

#### Release to production
```bash
git checkout main
git merge dev -m "Release: merge tested dev into main"
```

#### Push to GitHub
```bash
git remote add origin https://github.com/mtahanaeem/mtahanaeem-Web.Scraper.for.E-Commerce.Site.git
git push -u origin main
git push -u origin dev
```

#### Clean up local branches
```bash
git branch -d feature/catalog-navigation feature/product-details
git branch -d fix/url-resolution fix/deduplication
```

---

## 📈 Scraping Results

### Discovery Statistics

```
Total products discovered:  93
After deduplication:        92 unique products
Duplicates removed:         1
Categories found:           2 (Computers, Phones)
Subcategories found:        4
```

### Quality Metrics

```
Products with descriptions: 92/92 (100%)
Products with images:       92/92 (100%)
Products with ratings:      92/92 (100%)
Average review count:       7.1 per product
```

### Price Statistics

```
Average price:    $546.84
Minimum price:    $24.99
Maximum price:    $1,799.00
Price range:      9 different price categories
```

### Breakdown by Category

```
Computers (83 products):
  - Home: 3 products
  - Laptops: 59 products
  - Tablets: 21 products

Phones (9 products):
  - Touch: 9 products
```

---

## 🛡️ Error Handling & Best Practices

### Implemented Features

✅ **Request timeouts:** 10-second timeout per page  
✅ **Connection retry:** Automatic retry on failure  
✅ **Safe HTML parsing:** Default values for missing data  
✅ **Optional detail scraping:** Skip slow pages if needed  
✅ **Rate limiting:** Configurable delay between requests  
✅ **Data validation:** Check required fields exist  

### Example: Error Handling in Code

```python
try:
    response = session.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")
    continue
```

---

## 🚨 Troubleshooting

### Issue: "Module not found" error

**Solution:** Ensure dependencies are installed:
```bash
uv sync
```

### Issue: CSV files not generated

**Solution:** Check directory exists:
```bash
mkdir data
```

### Issue: Website connection timeout

**Solution:** Site may be temporarily unavailable. Retry:
```bash
uv run python src/main.py
```

### Issue: Python not found

**Solution:** Verify Python installation:
```bash
python --version
```

---

## ✅ Project Completion Checklist

- ✅ Web scraper fully functional
- ✅ All 92 products successfully scraped
- ✅ CSV files with correct format
- ✅ Category summary with statistics
- ✅ Deduplication working (1 duplicate removed)
- ✅ Git merge workflow completed
- ✅ Local feature/fix branches deleted
- ✅ Pushed to GitHub repository
- ✅ README with setup & run instructions
- ✅ Proper project structure & modularity
- ✅ Error handling & rate limiting
- ✅ Code documentation & comments

---

## 📝 Key Implementation Details

### Parser Accuracy
Uses correct CSS selectors specifically tuned for the target website structure

### Data Integrity
Normalizes prices properly and handles null/missing values with defaults

### Performance
Scrapes 92 products in approximately 3-5 minutes with rate limiting

### Code Quality
Clean, modular, reusable code with proper separation of concerns

### Documentation
Comprehensive README and inline code comments

---

## 👨‍💻 Author

**Muhammad Taham Abubakar**  
University of Central Punjab  
T&T Quiz 1 Assignment - 2026

---

## 📄 License

This project is created for educational purposes as part of the Tools & Tech for Data Science course at University of Central Punjab.

---

## 🔗 Useful Resources

- [WebScraper Test Site](https://webscraper.io/test-sites/e-commerce/static)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://requests.readthedocs.io/)
- [uv Package Manager](https://github.com/astral-sh/uv)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

**Last Updated:** March 14, 2026  
**Status:** ✅ Complete



