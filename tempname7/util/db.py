import sqlite3

def init_db(f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    try:
        c.execute("CREATE TABLE users(username TEXT PRIMARY KEY, password TEXT)")
        c.execute("CREATE TABLE board(name TEXT, id INTEGER PRIMARY KEY)")
        c.execute("CREATE TABLE cards(id INTEGER PRIMARY KEY, description TEXT NOT NULL)")
    except:
        print "Database has already been initialized!"
        return False
        
    db.commit()
    db.close()
    return True
    
#returns true if there's a possible injection
def checc_injecc(strr):
    bad_chars = '~`!@#$%^&*()_+-=[]{}\|:;",./<>?\\\''
    for charr in bad_chars:
        if charr in strr:
            return True
    return False

#==========================USERS FUNCTIONS==========================
def add_user(username, password, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    if checc_injecc(username) or checc_injecc(password):
        print "Don't use special characters buddy"
        return False #failed
    
    #inserts into table
    try:
        comm = 'INSERT INTO users VALUES("%s", "%s")' %(username, password)
        c.execute(comm)
    except:
        print "Username taken!"
        return False
    
    db.commit()
    db.close()
    return True
    
def get_user(username, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    if checc_injecc(username):
        print "Don't use special characters buddy"
        return False #failed
    
    comm = 'SELECT * FROM users WHERE username="%s";' %(username)
    c.execute(comm)
    #returns a list
    fet = c.fetchall()
    if len(fet) == 0:
        return fet
    return fet[0]

#==========================BOARD FUNCTIONS==========================
'''
board: street name, color value, price, etc
cards: attributes
  split them up into chance cards db and community (?) cards db
'''






#==========================CARDS FUNCTIONS==========================




#===============================TESTS===============================

init_db("data.db")
print get_user("jenni", "data.db")
add_user("jenni", "12345", "data.db")
print get_user("jenni", "data.db")

add_user("'sdfajslk", "12345", "data.db")
print get_user("'sdfajslk", "data.db")
