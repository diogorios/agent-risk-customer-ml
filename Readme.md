🤖 AI Agent for Credit Risk Analysis

A Machine Learning-based credit analysis system capable of automatically assessing customers' financial risk using accounts receivable data, generating scores, risk classification, and commercial recommendations.

🚀 Objective

Provide an intelligent API that:

Evaluates default risk
Generates a credit score (0–100)
Classifies customers (LOW / MEDIUM / HIGH)
Explains decision factors
Suggests commercial actions
Defines recommended credit limits
Determines minimum down payment

All automatically and fully integrated with ERP systems.

🧠 How It Works

The system is built with two main layers:

1. Machine Learning

A model trained with synthetic data that identifies risk patterns based on:

Average delay (days overdue)
Number of open invoices
Outstanding balance
Customer relationship duration
Average ticket value

Generates a base risk score.

2. Credit Policy Engine (Business Rules)

After the ML model, a rule-based system:

Adjusts the score based on critical behavior
Identifies risk factors (red flags)
Classifies the customer
Calculates credit limits
Generates commercial recommendations

📊 Response Example
{
  "customer_name_v3": "Sample Customer",
  "score": 68,
  "risk_level": "MEDIUM",
  "credit_assessment": "Customer presents moderate risk, requiring caution.",
  "reasons": [
    "3 open invoices",
    "Recent delay of up to 49 days",
    "High historical delay percentage"
  ],
  "recommended_actions": [
    "Approve partial credit",
    "Apply reduced limit",
    "Monitor future purchases"
  ],
  "recommended_limit": 300,
  "minimum_down_payment": 20
}