import sqlite3
from hashlib import sha1
from random import random

def init_db(f='data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    try:
        init_users(c)
        init_board(c)
        init_cards(c)
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
def init_users(c, populate=True):
    c.execute("CREATE TABLE users(username TEXT PRIMARY KEY, password TEXT)")
    if populate:
        add_user("jenni", "12345")
        add_user("jzhang", "123456")
        add_user("cweng", "abcde")
        add_user("jyu", "abcd123")
        add_user("kwang", "123abcd")
        
def add_user(username, password, f='data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    if checc_injecc(username) or checc_injecc(password):
        print "Don't use special characters buddy"
        return False #failed
    
    #inserts into table
    try:
        passs = sha1(password).hexdigest()
        comm = 'INSERT INTO users VALUES("%s", "%s")' %(username, passs)
        c.execute(comm)
    except:
        print "Username taken!"
        return False
    
    db.commit()
    db.close()
    return True
    
def get_user(username, f='data.db'):
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
        return False
    return fet[0]

def auth(username, password, f='data.db'):
    return sha1(password).hexdigest() == get_user(username)[1]

#==========================BOARD FUNCTIONS==========================
#id is the place of the space, where 0 is go
#type is the type of place it is:
#  chance, community, tax, railroad, jail, go to jail, free parking, house, electric company, water works
def init_board(c, populate=True):
    c.execute("CREATE TABLE board(id INTEGER PRIMARY KEY, type INTEGER, name TEXT, color TEXT, price INTEGER)")

    '''
    if populate:
        comm = 'INSERT INTO board VALUES(%d, "%s", "%s", %d)' %(id, name, color, price)
        c.execute(comm)
    '''




#==========================CARDS FUNCTIONS==========================
def init_cards(c, populate=True):
    c.execute("CREATE TABLE chance_cards(id INTEGER PRIMARY KEY, description TEXT)")
    c.execute("CREATE TABLE comm_cards(id INTEGER PRIMARY KEY, description TEXT)")
    '''
    if populate:
        comm = 'INSERT INTO chance_cards VALUES(%d, "%s")' %(id, description)
        comm = 'INSERT INTO comm_cards VALUES(%d, "%s")' %(id, description)
        c.execute(comm)
    '''


#===============================TESTS===============================
'''

init_db("data.db")
print get_user("jenni", "data.db")
add_user("jenni", "12345", "data.db")
print get_user("jenni", "data.db")

add_user("'sdfajslk", "12345", "data.db")
print get_user("'sdfajslk", "data.db")

=======

init_db()
#print get_user("jenni")
add_user("jenni", "12345")
print get_user("jenni")
print auth("jenni", "12345")
print auth("jenni", "123452")
#add_user("'sdfajslk", "12345")
#print get_user("'sdfajslk")

'''
