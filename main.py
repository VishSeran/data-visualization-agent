
from app import Application
from config.logger import get_logger
import gradio as gr


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
    

import gradio as gr

def gradio_interface():

    with gr.Blocks() as interface:

        gr.Markdown("""
        # 📊 Pandas AI Agent
        
        Upload a CSV dataset and ask questions about your data.
        """)

        file_input = gr.File(
            label="Upload a CSV file",
            file_types=[".csv"]
        )

        question_input = gr.Textbox(
            label="Type your question here"
        )

        intermediate_checkbox = gr.Checkbox(
            label="Return Intermediate Steps"
        )

        response_output = gr.Textbox(
            label="Response"
        )

        intermediate_output = gr.Textbox(
            label="Intermediate Steps (Optional)",
            lines=10
        )

        submit_btn = gr.Button("Ask")

        submit_btn.click(
            fn=chatbot,
            inputs=[
                file_input,
                question_input,
                intermediate_checkbox
            ],
            outputs=[
                response_output,
                intermediate_output
            ]
        )

    return interface

if __name__ == "__main__":
    interface = gradio_interface()
    interface.launch()