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
        
    def agent_response(self, query):
        
        try:
            
            if not query:
                raise ValueError("Query is empty or none")
            
            logger.info("Response is fetching...")
            response = self.agent.invoke(query)
            logger.info("Response fetched")
            
            return response['output']
        
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
        
        except Exception as e:
            logger.error(f"Error in agent response: {e}")
            raise
        