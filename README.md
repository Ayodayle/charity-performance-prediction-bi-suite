# Charity Performance Prediction BI Suite

This project is a toolkit for helping non-profits and public sector organisations build predictive models to forecast and monitor key performance outcomes; such as employment success, housing stability, or program engagement.

By using simulated data, Python, and Power BI, the project demonstrates how organisations can proactively track outcome metrics and make data-informed decisions with minimal technical overhead.

---

## 🎯 Project Goals

- Provide a reusable template for predicting service delivery outcomes
- Help charities and local councils improve performance monitoring
- Demonstrate low-code integrations with Power BI and Python
- Enable transparency and scalability with open data workflows

---

## 📦 Features

- ✅ Simulated public service data using Python + Faker
- 🧠 Machine learning model (Random Forest) for binary outcome prediction
- 📊 Power BI dashboard integration
- ⚙️ Ready for low-code automation and alerting (Power Automate/Azure Logic)
- 🔁 Easily extensible for real-world datasets

---

## 📁 Folder Structure
charity-performance-prediction-bi-suite/
├── data/ # Simulated and predicted data files (CSV)
├── models/ # Trained machine learning model (.pkl)
├── power-bi/ # Power BI dashboard files (.pbix)
├── simulate_data.py # Script to generate synthetic data
├── train_model.py # Script to train ML model
├── predict.py # Script to generate predictions
└── README.md


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ayodayle/charity-performance-prediction-bi-suite.git
cd charity-performance-prediction-bi-suite

### 2. Install dependencies
bash
Copy
Edit
pip install pandas faker scikit-learn joblib
### 3. Generate data and train the model
bash
Copy
Edit
python simulate_data.py
python train_model.py
python predict.py

📊 Power BI Integration
Open power-bi/outcome-dashboard.pbix to explore the predictions visually. Connect to data/predictions.csv for real-time dashboard refresh.

🤝 Contributing
Contributions are welcome! Whether you’re a BI developer, data scientist, or public sector professional, your insights can help make this more valuable.

To contribute:
Fork the repo

Create a feature branch

Submit a pull request

📬 Feel free to open issues or reach out if you'd like to collaborate.

📜 License
MIT License — open to all, especially the mission-driven community.
