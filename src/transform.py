import pandas as pd
from src.utils import ensure_directory

RAW_PATH = "data/raw/sample.csv"
OUTPUT_DIR = "data/processed"
OUTPUT_PATH = "data/processed/cleaned_sample.csv"


def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Drop missing values
    df = df.dropna()

    # Create new feature
    df["total"] = df["quantity"] * df["price"]

    return df


def run_pipeline():
    ensure_directory(OUTPUT_DIR)
    df = clean_data(RAW_PATH)
    df.to_csv(OUTPUT_PATH, index=False)
    print("Pipeline executed successfully!")


if __name__ == "__main__":
    run_pipeline()
