# Chat With Your DataFrame using LangChain 🤖📊

Talk to your CSV data in plain English — ask questions, get answers, and generate charts on the fly, powered by **LangChain**, **LangChain-HuggingFace**, and the `create_pandas_dataframe_agent`.

## Overview

This project turns a pandas DataFrame into a conversational data analyst. Instead of writing pandas code or SQL queries by hand, you simply ask natural-language questions like:

- "How many rows are in this file?"
- "Generate a bar chart of the gender count."
- "Create box plots showing the relationship between free time and final grades."

Under the hood, LangChain's `create_pandas_dataframe_agent` uses an LLM to translate your question into executable Python/pandas code, runs it against the DataFrame, and returns both the answer and (when relevant) a chart.

> **Note:** This project is adapted from an IBM Skills Network lab that originally used IBM watsonx.ai. This version has been modified to use **`langchain-huggingface`**, letting you run the same workflow with open models hosted on the Hugging Face Hub (or a local Hugging Face pipeline) instead of watsonx.

## Features

- 💬 Ask questions about your dataset in plain English
- 📈 Generate bar charts, pie charts, box plots, and scatter plots via natural language prompts
- 🔍 Inspect the exact Python code the LLM generated to produce each answer/chart
- 🧪 Includes guided exercises for practicing prompt-driven data exploration

## Dataset

The demo uses the **Student Alcohol Consumption** dataset (`student-mat.csv`) from UCI Machine Learning / Kaggle, containing demographic, academic, and lifestyle data for 395 students from two Portuguese secondary schools.

## Tech Stack

| Component | Purpose |
|---|---|
| [LangChain](https://www.langchain.com/) | Orchestrates the conversational agent |
| [`langchain-huggingface`](https://python.langchain.com/docs/integrations/providers/huggingface/) | Connects LangChain to Hugging Face-hosted or local LLMs |
| `langchain-experimental` | Provides `create_pandas_dataframe_agent` |
| pandas | DataFrame handling |
| matplotlib / seaborn | Chart rendering |

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/chat-with-your-dataframe-langchain.git
cd chat-with-your-dataframe-langchain
```

### 2. Install dependencies

```bash
pip install langchain langchain-huggingface langchain-experimental pandas matplotlib seaborn
```

### 3. Set your Hugging Face credentials

Create a `.env` file or export an environment variable with your Hugging Face access token (required for calling hosted inference endpoints):

```bash
export HUGGINGFACEHUB_API_TOKEN="your_hf_token_here"
```

### 4. Configure the LLM

Replace the watsonx model initialization with a Hugging Face model, for example:

```python
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd

df = pd.read_csv("student-mat.csv")

llm_endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",  # or any model of your choice
    max_new_tokens=512,
    temperature=0,
)
llm = ChatHuggingFace(llm=llm_endpoint)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True,
)
```

### 5. Run the notebook

Open `chat-with-your-dataframe-using-langchain.ipynb` in Jupyter and run the cells in order.

## Example Prompts

```python
agent.invoke("How many rows of data are in this file?")
agent.invoke("Generate a bar chart to plot the gender count.")
agent.invoke("Generate a pie chart to display the average value of Walc for each gender.")
agent.invoke("Create box plots to analyze the relationship between freetime and G3.")
agent.invoke("Generate scatter plots to examine the correlation between Dalc and G3, and between Walc and G3.")
```

## Exercises Included

1. Relationship between parental education level and student grades
2. Impact of internet access at home on grades
3. Exploring the LLM-generated code behind a scatter plot of absences vs. grades

## Acknowledgements

Original lab content created for IBM Skills Network by Kang Wang, Wojciech Fulmyk, and Ricky Shi. This version has been adapted to replace IBM watsonx.ai with `langchain-huggingface` for an open-model workflow.

## License

This project is for educational purposes. Please check the license terms of the original dataset and any Hugging Face models you use.
