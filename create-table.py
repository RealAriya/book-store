import sqlite3

def create_table():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY, 
        title TEXT, 
        author TEXT, 
        year INTEGER, 
        isbn INTEGER
    )
    """)
    conn.commit()
    conn.close()

create_table()
