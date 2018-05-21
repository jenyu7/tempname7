import sqlite3

def init_db(f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("CREATE TABLE board(name TEXT, id INTEGER PRIMARY KEY)")
    c.execute("CREATE TABLE cards(id INTEGER PRIMARY KEY, description TEXT NOT NULL)")
    db.commit()
    db.close()
