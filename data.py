import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS contacts 
                         (id INTIGER PRIMARY KEY , fname TEXT , lname TEXT , email TEXT ,password TEXT )''')
        self.con.commit ()
        
    def fetch(self):
        self.cur.execute('SELECT * FROM contacts')
        rows = self .cur.fetchall()
        return rows 
    
    def insert (self,fname,lname,email,password):
        self.cur.execute('INSERT INTO contacts VALUES (null,?,?,?,?)',( fname , lname , email , password))
        self.con.commit()
    
    def search (self,fname):
        self.cur.execute ('''SELECT * FROM contacts WHERE id = ? or fname=? or lname=? or email=? or password=?'''
                            ,(fname,fname,fname,fname,fname))
        recs = self.cur.fetchall()
        return recs
        
# db=Database('c:/project/data.db')
# db.con.close()
                      
        