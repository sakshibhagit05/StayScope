
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned_airbnb.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("========== STAYSCOPE PATTERN ANALYSIS ==========")

# Load dataset
df = pd.read_csv(DATA_PATH)

# 1. Listings in each neighbourhood group
neighbourhood_counts = (
    df["neighbourhood_group"]
    .value_counts()
)

print("\nListings by Neighbourhood Group:")
print(neighbourhood_counts)

# 2. Room type distribution by neighbourhood group
room_patterns = pd.crosstab(
    df["neighbourhood_group"],
    df["room_type"]
)

print("\nRoom Type Distribution by Neighbourhood Group:")
print(room_patterns)

# 3. Average price by neighbourhood group and room type
price_patterns = df.pivot_table(
    values="price",
    index="neighbourhood_group",
    columns="room_type",
    aggfunc="mean"
).round(2)

print("\nAverage Price by Neighbourhood Group and Room Type:")
print(price_patterns)

# Save analysis results
neighbourhood_counts.to_csv(
    os.path.join(OUTPUT_DIR, "neighbourhood_counts.csv")
)

room_patterns.to_csv(
    os.path.join(OUTPUT_DIR, "room_type_patterns.csv")
)

price_patterns.to_csv(
    os.path.join(OUTPUT_DIR, "price_patterns.csv")
)

# 4. Visualize room type distribution
room_patterns.plot(
    kind="bar",
    figsize=(11, 6)
)

plt.title("Room Type Distribution by Neighbourhood Group")
plt.xlabel("Neighbourhood Group")
plt.ylabel("Number of Listings")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "room_type_patterns.png")
)

plt.show()

# 5. Visualize average price patterns
plt.figure(figsize=(11, 6))

sns.heatmap(
    price_patterns,
    annot=True,
    fmt=".1f",
    cmap="YlGnBu"
)

plt.title("Average Airbnb Price by Neighbourhood Group and Room Type")
plt.xlabel("Room Type")
plt.ylabel("Neighbourhood Group")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "price_patterns_heatmap.png")
)

plt.show()

print("\nPattern Analysis Completed Successfully!")

print("\nGenerated files:")
print("neighbourhood_counts.csv")
print("room_type_patterns.csv")
print("price_patterns.csv")
print("room_type_patterns.png")
print("price_patterns_heatmap.png")

print("\n========== END ==========")
