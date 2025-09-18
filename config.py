import MySQLdb

def get_db_connection():
    connection = MySQLdb.connect(
        host="localhost",     # your MySQL host
        user="root",          # your MySQL username
        passwd="",    # your MySQL password
        db="todo_db",         # your database name
        charset="utf8mb4"     # ensures UTF-8 encoding
    )
    return connection
