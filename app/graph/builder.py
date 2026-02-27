from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes.memory import memory_node
from app.graph.nodes.planner import planner_node
from app.graph.nodes.architect import architect_node
from app.graph.nodes.reflection import reflection_node
from app.graph.nodes.codegen import codegen_node
from app.graph.nodes.log_analyzer import log_analyzer_node
from app.graph.nodes.optimizer import optimizer_node

def route_reflection(state):
    reflection = state["reflection"]

    # support both plain dicts and Pydantic-like objects
    if isinstance(reflection, dict):
        quality = reflection.get("quality")
    else:
        quality = getattr(reflection, "quality", None)

    if quality == "bad":
        return "architect"

    return "codegen"


def build_graph():
    builder = StateGraph(GraphState)

    # nodes
    builder.add_node("memory", memory_node)
    builder.add_node("planner", planner_node)
    builder.add_node("architect", architect_node)
    builder.add_node("reflection", reflection_node)
    builder.add_node("codegen", codegen_node)
    builder.add_node("log_analyzer", log_analyzer_node)
    builder.add_node("optimizer", optimizer_node)

    # entry
    builder.set_entry_point("memory")

    # edges
    builder.add_edge("memory", "planner")
    builder.add_edge("planner", "architect")
    builder.add_edge("architect", "reflection")

    # conditional from reflection
    builder.add_conditional_edges(
        "reflection",
        route_reflection,
        {
            "architect": "architect",
            "codegen": "codegen"
        }
    )

    # final
    builder.add_edge("codegen", "log_analyzer")
    builder.add_edge("log_analyzer", "optimizer")
    builder.add_edge("optimizer", END)
    
    return builder.compile()