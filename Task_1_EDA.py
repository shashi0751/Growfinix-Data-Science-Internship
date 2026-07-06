import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset inside Python
data = {
    "Price": [4500000,6200000,7500000,5200000,8900000,6700000,4800000,9300000,5800000,7100000,6400000,8100000,5600000,6900000,9800000],
    "Area": [1200,1500,1800,1400,2200,1700,1300,2400,1600,1900,1650,2100,1450,1750,2500],
    "Bedrooms": [2,3,3,2,4,3,2,4,3,3,3,4,2,3,5],
    "Bathrooms": [2,2,3,2,3,2,2,4,2,3,2,3,2,3,4],
    "Location": ["Jaipur","Jaipur","Delhi","Mumbai","Bangalore","Pune","Jaipur","Delhi","Mumbai","Bangalore","Pune","Delhi","Jaipur","Mumbai","Bangalore"]
}

df = pd.DataFrame(data)

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Graph 1
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=8, kde=True)
plt.title("Price Distribution")
plt.show()

# Graph 2
plt.figure(figsize=(8,5))
sns.boxplot(x=df["Price"])
plt.title("Price Boxplot")
plt.show()

# Graph 3
plt.figure(figsize=(8,5))
sns.scatterplot(x="Area", y="Price", data=df)
plt.title("Area vs Price")
plt.show()

# Graph 4
plt.figure(figsize=(8,5))
sns.countplot(x="Location", data=df)
plt.title("Properties by Location")
plt.show()

# Correlation
plt.figure(figsize=(6,5))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()