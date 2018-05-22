#note to self:
#careful for injections

import sqlite3

def init_db(f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("CREATE TABLE board(name TEXT, id INTEGER PRIMARY KEY)")
    c.execute("CREATE TABLE cards(id INTEGER PRIMARY KEY, description TEXT NOT NULL)")
    c.execute("CREATE TABLE users(username TEXT PRIMARY KEY, password TEXT)")
    db.commit()
    db.close()

def add_user(username, password, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    #inserts into table
    comm = 'INSERT INTO users VALUES("%s", "%s")' %(username, password)
    c.execute(comm)

    db.commit()
    db.close()
    
def get_user(username, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    comm = 'SELECT * FROM users WHERE username="%s";' %(username)
    c.execute(comm)
    #returns a list
    fet = c.fetchall()
    if len(fet) == 0:
        return fet
    return fet[0]

init_db("data.db")
print get_user("jenni", "data.db")
add_user("jenni", "12345", "data.db")
print get_user("jenni", "data.db")
