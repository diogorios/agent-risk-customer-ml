def generate_credit_decision(features: dict, prediction: dict):
    score = prediction["score"]
    nivel = prediction["nivel_risco"]

    motivos = []

    red_flags = 0
    yellow_flags = 0

    # RED FLAGS
    if features["dias_medio_atraso"] > 15:
        motivos.append(
            f"Média de atraso alta ({features['dias_medio_atraso']:.1f} dias)"
        )
        red_flags += 1
    elif features["dias_medio_atraso"] > 5:
        motivos.append(
            f"Média de atraso moderada ({features['dias_medio_atraso']:.1f} dias)"
        )
        yellow_flags += 1

    if features["qtd_titulos_abertos"] >= 3:
        motivos.append(
            f"{features['qtd_titulos_abertos']} títulos em aberto"
        )
        red_flags += 1
    elif features["qtd_titulos_abertos"] >= 1:
        motivos.append(
            f"{features['qtd_titulos_abertos']} título(s) em aberto"
        )
        yellow_flags += 1

    if features["maior_atraso"] >= 30:
        motivos.append(
            f"Maior atraso recente de {features['maior_atraso']} dias"
        )
        red_flags += 1
    elif features["maior_atraso"] >= 10:
        motivos.append(
            f"Atrasos recentes recorrentes ({features['maior_atraso']} dias)"
        )
        yellow_flags += 1

    if features["percentual_atraso"] >= 0.30:
        motivos.append("Percentual histórico de atraso elevado")
        red_flags += 1
    elif features["percentual_atraso"] >= 0.10:
        motivos.append("Percentual histórico de atraso moderado")
        yellow_flags += 1

    # AJUSTES DE SCORE
    score += yellow_flags * 10
    score += red_flags * 20

    score = min(score, 100)

    # Reclassificação Final
    if score >= 70:
        nivel = "ALTO"
    elif score >= 40:
        nivel = "MEDIO"
    else:
        nivel = "BAIXO"

    # Decisão final
    if nivel == "ALTO":
        parecer = "Cliente apresenta risco elevado de inadimplência."
        acoes = [
            "Solicitar aprovação manual",
            "Reduzir limite de crédito",
            "Exigir entrada mínima"
        ]
        limite = 0
        entrada = 50

    elif nivel == "MEDIO":
        parecer = "Cliente apresenta risco moderado, exigindo cautela."
        acoes = [
            "Liberar crédito parcial",
            "Aplicar limite reduzido",
            "Monitorar próximas compras"
        ]
        limite = 3000
        entrada = 20

    else:
        parecer = "Cliente apto para crédito dentro da política padrão."
        acoes = [
            "Crédito aprovado",
            "Manter limite padrão"
        ]
        limite = 10000
        entrada = 0

    return {
        "score_ajustado": score,
        "nivel_risco_ajustado": nivel,
        "parecer_credito": parecer,
        "motivos": motivos,
        "acao_sugerida": acoes,
        "limite_recomendado": limite,
        "entrada_minima": entrada
    }