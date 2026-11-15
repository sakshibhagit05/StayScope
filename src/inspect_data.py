
import pandas as pd
import os

# Get the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
DATASET_PATH = os.path.join(BASE_DIR, "data", "AB_NYC_2019.csv")

# Check dataset
if not os.path.exists(DATASET_PATH):
    print("Dataset not found! Check the file location.")
else:
    # Load dataset
    df = pd.read_csv(DATASET_PATH)

    print("\n========== STAYSCOPE ==========")
    print("\nDataset loaded successfully!")

    # Display dataset shape
    print("\nDataset Shape:")
    print(df.shape)

    # Display first five records
    print("\nFirst 5 Records:")
    print(df.head())

    # Display column names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # Display dataset information
    print("\nDataset Information:")
    df.info()

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\n========== END ==========")
