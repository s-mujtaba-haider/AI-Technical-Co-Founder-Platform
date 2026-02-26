from langchain_openai import ChatOpenAI
from app.schemas import ArchitectureSchema
from app.config import MODEL_NAME, TEMPERATURE, OPENAI_API_KEY

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY,
)



def architect_node(state):
    plan = state["plan"]
    structured_llm = llm.with_structured_output(ArchitectureSchema)
    
    result = structured_llm.invoke(
        f"""
        You are a senior software architect.
        
        Design the technical architecture  for this startup plan.
        
        Startup Plan:
        {plan}
        """
    )
    
    return {
        "architecture": result
    }

