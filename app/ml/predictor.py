import joblib
import numpy as np
from pathlib import Path
import joblib


#model = joblib.load("app/ml/model.pkl")

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"

model = joblib.load(MODEL_PATH)


def classify_risk(score):
    if score >= 70:
        return "ALTO"
    elif score >= 40:
        return "MEDIO"
    return "BAIXO"


def predict_customer_risk(features: dict):
    X = np.array([[
        features["dias_medio_atraso"],
        features["qtd_titulos_abertos"],
        features["valor_total_aberto"],
        features["tempo_relacionamento"],
        features["ticket_medio"]
    ]])

    prob = model.predict_proba(X)[0][1]
    score = int(round(prob * 100))

    return {
        "score": score,
        "probabilidade": round(float(prob), 4),
        "nivel_risco": classify_risk(score)
    }