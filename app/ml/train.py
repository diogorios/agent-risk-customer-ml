import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def generate_synthetic_data(samples=5000):
    X = []
    y = []

    for _ in range(samples):
        dias_medio_atraso = np.random.randint(0, 90)
        qtd_titulos_abertos = np.random.randint(0, 15)
        valor_total_aberto = np.random.randint(0, 20000)
        tempo_relacionamento = np.random.randint(1, 120)
        ticket_medio = np.random.randint(100, 10000)

        linear_score = (
            dias_medio_atraso * 0.05 +
            qtd_titulos_abertos * 0.35 +
            valor_total_aberto * 0.00008 -
            tempo_relacionamento * 0.04 +
            ticket_medio * 0.00003 -
            3.5
        )

        probability = sigmoid(linear_score)

        inadimplente = np.random.binomial(1, probability)

        X.append([
            dias_medio_atraso,
            qtd_titulos_abertos,
            valor_total_aberto,
            tempo_relacionamento,
            ticket_medio
        ])

        y.append(inadimplente)

    return np.array(X), np.array(y)


def train_model():
    X, y = generate_synthetic_data()

    model = LogisticRegression(max_iter=3000)
    model.fit(X, y)

    joblib.dump(model, "app/ml/model.pkl")

    print("Modelo recalibrado e salvo com sucesso")


if __name__ == "__main__":
    train_model()