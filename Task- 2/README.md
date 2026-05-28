# Task 2 - Data Pipeline
## Overview

This project demonstrates a simple ETL data pipeline using Python and Google BigQuery.

----------------------------

## Pipeline Flow

API → Python → Data Transformation → BigQuery → SQL Analysis

--------------------------------
## API Used

Open-Meteo Weather API

---------------------------
## Features

* Fetches real-time weather data
* Performs data transformation
* Adds derived fields
* Uploads data to BigQuery
* Executes SQL analysis

-------------------------------------
## Technologies Used

* Python
* Pandas
* Requests
* Google BigQuery

-----------------------------------------
## Derived Field

Temperature in Fahrenheit was calculated from Celsius data.

------------------------------------------------
## Error Handling

The pipeline includes:

* API error handling
* Exception handling
* Logging

## Future Improvements

* Automate pipeline scheduling
* Add real-time streaming
* Support multiple cities
