from app.graph.nodes.agents import make_agent

idea_validator = make_agent(
    "idea_validator",
    "Validate if idea is viable and clear"
)

market_analyst = make_agent(
    "market_analyst",
    "Analyze market size, demand, and trends."
)

competitor_researcher = make_agent(
    "competitor_researcher",
    "Identify competitors and gaps"
)

pricing_strategist = make_agent(
    "pricing_strategist",
    "Suggest revenue model and pricing."
)

technical_architect = make_agent(
    "technical_architect",
    "Design tech stack and architecture"
)

security_analyst = make_agent(
    "security_analyst",
    "Identify risks."
)

devops_advisor = make_agent(
    "devops_advisor",
    "Suggest deployment and ops strategy."
)