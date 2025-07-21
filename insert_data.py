from streaming_data import  mock_data
import json
# download the psycopg2-binary package
import psycopg2
from dotenv import load_dotenv
import os

def connect_to_db():
    load_dotenv()
    password = os.getenv("PASSWORD_DB")
    
    try:
        conn = psycopg2.connect(
            dbname="weather_streaming",
            user="weather_streaming",
            password=password,
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        raise

def create_schema(conn):
    query = """
        CREATE SCHEMA IF NOT EXISTS dev;
    """
    try:
        print("Creating schema...")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        print("Schema created successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred while creating schema: {e}")
        raise
    
def create_table(conn):
    query= """
    CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
    id SERIAL PRIMARY KEY,
    
    -- Location info
    location_name VARCHAR(100),
    region VARCHAR(100),
    country VARCHAR(100),
    lat FLOAT,
    lon FLOAT,
    tz_id VARCHAR(50),
    local_time TIMESTAMP,
    
    -- Current weather info
    last_updated TIMESTAMP,
    temp_c REAL,
    temp_f REAL,
    is_day BOOLEAN,
    condition_text VARCHAR(100),
    condition_icon VARCHAR(255),
    condition_code INTEGER,
    wind_mph REAL,
    wind_kph REAL,
    wind_degree INTEGER,
    wind_dir VARCHAR(10),
    pressure_mb REAL,
    pressure_in REAL,
    precip_mm REAL,
    precip_in REAL,
    humidity INTEGER,
    cloud INTEGER,
    feelslike_c REAL,
    feelslike_f REAL,
    windchill_c REAL,
    heatindex_f REAL,
    dewpoint_c REAL,
    dewpoint_f REAL,
    vis_km REAL,
    vis_miles REAL,
    gust_mph REAL,
    gust_kph REAL,
    
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    );
    """
    try:
        print("Creating Table...")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Table created successfully.")
        cursor.close()
    
    except psycopg2.Error as e:
        print(f"An error occurred while creating table: {e}")
        raise


   

def inserting_data(conn, data):
    query = """
    INSERT INTO dev.raw_weather_data (
        location_name, region, country, lat, lon, tz_id, local_time,
        last_updated, temp_c, temp_f, is_day, condition_text, condition_icon, condition_code,
        wind_mph, wind_kph, wind_degree, wind_dir, pressure_mb, pressure_in,
        precip_mm, precip_in, humidity, cloud, feelslike_c, feelslike_f,
        windchill_c, heatindex_f, dewpoint_c, dewpoint_f, vis_km, vis_miles,
        gust_mph, gust_kph
    )
    VALUES (
        %(location_name)s, %(region)s, %(country)s, %(lat)s, %(lon)s, %(tz_id)s, %(local_time)s,
        %(last_updated)s, %(temp_c)s, %(temp_f)s, %(is_day)s, %(condition_text)s, %(condition_icon)s, %(condition_code)s,
        %(wind_mph)s, %(wind_kph)s, %(wind_degree)s, %(wind_dir)s, %(pressure_mb)s, %(pressure_in)s,
        %(precip_mm)s, %(precip_in)s, %(humidity)s, %(cloud)s, %(feelslike_c)s, %(feelslike_f)s,
        %(windchill_c)s, %(heatindex_f)s, %(dewpoint_c)s, %(dewpoint_f)s, %(vis_km)s, %(vis_miles)s,
        %(gust_mph)s, %(gust_kph)s
    );
    """

    values = {
        "location_name": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "lat": data["location"]["lat"],
        "lon": data["location"]["lon"],
        "tz_id": data["location"]["tz_id"],
        "local_time": data["location"]["localtime"],

        "last_updated": data["current"]["last_updated"],
        "temp_c": data["current"]["temp_c"],
        "temp_f": data["current"]["temp_f"],
        "is_day": bool(data["current"]["is_day"]),
        "condition_text": data["current"]["condition"]["text"],
        "condition_icon": data["current"]["condition"]["icon"],
        "condition_code": data["current"]["condition"]["code"],

        "wind_mph": data["current"]["wind_mph"],
        "wind_kph": data["current"]["wind_kph"],
        "wind_degree": data["current"]["wind_degree"],
        "wind_dir": data["current"]["wind_dir"],
        "pressure_mb": data["current"]["pressure_mb"],
        "pressure_in": data["current"]["pressure_in"],
        "precip_mm": data["current"]["precip_mm"],
        "precip_in": data["current"]["precip_in"],
        "humidity": data["current"]["humidity"],
        "cloud": data["current"]["cloud"],
        "feelslike_c": data["current"]["feelslike_c"],
        "feelslike_f": data["current"]["feelslike_f"],
        "windchill_c": data["current"]["windchill_c"],
        "heatindex_f": data["current"]["heatindex_f"],
        "dewpoint_c": data["current"]["dewpoint_c"],
        "dewpoint_f": data["current"]["dewpoint_f"],
        "vis_km": data["current"]["vis_km"],
        "vis_miles": data["current"]["vis_miles"],
        "gust_mph": data["current"]["gust_mph"],
        "gust_kph": data["current"]["gust_kph"]
    }

    try:
        print("Inserting data...")
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("Data inserted successfully.")
        cursor.close()

    except psycopg2.Error as e:
        print(f"An error occurred while inserting data: {e}")
        raise
  
conn = connect_to_db()
if conn:
    print("Connected to the database successfully.")
    create_schema(conn)
    create_table(conn)
    data = mock_data()  
    inserting_data(conn, data)
    
    conn.close()
    print("Connection closed.")

