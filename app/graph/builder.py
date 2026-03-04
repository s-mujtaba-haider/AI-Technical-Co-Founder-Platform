from langgraph.graph import StateGraph, END
from app.graph.state import GraphState

from app.graph.nodes.memory import memory_node
from app.graph.nodes.planner import planner_node
from app.graph.nodes.architect import architect_node
from app.graph.nodes.reflection import reflection_node
from app.graph.nodes.codegen import codegen_node
from app.graph.nodes.log_analyzer import log_analyzer_node
from app.graph.nodes.optimizer import optimizer_node

from app.graph.nodes.swarm_agents import (
    idea_validator,
    market_analyst,
    competitor_researcher,
    pricing_strategist,
    technical_architect,
    security_analyst,
    devops_advisor,
)
from app.graph.nodes.aggregator import aggregator_node


def route_reflection(state):
    reflection = state["reflection"]

    if isinstance(reflection, dict):
        quality = reflection.get("quality")
    else:
        quality = getattr(reflection, "quality", None)

    return "architect" if quality == "bad" else "codegen"


def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("idea_validator", idea_validator)
    builder.add_node("market_analyst", market_analyst)
    builder.add_node("competitor", competitor_researcher)
    builder.add_node("pricing", pricing_strategist)
    builder.add_node("architect_agent", technical_architect)
    builder.add_node("security", security_analyst)
    builder.add_node("devops", devops_advisor)

    builder.add_node("aggregator", aggregator_node)

    builder.add_node("memory", memory_node)
    builder.add_node("planner", planner_node)
    builder.add_node("architect", architect_node)
    builder.add_node("reflection", reflection_node)
    builder.add_node("codegen", codegen_node)
    builder.add_node("log_analyzer", log_analyzer_node)
    builder.add_node("optimizer", optimizer_node)

    builder.set_entry_point("idea_validator")

    builder.add_edge("idea_validator", "market_analyst")
    builder.add_edge("market_analyst", "competitor")
    builder.add_edge("competitor", "pricing")
    builder.add_edge("pricing", "architect_agent")
    builder.add_edge("architect_agent", "security")
    builder.add_edge("security", "devops")
    builder.add_edge("devops", "aggregator")

    builder.add_edge("aggregator", "memory")
    builder.add_edge("memory", "planner")
    builder.add_edge("planner", "architect")
    builder.add_edge("architect", "reflection")

    builder.add_conditional_edges(
        "reflection",
        route_reflection,
        {
            "architect": "architect",
            "codegen": "codegen",
        },
    )

    builder.add_edge("codegen", "log_analyzer")
    builder.add_edge("log_analyzer", "optimizer")
    builder.add_edge("optimizer", END)

    return builder.compile()