
from app import Application
from config.logger import get_logger


logger = get_logger("main")


app = None
current_dataset = None

def chatbot(file, query, intermediate_steps):
    
    global app, current_dataset
    
    try:
        
        if file is None:
            return "Please upload a dataset."
        
        dataset_path = file.name
        
        if app is None or current_dataset != dataset_path:
            app = Application(dataset_path)
            current_dataset=dataset_path
        
        return app.ask(query, intermediate_steps)
    
    except ValueError as e:
                logger.error(f"Value error: {e}")
                raise

    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise