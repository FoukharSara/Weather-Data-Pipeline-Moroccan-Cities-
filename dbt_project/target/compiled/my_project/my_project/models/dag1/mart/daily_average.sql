

select 
    city,
    date(local_time) as date,
    ROUND(AVG(temperature_F)::numeric, 2) AS avg_temperature_F,
    ROUND(AVG(temperature_C)::numeric, 2) as avg_temperature_C,
    ROUND(AVG(humidity)::numeric, 2) as avg_humidity,
    ROUND(AVG(wind_Speed_KPH)::numeric, 2) as avg_wind_speed_KPH,
    ROUND(AVG(pressure_MB)::numeric, 2) as avg_pressure_MB
from "weather_streaming"."dev"."stg_weather_data"
group by city, date(local_time)
order by city, date(local_time)