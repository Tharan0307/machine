import mysql.connector
import os

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="shinkansen.proxy.rlwy.net",
            port=30624,
            user="root",
            password="lKbGJmmzVgOmDcTQlOceqXdNEsVrCKJb",
            database="machine_db",
            connection_timeout=30,
            ssl_disabled=True
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        raise e