from typing import TypedDict, Optional, Dict, Any
from app.schemas import PlanSchema, ArchitectureSchema

class GraphState(TypedDict, total=False):
    idea: str
    plan: Optional[PlanSchema]
    architecture: Optional[ArchitectureSchema]
    code: Optional[dict]
    reflection: Optional[dict]
    memory: Optional[str]
    logs: Optional[str]
    log_analysis: Optional[str]
    optimization: Optional[str]
    swarm: Optional[Dict[str, Any]]

    # Swarm agent outputs (allow to be stored in state)
    idea_validator: Optional[Dict[str, Any]]
    market_analyst: Optional[Dict[str, Any]]
    competitor_researcher: Optional[Dict[str, Any]]
    pricing_strategist: Optional[Dict[str, Any]]
    technical_architect: Optional[Dict[str, Any]]
    security_analyst: Optional[Dict[str, Any]]
    devops_advisor: Optional[Dict[str, Any]]