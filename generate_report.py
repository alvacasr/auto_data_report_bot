"""
generate_report.py

Generates a simple analytical report from cleaned cryptocurrency data.
Creates summary statistics and visualization charts.

Author: Ramon Alvarado
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


INPUT_FILE = Path("data/crypto_prices_clean.csv")
REPORT_DIR = Path("reports")


def load_data():
    """Load cleaned dataset."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Clean dataset not found: {INPUT_FILE}. Run clean_data.py first."
        )

    print("Loading cleaned data...")
    df = pd.read_csv(INPUT_FILE, parse_dates=["timestamp"])

    return df


def generate_summary(df):
    """Generate summary statistics."""

    print("Generating summary statistics...")

    summary = df.groupby("name").agg(
        avg_price=("price_usd", "mean"),
        max_price=("price_usd", "max"),
        min_price=("price_usd", "min"),
        avg_volume=("volume_24h", "mean")
    )

    summary = summary.sort_values("avg_price", ascending=False)

    return summary


def plot_top_prices(df):
    """Create bar chart for top cryptocurrencies by price."""

    print("Generating price chart...")

    latest = df.loc[df.groupby("name")["timestamp"].idxmax()]

    top = latest.sort_values("price_usd", ascending=False).head(10)

    plt.figure()

    plt.bar(top["name"], top["price_usd"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Price (USD)")
    plt.title("Top 10 Cryptocurrencies by Price")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    chart_path = REPORT_DIR / "top_crypto_prices.png"
    plt.tight_layout()
    plt.savefig(chart_path)
    
    plt.close()

    print(f"Chart saved to {chart_path}")


def save_summary(summary):
    """Save summary table."""

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = REPORT_DIR / "summary_statistics.csv"

    summary.to_csv(output_file)

    print(f"Summary statistics saved to {output_file}")


def main():
    """Main report generation pipeline."""

    df = load_data()

    summary = generate_summary(df)

    save_summary(summary)

    plot_top_prices(df)

    print("Report generation completed successfully.")


if __name__ == "__main__":
    main()
