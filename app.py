import streamlit as st
import numpy as np
import joblib
import pandas as pd
from datetime import datetime
import plotly.express as px
from sklearn.linear_model import LinearRegression
import shap
import matplotlib.pyplot as plt

# Load model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(
    page_title="California Smart Home Estimator",
    page_icon="🏡",
    layout="wide"
)

# Light theme styling
st.markdown("""
    <style>
    .stApp {
        background-color: white;
        color: black;
    }
    .st-emotion-cache-1v0mbdj {
        background-color: rgba(255,255,255,0.9) !important;
    }
    .st-emotion-cache-1r6slb0 p, .st-emotion-cache-10trblm {
        color: black !important;
    }
    button[kind="primary"] {
        background-color: black !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🏠 California Smart Housing Price Predictor")
st.markdown("Predict **median home values** based on California housing block data using machine learning.")
st.caption(f"🕒 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Sidebar Inputs
st.sidebar.title("📊 Input Parameters")
st.sidebar.markdown("Provide the following details about the area:")

feature_labels = {
    'MedInc': ("Median Income (in $10,000)", "Higher income areas tend to have higher house values."),
    'HouseAge': ("Median Age of Houses", "Newer or older homes affect value differently."),
    'AveRooms': ("Average Rooms per House", "Larger homes generally cost more."),
    'AveBedrms': ("Average Bedrooms per House", "More bedrooms often increase value."),
    'Population': ("Total Population", "Population density affects desirability."),
    'AveOccup': ("Average People per Household", "Indicates crowding or efficiency."),
    'Latitude': ("Latitude", "Geographical location (North–South)."),
    'Longitude': ("Longitude", "Geographical location (East–West).")
}

user_inputs = []
for feature, (label, help_text) in feature_labels.items():
    val = st.sidebar.slider(label, 0.0, 100.0, 5.0, 0.1, help=help_text)
    user_inputs.append(val)

# Tabs
prediction_tab, info_tab, map_tab, history_tab, feature_tab, explain_tab = st.tabs([
    "🔍 Prediction", "📘 Model Info", "🗺️ Location Map", "📈 History", "📊 Feature Impact", "🧠 Explainability"
])

# --- Prediction Tab ---
with prediction_tab:
    st.subheader("🏡 Predicted Home Price")
    if st.button("🚀 Estimate Now"):
        input_array = np.array(user_inputs).reshape(1, -1)
        prediction_rf = model.predict(input_array)[0] * 100000

        # Compare with Linear Regression
        linear_model = LinearRegression()
        try:
            X_train = joblib.load("X_train.pkl")
            y_train = joblib.load("y_train.pkl")
            linear_model.fit(X_train, y_train)
            prediction_lr = linear_model.predict(input_array)[0] * 100000
        except:
            prediction_lr = prediction_rf

        lower = prediction_rf - 20000
        upper = prediction_rf + 20000

        if prediction_rf > 500000:
            color = "lightgreen"
            message = "🔥 Hot Property Zone!"
        elif prediction_rf > 200000:
            color = "orange"
            message = "👍 Good Investment Area"
        else:
            color = "lightcoral"
            message = "📉 Lower Value Area"

        st.markdown(f"""
            <div style='padding:10px; border-radius:8px; background-color:{color}; text-align:center; margin-top:20px'>
                <h3 style='color:black; margin:5px'>${prediction_rf:,.2f}</h3>
                <p style='font-size:16px; color:black; margin:0'>{message}</p>
                <small>Confidence range: ${lower:,.0f} - ${upper:,.0f}</small>
            </div>
        """, unsafe_allow_html=True)

        st.caption(f"🕒 Prediction made on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Model Comparison Chart
        st.subheader("🔁 Compare Models")
        st.plotly_chart(px.bar(
            x=["Random Forest", "Linear Regression"],
            y=[prediction_rf, prediction_lr],
            labels={"x": "Model", "y": "Predicted Price"},
            title="Model Prediction Comparison"
        ))

        # Region Tips
        lat, lon = user_inputs[6], user_inputs[7]
        if lat > 36.0 and lon < -120.0:
            st.success("📍 This area is near San Jose – known for high-tech real estate growth.")
        elif lat > 34.0 and lon < -118.0:
            st.info("📍 This area is near Los Angeles – property values are often dynamic here.")

        # Save History
        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append({
            "Time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Price ($)": round(prediction_rf, 2),
            **{label: val for (label, _), val in zip(feature_labels.values(), user_inputs)}
        })

        # Download Button
        hist_df = pd.DataFrame(st.session_state.history)
        csv = hist_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Report as CSV", csv, "prediction_report.csv", "text/csv")

        # Trend Plot
        st.subheader("📈 Prediction Trend")
        st.plotly_chart(px.line(hist_df, x="Time", y="Price ($)", title="Prediction Trend Over Time"))

# --- Model Info Tab ---
with info_tab:
    st.subheader("📘 About This Model")
    st.markdown("""
    - **Model**: Random Forest Regressor  
    - **Dataset**: California Housing (scikit-learn)  
    - **Features**: Income, room size, population, and location  
    - **Prediction**: Median home value in each housing block  
    - 💡 *Note*: Predictions are for district-level average prices, not for individual homes.  
    ---
    Made by Ananya SM | Powered by Streamlit & Scikit-learn
    """)

# --- Map Tab ---
with map_tab:
    st.subheader("📍 Mapped Input Location")
    lat = user_inputs[6]
    lon = user_inputs[7]
    if lat != 0.0 or lon != 0.0:
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))
    else:
        st.info("Adjust latitude and longitude in the sidebar to display a location.")

# --- History Tab ---
with history_tab:
    st.subheader("📈 Prediction History")
    if "history" in st.session_state and st.session_state.history:
        hist_df = pd.DataFrame(st.session_state.history)
        st.dataframe(hist_df, use_container_width=True)
    else:
        st.info("No predictions yet. Click 'Estimate Now' to start.")

# --- Feature Importance Tab ---
with feature_tab:
    st.subheader("📊 Feature Importance")
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        labels = list(feature_labels.keys())
        fig = px.bar(x=labels, y=importances, labels={"x": "Feature", "y": "Importance"}, title="Model Feature Importance")
        st.plotly_chart(fig)
    else:
        st.warning("This model does not support feature importance extraction.")

# --- Explainability Tab ---
with explain_tab:
    st.subheader("🧠 SHAP Explainability")
    try:
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(np.array(user_inputs).reshape(1, -1))
        fig, ax = plt.subplots()
        shap.plots.waterfall(shap.Explanation(values=shap_values[0], base_values=explainer.expected_value, data=user_inputs, feature_names=list(feature_labels.keys())), max_display=8)
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Unable to generate SHAP explanation: {e}")








