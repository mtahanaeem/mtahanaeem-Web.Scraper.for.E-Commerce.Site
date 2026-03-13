"""Web crawler for navigating through website structure."""

import requests
from typing import List, Dict, Optional
from urllib.parse import urljoin
from .parsers import ProductParser
from .utils import remove_duplicates
import time


class WebCrawler:
    """Crawl website structure and products."""
    
    def __init__(self, base_url: str, delay: float = 0.5):
        """
        Initialize crawler.
        
        Args:
            base_url: Starting URL
            delay: Delay between requests in seconds
        """
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.parser = ProductParser(base_url)
        self.visited_urls = set()
    
    def fetch_page(self, url: str) -> Optional[str]:
        """
        Fetch a page with error handling.
        
        Args:
            url: URL to fetch
        
        Returns:
            HTML content or None if error
        """
        try:
            time.sleep(self.delay)  # Rate limiting
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def discover_categories_and_subcategories(self) -> List[Dict]:
        """
        Discover all categories and subcategories.
        
        Returns:
            List of category dictionaries with subcategories
        """
        html = self.fetch_page(self.base_url)
        if not html:
            return []
        
        categories_list = []
        categories = self.parser.parse_categories(html)
        
        for category in categories:
            cat_url = category['url']
            if cat_url in self.visited_urls:
                continue
            
            self.visited_urls.add(cat_url)
            
            cat_html = self.fetch_page(cat_url)
            if not cat_html:
                continue
            
            subcategories = self.parser.parse_subcategories(cat_html)
            
            category['subcategories'] = [
                {
                    'name': sub['name'],
                    'url': sub['url']
                }
                for sub in subcategories
            ]
            
            categories_list.append(category)
            print(f"Discovered category: {category['name']} with {len(subcategories)} subcategories")
        
        return categories_list
    
    def scrape_products_with_pagination(self, category_url: str, 
                                       category_name: str, 
                                       subcategory_name: str) -> List[Dict]:
        """
        Scrape all products from a category with pagination.
        
        Args:
            category_url: URL of category/subcategory
            category_name: Name of parent category
            subcategory_name: Name of subcategory
        
        Returns:
            List of product dictionaries
        """
        all_products = []
        current_url = category_url
        page_count = 0
        
        while current_url and page_count < 10:  # Limit to 10 pages per category
            print(f"Scraping: {subcategory_name} (Page {page_count + 1})")
            
            if current_url in self.visited_urls:
                break
            self.visited_urls.add(current_url)
            
            html = self.fetch_page(current_url)
            if not html:
                break
            
            # Parse products
            products = self.parser.parse_product_listing(html)
            
            for product in products:
                product['category'] = category_name
                product['subcategory'] = subcategory_name
            
            all_products.extend(products)
            print(f"Found {len(products)} products on page {page_count + 1}")
            
            # Get next page
            current_url = self.parser.parse_pagination(html)
            page_count += 1
        
        return all_products
    
    def scrape_product_details(self, products: List[Dict]) -> List[Dict]:
        """
        Scrape detail pages for products.
        
        Args:
            products: List of product dictionaries with URLs
        
        Returns:
            List of enriched product dictionaries
        """
        detailed_products = []
        
        for idx, product in enumerate(products):
            if idx % 10 == 0:
                print(f"Scraping details: {idx}/{len(products)}")
            
            url = product.get('url')
            if not url or url in self.visited_urls:
                detailed_products.append(product)
                continue
            
            self.visited_urls.add(url)
            
            html = self.fetch_page(url)
            if html:
                details = self.parser.parse_product_detail(html, url)
                product.update(details)
            
            detailed_products.append(product)
        
        return detailed_products
    
    def crawl_all(self) -> List[Dict]:
        """
        Crawl entire website for products.
        
        Returns:
            List of all products with all details
        """
        print("Starting web scraping...")
        print(f"Base URL: {self.base_url}\n")
        
        # Discover categories and subcategories
        categories = self.discover_categories_and_subcategories()
        
        if not categories:
            print("No categories found. Trying direct scrape of base URL...")
            html = self.fetch_page(self.base_url)
            if not html:
                return []
            categories = [{'name': 'Default', 'url': self.base_url, 'subcategories': []}]
        
        all_products = []
        
        # Scrape products from each category/subcategory
        for category in categories:
            cat_name = category['name']
            
            if category.get('subcategories'):
                for subcategory in category['subcategories']:
                    subcat_name = subcategory['name']
                    subcat_url = subcategory['url']
                    
                    products = self.scrape_products_with_pagination(
                        subcat_url, cat_name, subcat_name
                    )
                    all_products.extend(products)
            else:
                # Scrape category directly if no subcategories
                products = self.scrape_products_with_pagination(
                    category['url'], cat_name, 'General'
                )
                all_products.extend(products)
        
        print(f"\nFound {len(all_products)} total products")
        
        # Remove duplicates
        all_products = remove_duplicates(all_products, key='url')
        print(f"After deduplication: {len(all_products)} unique products")
        
        # Scrape product details
        print("\nScraping product details...")
        all_products = self.scrape_product_details(all_products)
        
        print("Scraping complete!")
        return all_products
