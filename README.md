\# E-Commerce Web Scraper



A \*\*modular Python web scraper\*\* built using \*\*Requests\*\* and \*\*BeautifulSoup\*\* to collect product information from the WebScraper test e-commerce website.



This project follows \*\*clean architecture, modular code structure, proper Git workflow, and data processing practices\*\*.



\## Project Information



\* \*\*University:\*\* University of Central Punjab

\* \*\*Course:\*\* Tools \& Tech for Data Science

\* \*\*Project:\*\* T\&T Quiz

\* \*\*Target Website:\*\* https://webscraper.io/test-sites/e-commerce/static



---



\# Features



✅ Automatic category \& subcategory discovery

✅ Pagination handling across multiple pages

✅ Detailed product page scraping

✅ Data cleaning \& normalization

✅ Duplicate removal

✅ CSV data export

✅ Error handling with request timeouts

✅ Rate limiting for ethical scraping



---



\# Project Structure



```

T-T-Quiz/

│

├── data/                  # Output data (generated CSV files)

│

├── src/

│   ├── main.py            # Project entry point

│   │

│   └── scraper/

│       ├── \_\_init\_\_.py

│       ├── crawler.py     # Website crawling \& navigation logic

│       ├── parsers.py     # HTML parsing and data extraction

│       ├── exporters.py   # CSV export and statistics

│       └── utils.py       # Helper utilities

│

├── pyproject.toml         # Project configuration

├── uv.lock                # Dependency lock file

├── .gitignore             # Git ignore rules

└── README.md              # Project documentation

```



---



\# Data Fields Collected



The scraper collects the following product information:



| Field        | Description              |

| ------------ | ------------------------ |

| Category     | Product category         |

| Subcategory  | Product subcategory      |

| Title        | Product name             |

| Price        | Normalized numeric price |

| URL          | Product page link        |

| Description  | Product description      |

| Review Count | Number of reviews        |

| Availability | Stock status             |



---



\# Environment Setup



\## Prerequisites



\* Python \*\*3.8+\*\*

\* \*\*uv package manager\*\*



Install uv:



```

pip install uv

```



---



\# Installation



Navigate to the project folder:



```

cd T-T-Quiz

```



Install dependencies:



```

uv sync

```



Or manually install packages:



```

uv add requests beautifulsoup4 pandas lxml

```



Verify Python:



```

uv run python --version

```



---



\# Running the Scraper



Run the project using uv:



```

uv run src/main.py

```



Or using Python:



```

python src/main.py

```



---



\# Output Files



The scraper generates CSV files inside the \*\*data/\*\* folder.



Example structure:



```

data/

├── products.csv

└── category\_summary.csv

```



\### products.csv



Contains all scraped product data:



```

category,subcategory,title,price,url,description,review\_count,availability

```



\### category\_summary.csv



Contains aggregated statistics:



```

Category,Subcategory,Product\_Count,Avg\_Price,Min\_Price,Max\_Price,Avg\_Review\_Count

```



---



\# Code Modules



\## crawler.py



Handles navigation, pagination, and product discovery.



Key methods:



\* discover\_categories\_and\_subcategories()

\* scrape\_products\_with\_pagination()

\* scrape\_product\_details()

\* crawl\_all()



Example:



```python

crawler = WebCrawler(base\_url, delay=0.5)

products = crawler.crawl\_all()

```



---



\# parsers.py



Responsible for \*\*extracting information from HTML pages\*\* using BeautifulSoup.



Functions include:



\* parse\_product\_listing()

\* parse\_product\_detail()

\* parse\_categories()

\* parse\_subcategories()

\* parse\_pagination()



---



\# exporters.py



Handles \*\*data export and statistical summaries\*\*.



Key methods:



\* export\_products()

\* export\_category\_summary()

\* get\_statistics()



---



\# utils.py



Contains helper utilities for data processing.



| Function                | Purpose                          |

| ----------------------- | -------------------------------- |

| normalize\_price()       | Convert price string to float    |

| clean\_text()            | Remove unnecessary whitespace    |

| resolve\_url()           | Convert relative URL to absolute |

| remove\_duplicates()     | Remove duplicate products        |

| validate\_product\_data() | Ensure required fields exist     |



---



\# Deduplication Strategy



The scraper avoids duplicate entries using:



\### 1. Visited URL tracking



```python

if url in self.visited\_urls:

&nbsp;   continue

```



\### 2. Post-scraping duplicate removal



```python

all\_products = remove\_duplicates(all\_products, key='url')

```



---



\# Data Cleaning



\### Price Normalization



\* Removes currency symbols

\* Converts to float

\* Handles decimal separators



\### Text Cleaning



\* Removes extra spaces

\* Strips leading/trailing whitespace



\### Missing Data Handling



\* Missing prices → `None`

\* Missing descriptions → default text

\* Missing reviews → `0`



---



\# Error Handling



Each request includes:



\* Timeout protection

\* Exception handling

\* Informative error messages



Example:



```python

try:

&nbsp;   response = session.get(url, timeout=10)

&nbsp;   response.raise\_for\_status()

except requests.RequestException as e:

&nbsp;   print(f"Error fetching {url}: {e}")

```



---



\# Rate Limiting



The scraper includes delay between requests to prevent server overload.



Example:



```python

crawler = WebCrawler(base\_url, delay=0.5)

```



---



\# Dependencies



| Package        | Purpose                        |

| -------------- | ------------------------------ |

| requests       | HTTP requests                  |

| beautifulsoup4 | HTML parsing                   |

| lxml           | Fast HTML parser               |

| pandas         | Data processing and CSV export |



---



\# Troubleshooting



\### Module Not Found



Run:



```

uv sync

```



---



\### No Products Found



Check:



\* Website URL

\* HTML structure

\* CSS selectors inside `parsers.py`



---



\# Learning Outcomes



This project demonstrates:



✔ Web scraping with Requests \& BeautifulSoup

✔ Pagination crawling

✔ Data cleaning \& normalization

✔ Modular Python architecture

✔ CSV export with Pandas

✔ Error handling in scraping

✔ Structured project documentation



---



\# Author



\*\*Muhammad Taha Naeem\*\*

University of Central Punjab



---



\# License



Educational Use Only



