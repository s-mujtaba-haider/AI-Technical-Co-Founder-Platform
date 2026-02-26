from langchain_openai import ChatOpenAI
from app.config import MODEL_NAME, TEMPERATURE, OPENAI_API_KEY
from app.schemas import PlanSchema, ArchitectureSchema, ReflectionSchema

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY,
)

def reflection_node(state):
    plan: PlanSchema = state["plan"]
    architecture: ArchitectureSchema = state["architecture"]
    
    prompt = f"""
    You are a quality reviewer.
    
    Review the following:
    
    PLAN:
    {plan}
    
    ARCHITECTURE:
    {architecture}
    
    Evaluate quality and return structured JSON:
    
    {{
        "quality": "good" | "bad",
        "comments": "string",
        "suggestions": ["..."]
    }}
    """
    
    structured_llm = llm.with_structured_output(ReflectionSchema)
    
    result = structured_llm.invoke(prompt)
    
    return {
        "reflection": result
    }