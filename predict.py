import pandas as pd
import joblib

# Load model
model = joblib.load("models/rf_model.pkl")

# Load data
df = pd.read_csv("data/simulated_clients.csv")

# Prepare features (same as training)
df['TrainingCompleted'] = df['TrainingCompleted'].map({'Yes': 1, 'No': 0})
X = df[['Age', 'SessionsAttended', 'TrainingCompleted', 'UnemploymentRate', 'EngagementScore']]

# Predict outcomes
df['PredictedOutcome'] = model.predict(X)
df['PredictedOutcome'] = df['PredictedOutcome'].map({1: 'Yes', 0: 'No'})

# Save to new CSV for Power BI
df.to_csv("data/predictions.csv", index=False)

print("✅ Predictions saved to data/predictions.csv")
