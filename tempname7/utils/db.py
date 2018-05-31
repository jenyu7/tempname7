import sqlite3
from hashlib import sha1
from random import random
import math

# path = ''
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

def get_board_info(name, f=path+'data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    comm = 'SELECT * FROM board WHERE name="%s";' %(name)
    c.execute(comm)
    #returns a list
    fet = c.fetchall()

    if len(fet) == 0:
        return False
    return fet[0]

def get_colors(color, f=path+'data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    comm = 'SELECT * FROM board WHERE color="%s";' %(color)
    c.execute(comm)
    #returns a list
    fet = c.fetchall()

    if len(fet) == 0:
        return False
    return fet


#==========================CARDS FUNCTIONS==========================
def init_cards(c, populate=True):
    c.execute("CREATE TABLE chance_cards(id INTEGER PRIMARY KEY, description TEXT)")
    c.execute("CREATE TABLE comm_cards(id INTEGER PRIMARY KEY, description TEXT)")

    if populate:
        #populating chance cards
        chance = [
            'Advance to Go (Collect $200)',
            'Advance to Illinois Ave. - If you pass Go, collect $200',
            'Advance to St. Charles Place - If you pass Go, collect $200',
            'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.',
            'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.',
            'Bank pays you dividend of $50',
            'Get out of Jail Free - This card may be kept until needed, or traded/sold',
            'Go Back 3 Spaces',
            'Go to Jail - Go directly to Jail - Do not pass Go, do not collect $200',
            'Make general repairs on all your property - For each house pay $25 - For each hotel $100',
            'Pay poor tax of $15 ',
            'Take a trip to Reading Railroad - If you pass Go, collect $200',
            'Take a walk on the Boardwalk - Advance token to Boardwalk.',
            'You have been elected Chairman of the Board - Pay each player $50',
            'Your building and loan matures - Collect $150',
            'You have won a crossword competition - Collect $100'
            ]

        i = 0
        while i < len(chance):
            comm = 'INSERT INTO chance_cards VALUES(%d, "%s")' %(i, chance[i])
            c.execute(comm)
            i+=1


        #populating community cards
        commun = [
            'Advance to Go (Collect $200)',
            'Bank error in your favor - Collect $200',
            "Doctor's fees - Pay $50",
            'From sale of stock you get $50',
            'Get Out of Jail Free - This card may be kept until needed or sold',
            'Go to Jail - Go directly to jail - Do not pass Go - Do not collect $200',
            'Grand Opera Night - Collect $50 from every player for opening night seats',
            'Holiday Fund matures - Receive $100',
            'Income tax refund - Collect $20',
            'It is your birthday - Collect $10 from each player',
            'Life insurance matures - Collect $100',
            'Pay hospital fees of $100',
            'Pay school fees of $150',
            'Receive $25 consultancy fee',
            'You are assessed for street repairs - $40 per house - $115 per hotel',
            'You have won second prize in a beauty contest - Collect $10',
            'You inherit $100'
            ]

        i = 0
        while i < len(commun):
            comm = 'INSERT INTO comm_cards VALUES(%d, "%s")' %(i, commun[i])
            c.execute(comm)
            i+=1

def get_chance(f=path+'data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT id FROM chance_cards WHERE id = (SELECT MAX(id) FROM chance_cards)")
    max_id = c.fetchall()[0][0]
    idd = math.floor(random() * (max_id+1))

    comm = 'SELECT * FROM chance_cards WHERE id=%d;' %(idd)
    c.execute(comm)
    #returns a list
    fet = c.fetchall()

    if len(fet) == 0:
        return False
    return fet[0]

def get_comm(f=path+'data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT id FROM chance_cards WHERE id = (SELECT MAX(id) FROM chance_cards)")
    max_id = c.fetchall()[0][0]
    idd = math.floor(random() * (max_id+1))

    comm = 'SELECT * FROM comm_cards WHERE id=%d;' %(idd)
    c.execute(comm)
    #returns a list
    fet = c.fetchall()

    if len(fet) == 0:
        return False
    return fet[0]

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
#init_cards(c)

#init_db()
'''
print get_board_info('Baltic Avenue')
print get_board_info('Baltic Avenues')

print get_colors('brown')
print get_colors('red')
print get_colors('rainbow')
'''

'''
print get_chance(2)
print get_chance(5)
print get_chance(7)
print get_chance(19)

print '========'
print get_comm(0)
print get_comm(2)
print get_comm(5)
print get_comm(7)
print get_comm(19)
'''
