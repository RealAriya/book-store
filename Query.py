import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect('books.db')  # It create database itself
        self.cur = self.conn.cursor
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        self.conn.close()
    

    