

  create  table "weather_streaming"."dev"."weather_report__dbt_tmp"
  as (
    

select 
    city,
    local_time,
    temperature_F,
    temperature_C,
    humidity,
    wind_Speed_KPH,
    pressure_MB
from "weather_streaming"."dev"."stg_weather_data"
  );