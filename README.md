# 🛒 AI-Driven Retail Intelligence & Smart Inventory Optimization Platform

An end-to-end Machine Learning application that predicts retail product demand and provides inventory optimization recommendations to minimize stock shortages and overstock situations. The project integrates Machine Learning with an interactive Streamlit dashboard for real-time demand forecasting and business decision support.

---

## Demo Link of the Project : https://smart-optimization-platform-9zhcennvtqvkkfiawdxqxn.streamlit.app/

## 📌 Project Overview

Retail businesses often struggle with maintaining optimal inventory levels due to fluctuating customer demand. This project leverages Machine Learning to accurately forecast product demand and recommend inventory actions, enabling better procurement planning and reducing operational costs.

The best-performing model (CatBoost Regressor) is deployed through a Streamlit web application, allowing users to input product and inventory details and receive demand predictions along with actionable inventory recommendations.

---

## 🚀 Features

- 📈 Retail demand forecasting using Machine Learning
- 📦 Inventory optimization recommendations
- 🔍 Understock, Overstock, and Optimal inventory detection
- 📊 Interactive Streamlit dashboard
- 🤖 Comparison of multiple Machine Learning models
- 📉 Business analytics dashboard
- 💾 Saved ML model for real-time predictions

---

## 🛠 Tech Stack

### Programming
- Python

### Machine Learning
- Scikit-learn
- CatBoost
- Random Forest
- XGBoost
- LSTM

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly

### Deployment
- Streamlit

---

## 📂 Dataset

- Retail Inventory Dataset
- **73,100** transaction records
- Multiple stores and products
- Includes inventory, pricing, promotions, weather, competitor pricing, and seasonal information.

---

## ⚙️ Machine Learning Workflow

```
Retail Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
(Random Forest, XGBoost, CatBoost, LSTM)
        │
        ▼
Model Evaluation
        │
        ▼
Best Model Selection
(CatBoost)
        │
        ▼
Model Serialization (.pkl)
        │
        ▼
Streamlit Deployment
```

---

## 📊 Model Performance

| Model | R² Score |
|--------|---------:|
| Random Forest | 0.715 |
| XGBoost | 0.715 |
| **CatBoost** | **0.716** |
| LSTM | -0.002 |

**Best Performing Model:** CatBoost Regressor

---

## 💡 Dashboard Features

### 🏠 Home
- Project overview
- Dataset summary
- Technology stack

### 📦 Demand Forecast
- Product demand prediction
- Inventory status analysis
- Reorder quantity recommendation
- Business recommendations

### 📊 Model Performance
- Model comparison
- Performance visualization

### 📈 Business Analytics
- Retail insights
- Inventory metrics

### ℹ️ About
- Project details
- Technologies used

---

## 📁 Project Structure

```
Smart-Inventory-Optimization-Platform/
│
├── app.py
├── retail_dataset.csv
├── catboost_inventory_model.pkl
├── feature_columns.pkl
├── label_encoders.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Smart-Inventory-Optimization-Platform.git
```

Navigate to the project folder

```bash
cd Smart-Inventory-Optimization-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Business Benefits

- Improved demand forecasting
- Reduced inventory holding costs
- Minimized stock shortages
- Better procurement planning
- Data-driven business decisions
- Enhanced inventory management

---

## 🔮 Future Enhancements

- Cloud deployment with AWS/Azure
- Real-time sales data integration
- Time-series demand forecasting
- Multi-store inventory optimization
- Automated procurement recommendations
- AI-powered chatbot for inventory insights

---

## 👨‍💻 Author

**Akshay J Kulkarni**

Information Science & Engineering

Data Science | Machine Learning | AI

GitHub: https://github.com/AkshayJKulkarni

---

## ⭐ If you found this project useful, consider giving it a star!
