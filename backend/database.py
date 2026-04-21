import mysql.connector

# Database connection config
def get_connection():
    connection = mysql.connector.connect(
        host="localhost",        # MySQL server host
        user="root",             # MySQL username
        password="your-password", # ← Change this to your MySQL password
        database="machine_db"   # Database name
    )
    return connection