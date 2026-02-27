from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY,
)

def optimizer_node(state):
    plan = state["plan"]
    architecture = state["architecture"]
    log_analysis = state["log_analysis"]
    
    prompt = f"""
    You are a principal software architect.
    
    Based on:
    
    Startup Plan:
    {plan}
    
    Architecture:
    {architecture}
    
    Log Analysis:
    {log_analysis}
    
    Suggest:
    
    - Code Improvements
    - Architecture Optimizations
    - Scaling Improvements
    - Security Hardening
    - Cost Reduction Strategies
    
    Be Practical and production-ready.
    """
    
    result = llm.invoke(prompt)
    
    return {
        "optimization": result.content
    }