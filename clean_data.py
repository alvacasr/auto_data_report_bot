"""
clean_data.py

Loads raw cryptocurrency data, performs basic cleaning,
and saves a cleaned dataset for analysis.

Author: Ramon Alvarado
"""

import pandas as pd
from pathlib import Path


INPUT_FILE = Path("data/crypto_prices.csv")
OUTPUT_FILE = Path("data/crypto_prices_clean.csv")


def load_data():
    """Load raw dataset."""
    
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Raw data file not found: {INPUT_FILE}. Run fetch_data.py first."
        )

    print("Loading raw data...")
    df = pd.read_csv(INPUT_FILE, low_memory=False)

    return df


def clean_data(df):
    """Clean and prepare dataset."""
    
    print("Cleaning data...")

    # Remove rows with missing values in key fields
    df = df.dropna(subset=["name", "symbol", "price_usd"])

    # Remove duplicate records
    df = df.drop_duplicates()
    
    df = df.copy()

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Ensure numeric columns are numeric
    numeric_cols = ["price_usd", "market_cap", "volume_24h"]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows where price is invalid
    df = df[df["price_usd"].notna() & (df["price_usd"] > 0)]

    return df


def save_clean_data(df):
    """Save cleaned dataset."""

    print("Saving cleaned dataset...")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Clean dataset saved to {OUTPUT_FILE}")


def main():
    """Main cleaning pipeline."""

    df = load_data()
    clean_df = clean_data(df)
    save_clean_data(clean_df)

    print("Data cleaning pipeline completed successfully.")


if __name__ == "__main__":
    main()
