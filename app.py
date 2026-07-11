
from config.logger import get_logger
from data_extractor.data_extract import DataClass
from model_config.llm_model import LLMModel
from agent.agent import Agent

logger = get_logger("app")

class Application:
    
    def __init__(self, dataset_path):
        
        try:
            
            if not dataset_path:
                raise ValueError("Dataset path is not declared")
            
            logger.info("Dataset loading...")
            dataset = DataClass(dataset_path)
            
            logger.info("LLM loading...")
            llm_model = LLMModel()
            
            logger.info("Panda Agent loading...")
            self.agent = Agent(llm_model,dataset)
        
        except ValueError as e:
                logger.error(f"Value error: {e}")
                raise

        except Exception as e:
            logger.error(f"Error in agent initialization: {e}")
            raise
        
            
    def ask(self,query,return_intermediate:bool = False):
        
        try:
            
            if not query:
                raise ValueError("query is empty or none")
            
            response = self.agent.agent_response(query)
            
            if return_intermediate:
                steps = self.agent.return_intermediate_steps()
                
            return response, steps
            
        except ValueError as e:
                logger.error(f"Value error: {e}")
                raise

        except Exception as e:
            logger.error(f"Error in ask from agent: {e}")
            raise
        
        
        
        
    