from fastapi import FastAPI
from app.schemas.request import CustomerRiskRequest
from app.schemas.response import CustomerRiskResponse
from app.ml.feature_extractor import extract_features
from app.ml.predictor import predict_customer_risk
from app.services.credit_policy_engine import generate_credit_decision


app = FastAPI(title="AI Credit Risk Engine")


@app.get("/")
def health():
    return {"status": "online"}


@app.post("/avaliar-risco-cliente", response_model=CustomerRiskResponse)
def avaliar_cliente(payload: CustomerRiskRequest):
    raw = payload.dict()

    features = extract_features(raw)

    prediction = predict_customer_risk(features)

    decision = generate_credit_decision(features, prediction)

    return {
        "nome_cliente_v3": payload.cliente.nome,
        "score": decision["score_ajustado"],
        "nivel_risco": decision["nivel_risco_ajustado"],
        **decision
    }