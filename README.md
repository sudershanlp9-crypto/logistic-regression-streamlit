# 🩺 Diabetes Risk Predictor

An interactive **Machine Learning web application** that predicts diabetes risk using a **Logistic Regression** model. The application is built with Python and Streamlit and provides an easy-to-use interface where users can enter patient information and receive a predicted diabetes outcome along with the probability.

## 🚀 Live Demo

Once deployed, add your Streamlit application URL here:

**Live App:** `https://diabetes-risk-predictor-lr.streamlit.app/)`

---

## 📌 Project Overview

Diabetes is a common health condition that can be influenced by several factors such as glucose level, blood pressure, insulin level, BMI, and age.

This project uses **Logistic Regression**, a supervised machine learning algorithm for binary classification, to predict whether a patient is likely to have diabetes.

The trained model is integrated into a **Streamlit web application** so that users can enter patient information and obtain predictions interactively.

---

## 🎯 Objectives

* Perform Exploratory Data Analysis (EDA)
* Understand the dataset and its features
* Handle data preprocessing and outliers
* Build a Logistic Regression classification model
* Evaluate the model using classification metrics
* Analyze the model coefficients
* Save the trained machine learning model
* Build an interactive Streamlit application
* Deploy the application online using Streamlit Community Cloud

---

## 📊 Features Used by the Model

The final trained model uses the following five features:

| Feature       | Description                  |
| ------------- | ---------------------------- |
| Glucose       | Plasma glucose concentration |
| BloodPressure | Blood pressure measurement   |
| Insulin       | Serum insulin level          |
| BMI           | Body Mass Index              |
| Age           | Patient age                  |

### Target Variable

**Outcome**

* `0` → No Diabetes
* `1` → Diabetes

---

## 🤖 Machine Learning Model

The project uses:

**Algorithm:** Logistic Regression

Logistic Regression is suitable for this problem because the target variable is binary.

The model produces:

1. A predicted class
2. A probability of diabetes

---

## 🔧 Data Preprocessing

The project includes preprocessing before model training.

### Outlier Handling

IQR-based outlier capping is applied to:

* Blood Pressure
* BMI
* Insulin

The same preprocessing logic is applied to user inputs in the Streamlit application before making predictions.

---

## 📈 Model Evaluation

The model is evaluated using classification metrics including:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* ROC Curve

Cross-validation is also used to evaluate model performance more reliably.

---

## 🌐 Streamlit Application

The Streamlit application provides an interactive interface where users can enter:

* Glucose
* Blood Pressure
* Insulin
* BMI
* Age

After clicking **Predict Diabetes Risk**, the application displays:

### Prediction

* ✅ No Diabetes
* ⚠️ Diabetes

### Probability

The application also displays the predicted probability of diabetes as a percentage.

---

## 🖥️ Application Interface

The application includes:

* 🩺 Diabetes Risk Predictor dashboard
* 📊 Model information
* 👤 Patient input section
* 🔍 Prediction button
* 📈 Probability visualization
* 📋 Input data preview
* ⚠️ Educational-use disclaimer

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**
* **Streamlit**
* **Jupyter Notebook**
* **GitHub**
* **Streamlit Community Cloud**

---

## 📁 Project Structure

```text
logistic-regression-streamlit/
│
├── app.py
├── logistic_regression_model.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                            | Description                       |
| ------------------------------- | --------------------------------- |
| `app.py`                        | Streamlit web application         |
| `logistic_regression_model.pkl` | Trained Logistic Regression model |
| `requirements.txt`              | Required Python libraries         |
| `README.md`                     | Project documentation             |

---

## ⚙️ Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/logistic-regression-streamlit.git
```

### 2. Navigate to the project directory

```bash
cd logistic-regression-streamlit
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

---

## ☁️ Online Deployment

This project can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Upload the project to GitHub.
2. Connect GitHub with Streamlit Community Cloud.
3. Select the repository.
4. Select the `main` branch.
5. Select `app.py` as the main file.
6. Click **Deploy**.
7. Streamlit will generate a public `streamlit.app` URL.

---

## 🔮 Future Improvements

Possible improvements include:

* Adding more machine learning algorithms
* Comparing Logistic Regression with Random Forest, XGBoost, etc.
* Improving model performance through hyperparameter tuning
* Adding interactive data visualizations
* Adding model explainability
* Adding a database for storing predictions
* Improving the user interface
* Adding authentication

---

## ⚠️ Disclaimer

This project is developed for **educational and machine learning demonstration purposes**.

The predictions generated by this application should **not be considered a medical diagnosis**. Users should consult a qualified healthcare professional for medical advice.

---

## 👨‍💻 Author

**Sudershan Pulgamwar**

BCA Graduate | Python & Machine Learning Enthusiast

---

## ⭐ Acknowledgements

This project was developed as a practical implementation of **Logistic Regression and Machine Learning model deployment using Streamlit**.
