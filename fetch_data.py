"""
fetch_data.py

Fetches cryptocurrency market data from the CoinGecko API
and saves it to a CSV file for further analysis.

Author: Ramon Alvarado Castillo
"""

import requests
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path


API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1,
    "sparkline": False
}


OUTPUT_DIR = Path("data")
OUTPUT_FILE = OUTPUT_DIR / "crypto_prices.csv"


def fetch_crypto_data():
    """Fetch cryptocurrency market data from CoinGecko."""
    
    print("Fetching data from CoinGecko API...")

    headers = {
        "accept": "application/json"
    }

    response = requests.get(API_URL, params=PARAMS, headers=headers timeout=10)
    response.raise_for_status()

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    data = response.json()

    print("Data fetched successfully.")
    return data


def transform_data(data):
    """Transform raw JSON into a clean pandas DataFrame."""
    
    records = []

    for coin in data:
        records.append({
            "timestamp": datetime.now(timezone.utc),
            "name": coin.get["name"],
            "symbol": coin.get["symbol"],
            "price_usd": coin.get["current_price"],
            "market_cap": coin.get["market_cap"],
            "volume_24h": coin.get["total_volume"]
        })

    df = pd.DataFrame(records)

    return df


def save_data(df):
    """Save DataFrame to CSV."""
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if OUTPUT_FILE.exists():
        df.to_csv(OUTPUT_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(OUTPUT_FILE, index=False)

    print(f"Data saved to {OUTPUT_FILE}")


def main():
    """Main pipeline execution."""
    
    raw_data = fetch_crypto_data()
    df = transform_data(raw_data)
    save_data(df)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
