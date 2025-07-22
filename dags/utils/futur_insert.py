from utils.forecasting_future import stream_data
import psycopg2
from datetime import datetime
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
            host="postgres",  
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
    CREATE TABLE IF NOT EXISTS dev.future_raw_data (
    id SERIAL PRIMARY KEY,
    location_name TEXT,
    country TEXT,
    forecast_date DATE,
    forecast_time TIMESTAMP,
    temp_c NUMERIC,
    condition TEXT,
    wind_kph NUMERIC,
    humidity INT,
    chance_of_rain INT

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
    cursor = conn.cursor()

    location_name = data['location']['name']
    country = data['location']['country']

    for day in data['forecast']['forecastday']:
        for hour in day['hour']:
            forecast_date = hour['time'].split(' ')[0]
            forecast_time = datetime.strptime(hour['time'], '%Y-%m-%d %H:%M')
            temp_c = hour['temp_c']
            condition = hour['condition']['text']
            wind_kph = hour['wind_kph']
            humidity = hour['humidity']
            chance_of_rain = hour.get('chance_of_rain', 0)

            cursor.execute("""
                INSERT INTO dev.future_raw_data (
                    location_name, country, forecast_date, forecast_time,
                    temp_c, condition, wind_kph, humidity, chance_of_rain
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                location_name, country, forecast_date, forecast_time,
                temp_c, condition, wind_kph, humidity, chance_of_rain
            ))

    conn.commit()
    cursor.close()
    print("All forecast data inserted.")

def main():
    conn = connect_to_db()
    if conn:
        print("Connected to the database successfully.")
        create_schema(conn)
        create_table(conn)
        data = stream_data("Oujda",4)  
        inserting_data(conn, data)
        
        conn.close()
        print("Connection closed.")

main()