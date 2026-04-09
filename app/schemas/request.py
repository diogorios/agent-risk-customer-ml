from pydantic import BaseModel

class CustomerRiskRequest(BaseModel):
    dias_medio_atraso: float
    qtd_titulos_abertos: int
    valor_total_aberto: float
    tempo_relacionamento: float
    ticket_medio: float
