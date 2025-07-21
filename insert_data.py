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
    CREATE TABLE dev.raw_weather_data (
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


        
conn = connect_to_db()
if conn:
    print("Connected to the database successfully.")
    create_schema(conn)
    create_table(conn)
    
    conn.close()
    print("Connection closed.")

