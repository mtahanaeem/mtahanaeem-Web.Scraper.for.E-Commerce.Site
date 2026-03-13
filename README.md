Catalog Scraper: Modular E-Commerce ETL Project
This repository contains a Python-based web scraping and data processing pipeline developed for the Tools & Tech for Data Science course at the University of Central Punjab. The project demonstrates a robust ETL (Extract, Transform, Load) workflow, focusing on programmatic navigation of structured catalogs and professional version control.

🛠️ Technical Stack & Environment
The project is built for performance and reproducibility:

Environment Management: Fully managed via uv for lightning-fast dependency resolution and isolated virtual environments.

Extraction: Built using Requests and BeautifulSoup4 (lxml parser).

Data Transformation: Pandas is utilized for data cleaning and generating statistical summaries.

Constraints: Developed strictly without browser automation (Selenium/Playwright) to prioritize efficiency and meet academic requirements.

📂 Project Structure
The repository follows a modular architecture to separate concerns and ensure scalability:

Plaintext
.
├── pyproject.toml          # uv configuration and dependencies
├── README.md               # Project documentation
├── data/                   # Generated CSV output
└── src/
    ├── main.py             # Application orchestrator
    └── scraper/
        ├── crawler.py      # Category discovery and pagination logic
        ├── parsers.py      # HTML element extraction and parsing
        ├── exporters.py    # Data persistence and aggregation
        └── utils.py        # Price normalization and URL resolution
📊 Data & Reporting
The scraper performs a multi-level crawl—programmatically discovering categories, handling numbered pagination, and visiting individual product detail pages to extract enriched data.

Outputs (Stored in /data)
products.csv: A comprehensive dataset containing Category, Subcategory, Title, Price (normalized to numeric format), Description, and Review Counts.

category_summary.csv: A statistical report providing:

Total product counts per subcategory.

Price distribution metrics (Average, Minimum, and Maximum).

Deduplication and missing data statistics.

🔄 Git Workflow & Development
This project follows a professional branching strategy to ensure code integrity:

Main Branches: main (stable releases) and dev (integration).

Feature Branches: feature/catalog-navigation and feature/product-details were used for initial builds.

Maintenance: fix/url-resolution and fix/deduplication were used to refine data quality.

🚀 Getting Started
Prerequisites
Python 3.14+

uv package manager

Installation & Execution
Bash
# Clone the repository
git clone https://github.com/mtahanaeem/T-T-Quiz.git
cd T-T-Quiz

# Sync environment and run
uv sync
uv run src/main.py
🔍 Technical Decisions
Price Cleaning: Implemented regex-based cleaning to convert currency strings into sortable float values.

Deduplication: Logic implemented in the exporter layer to ensure 100% unique records based on product URLs.

Resilience: Integrated retry logic and error handling for network-level exceptions.