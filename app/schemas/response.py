from pydantic import BaseModel
from typing import List


class CustomerRiskResponse(BaseModel):
    nome_cliente_v3: str
    score: int
    nivel_risco: str
    parecer_credito: str
    motivos: List[str]
    acao_sugerida: List[str]
    limite_recomendado: float
    entrada_minima: float