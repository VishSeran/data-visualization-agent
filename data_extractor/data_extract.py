import pandas as pd
from config.logger import get_logger


logger = get_logger("data-extract")

class DataClass:
    
    def __init__(self, csv_path):
        
        try:
            
            if not csv_path:
                raise ValueError("CSV URL is required to process")
            
            self.data_frame = self.load_csv(csv_path)
            
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise

        except Exception as e:
            logger.error(f"Error in data class initialization: {e}")
            raise
        
    def load_csv(self, csv_path):
        
        try:
            df = pd.read_csv(csv_path)
            logger.info("CSV loaded successfully")
            return df
                
        except ValueError as e:
            logger.error(f"Value error: {e}")
            return False

        except Exception as e:
            logger.error(f"Error in load csv file: {e}")
            return False
            