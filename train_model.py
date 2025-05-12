import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load your data
df = pd.read_csv("data/simulated_clients.csv")

# Convert Yes/No to 1/0 for training
df['TrainingCompleted'] = df['TrainingCompleted'].map({'Yes': 1, 'No': 0})
df['Outcome'] = df['Outcome'].map({'Yes': 1, 'No': 0})

# Features and target
X = df[['Age', 'SessionsAttended', 'TrainingCompleted', 'UnemploymentRate', 'EngagementScore']]
y = df['Outcome']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/rf_model.pkl")
print("✅ Model trained and saved to models/rf_model.pkl")
