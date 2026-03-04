from pydantic import BaseModel
from typing import List, Literal, Dict

class PlanSchema(BaseModel):
    problem_statement: str
    target_users: str
    mvp_features: List[str]
    advanced_features: List[str]
    revenue_model: str
    risks: str
    
    model_config = {
        "json_schema_extra": {
            "required":[
                "problem_statement",
                "target_users",
                "mvp_features",
                "advanced_features",
                "revenue_model",
                "risks"
            ]
        }
    }
    
class ArchitectureSchema(BaseModel):
    tech_stack: List[str]
    backend_architecture: str
    database_schema: str
    api_design: str
    scaling_strategy: str
    
    model_config = {
        "json_schema_extra":{
            "required": [
                "tech_stack",
                "backend_architecture",
                "database_schema",
                "api_design",
                "scaling_strategy"
            ]
        }
    }
    
class ReflectionSchema(BaseModel):
    quality: Literal["good", "bad"]
    comments: str
    suggestions: List[str]
    
    model_config = {
        "json_schema_extra":{
            "required":[
                "quality",
                "comments",
                "suggestions"
            ]
        }
    }
    
class CodegenSchema(BaseModel):
    folders: List[str]
    files: Dict[str, str]

    model_config = {
        "json_schema_extra": {
            "required": [
                "folders", 
                "files"
            ]
        }
    }

class AgentOutput(BaseModel):
    insight: str
    score: int
    notes: str

    model_config = {
        "json_schema_extra": {
            "required": ["insight", "score", "notes"]
        }
    }

class AggregatorOutput(BaseModel):
    recommendation: str
    confidence: int
    summary: str

    model_config = {
        "json_schema_extra": {
            "required": ["recommendation", "confidence", "summary"]
        }
    }