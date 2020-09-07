import psycopg2

class Database:

    def __init__(self):
        self.conn=psycopg2.connect("dbname='Bookstore' user='postgres' password='root' host='localhost' port='5432'")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id SERIAL PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
        self.conn.commit()


    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book(title,author,year,isbn) VALUES ('%s','%s','%s','%s')" %(title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book ORDER BY id ASC")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title='%s' OR author='%s' OR year='%s' OR isbn='%s'" %(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id='%s'" %(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title='%s',author='%s',year=%s,isbn=%s WHERE id=%s" %(title,author,year,isbn,id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
