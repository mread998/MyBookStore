import sqlite3

# inital database
def connect():
    conn=sqlite3.connect("book_Inventory.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("book_Inventory.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book_Inventory.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("book_Inventory.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? or author=? or year=? or isbn=?", (title.lower(), author.lower(), year, isbn))
    search_return=cur.fetchall()
    conn.close()
    return search_return

def delete(id):
    conn=sqlite3.connect("book_Inventory.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title, author, year, isbn):
    conn=sqlite3.connect("book_Inventory.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()

#checking if works
# insert("the sea", "john  tablet", 1918, 8938928394)
# delete(1)
# update(1, "the son", "John Table", 1918,8938928394)
# print(view())
# print(search(title="The sea"))