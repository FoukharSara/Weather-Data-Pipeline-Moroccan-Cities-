{{ config(
    materialized='table',
    unique_key='id'
)}}


with source as (

    select *
    from {{ source('dev', 'raw_weather_data') }}
),

de_dup as (
    select
        row_number() over (partition by location_name, local_time order by recorded_at) as row_num,
        *
    from source
)



select
    id,
    location_name as city,
    country as country,
    local_time ,
    temp_c as temperature_C,
    temp_f as temperature_F,
    humidity as humidity,
    wind_kph as wind_Speed_KPH,
    pressure_mb as pressure_MB,
    cloud,
    recorded_at as recorded_At
from de_dup
where row_num = 1
