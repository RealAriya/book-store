import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect('books.db')  # It create database itself
        self.cur = self.conn.cursor
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)" , (title, author, year, isbn))
        self.conn.commit()

    
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows
    

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows