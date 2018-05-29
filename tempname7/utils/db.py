import sqlite3
from hashlib import sha1
from random import random

path = 'utils/db/'
# ******************* UNCOMMENT THIS FOR LAUNCH *******************************
# path = '/var/www/tempname7/tempname7/utils/db/'


def init_db(f=path+'data.db'):
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

def add_user(username, password, f=path+'data.db'):
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

def get_user(username, f=path+'data.db'):
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

def auth(username, password, f=path+'data.db'):
    return sha1(password).hexdigest() == get_user(username)[1]

#==========================BOARD FUNCTIONS==========================
#id is the place of the space, where 0 is go
#type is the type of place it is:
#  chance, community, tax, railroad, jail, go to jail, free parking, house, electric company, water works
def init_board(c, populate=True):
    c.execute("CREATE TABLE board(id INTEGER PRIMARY KEY, name TEXT, color TEXT, price INTEGER)")


    if populate:
        board =  []
        names =  ['Mediterranean Avenue', 'Baltic Avenue',
                  'Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue',
                  'St. Charles Place', 'States Avenue', 'Virginia Avenue',
                  'St. James Place', 'Tennessee Avenue', 'New York Avenue',
                  'Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue',
                  'Atlantic Avenue', 'Ventnor Avenue', 'Marvin Gardens',
                  'Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue',
                  'Park Place', 'Boardwalk'
                      ]
        colors = ['brown',
                  'white',
                  'pink',
                  'orange',
                  'red',
                  'yellow',
                  'green',
                  'blue'
                      ]
        prices = [60, 60,
                  100, 100, 120,
                  140, 140, 160,
                  180, 180, 200,
                  220, 220, 240,
                  260, 260, 280,
                  300, 300, 320,
                  350, 400
                      ]

        i = 0
        while i < 2:
            curr = [i, names[i], colors[0], prices[i]]
            board.append(curr)
            i+=1

        while i < len(names):
            #since first color only has 2
            curr = [i, names[i], colors[(i+1)/3], prices[i]]
            board.append(curr)
            i+=1

        miscnames  = [
            'Reading Railroad',
            'Electric Company',
            'Pennsylvania Railroad',
            'B. & O. Railroad',
            'Water Works',
            'Short Line'
            ]
        miscprices = [
            200,
            150,
            200,
            200,
            150,
            200
            ]

        i = 0
        while i < len(miscnames):
            curr = [i+len(names), miscnames[i], 'misc', miscprices[i]]
            board.append(curr)
            i+=1

            
        for b in board:
            comm = 'INSERT INTO board VALUES(%d, "%s", "%s", %d)' %(b[0], b[1], b[2], b[3])
            c.execute(comm)
            #print b

            

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

    
#db = sqlite3.connect('data.db')
#c = db.cursor()

#init_board(c)
