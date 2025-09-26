


with source as (
    select *
    from "weather_streaming"."dev"."future_raw_data"
),

de_dup as (
    select
        row_number() over (partition by location_name order by forecast_time) as row_num,
        *
    from source
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
FROM de_dup