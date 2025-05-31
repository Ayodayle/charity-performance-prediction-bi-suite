import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load predictions
df = pd.read_csv("data/predictions.csv")

# Plot actual vs predicted outcomes
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='Outcome', hue='PredictedOutcome')
plt.title("Actual vs Predicted Outcomes")
plt.xlabel("Actual Outcome")
plt.ylabel("Count")
plt.legend(title="Predicted")
plt.tight_layout()
plt.show()

# Plot predicted outcomes by engagement score
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='PredictedOutcome', y='EngagementScore')
plt.title("Engagement Score by Predicted Outcome")
plt.xlabel("Predicted Outcome")
plt.ylabel("Engagement Score")
plt.tight_layout()
plt.savefig("visuals/actual_vs_predicted.png")
plt.show()
