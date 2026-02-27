from app.services.memory import MemoryService
memory = MemoryService()

def memory_node(state):
    idea = state["idea"] if "idea" in state else ""
    results = memory.search(idea, k=2)
    
    chunks = []
    
    for r in results:
        text = r.page_content.strip()
        chunks.append(text[:800])
    
    context = "\n".join(chunks)[:2000]
    
    return {
        "memory": context
    }