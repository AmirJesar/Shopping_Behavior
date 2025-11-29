# pages/4_🔮_Predictions.py
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from app import df, filtered_df  # Use full df for training

st.title("🔮 Purchase Amount Predictor")

# Preprocess data for ML
@st.cache_resource
def train_model():
    # Encode categorical columns
    le_dict = {}
    for col in ['Gender', 'Category', 'Location', 'Size', 'Color', 'Season', 'Subscription Status', 'Discount Applied', 'Payment Method', 'Frequency of Purchases']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        le_dict[col] = le

    X = df.drop(['Customer ID', 'Item Purchased', 'Purchase Amount (USD)', 'Review Rating'], axis=1)  # Drop non-features
    y = df['Purchase Amount (USD)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, "purchase_model.pkl")
    return model, le_dict, mean_squared_error(y_test, model.predict(X_test), squared=False)

model, le_dict, rmse = train_model()
st.write(f"Model trained with RMSE: ${rmse:.2f} (lower is better)")

# User input for prediction
st.subheader("Predict Purchase Amount")
age = st.slider("Age", 18, 70, 30)
gender = st.selectbox("Gender", df['Gender'].unique())
category = st.selectbox("Category", df['Category'].unique())
location = st.selectbox("Location", df['Location'].unique())
size = st.selectbox("Size", df['Size'].unique())
color = st.selectbox("Color", df['Color'].unique())
season = st.selectbox("Season", df['Season'].unique())
review_rating = st.slider("Review Rating", 2.5, 5.0, 4.0)
subscription = st.selectbox("Subscription Status", df['Subscription Status'].unique())
discount = st.selectbox("Discount Applied", df['Discount Applied'].unique())
previous = st.slider("Previous Purchases", 1, 50, 10)
payment = st.selectbox("Payment Method", df['Payment Method'].unique())
frequency = st.selectbox("Frequency of Purchases", df['Frequency of Purchases'].unique())

if st.button("Predict"):
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [le_dict['Gender'].transform([gender])[0]],
        'Category': [le_dict['Category'].transform([category])[0]],
        'Location': [le_dict['Location'].transform([location])[0]],
        'Size': [le_dict['Size'].transform([size])[0]],
        'Color': [le_dict['Color'].transform([color])[0]],
        'Season': [le_dict['Season'].transform([season])[0]],
        'Review Rating': [review_rating],
        'Subscription Status': [le_dict['Subscription Status'].transform([subscription])[0]],
        'Discount Applied': [le_dict['Discount Applied'].transform([discount])[0]],
        'Previous Purchases': [previous],
        'Payment Method': [le_dict['Payment Method'].transform([payment])[0]],
        'Frequency of Purchases': [le_dict['Frequency of Purchases'].transform([frequency])[0]]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Purchase Amount: **${prediction:.2f}**")
    st.balloons()
