"""Utility functions for cleaning and URL resolution."""

import re
from typing import Optional, Any
from urllib.parse import urljoin


def normalize_price(price_str: str) -> Optional[float]:
    """
    Normalize price string to float.
    
    Args:
        price_str: Price string (e.g., "$19.99", "19,99€")
    
    Returns:
        Float price or None if cannot parse
    """
    if not price_str or not isinstance(price_str, str):
        return None
    
    # Remove whitespace
    price_str = price_str.strip()
    
    # Extract numbers and decimal points
    match = re.search(r'[\d,\.]+', price_str)
    if not match:
        return None
    
    price_value = match.group()
    # Handle different decimal separators
    price_value = price_value.replace(',', '.')
    
    try:
        return float(price_value)
    except ValueError:
        return None


def clean_text(text: str) -> str:
    """
    Clean whitespace and normalize text.
    
    Args:
        text: Raw text to clean
    
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.strip()


def resolve_url(base_url: str, relative_url: str) -> str:
    """
    Resolve relative URLs to absolute URLs.
    
    Args:
        base_url: Base URL of the page
        relative_url: Relative or absolute URL
    
    Returns:
        Absolute URL
    """
    return urljoin(base_url, relative_url)


def remove_duplicates(items: list, key: str = 'url') -> list:
    """
    Remove duplicate items from list based on key.
    
    Args:
        items: List of dictionaries
        key: Key to check for duplicates (default: 'url')
    
    Returns:
        List with duplicates removed
    """
    seen = set()
    result = []
    
    for item in items:
        if item.get(key) not in seen:
            seen.add(item.get(key))
            result.append(item)
    
    return result


def validate_product_data(product: dict) -> bool:
    """
    Validate that product has all required fields.
    
    Args:
        product: Product dictionary
    
    Returns:
        True if valid, False otherwise
    """
    required_fields = ['title', 'category', 'subcategory', 'price', 'url']
    return all(field in product and product[field] for field in required_fields)
