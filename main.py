
from config.logger import get_logger
from data_extractor.data_extract import DataClass
from model_config.llm_model import LLMModel
from agent.agent import Agent



logger = get_logger("main")

def init(dataset_path, query):
    
    try:
        
        if not dataset_path:
            raise ValueError("Dataset path is not declared")
        
        if not query:
            raise ValueError("User query is missing")
        
        logger.info("Dataset loading...")
        dataset = DataClass(dataset_path)
        
        logger.info("LLM loading...")
        llm_model = LLMModel()
        
        logger.info("Panda Agent loading...")
        agent = Agent(llm_model,dataset)
        
        return agent
    
    except ValueError as e:
            logger.error(f"Value error: {e}")
            raise

    except Exception as e:
        logger.error(f"Error in agent initialization: {e}")
        raise
    
        
        
        
        
        
    