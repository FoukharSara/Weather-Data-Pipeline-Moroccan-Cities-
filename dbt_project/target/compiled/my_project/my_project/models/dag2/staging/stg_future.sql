


with source as (
    select *
    from "weather_streaming"."dev"."future_raw_data"
)

SELECT id,
    location_name as city,
    country ,
    DATE(forecast_date) AS dateForecast,
    forecast_time::time AS timeForecast,
    temp_c as temperature_C,
    condition as weatherCondition,
    wind_kph as wind_Speed_KPH,
    humidity as humidity,
    chance_of_rain as chanceOfRain
FROM source