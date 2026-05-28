import requests
import pandas as pd
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)

# API URL
URL = "https://api.open-meteo.com/v1/forecast"

# Parameters
params = {
    "latitude": 13.08,
    "longitude": 80.27,
    "current_weather": True
}

try:
    logging.info("Fetching weather data...")

    response = requests.get(URL, params=params)

    # Check API response
    response.raise_for_status()

    data = response.json()

    logging.info("Data fetched successfully")

    # Extract current weather
    current_weather = data.get("current_weather", {})

    # Convert to DataFrame
    df = pd.DataFrame([current_weather])

    print(df)

except requests.exceptions.RequestException as e:
    logging.error(f"API request failed: {e}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")