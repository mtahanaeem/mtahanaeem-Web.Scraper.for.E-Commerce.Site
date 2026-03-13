"""Export scraped data to CSV files."""

import pandas as pd
from typing import List, Dict
from pathlib import Path


class CSVExporter:
    """Export product data to CSV files."""
    
    def __init__(self, output_dir: str = "output"):
        """Initialize exporter with output directory."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def export_products(self, products: List[Dict], filename: str = "products.csv") -> str:
        """
        Export products to CSV.
        
        Args:
            products: List of product dictionaries
            filename: Output filename
        
        Returns:
            Path to created file
        """
        if not products:
            print("No products to export")
            return None
        
        # Create DataFrame
        df = pd.DataFrame(products)
        
        # Ensure required columns exist
        required_columns = ['category', 'subcategory', 'title', 'price', 'url', 
                          'description', 'review_count', 'availability']
        
        for col in required_columns:
            if col not in df.columns:
                df[col] = None
        
        # Reorder columns
        column_order = required_columns + [col for col in df.columns if col not in required_columns]
        df = df[column_order]
        
        # Remove duplicate columns
        df = df.loc[:, ~df.columns.duplicated()]
        
        # Save to CSV
        filepath = self.output_dir / filename
        df.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"Exported {len(df)} products to {filepath}")
        return str(filepath)
    
    def export_category_summary(self, products: List[Dict], 
                               filename: str = "category_summary.csv") -> str:
        """
        Export category summary with statistics.
        
        Args:
            products: List of product dictionaries
            filename: Output filename
        
        Returns:
            Path to created file
        """
        if not products:
            print("No products for summary")
            return None
        
        df = pd.DataFrame(products)
        
        # Group by category and subcategory
        summary_data = []
        
        for (category, subcategory), group in df.groupby(['category', 'subcategory']):
            prices = pd.to_numeric(group['price'], errors='coerce').dropna()
            
            summary_data.append({
                'Category': category,
                'Subcategory': subcategory,
                'Product_Count': len(group),
                'Avg_Price': round(prices.mean(), 2) if len(prices) > 0 else None,
                'Min_Price': round(prices.min(), 2) if len(prices) > 0 else None,
                'Max_Price': round(prices.max(), 2) if len(prices) > 0 else None,
                'Avg_Review_Count': round(group['review_count'].astype(float).mean(), 1) 
                                    if 'review_count' in group.columns else 0
            })
        
        summary_df = pd.DataFrame(summary_data)
        
        # Save to CSV
        filepath = self.output_dir / filename
        summary_df.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"Exported category summary to {filepath}")
        return str(filepath)
    
    def get_statistics(self, products: List[Dict]) -> Dict:
        """
        Calculate and return scraping statistics.
        
        Args:
            products: List of product dictionaries
        
        Returns:
            Dictionary with statistics
        """
        if not products:
            return {}
        
        df = pd.DataFrame(products)
        prices = pd.to_numeric(df['price'], errors='coerce').dropna()
        
        stats = {
            'Total Products': len(df),
            'Unique Categories': df['category'].nunique(),
            'Unique Subcategories': df['subcategory'].nunique(),
            'Avg Price': round(prices.mean(), 2) if len(prices) > 0 else None,
            'Min Price': round(prices.min(), 2) if len(prices) > 0 else None,
            'Max Price': round(prices.max(), 2) if len(prices) > 0 else None,
            'Products with Description': len(df[df['description'].notna()]),
            'Avg Review Count': round(df.get('review_count', pd.Series([0])).astype(float).mean(), 1)
        }
        
        return stats
