import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import argparse

def splitData(df):
    train_size = int(0.8 * len(df))
    return df.iloc[:train_size], df.iloc[train_size:]

def splitDataRandom(df):
    return train_test_split(df, test_size=0.2, random_state=42)

def dataset_statistics(df):
    print("\n===== DATASET STATISTICS =====")
    print("\n--- Mean values ---")
    print(df.mean(numeric_only=True))   # mean of numeric columns

    print("\n--- Max values ---")
    print(df.max(numeric_only=True))    # max

    print("\n--- Min values ---")
    print(df.min(numeric_only=True))    # min

    print("\n--- Correlation Matrix ---")
    print(df.corr(numeric_only=True))   # correlation matrix


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to CSV dataset")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.file)
        print(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        
        # Statistics analysis
        dataset_statistics(df)

        # Sequential split
        train_seq, test_seq = splitData(df)
        print("\nSequential Split:")
        print(f"Training set size: {len(train_seq)}")
        print(f"Testing set size: {len(test_seq)}")

        # Random split
        train_rand, test_rand = splitDataRandom(df)
        print("\nRandom Split:")
        print(f"Training set size: {len(train_rand)}")
        print(f"Testing set size: {len(test_rand)}")

    except Exception as e:
        print("Error loading dataset:", e)
