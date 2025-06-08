import os
os.makedirs("visuals", exist_ok=True)  # Create the folder if it doesn't exist
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and data
model = joblib.load("models/rf_model.pkl")
df = pd.read_csv("data/simulated_clients.csv")

# Prepare feature names
df['TrainingCompleted'] = df['TrainingCompleted'].map({'Yes': 1, 'No': 0})
features = ['Age', 'SessionsAttended', 'TrainingCompleted', 'UnemploymentRate', 'EngagementScore']

# Get importance values
importances = model.feature_importances_

# Plot
plt.figure(figsize=(8, 5))
plt.barh(features, importances, color='skyblue')
plt.xlabel("Importance Score")
plt.title("Feature Importance (Random Forest)")
plt.tight_layout()

# Save to visuals/
plt.savefig("visuals/feature_importance.png")
print("✅ Feature importance plot saved to visuals/feature_importance.png")
