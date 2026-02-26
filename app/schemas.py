from pydantic import BaseModel
from typing import List, Literal, Dict

class PlanSchema(BaseModel):
    problem_statement: str
    target_users: str
    mvp_features: List[str]
    advanced_features: List[str]
    revenue_model: str
    risks: str
    
class ArchitectureSchema(BaseModel):
    tech_stack: List[str]
    backend_architecture: str
    database_schema: str
    api_design: str
    scaling_strategy: str
    
class ReflectionSchema(BaseModel):
    quality: Literal["good", "bad"]
    comments: str
    suggestions: List[str]
    
class CodegenSchema(BaseModel):
    folders: List[str]
    files: Dict[str, str]

    model_config = {
        "json_schema_extra": {
            "required": ["folders", "files"]
        }
    }