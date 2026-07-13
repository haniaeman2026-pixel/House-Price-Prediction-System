import os
import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# =====================================================
# House Price Prediction Model Training
# =====================================================

print("=" * 60)
print("🏡 House Price Prediction Model Training")
print("=" * 60)

# =====================================================
# Load Dataset
# =====================================================

DATA_PATH = "data/house_prices.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

data = pd.read_csv(DATA_PATH)

print(f"\n✅ Dataset Loaded Successfully")
print(f"Total Records : {len(data)}")

# =====================================================
# Select Required Columns
# =====================================================

required_columns = ["Super Area", "Price (in rupees)"]

missing_columns = [
    col for col in required_columns
    if col not in data.columns
]

if missing_columns:
    raise ValueError(
        f"Missing Columns: {missing_columns}"
    )

data = data[required_columns].copy()

# =====================================================
# Data Cleaning
# =====================================================

# Convert "680 sqft" → 680

data["Super Area"] = (
    data["Super Area"]
    .astype(str)
    .str.extract(r'(\d+\.?\d*)')[0]
)

data["Super Area"] = pd.to_numeric(
    data["Super Area"],
    errors="coerce"
)

data["Price (in rupees)"] = pd.to_numeric(
    data["Price (in rupees)"],
    errors="coerce"
)

# Remove Missing Values
data.dropna(inplace=True)

print(f"Clean Records : {len(data)}")

# =====================================================
# Features & Target
# =====================================================

X = data[["Super Area"]]
y = data["Price (in rupees)"]

# =====================================================
# Train Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print(f"\nTraining Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# =====================================================
# Train Model
# =====================================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\n✅ Model Trained Successfully")

# =====================================================
# Prediction
# =====================================================

y_pred = model.predict(X_test)

# =====================================================
# Evaluation
# =====================================================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\n" + "=" * 60)
print("📊 Model Performance")
print("=" * 60)

print(f"R² Score              : {r2:.4f}")
print(f"Mean Absolute Error   : {mae:,.2f}")
print(f"Root Mean Squared Err : {rmse:,.2f}")

# =====================================================
# Save Model
# =====================================================

MODEL_DIR = "model"
MODEL_PATH = os.path.join(
    MODEL_DIR,
    "house_price_model.pkl"
)

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, MODEL_PATH)

print("\n✅ Model Saved Successfully")
print(f"Location : {MODEL_PATH}")

# =====================================================
# Sample Prediction
# =====================================================

sample_area = 1500

prediction = model.predict([[sample_area]])[0]

print("\n" + "=" * 60)
print("🏠 Sample Prediction")
print("=" * 60)

print(f"House Area      : {sample_area} sqft")
print(f"Estimated Price : Rs. {prediction:,.0f}")

print("\n🎉 Training Completed Successfully!")