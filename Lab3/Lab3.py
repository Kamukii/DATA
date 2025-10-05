import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def splitData(df):
    """
    Sequentially split the dataset into 80% training and 20% testing.
    """
    split_index = int(len(df) * 0.8)
    train = df.iloc[:split_index]
    test = df.iloc[split_index:]
    return train, test

def splitDataRandom(df):
    """
    Randomly split the dataset into 80% training and 20% testing.
    """
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    return train, test

if __name__ == "__main__":
    # Argument parser for dataset file input
    parser = argparse.ArgumentParser(description="Lab3 dataset splitting")
    parser.add_argument("--file", required=True, help="Path to dataset file (CSV)")
    args = parser.parse_args()

    # Load dataset
    try:
        df = pd.read_csv(args.file)
        print(f"Dataset loaded successfully with {len(df)} rows and {len(df.columns)} columns.")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        exit(1)

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

