from app.services.memory import MemoryService
memory = MemoryService()

def memory_node(state):
    idea = state["idea"] if "idea" in state else ""
    
    results = memory.search(idea)
    
    context = "\n".join([r.page_content for r in results])
    
    return {
        "memory": context
    }