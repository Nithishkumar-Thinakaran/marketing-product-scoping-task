SELECT
    AVG(temperature_celsius) AS average_temperature,
    AVG(humidity) AS average_humidity
FROM
    `forward-cacao-497708-r6.weather_pipeline.weather_data`;