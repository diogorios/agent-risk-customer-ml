import joblib


model = joblib.load("app/ml/model.pkl")


FEATURE_NAMES = [
    "dias médio atraso",
    "títulos em aberto",
    "valor total aberto",
    "tempo relacionamento",
    "ticket médio"
]


def explain_prediction(data: dict):
    coefs = model.coef_[0]

    values = [
        data["dias_medio_atraso"],
        data["qtd_titulos_abertos"],
        data["valor_total_aberto"],
        data["tempo_relacionamento"],
        data["ticket_medio"]
    ]

    impacts = []

    for name, coef, value in zip(FEATURE_NAMES, coefs, values):
        impact = coef * value
        impacts.append((name, impact))

    impacts.sort(key=lambda x: abs(x[1]), reverse=True)

    explanation = []

    for name, impact in impacts[:3]:
        sign = "+" if impact > 0 else "-"
        explanation.append(f"{sign} influência relevante de {name}")

    return explanation