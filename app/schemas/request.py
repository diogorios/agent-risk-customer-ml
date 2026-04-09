from pydantic import BaseModel
from typing import List


class ClienteSchema(BaseModel):
    codigo: int
    nome: str


class TituloSchema(BaseModel):
    documento: int
    parcela: int
    data_vencimento: str
    valor: float
    dias_atraso: int


class ResumoHistoricoSchema(BaseModel):
    total_titulos: int
    titulos_pagos: int
    titulos_atrasados: int
    media_dias_atraso: float
    valor_total_faturado: float
    valor_em_aberto: float


class ContasReceberSchema(BaseModel):
    titulos_em_aberto: List[TituloSchema]
    resumo_historico: ResumoHistoricoSchema


class CustomerRiskRequest(BaseModel):
    empresa_id: int
    filial: int
    data_referencia: str
    cliente: ClienteSchema
    contas_receber: ContasReceberSchema