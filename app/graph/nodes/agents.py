from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE
from app.schemas import AgentOutput
from langsmith import traceable

llm = ChatOpenAI(
    model_name = MODEL_NAME,
    temperature = TEMPERATURE,
    openai_api_key = OPENAI_API_KEY
)

def make_agent(role, task):
    @traceable(name="idea_validator")
    def agent_node(state):
        idea = state.get("idea", "")
        
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
        
        structured = llm.with_structured_output(AgentOutput)
        try:
            result = structured.invoke(prompt)
        except Exception as e:
            # on failure return a safe, serializable minimal response
            return {role: {"insight": "", "score": 0, "notes": f"invoke_failed: {e}"}}
        
        # normalize to plain dict
        try:
            output = result.model_dump()
        except Exception:
            try:
                output = dict(result)
            except Exception:
                output = {"insight": str(result), "score": 0, "notes": "unserializable_result"}
        
        return {role: output}
        
    return agent_node