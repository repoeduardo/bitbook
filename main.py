from libs import database

# Example of use
connection, cursor = database.connect()
if connection and cursor:
    # Here you can execute SQL queries
    # For example, to insert a new book:
    # cursor.execute("INSERT INTO Book (AUTHOR, TITLE, SUBTITLE, GENRE, YEAR, PUBLISHER, DESCRIPTION) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    #                ('Example Author', 'Example Title', 'Example Subtitle', 'Fiction', 2023, 'Example Publisher', 'Example Description'))
    # connection.commit()

    # Close connection and cursor
    cursor.close()
    connection.close()
    print("MySQL connection has been closed")
