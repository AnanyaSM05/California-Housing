# 🏡 California Housing Price Prediction Web App

This is an interactive machine learning project built using Streamlit that predicts median house prices in California based on various neighborhood factors like income, population, housing age, and geographic location.

**📌 Project Objective**

The goal of this project is to demonstrate how machine learning models can be used in real-world scenarios for predictive analysis. The application allows users to enter custom input parameters and instantly view predicted home values along with feature impact, live history, and visual explanations.

**🔍 Key Features**

 Interactive Web Interface with sliders and tooltips for user-friendly input

 Real-Time Price Prediction using a trained Random Forest Regressor

 Feature Importance Visualization using Plotly bar chart

 Map Display based on latitude & longitude inputs

 Live Prediction History using st.session_state

 Timestamped Predictions showing when each estimate was made

 Downloadable CSV Report of inputs and prediction result

 Smart UI with emojis and conditional messages based on predicted value

 Built entirely using Streamlit, Python, and open-source libraries

**🛠️ Tech Stack**

Component	Technology

Language	Python 3.12+

Web Framework	Streamlit

ML Library	Scikit-learn

Model Storage	Joblib

Visualizations	Plotly

Mapping	Streamlit's st.map()

Styling	Custom HTML + CSS injected

**📚 Dataset Used**

Source: fetch_california_housing() from sklearn.datasets

**Features:**

MedInc – Median income in block

HouseAge – Median house age

AveRooms – Average rooms per household

AveBedrms – Average bedrooms

Population – Total population in the block

AveOccup – Average household occupancy

Latitude and Longitude – Location info

**How to Run**

**Clone the repo:**

git clone https://github.com/your-username/california-housing-predictor.git

cd california-housing-predictor

**Install dependencies:**

pip install -r requirements.txt

**Run the app:**

streamlit run app.py

**📁File	Description**

app.py	Streamlit app code

model.pkl	Trained RandomForest model

train_model.py	Script to train and save the model

requirements.txt	Required libraries

README.md	This project overview file

**🧠 Possible Enhancements**

Add more ML models (e.g., Linear Regression, XGBoost)

Add SHAP-based explanation plots

Use real estate APIs for current listings

Include data upload support for batch prediction

# Screenshots of web app

<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/07f00e23-8f4c-421d-b3eb-117ccb2b5353" />
<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/276221fa-3978-4a43-95db-e64ae9f8a183" />
<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/816def99-b4b6-4832-affd-25843ed47fbf" />
<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/8d14e67a-4161-443d-9db8-3e97297bb2fe" />
<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/3d4e2c31-fb3b-44aa-b466-76bf984ecbce" />
<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/f5953b79-4237-4d20-8aca-e31fc646a627" />





**👤 Author
Ananya SM
Final Year B.E. - Artificial Intelligence & Machine Learning
This project was built as part of a learning initiative combining machine learning, web development, and data visualization.**

