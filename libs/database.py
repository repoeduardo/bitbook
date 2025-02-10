import config
import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,  # or your MySQL server address
            database=config.DB_NAME,  # name of your database
            user=config.DB_USER,  # your MySQL username
            password=config.DB_PASSWORD  # your MySQL password
        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You are connected to the database: ", record)
            return connection, cursor

    except Error as e:
        print("Error connecting to MySQL", e)

    return None, None
