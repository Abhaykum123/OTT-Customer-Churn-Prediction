# 🎬 OTT Customer Churn Prediction
Welcome to the OTT Customer Churn Prediction project! This repository contains a machine learning-based solution to predict customer churn for OTT platforms using deep learning models, with both a Jupyter Notebook for model development and an interactive Streamlit web app for real-time predictions.

---

### 📂 Project Structure

├── OTT Customer Churn Prediction.ipynb   # Model training and evaluation notebook <br>
├── app.py                                # Streamlit app for live churn prediction <br>
├── Model.h5                              # Trained Keras model <br>
├── Scaler.pkl                            # Pre-fitted scaler for input normalization <br>
├── README.md                             # Project documentation <br>

---

### 📌 About the Project
This project aims to predict whether a customer is likely to churn (unsubscribe) from an OTT platform based on their demographic and account information.

#### 🔍 Key Features
* Deep Learning Model (Keras + TensorFlow) for accurate churn prediction.

* Real-time interactive predictions via a sleek Streamlit web app.

* Dark mode optimized UI with intuitive input fields and detailed result display.

* Custom styling and progress indicators for enhanced user experience.

---

### 📊 Technologies Used
* Python 3.11.1

* TensorFlow & Keras

* scikit-learn

* Pandas

* Streamlit

* Pickle (for model/scaler serialization)
---

### 📓 Jupyter Notebook: Model Development
* The OTT Customer Churn Prediction.ipynb file contains:

* Data loading and preprocessing

* Feature engineering (e.g., encoding, derived features like Loyalty ratio)

* Model building using TensorFlow Keras

* Model training, evaluation, and saving the trained model and scaler
* 
---

### 🌐 Streamlit App: Live Prediction
The app.py file powers an interactive Streamlit web application where users can:

Input customer details (age, credit score, tenure, balance, country, etc.)

Get real-time churn probability predictions

View a friendly, dark-themed UI with progress indicators and prediction summaries

---
### 🎥 Sample Screenshots:
![Screenshot 2025-04-21 165534](https://github.com/user-attachments/assets/d8824d5b-8b17-452d-ab31-0724f5c5f24a)

---
### 🚀 How to Run the App Locally
1. Clone the repository
      git clone https://github.com/Abhaykum123/OTT-Customer-Churn-Prediction <br>

2. Install dependencies
     pip install -r requirements.txt
3. Run the Streamlit app
     streamlit run app.py
   
---

### 📈 Model Inputs
<h2>📈 Model Inputs</h2>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreditScore</td>
      <td>Customer’s credit score</td>
    </tr>
    <tr>
      <td>Age</td>
      <td>Customer’s age</td>
    </tr>
    <tr>
      <td>Tenure</td>
      <td>Number of months subscribed</td>
    </tr>
    <tr>
      <td>Balance</td>
      <td>Customer’s account balance</td>
    </tr>
    <tr>
      <td>NumOfProducts</td>
      <td>Number of subscribed services</td>
    </tr>
    <tr>
      <td>HasCrCard</td>
      <td>Whether the customer holds a credit card</td>
    </tr>
    <tr>
      <td>IsActiveMember</td>
      <td>Whether the customer is an active member</td>
    </tr>
    <tr>
      <td>EstimatedSalary</td>
      <td>Estimated annual salary</td>
    </tr>
    <tr>
      <td>Geography</td>
      <td>Country of residence</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>Customer’s gender</td>
    </tr>
  </tbody>
</table>

---

### ❤️ Acknowledgements
Made with passion for OTT platforms and data science by Abhay Kumar Gupta.
---

### 📬 Contact
For feedback or collaborations:

* 📧 [abhaykumargupta9939@gmail.com]



