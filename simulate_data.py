import os
import pandas as pd
from faker import Faker
import random

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

fake = Faker()
data = []

for _ in range(500):
    data.append({
        "ClientID": fake.uuid4(),
        "Age": random.randint(18, 65),
        "SessionsAttended": random.randint(0, 10),
        "TrainingCompleted": random.choice(["Yes", "No"]),
        "UnemploymentRate": round(random.uniform(3.0, 8.0), 2),
        "EngagementScore": round(random.uniform(0.0, 1.0), 2),
        "Outcome": random.choice(["Yes", "No"])
    })

df = pd.DataFrame(data)
df.to_csv("data/simulated_clients.csv", index=False)

print("✅ Simulated data saved to data/simulated_clients.csv")
