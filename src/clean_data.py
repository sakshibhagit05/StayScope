
import pandas as pd
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths
INPUT_PATH = os.path.join(BASE_DIR, "data", "AB_NYC_2019.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "cleaned_airbnb.csv")

print("========== STAYSCOPE DATA CLEANING ==========")

# Check dataset
if not os.path.exists(INPUT_PATH):
    print("Dataset not found! Check the file location.")

else:
    # Load dataset
    df = pd.read_csv(INPUT_PATH)

    print("\nOriginal Dataset Shape:", df.shape)

    # 1. Remove duplicate records
    df.drop_duplicates(inplace=True)

    # 2. Handle missing listing names
    df["name"] = df["name"].fillna("Unknown Listing")

    # 3. Handle missing host names
    df["host_name"] = df["host_name"].fillna("Unknown Host")

    # 4. Handle missing monthly reviews
    df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

    # 5. Convert review date into datetime
    df["last_review"] = pd.to_datetime(
        df["last_review"],
        errors="coerce"
    )

    # 6. Remove invalid prices
    df = df[df["price"] > 0]

    # 7. Remove invalid coordinates
    df = df[
        df["latitude"].between(-90, 90) &
        df["longitude"].between(-180, 180)
    ]

    # 8. Save cleaned dataset
    df.to_csv(OUTPUT_PATH, index=False)

    print("\nCleaning Completed Successfully!")

    print("\nCleaned Dataset Shape:", df.shape)

    print("\nRemaining Missing Values:")
    print(df.isnull().sum())

    print("\nCleaned dataset saved at:")
    print(OUTPUT_PATH)

    print("\n========== END ==========")
