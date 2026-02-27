from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY,
)

def log_analyzer_node(state):
    logs = state["logs"] if "logs" in state else ""
    
    if not logs:
        return {
            "log_analysis": "No Logs Provided"
        }
        
    prompt = f"""
    You are a senior DevOps Engineer.
    
    Analyze the following production logs.
    
    Identify:
    - Errors
    - Performance Bottlenecks
    - Security Risks
    - Root Causes
    
    Logs:
    {logs[:5000]}
    
    Be structured and concise.
    
    """
    
    result = llm.invoke(prompt)
    
    return {
        "log_analysis": result.content
    }