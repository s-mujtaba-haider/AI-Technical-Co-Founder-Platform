from fastapi import FastAPI
from pydantic import BaseModel
from app.graph.builder import build_graph

app = FastAPI()
graph = build_graph()

class IdeaInput(BaseModel):
    idea: str
    
@app.post("/generate")
def generate(data: IdeaInput):
    result = graph.invoke({
        "idea": data.idea,
        "plan": None,
        "architecture": None,
        "codegen": None
    })
    
    return {
        "idea": result["idea"],
        "plan": result["plan"].model_dump(),
        "architecture": result["architecture"].model_dump(),
        "codegen": result["code"]
    }