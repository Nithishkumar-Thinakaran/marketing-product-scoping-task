import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# API URL (Chennai weather data)
API_URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "current": "temperature_2m,relative_humidity_2m"
}

try:
    logging.info("Fetching weather data from API...")

    response = requests.get(API_URL, params=params)

    # Raise error if request fails
    response.raise_for_status()

    data = response.json()

    logging.info("API data fetched successfully")

    # Extract current weather data
    current = data.get("current", {})

    weather_data = {
        "temperature_celsius": current.get("temperature_2m"),
        "humidity": current.get("relative_humidity_2m")
    }

    # Create DataFrame
    df = pd.DataFrame([weather_data])

    # Derived field
    df["temperature_fahrenheit"] = (
        df["temperature_celsius"] * 9/5
    ) + 32

    print(df)

except requests.exceptions.RequestException as e:
    logging.error(f"API request failed: {e}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")

from pandas_gbq import to_gbq
import os

# Set Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Task-2/weather-key.json"

# BigQuery project details
project_id = "forward-cacao-497708-r6"
table_id = "weather_pipeline.weather_data"

try:
    # Upload dataframe to BigQuery
    to_gbq(
        df,
        destination_table=table_id,
        project_id=project_id,
        if_exists="append"
    )

    logging.info("Data uploaded to BigQuery successfully")

except Exception as e:
    logging.error(f"BigQuery upload failed: {e}")