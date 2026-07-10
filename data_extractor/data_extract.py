import pandas as pd

from config.logger import get_logger
from urllib.parse import urlparse

logger = get_logger("data-extract")

class DataClass:
    
    def __init__(self, csv_path):
        
        try:
            
            if not csv_path:
                raise ValueError("CSV URL is required to process")
            
            if urllib.parse
            
            
            
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise

        except Exception as e:
            logger.error(f"Error in data class initialization: {e}")
            raise
        
    def is_url(self, url):
        
        try:
            result = urlparse(url)
            return all(result.scheme,)
                
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise

        except Exception as e:
            logger.error(f"Error in URL check: {e}")
            raise
            