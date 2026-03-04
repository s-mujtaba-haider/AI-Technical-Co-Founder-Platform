from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE
from app.schemas import AgentOutput

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY
)

def make_agent(role, task):
    def agent_node(state):
        idea = state["idea"]
        
        prompt = f"""
        
        You are a {role}.
        
        Task:
        {task}
        
        Idea:
        {idea}
        
        Return structured JSON:
        {{
            "insight": "...",
            "score": 0-100,
            "notes": "..."
        }}
        
        """
        
        result = llm.with_structured_output(AgentOutput).invoke(prompt)
        return {role: result}
    
    return agent_node