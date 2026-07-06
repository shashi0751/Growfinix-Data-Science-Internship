import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Create dataset
data = {
    "Area": [1200,1500,1800,1400,2200,1700,1300,2400,1600,1900],
    "Bedrooms": [2,3,3,2,4,3,2,4,3,3],
    "Bathrooms": [2,2,3,2,3,2,2,4,2,3],
    "Price": [4500000,6200000,7500000,5200000,8900000,6700000,4800000,9300000,5600000,7100000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Features and Target
X = df[["Area", "Bedrooms", "Bathrooms"]]
y = df["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

print("\nPredicted Prices:")
print(predictions)

print("\nActual Prices:")
print(y_test.values)

# Error
mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", mae)

# Predict a new house
new_house = [[2000, 3, 3]]
predicted_price = model.predict(new_house)

print("\nPredicted Price for New House:", predicted_price[0])