import logging

def get_logger(name:str):
    
    try:
        if not name:
            raise ValueError("Logger name is empty or none")
            
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)% - %(name)% - %(levelname)s - %(message)s"
        )
        
        name = name.join("-logger")
        logger = logging.getLogger(name)
        return logger
    
    except ValueError as e:
        print(f"Value error: {e}")
        raise

    except Exception as e:
        print(f"Error in {name} logger: {e}")
        raise