# train_and_predict.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

print("Starting model training...")

# Apna exact CSV name yahan change kar dena agar alag hai
df = pd.read_csv("shopping_behavior_updated.csv")

print(f"Data loaded: {df.shape[0]} rows")

# Encoding
cat_cols = ['Gender', 'Category', 'Location', 'Size', 'Color', 'Season',
            'Subscription Status', 'Discount Applied', 'Payment Method', 'Frequency of Purchases']

le_dict = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    le_dict[col] = le

# Features
features = ['Age', 'Gender', 'Category', 'Location', 'Size', 'Color', 'Season',
            'Review Rating', 'Subscription Status', 'Discount Applied',
            'Previous Purchases', 'Payment Method', 'Frequency of Purchases']

X = df[features]
y = df['Purchase Amount (USD)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Random Forest model...")
model = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("MODEL READY!")
print(f"R² Score  : {r2_score(y_test, pred):.4f}")
print(f"Error     : ${mean_absolute_error(y_test, pred):.2f}")

# Save everything
joblib.dump(model, "shopping_model.pkl")
joblib.dump(le_dict, "encoders.pkl")
joblib.dump(features, "features.pkl")

print("All files saved: shopping_model.pkl, encoders.pkl, features.pkl")
print("Ab 'app.py' chalao GUI ke liye")
