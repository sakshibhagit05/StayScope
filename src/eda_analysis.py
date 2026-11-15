
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned_airbnb.csv")

# Output directory
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA_PATH)

print("========== STAYSCOPE EDA ANALYSIS ==========")

# 1. Basic statistics
print("\nDataset Overview:")
print(df.describe())

# 2. Average price
print("\nAverage Airbnb Price:")
print(round(df["price"].mean(), 2))

# 3. Room type distribution
print("\nRoom Type Distribution:")
print(df["room_type"].value_counts())

# 4. Average price by room type
print("\nAverage Price by Room Type:")
print(df.groupby("room_type")["price"].mean().round(2))

# 5. Top 10 neighbourhoods by listing count
print("\nTop 10 Neighbourhoods:")
print(df["neighbourhood"].value_counts().head(10))

# 6. Average price by neighbourhood group
print("\nAverage Price by Neighbourhood Group:")
print(
    df.groupby("neighbourhood_group")["price"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# 7. Room Type Distribution Graph
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="room_type", hue="room_type", legend=False)
plt.title("Airbnb Room Type Distribution")
plt.xlabel("Room Type")
plt.ylabel("Number of Listings")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "room_type_distribution.png"))
plt.show()

# 8. Average Price by Room Type Graph
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="room_type", y="price", hue="room_type", legend=False)
plt.title("Average Price by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Average Price ($)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "average_price_by_room_type.png"))
plt.show()

# 9. Price Distribution Graph
plt.figure(figsize=(8, 5))
sns.histplot(df["price"], bins=50, kde=True)
plt.title("Airbnb Price Distribution")
plt.xlabel("Price ($)")
plt.ylabel("Number of Listings")
plt.xlim(0, 1000)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "price_distribution.png"))
plt.show()

# 10. Top 10 Neighbourhoods Graph
top_neighbourhoods = df["neighbourhood"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_neighbourhoods.values,
    y=top_neighbourhoods.index,
    hue=top_neighbourhoods.index,
    legend=False
)
plt.title("Top 10 Neighbourhoods by Listings")
plt.xlabel("Number of Listings")
plt.ylabel("Neighbourhood")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_neighbourhoods.png"))
plt.show()

print("\nEDA Analysis Completed Successfully!")
print("\nGraphs saved in outputs folder.")
print("\n========== END ==========")
