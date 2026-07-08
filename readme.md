# 🚗 Car Price Prediction using Random Forest

An end-to-end Machine Learning application that predicts the selling price of used cars based on their specifications. The project demonstrates the complete ML lifecycle—from data preprocessing and model training to deployment with an interactive Gradio web interface.

## 🌐 Live Demo

**Try the application here:**

https://huggingface.co/spaces/aryan-p/car-price-prediction-random-forest

---

# 📌 Project Overview

This project predicts the selling price of used cars using a **Random Forest Regressor** trained on historical vehicle data. The application allows users to upload a CSV file containing vehicle information and receive predicted selling prices in a downloadable CSV format.

The project demonstrates:

* End-to-End Machine Learning Pipeline
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training & Evaluation
* Model Serialization with Joblib
* Batch Prediction using CSV Upload
* Interactive Gradio Web Application
* Deployment on Hugging Face Spaces

---

# ✨ Features

* 🚗 Predict used car selling prices
* 📁 Upload CSV files for batch prediction
* 📥 Download prediction results as CSV
* 🤖 Random Forest Regression model
* ⚙️ Automated preprocessing pipeline
* 💾 Serialized model using Joblib
* 🌐 Browser-based interface powered by Gradio

---

# 📂 Dataset

The dataset contains information about used cars, including:

| Feature       | Description                       |
| ------------- | --------------------------------- |
| Car_Name      | Name of the Car                   |
| Year          | Manufacturing Year                |
| Present_Price | Current Ex-Showroom Price (Lakhs) |
| Kms_Driven    | Kilometers Driven                 |
| Fuel_Type     | Petrol / Diesel / CNG             |
| Selling_type  | Dealer or Individual              |
| Transmission  | Manual / Automatic                |
| Owner         | Number of Previous Owners         |
| Selling_Price | Target Variable                   |

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Gradio
* Joblib
* Matplotlib
* Seaborn

---

# 📊 Machine Learning Workflow

### 1. Data Preparation

* Dataset loading
* Data cleaning
* Missing value inspection
* Feature selection

### 2. Exploratory Data Analysis

* Correlation analysis
* Feature distribution
* Heatmaps
* Data visualization

### 3. Data Preprocessing

* One-Hot Encoding
* ColumnTransformer Pipeline
* Stratified Train-Test Split
* Feature Engineering

### 4. Model Training

**Algorithm Used**

* ✅ Random Forest Regressor

### Why Random Forest?

* Better generalization
* Reduced overfitting
* Handles nonlinear relationships
* High prediction accuracy

### 5. Model Evaluation

Metrics Used

* Mean Squared Error (MSE)
* R² Score

### Final Performance

| Model                   |  R² Score |
| ----------------------- | --------: |
| Random Forest Regressor | **0.969** |

---

# 🌐 Web Application

The project includes a Gradio web application where users can predict selling prices without writing any code.

### Workflow

```text
Upload CSV
      │
      ▼
Validate Input
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Random Forest Model
      │
      ▼
Generate Predictions
      │
      ▼
Download Output CSV
```

---

# 📁 Project Structure

```text
car-price-predictor/
│
├── app.py                  # Gradio Frontend
├── predictor.py            # Prediction Logic
├── model.py                # Model Training
├── model.pkl               # Trained Model
├── pipeline.pkl            # Preprocessing Pipeline
│
├── data/
│   └── car data.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/car-price-predictor.git
```

Move into the project directory:

```bash
cd car-price-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Step 1: Train the Model

```bash
python model.py
```

This generates:

* `model.pkl`
* `pipeline.pkl`

---

## Step 2: Launch the Web Application

```bash
python app.py
```

Open the generated local URL in your browser.

---

# 📥 How to Use

1. Launch the application.
2. Upload a CSV containing vehicle information.
3. Click **Submit**.
4. Wait for the prediction to complete.
5. Download the generated CSV file containing predicted selling prices.

> **Note:** If the uploaded CSV already contains the `Selling_Price` column, it is automatically ignored during prediction.

---

# 📄 Expected Input Columns

Your CSV should contain:

* Year
* Present_Price
* Kms_Driven
* Fuel_Type
* Selling_type
* Transmission
* Owner

---

# 📈 Sample Prediction

| Present Price | Year | Fuel Type | Predicted Selling Price |
| ------------- | ---- | --------- | ----------------------: |
| 5.25          | 2018 | Petrol    |                    4.92 |

---

# 📚 Concepts Demonstrated

* Machine Learning Regression
* Random Forest Regression
* Feature Engineering
* One-Hot Encoding
* Scikit-learn Pipelines
* ColumnTransformer
* Stratified Sampling
* Model Serialization
* Batch Inference
* Model Deployment

---

# 💡 Challenges & Learnings

During this project I gained hands-on experience with:

* Building reusable preprocessing pipelines
* Using ColumnTransformer correctly
* One-Hot Encoding categorical variables
* Understanding when feature scaling is necessary
* Debugging scikit-learn pipeline issues
* Separating training and inference code
* Model serialization using Joblib
* Deploying ML models with Gradio
* Creating batch prediction workflows using CSV files

---

# 🚀 Future Improvements

* Hyperparameter tuning using GridSearchCV
* Cross-validation
* SHAP Explainability
* Feature Importance Visualization
* Docker Support
* Prediction Confidence Scores
* CI/CD Pipeline
* Cloud Deployment

---

# 👨‍💻 Author

**Aryan Kumar Prajapati**

B.Tech Computer Science Engineering

Aspiring Machine Learning & Data Science Engineer

**GitHub**: https://github.com/Aryan2006-code

**LinkedIn**: www.linkedin.com/in/aryankumar2006

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. It helps others discover the project and supports future improvements.
