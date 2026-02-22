import os
from src.transform import clean_data

TEST_FILE = "data/raw/sample.csv"


def test_clean_data():
    assert os.path.exists(TEST_FILE), "Test data file does not exist."

    df = clean_data(TEST_FILE)

    # Check no null values
    assert df.isnull().sum().sum() == 0

    # Check total column exists
    assert "total" in df.columns

    # Validate calculation
    first_row = df.iloc[0]
    assert first_row["total"] == first_row["quantity"] * first_row["price"]
