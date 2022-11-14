import sqlite3
import os
absolute_path = os.path.dirname(__file__)
def create_db():
    relative_path = r"ims.db"
    full_path = os.path.join(absolute_path, relative_path)
    con=sqlite3.connect(database=full_path)
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text ,dob text,doj text, pass text, utype text, address text, salary text)")
    con.commit()


create_db()