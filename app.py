import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Frameworks Assignment App")

# Load dataset
df = pd.read_csv("metadata.csv")
st.write("### Dataset Preview", df.head())

# Show statistics
st.write("### Summary Statistics")
st.write(df.describe())

# -----------------
# Visualization
# ------------------

# Sales Distribution
st.write("### Sales Distribution")
fig, ax = plt.subplots()
sns.histplot(df['Sales'], bins=10, kde=True, ax=ax)
st.pyplot(fig)

# Bar chart of Sales by Product
st.write("### Sales by Product")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="Product", y="Sales", data=df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Boxplot of Sales
st.write("### Boxplot of Sales")
fig, ax = plt.subplots()
sns.boxplot(y=df['Sales'], ax=ax)
st.pyplot(fig)