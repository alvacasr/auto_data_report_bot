# Auto Data Report Bot

Automated Python bot that fetches real-world data from an API, cleans it, and generates analytical reports automatically.

## Overview

This project demonstrates a simple data pipeline built with Python that collects cryptocurrency market data, processes it, and generates visual reports.

The goal of this project is to show how real-world data can be ingested, cleaned, analyzed, and transformed into automated reports.

## Features

- Fetch real-time cryptocurrency data from an API
- Clean and validate the dataset
- Generate summary statistics
- Create visual reports automatically
- Reproducible data pipeline

## Technologies Used

- Python
- Pandas
- Matplotlib
- Requests

## Project Structure


auto-data-report-bot
│
├── fetch_data.py # Fetches cryptocurrency data from API
├── clean_data.py # Cleans and validates dataset
├── generate_report.py # Generates charts and summary statistics
│
├── data/
│ ├── crypto_prices.csv
│ └── crypto_prices_clean.csv
│
├── reports/
│ ├── summary_statistics.csv
│ └── top_crypto_prices.png
│
└── README.md


## Data Source

Cryptocurrency data is retrieved from the public API of CoinGecko.

https://www.coingecko.com/

## Pipeline Workflow

The pipeline follows three main steps:

1. Data ingestion  
   - Fetch cryptocurrency market data from the API.

2. Data cleaning  
   - Remove missing values  
   - Validate numeric fields  
   - Prepare dataset for analysis

3. Report generation  
   - Calculate summary statistics  
   - Generate visualizations  
   - Save reports automatically

Pipeline flow:

fetch_data.py → clean_data.py → generate_report.py

## Installation

Clone the repository:


git clone https://github.com/yourusername/auto-data-report-bot.git

cd auto-data-report-bot


Install dependencies:


pip install -r requirements.txt


## Usage

Run the pipeline step by step:

### 1. Fetch data


python fetch_data.py


### 2. Clean data


python clean_data.py


### 3. Generate report


python generate_report.py


The generated charts and summary files will be stored in the `reports/` directory.

## Example Output

The project generates:

- Summary statistics for each cryptocurrency
- Visualization of the top cryptocurrencies by price

Example chart:

reports/top_crypto_prices.png

## Future Improvements

Possible improvements include:

- Scheduling automatic data collection
- Adding more visualizations
- Building an interactive dashboard
- Storing data in a database
- Creating a web interface
