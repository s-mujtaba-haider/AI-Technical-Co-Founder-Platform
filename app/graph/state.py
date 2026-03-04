from typing import TypedDict, Optional, Dict
from app.schemas import PlanSchema, ArchitectureSchema

class GraphState(TypedDict):
    idea: str
    plan: Optional[PlanSchema]
    architecture:Optional[ArchitectureSchema]
    code: Optional[dict]
    reflection: Optional[dict]
    memory: Optional[str]
    logs: Optional[str]
    log_analysis: Optional[str]
    optimization: Optional[str]
    swarm: Optional[Dict]