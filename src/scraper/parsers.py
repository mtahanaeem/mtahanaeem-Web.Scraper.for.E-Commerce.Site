"""Data extraction and parsing from HTML."""

from typing import Optional, Dict, List
from bs4 import BeautifulSoup
import re
from .utils import clean_text, normalize_price, resolve_url


class ProductParser:
    """Extract product data from HTML."""
    
    def __init__(self, base_url: str):
        """Initialize parser with base URL for relative URL resolution."""
        self.base_url = base_url
    
    def parse_product_listing(self, html: str) -> List[Dict]:
        """
        Parse products from a listing page.
        
        Args:
            html: HTML content of listing page
        
        Returns:
            List of product dictionaries with basic info
        """
        soup = BeautifulSoup(html, 'lxml')
        products = []
        
        # Find all product containers (adjust selector based on site structure)
        product_elements = soup.find_all('div', class_='product')
        
        for element in product_elements:
            try:
                product = self._extract_product_basic_info(element)
                if product:
                    products.append(product)
            except Exception as e:
                print(f"Error parsing product: {e}")
                continue
        
        return products
    
    def _extract_product_basic_info(self, element) -> Optional[Dict]:
        """Extract basic product info from element."""
        try:
            # Product title
            title_elem = element.find('h2', class_='title')
            if not title_elem:
                title_elem = element.find('a', class_='title')
            title = clean_text(title_elem.get_text()) if title_elem else None
            
            # Product price
            price_elem = element.find('h4', class_='price')
            price_str = clean_text(price_elem.get_text()) if price_elem else None
            price = normalize_price(price_str) if price_str else None
            
            # Product URL (detail page link)
            url_elem = element.find('a', class_='title')
            if not url_elem:
                url_elem = element.find('a', href=True)
            url = None
            if url_elem and url_elem.get('href'):
                url = resolve_url(self.base_url, url_elem['href'])
            
            if not title or not url:
                return None
            
            return {
                'title': title,
                'price': price,
                'price_str': price_str,
                'url': url,
            }
        except Exception as e:
            print(f"Error extracting product info: {e}")
            return None
    
    def parse_product_detail(self, html: str, product_url: str) -> Dict:
        """
        Parse product detail page.
        
        Args:
            html: HTML content of detail page
            product_url: URL of the product page
        
        Returns:
            Dictionary with detailed product info
        """
        soup = BeautifulSoup(html, 'lxml')
        
        detail = {
            'url': product_url,
        }
        
        try:
            # Description
            desc_elem = soup.find('p') or soup.find('div', class_='description')
            if desc_elem:
                detail['description'] = clean_text(desc_elem.get_text())
            else:
                detail['description'] = "No description available"
            
            # Review count
            review_elem = soup.find(text=re.compile(r'reviews?', re.I))
            if review_elem:
                match = re.search(r'(\d+)', str(review_elem))
                detail['review_count'] = int(match.group(1)) if match else 0
            else:
                detail['review_count'] = 0
            
            # Additional detail field: availability/stock status
            availability_text = soup.get_text(separator=' ')
            if 'in stock' in availability_text.lower():
                detail['availability'] = 'In Stock'
            elif 'out of stock' in availability_text.lower():
                detail['availability'] = 'Out of Stock'
            else:
                detail['availability'] = 'Unknown'
            
        except Exception as e:
            print(f"Error parsing product detail at {product_url}: {e}")
        
        return detail
    
    def parse_categories(self, html: str) -> List[Dict]:
        """
        Parse category links from navigation.
        
        Args:
            html: HTML content
        
        Returns:
            List of category dictionaries with name and URL
        """
        soup = BeautifulSoup(html, 'lxml')
        categories = []
        
        try:
            # Look for category links (adjust selector based on site structure)
            category_links = soup.find_all('a', class_='category-link')
            if not category_links:
                category_links = soup.find('ul', class_='nav')
                if category_links:
                    category_links = category_links.find_all('a')
            
            for link in category_links:
                href = link.get('href')
                if href:
                    cat_name = clean_text(link.get_text())
                    if cat_name:
                        categories.append({
                            'name': cat_name,
                            'url': resolve_url(self.base_url, href)
                        })
        except Exception as e:
            print(f"Error parsing categories: {e}")
        
        return categories
    
    def parse_subcategories(self, html: str) -> List[Dict]:
        """
        Parse subcategory links.
        
        Args:
            html: HTML content
        
        Returns:
            List of subcategory dictionaries
        """
        soup = BeautifulSoup(html, 'lxml')
        subcategories = []
        
        try:
            # Look for subcategory links
            subcat_links = soup.find_all('a', class_='subcategory-link')
            if not subcat_links:
                # Try alternative selector
                subcat_container = soup.find('div', class_='subcategories')
                if subcat_container:
                    subcat_links = subcat_container.find_all('a')
            
            for link in subcat_links:
                href = link.get('href')
                if href:
                    subcat_name = clean_text(link.get_text())
                    if subcat_name:
                        subcategories.append({
                            'name': subcat_name,
                            'url': resolve_url(self.base_url, href)
                        })
        except Exception as e:
            print(f"Error parsing subcategories: {e}")
        
        return subcategories
    
    def parse_pagination(self, html: str) -> Optional[str]:
        """
        Parse next page URL from pagination.
        
        Args:
            html: HTML content
        
        Returns:
            URL of next page or None
        """
        soup = BeautifulSoup(html, 'lxml')
        
        try:
            # Look for "next" button
            next_btn = soup.find('a', class_='page-link', text=re.compile(r'next', re.I))
            if not next_btn:
                next_btn = soup.find('a', text='>')
            if not next_btn:
                next_btn = soup.find('a', text=re.compile(r'next', re.I))
            
            if next_btn and next_btn.get('href'):
                return resolve_url(self.base_url, next_btn['href'])
        except Exception as e:
            print(f"Error parsing pagination: {e}")
        
        return None
