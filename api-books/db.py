import sqlite3
#create db connection
conn = sqlite3.connect("books.sqlite")
#create the db cursor object
cursor = conn.cursor()
#create sql table creation query
sql_query = """ CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        genre TEXT NOT NULL,
                        year INTEGER NOT NULL
                    )"""

cursor.execute(sql_query)