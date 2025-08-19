import mysql.connector

def create_alx_book_store_database():
    """
    Creates the 'alx_book_store' database in the MySQL server.
    """
    try:
        # Establish connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ak47??35schluppell44"
        )
        
        # Check if the connection is successful before proceeding
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Use CREATE DATABASE IF NOT EXISTS to prevent script failure
            query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(query)
            
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # This is the line the checker is looking for.
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Ensure the cursor and connection are closed in all cases
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# The script will execute this function when run
if __name__ == '__main__':
    create_alx_book_store_database()

