from langchain_openai import ChatOpenAI
from app.schemas import PlanSchema
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

llm = ChatOpenAI(
    model = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY,
)

def planner_node(state):
    idea = state["idea"]
    memory = state["memory"] if "memory" in state else ""
    
    structured_llm = llm.with_structured_output(PlanSchema)
    
    result = structured_llm.invoke(
        f"""
        You are a startup strategist.
        Analyze the following startup idea and return structured data.
        
        Startup Idea:
        {idea}
        
        Relevant Context (If Useful):
        {memory}
        
        Generate a structured startup plan.
        Be concise and structured.
        """
    )
    
    return {
        "plan" : result
    }