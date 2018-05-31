import db
import math
import random

db.init_db()


'''
codes:
0: Property (house, railroad, etc.)
1: Community Chest
2: Chance
3: Misc
'''

board = [
    [3, 'Go'],
    [0, 'Mediterranean Avenue'],
    [1, 'Community Chest'],
    [0, 'Baltic Avenue'],
    [3, 'Income Tax'],
    [0, 'Reading Railroad'],
    [0, 'Oriental Avenue'],
    [2, 'Chance'],
    [0, 'Vermont Avenue'],
    [0, 'Connecticut Avenue'],
    [3, 'Jail'],
    [0, 'St.Charles Place'],
    [0, 'Electric Company'],
    [0, 'States Avenue'],
    [0, 'Virginia Avenue'],
    [0, 'Pennsylvania Railroad'],
    [0, 'St.James Place'],
    [1, 'Community Chest'],
    [0, 'Tennessee Avenue'],
    [0, 'New York Avenue'],
    [3, 'Free Parking'],
    [0, 'Kentucky Avenue'],
    [2, 'Chance'],
    [0, 'Indiana Avenue'],
    [0, 'Illinois Avenue'],
    [0, 'B.& O. Railroad'],
    [0, 'Atlantic Avenue'],
    [0, 'Ventnor Avenue'],
    [0, 'Water Works'],
    [0, 'Marvin Gardens'],
    [3, 'Go to Jail'],
    [0, 'Pacific Avenue'],
    [0, 'North Carolina Avenue'],
    [1, 'Community Chest'],
    [0, 'Pennsylvania Avenue'],
    [0, 'Short Line'],
    [2, 'Chance'],
    [0, 'Park Place'],
    [3, 'Luxury Tax'],
    [0, 'Boardwalk']
]

#for b in board:
#    if b[0] == 0:
#        print db.get_board_info(b[1])
           
def roll_dice():
    return math.floor(random() * 7)

def go():
    pass
