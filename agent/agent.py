from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

from config.logger import get_logger 

logger = get_logger("agent")

class Agent:
    
    def __init__(self, llm, data_frame):
        
        try:
            
            self.agent = create_pandas_dataframe_agent(
                llm=llm,
                df=data_frame,
                verbose=True,
                return_intermediate_steps=True,
                handle_parsing_errors=True,
                
            )
        
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
        
        except Exception as e:
            logger.error(f"Error in agent initialization: {e}")
            raise
        
        