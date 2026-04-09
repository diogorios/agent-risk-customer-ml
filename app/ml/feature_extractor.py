def extract_features(payload: dict):
    resumo = payload["contas_receber"]["resumo_historico"]
    titulos = payload["contas_receber"]["titulos_em_aberto"]

    total_titulos = resumo["total_titulos"] or 1

    ticket_medio = resumo["valor_total_faturado"] / total_titulos

    maior_atraso = max(
        [t["dias_atraso"] for t in titulos],
        default=0
    )

    percentual_atraso = (
        resumo["titulos_atrasados"] / total_titulos
    )

    return {
        "dias_medio_atraso": resumo["media_dias_atraso"] or 0,
        "qtd_titulos_abertos": len(titulos),
        "valor_total_aberto": resumo["valor_em_aberto"] or 0,
        "tempo_relacionamento": total_titulos,
        "ticket_medio": ticket_medio,
        "maior_atraso": maior_atraso,
        "percentual_atraso": percentual_atraso
    }