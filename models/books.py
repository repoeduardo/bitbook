import config
import mysql.connector
from mysql.connector import Error
from rich.console import Console

class Book:

    def __init__(self, author="", title="", subtitle="", genre="", book_year=0, publisher="", book_description=""):
        self.author = str(author)
        self.title = str(title)
        self.subtitle = str(subtitle)
        self.genre = str(genre)
        self.book_year = int(book_year) if book_year else 0 # Convert to int only if is not 0
        self.publisher = str(publisher)
        self.book_description = str(book_description)

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=config.DB_HOST,  # or your MySQL server address
                database=config.DB_NAME,  # name of your database
                user=config.DB_USER,  # your MySQL username
                password=config.DB_PASSWORD  # your MySQL password
            )

            if connection.is_connected():
                db_Info = connection.get_server_info()
                #print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                #print("You are connected to the database: ", record)
                return connection, cursor

        except Error as e:
            print("Error connecting to MySQL", e)

        return None, None

    def insert(self):
        # Establish connection with the database
        connection, cursor = self.connect()
        if connection and cursor:
            try:
                # Prepare data for insertion
                insert_query = """
                INSERT INTO Books (author, title, subtitle, genre, book_year, publisher, book_description)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                # Values are passed as a tuple
                data = (
                    self.author,
                    self.title,
                    self.subtitle,
                    self.genre,
                    self.book_year,
                    self.publisher,
                    self.book_description
                )

                # Execute the insertion query
                cursor.execute(insert_query, data)

                # Commit the transaction
                connection.commit()
                console = Console()

                console.print(f"[green]Book '{self.title}' inserted successfully into the database.")

            except Error as e:
                # Rollback the transaction in case of an error
                connection.rollback()
                print(f"Error inserting book into MySQL: {e}")

            finally:
                # Close the connection and cursor
                cursor.close()
                connection.close()
                #print("MySQL connection has been closed")
        else:
            print("Failed to connect to the database. Insertion not performed.")

    def select_all(self):
        # Establish connection with the database
        connection, cursor = self.connect()
        if connection and cursor:
            try:
                # Prepare the query to select all books
                select_query = "SELECT * FROM books"

                # Execute the query
                cursor.execute(select_query)

                # Fetch all results
                results = cursor.fetchall()

                # Print each book's details
                #for row in results:
                #    print(f"ID: {row[0]}, Author: {row[1]}, Title: {row[2]}, Subtitle: {row[3]}, Genre: {row[4]}, Year: {row[5]}, Publisher: {row[6]}, Description: {row[7]}")

                return results  # Return all books if needed for further processing

            except Error as e:
                print(f"Error selecting books from MySQL: {e}")

            finally:
                # Close the connection and cursor
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
                #print("MySQL connection has been closed")
        else:
            print("Failed to connect to the database. Selection not performed.")
            return None

    def delete_by_id(self, book_id):
        console = Console()

        # Establish connection with the database
        connection, cursor = self.connect()
        if connection and cursor:
            try:
                # Prepare the query to delete a book by ID
                delete_query = "DELETE FROM books WHERE id = %s"

                # Execute the query with the specified ID
                cursor.execute(delete_query, (book_id,))

                # Commit the transaction
                connection.commit()
                console.print(f"[green]Book with ID {book_id} has been deleted from the database.[/green]\n")
                #print(f"Book with ID {book_id} has been deleted from the database.")

            except Error as e:
                # Rollback the transaction in case of an error
                connection.rollback()
                print(f"Error deleting book from MySQL: {e}")

            finally:
                # Close the connection and cursor
                cursor.close()
                connection.close()
                #print("MySQL connection has been closed")
        else:
            print("Failed to connect to the database. Deletion not performed.")
            # book = Book("Eduardo Araujo", "The cars", "tires over tires", "literature", 2025, "Banker", "Just a history, nothing much")
            # book.delete_by_id(3)

    def this_id_exist(self, book_id):

        connection, cursor = self.connect()

        if cursor and connection:
            try:
                # SQL query to check if the book_id exists
                query = "SELECT COUNT(*) FROM books WHERE id = %s"
                cursor.execute(query, (book_id,))

                # Fetch the count
                count = cursor.fetchone()[0]

                # If count is greater than 0, the ID exists. Returning True
                return count > 0
            except Error as e:
                #print(f"Error checking book id from MySQL: {e}")
                return False
            finally:
                # Close the connection and cursor
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
                #print("MySQL connection has been closed")
        else:
            #print("Failed to establish connection to database.")
            return False  # Return False if connection failed
