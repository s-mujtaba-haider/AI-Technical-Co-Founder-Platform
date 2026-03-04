from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE
from app.schemas import AggregatorOutput

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY
)

def aggregator_node(state):
    results = {
        "idea_validator": state.get("idea_validator"),
        "market_analyst": state.get("market_analyst"),
        "competitor_researcher": state.get("competitor_researcher"),
        "pricing_strategist": state.get("pricing_strategist"),
        "technical_architect": state.get("technical_architect"),
        "security_analyst": state.get("security_analyst"),
        "devops_advisor": state.get("devops_advisor")
    }
    
    prompt = f"""
    
    Aggregate these opinions and give final recommendations.
    
    Opinions:
    {results}
    
    Return JSON:
    {{
        "recommendation": "...",
        "confidence": 0-100,
        "summary": "..."
    }}
    
    """
    
    result = llm.with_structured_output(AggregatorOutput).invoke(prompt)
    
    return {
        "swarm": results,
        "recommendation": result
    }