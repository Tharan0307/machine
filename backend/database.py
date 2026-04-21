import mysql.connector
import os

def get_connection():
    connection = mysql.connector.connect(
        host=os.environ.get("shinkansen.proxy.rlwy.net"),
        user=os.environ.get("root"),
        password=os.environ.get("lKbGJmmzVgOmDcTQlOceqXdNEsVrCKJb"),
        database=os.environ.get("machine_db"),
        port=int(os.environ.get("DB_PORT", 30624))
    )
    return connection