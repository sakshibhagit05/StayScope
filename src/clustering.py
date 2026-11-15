
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned_airbnb.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("========== STAYSCOPE K-MEANS CLUSTERING ==========")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Select features
features = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "availability_365"
]

# Prepare data
X = df[features].copy()

# Reduce extreme skew in numerical features
X["price"] = np.log1p(X["price"])
X["minimum_nights"] = np.log1p(X["minimum_nights"])
X["number_of_reviews"] = np.log1p(X["number_of_reviews"])
X["reviews_per_month"] = np.log1p(X["reviews_per_month"])

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X_scaled)

# Evaluate clustering
score = silhouette_score(
    X_scaled,
    df["cluster"],
    sample_size=5000,
    random_state=42
)

print("\nSilhouette Score:", round(score, 3))

# Cluster summary
print("\nCluster Summary:")

summary = df.groupby("cluster")[features].mean().round(2)
print(summary)

# Number of listings in each cluster
print("\nListings per Cluster:")
print(df["cluster"].value_counts().sort_index())

# Save clustered dataset
clustered_path = os.path.join(
    OUTPUT_DIR,
    "clustered_airbnb.csv"
)

df.to_csv(clustered_path, index=False)

# Cluster visualization
plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df.sample(min(5000, len(df)), random_state=42),
    x="minimum_nights",
    y="price",
    hue="cluster",
    palette="viridis",
    alpha=0.7
)

plt.title("Airbnb Listings - K-Means Clustering")
plt.xlabel("Minimum Nights")
plt.ylabel("Price (USD)")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "kmeans_clusters.png")
)

plt.show()

print("\nClustering Completed Successfully!")
print("\nClustered dataset saved at:", clustered_path)

print("\n========== END ==========")
