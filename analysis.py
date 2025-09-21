import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("metadata.csv")

# Basic info
print("First 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

# -----------------
# Visualization
# ------------------

# Sales Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Sales'], kde=True, bins=10)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Count")
plt.savefig("sales_distribution.png")
plt.show()

# Bar chart of Sales by Product
plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales by Product")
plt.xticks(rotation=45)
plt.savefig("sales_by_product.png")
plt.show()

# Boxplot of Sales
plt.figure(figsize=(6, 4))
sns.boxplot(y=df['Sales'])
plt.title("Boxplot of Sales")
plt.savefig("sales_boxplot.png")
plt.show()
