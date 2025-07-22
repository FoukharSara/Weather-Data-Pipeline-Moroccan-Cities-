{{config(
    materialized='table',
    unique_key='id'
)}}

select 
    city,
    local_time,
    temperature_F,
    temperature_C,
    humidity,
    wind_Speed_KPH,
    pressure_MB
from {{ ref('stg_weather_data') }}
