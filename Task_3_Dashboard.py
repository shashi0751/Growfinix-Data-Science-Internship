import streamlit as st
import pandas as pd

# Sample Tour Enquiry Data
data = {
    "Customer": ["Aman", "Priya", "Rahul", "Sneha", "Rohan", "Anjali", "Vikas", "Neha"],
    "Destination": ["Goa", "Manali", "Goa", "Jaipur", "Manali", "Goa", "Kerala", "Jaipur"],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Pune", "Delhi", "Bangalore", "Jaipur"],
    "Enquiries": [5, 3, 7, 2, 6, 4, 5, 3]
}

df = pd.DataFrame(data)

st.title("🌍 Tour Enquiry Dashboard")

st.subheader("Tour Enquiry Data")
st.dataframe(df)

st.subheader("Most Popular Destinations")
st.bar_chart(df["Destination"].value_counts())

st.subheader("City-wise Enquiries")
st.bar_chart(df.groupby("City")["Enquiries"].sum())

st.subheader("Destination Distribution")
st.write(df["Destination"].value_counts())