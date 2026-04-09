from fastapi import FastAPI
from app.schemas.request import CustomerRiskRequest
from app.schemas.response import CustomerRiskResponse
from app.ml.predictor import predict_customer_risk
from app.services.explainer import explain_prediction


app = FastAPI(title="AI Credit Risk API")


@app.get("/")
def health_check():
    return {"status": "online"}


@app.post("/avaliar_cliente", response_model=CustomerRiskResponse)
def avaliar_cliente(payload: CustomerRiskRequest):
    data = payload.dict()

    prediction = predict_customer_risk(data)
    explanation = explain_prediction(data)

    return {
        **prediction,
        "explicacao": explanation
    }