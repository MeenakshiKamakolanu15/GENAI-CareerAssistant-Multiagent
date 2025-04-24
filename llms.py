from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os

def load_llm(llm_name):
    if llm_name == 'openai':
        # Options: gpt-4o, gpt-4-turbo, gpt-3.5-turbo
        return ChatOpenAI(
            model_name="gpt-4o",  # or gpt-4-turbo-2024-04-09
            openai_api_key=os.environ["OPENAI_API_KEY"],
            temperature=0.1,
            streaming=True
        )
    
    elif llm_name == 'groq':
        # Options: llama3-70b-8192, llama3-8b-8192, mixtral-8x7b-32768
        return ChatGroq(
            model_name="llama3-70b-8192",  # ✅ Updated from deprecated
            groq_api_key=os.environ["GROQ_API_KEY"],
            temperature=0.2
        )
    
    elif llm_name == "llama3":
        # Local Ollama model running
        return ChatOpenAI(
            model="llama3",
            base_url="http://localhost:11434/v1",
            temperature=0.0
        )
    
    else:
        raise ValueError(f"Unsupported LLM name: {llm_name}")