import joblib
import numpy as np


model = joblib.load("app/ml/model.pkl")


def classify_risk(score: int) -> str:
    if score >= 60:
        return "ALTO"
    elif score >= 30:
        return "MEDIO"
    return "BAIXO"


def predict_customer_risk(data: dict):
    features = np.array([[
        data["dias_medio_atraso"],
        data["qtd_titulos_abertos"],
        data["valor_total_aberto"],
        data["tempo_relacionamento"],
        data["ticket_medio"]
    ]])

    probability = model.predict_proba(features)[0][1]
    score = int(round(probability * 100))

    return {
        "score": score,
        "probabilidade_inadimplencia": round(float(probability), 4),
        "nivel_risco": classify_risk(score)
    }