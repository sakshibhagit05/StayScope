
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned_airbnb.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# Load dataset
df = pd.read_csv(DATA_PATH)

print("========== PRICE OUTLIER ANALYSIS ==========")

# Price statistics
print("\nPrice Statistics:")
print(df["price"].describe())

# Calculate quartiles
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Identify outliers
outliers = df[
    (df["price"] < lower_limit) |
    (df["price"] > upper_limit)
]

print("\nTotal Outliers:", len(outliers))

print("\nTop 10 Most Expensive Listings:")
print(
    df.nlargest(10, "price")[
        ["name", "neighbourhood_group", "room_type", "price"]
    ]
)

# Boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(x=df["price"])

plt.title("Airbnb Price Outlier Analysis")
plt.xlabel("Price (USD)")
plt.xlim(0, upper_limit * 1.5)

plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "price_outliers.png")
)
plt.show()

print("\nOutlier Analysis Completed!")
print("========== END ==========")
