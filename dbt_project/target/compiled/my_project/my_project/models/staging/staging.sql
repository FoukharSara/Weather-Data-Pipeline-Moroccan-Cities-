


with source as (

    select *
    from "weather_streaming"."dev"."raw_weather_data"
)
select
    id,
    location_name as City,
    country as Country,
    local_time as Local_Time,
    temp_c as Temperature_C,
    temp_f as Temperature_F,
    humidity as Humidity,
    wind_kph as Wind_Speed_KPH,
    pressure_mb as Pressure_MB,
    cloud
from source