from streaming_data import  mock_data
import json
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
        print(conn) 
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

# def insert_data():
#     data = mock_data()
#     if data:
#         print("Inserting data into the database...")
#         try:
            
        
#         except Exception as e:
#             print(f"An error occurred while inserting data: {e}")
#     else:
#         print("No data to insert.")
        
connect_to_db()