from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from app.graph.builder import build_graph
from app.services.memory import MemoryService
from pypdf import PdfReader
import io

app = FastAPI()
memory = MemoryService()
graph = build_graph()

class IdeaInput(BaseModel):
    idea: str

@app.post("/generate")
def generate(data: IdeaInput):
    result = graph.invoke({
        "idea": data.idea,
        "plan": None,
        "swarm": None,
        "architecture": None,
        "codegen": None
    })
    
    return {
        "idea": result["idea"],
        "plan": result["plan"].model_dump(),
        "swarm": result["swarm"],
        "architecture": result["architecture"].model_dump(),
        "codegen": result["code"]
    }
    
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    
    content = await file.read()
    if file.filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        text = "\n".join(page.extract_text() for page in reader.pages)
    else:
        text = content.decode("utf-8", errors="ignore")
        
    documents = text.split("\n\n")
    memory.load_or_create(documents)
    
    return {"status": "stored", "chunks": len(documents)}

@app.get("/search")
def search(q: str):
    results = memory.search(q)
    
    return {
        "query": q,
        "results": [r.page_content for r in results]
    }