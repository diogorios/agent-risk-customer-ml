from pydantic import BaseModel
from typing import List

class CustomerRiskResponse(BaseModel):
    score: int
    probabilidade_inadimplencia: float
    nivel_risco: str
    explicacao: List[str]
