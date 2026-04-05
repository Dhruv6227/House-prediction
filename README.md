# 🏠 🏡 House Prediction System

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine-Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Data-Analysis](https://img.shields.io/badge/Data%20Analysis-1572B6?style=for-the-badge&logo=pandas&logoColor=white)

An AI-driven house price prediction system that leverages machine learning to estimate home values based on various features such as living area, bedrooms, bathrooms, and property condition. Built using Python, Scikit-Learn, and Streamlit for a premium user experience.

---

## 🚀 Key Features

- **Intuitive UI**: A modern, responsive dashboard with a premium look and feel.
- **Real-Time Predictions**: Instantaneous price estimations using a trained linear regression model.
- **Comprehensive Analysis**: Evaluates 12 different features including:
  - Living and Lot Area
  - Waterfront View and Overall Condition
  - Year Built and Renovation details
  - Basement and Above-Ground space
- **Visual Outcome**: Clear, styled results showing estimated value in currency.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core Programming Language |
| **Streamlit** | Web Interface and UI Components |
| **Scikit-Learn** | ML Model Training and Prediction Logic |
| **NumPy** | Numerical Operations and Data Formatting |
| **Pickle** | Model Serialization and Loading |
| **Pandas** | Data Processing and Exploratory Analysis |

---

## 📂 Project Structure

```text
├── app.py             # Main Streamlit application file
├── data.csv            # Dataset used for training (King County Housing)
├── modal.ipynb         # Jupyter Notebook for EDA & Model training
├── model.pkl           # Pre-trained ML model (binary format)
├── .venv/              # Virtual environment directory
└── README.md           # Project documentation
```

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Dhruv6227/House-prediction.git
cd House-prediction
```

### 2️⃣ Set up Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install streamlit numpy pandas scikit-learn
```

### 4️⃣ Launch the Application
```bash
streamlit run app.py
```

---

## 🧠 Behind the Model

The core of this application uses a **Linear Regression** algorithm trained on residential housing data. It focuses on several critical factors:
- **Spatial Features**: Square footage of the living area, lot, and basement.
- **Architectural Details**: Number of floors, bedrooms, and bathrooms.
- **Contextual Data**: Waterfront proximity, view ratings, and property condition rank.
- **Historical Context**: The age of the house (Year Built) and recent upgrades (Year Renovated).

The model is serialized into `model.pkl` for fast loading and low-latency prediction.

---

## 🎨 UI Aesthetics

The application features a sleek **glassmorphic design** with:
- Linear gradients on action buttons.
- Centered layout for maximum focus.
- Custom styled prediction boxes for a modern enterprise feel.

---

## 📝 License

This project is open-source and available under the MIT License.

---

*Developed by [Dhruv6227](https://github.com/Dhruv6227)*
