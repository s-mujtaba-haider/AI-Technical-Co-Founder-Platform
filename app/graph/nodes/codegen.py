from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE
from app.schemas import PlanSchema, ArchitectureSchema, CodegenSchema

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY,
)

def codegen_node(state):
    plan: PlanSchema = state["plan"]
    architecture: ArchitectureSchema = state["architecture"]
    
    prompt = f"""
    You are a senior backend developer.
    
    Generate FastAPI project structure based on:
    
    PLAN:
    {plan}
    
    ARCHITECTURE:
    {architecture}
    
    Return only code and project structure in JSON:
    
    {{
        "folders": [...],
        "files": {{
            "path": "content"
        }}
    }}
    """
    
    structured_llm = llm.with_structured_output(CodegenSchema, method="json_mode")
    
    result = structured_llm.invoke(prompt)
    
    return {
        "code" : result
    }