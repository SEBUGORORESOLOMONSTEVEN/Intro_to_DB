import mysql.connector
from mysql.connector import Error

def create_alx_book_store_database():
    """
    Creates the 'alx_book_store' database in the MySQL server.
    """
    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ak47??35schluppell44"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(query)

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    create_alx_book_store_database()

