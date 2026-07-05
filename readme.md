# 🚗 Car Price Prediction using Machine Learning

A Machine Learning project that predicts the selling price of a used car based on various vehicle attributes. This project demonstrates the complete ML workflow, from data preprocessing and feature engineering to model training, evaluation, and inference.

---

## 📌 Project Overview

The objective of this project is to build a regression model capable of estimating the selling price of a used car using historical car sales data.

The project covers:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Categorical Encoding
* Train-Test Splitting
* Model Training
* Model Evaluation
* Model Serialization
* Inference on unseen data

---

## 📂 Dataset

The dataset contains information about used cars, including:

| Feature       | Description                          |
| ------------- | ------------------------------------ |
| Car_Name      | Name of the Car                      |
| Year          | Manufacturing Year                   |
| Present_Price | Current Ex-Showroom Price (in Lakhs) |
| Kms_Driven    | Kilometers Driven                    |
| Fuel_Type     | Petrol / Diesel / CNG                |
| Selling_type  | Dealer or Individual                 |
| Transmission  | Manual / Automatic                   |
| Owner         | Number of Previous Owners            |
| Selling_Price | Target Variable                      |

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib

---

## 📊 Workflow

### 1. Data Loading

* Imported the dataset
* Checked dataset information
* Verified data types
* Checked for missing values

---

### 2. Exploratory Data Analysis

Performed:

* Dataset summary
* Correlation analysis
* Correlation Heatmap
* Feature inspection
* Distribution analysis

---

### 3. Data Preprocessing

Performed preprocessing steps including:

* One-Hot Encoding for categorical variables
* Feature selection
* Stratified Train-Test Split
* Model Pipeline using `ColumnTransformer`

---

### 4. Model Training

Initially trained:

* Decision Tree Regressor

Later replaced with:

* ✅ Random Forest Regressor

Reason:

* Better generalization
* Reduced overfitting
* Improved prediction accuracy

---

### 5. Model Evaluation

Evaluation Metrics Used:

* Mean Squared Error (MSE)
* R² Score

### Final Model Performance

* **Model:** Random Forest Regressor
* **R² Score:** **0.969**
* Successfully predicts selling prices with high accuracy.

---

## 📁 Project Structure

```
car-price-predictor/
│
├── data/
│   └── car data.csv
│
├── main.py
├── test.ipynb
├── input.csv
├── output.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── model_pkl
└── pipeline_pkl
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/car-price-predictor.git
```

Move inside the project:

```bash
cd car-price-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Train the model:

```bash
python main.py
```

The script will:

* Train the Random Forest model
* Save the trained model
* Save the preprocessing pipeline

For inference:

Place new car details inside `input.csv` and run:

```bash
python main.py
```

Predictions will be saved in:

```
output.csv
```

---

## 📈 Sample Prediction

| Present Price | Year | Fuel Type | Predicted Selling Price |
| ------------- | ---- | --------- | ----------------------- |
| 5.25          | 2018 | Petrol    | 4.92                    |

---

## 💡 Challenges Faced

During development, I encountered several implementation challenges that helped deepen my understanding of Machine Learning and Scikit-learn.

Some of the key learnings include:

* Correct use of `precision_score()` parameters.
* Passing column names instead of DataFrames to `ColumnTransformer`.
* Understanding why `SimpleImputer` expects 2D input.
* Different imputation strategies (mean, median, most frequent, constant).
* Debugging visualization errors caused by variable naming mistakes.
* Building preprocessing pipelines correctly.
* Understanding when feature scaling is necessary.
* Learning that Decision Trees do not require feature scaling.
* Replacing Decision Tree with Random Forest to improve model performance.
* Identifying that removing the high-cardinality `Car_Name` feature improved prediction accuracy.

---

## 📚 Key Concepts Learned

* Regression
* Random Forest
* Decision Trees
* Train-Test Split
* Stratified Sampling
* One-Hot Encoding
* Feature Engineering
* Feature Selection
* Model Evaluation
* Scikit-learn Pipelines
* ColumnTransformer
* Model Serialization using Joblib

---

## 🚀 Future Improvements

* Hyperparameter Tuning using GridSearchCV
* Cross Validation
* Feature Importance Visualization
* SHAP Explainability
* Streamlit Web Application
* REST API Deployment using Flask/FastAPI
* Docker Support

---

## 👨‍💻 Author

**Aryan Kumar Prajapati**

B.Tech Computer Science Engineering

Aspiring Machine Learning & Data Science Engineer

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ If you found this project helpful, consider giving it a star!
