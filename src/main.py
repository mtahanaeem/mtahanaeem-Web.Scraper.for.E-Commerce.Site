"""Main entry point for web scraper."""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from scraper.crawler import WebCrawler
from scraper.exporters import CSVExporter


def main():
    """Run the web scraper."""
    
    # Target URL
    base_url = "https://webscraper.io/test-sites/e-commerce/static"
    
    print("=" * 60)
    print("Web Scraper for E-Commerce Site")
    print("=" * 60)
    print(f"Target: {base_url}\n")
    
    # Initialize crawler
    crawler = WebCrawler(base_url, delay=0.5)
    
    # Crawl and scrape
    products = crawler.crawl_all()
    
    if not products:
        print("No products found!")
        return
    
    # Export data
    exporter = CSVExporter(output_dir="output")
    
    exporter.export_products(products, "products.csv")
    exporter.export_category_summary(products, "category_summary.csv")
    
    # Display statistics
    stats = exporter.get_statistics(products)
    
    print("\n" + "=" * 60)
    print("Scraping Statistics")
    print("=" * 60)
    for key, value in stats.items():
        print(f"{key}: {value}")
    print("=" * 60)


if __name__ == "__main__":
    main()
