/*
codes:
0: Property (house, railroad, etc.)
1: Community Chest
2: Chance
3: Misc
*/

//if property is owned by someone, its' third slot will be the id of the player
var board = [
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



//players
var init_player = function(player){
    player.location = 0;
    player.properties = 0;
    player.money = 1500;
    player.in_jail = false;
    player.get_out_jail = 0;
    player.alive = true;
};

var p0 = {name: 'jenni'};
var p1 = {name: 'jen'};
var p2 = {name: 'kelly'};
var p3 = {name: 'charles'};

var players = [p0, p1, p2, p3]

var i = 0;
while (i < players.length){
    init_player(players[i]);
    i++;
}

var player = p0;

//call this on every players' turn
//turn should be 0 when the players' turn starts -- it's only not 0 when they double roll
var go = function(player, turn = 0){
    //rolls die
    var d0 = Math.floor(Math.random() * 6) + 1
    var d1 = Math.floor(Math.random() * 6) + 1
   
    if (player.in_jail){
	if(d0 != d1){
	    console.log('you aint getting out');
	    return 'jail';
	}
	else{
	    player.in_jail = false;
	}
    }
    else{
	//if this is your third turn(double roll), you get placed in jail
	if (turn >= 2 && d0 == d1){
	    player.in_jail = true;
	    //10 is where Jail is
	    player.location = 10
	}
	else{
	    //move
	    loca = player.location + d0 + d1
	    //40 is number of spaces in entire board, if loca is greater than 40 then it passed go
	    if (loca >= 40){
		loca = loca % 40;
		player.money += 200;
	    }
	    player.location = loca;
	    
	    //see player location and link that with whatevers gonna happen
	    loca_type = board[loca][0];
	    loca_name = board[loca][1];
	    
	    //0: property
	    if (loca_type == 0){
		//if unowned
		if(board[loca].length == 3){
		    //give option to buy
		    //if they buy it, then call: board[loca].append(<id>)
		}
		//if owned
		else{
		    //go to db to check price, and pay whoever owns it
		}
	    }
	    //1: community chest
	    if (loca_type == 1){
		//go to db, get id of carcd drawn
	    }
	    //2: chance
	    if (loca_type == 2){
		//go to db, get id of card drawn
	    }
	    //3: misc
	    if (loca_type == 3){
		if(name == "Income Tax"){
		    player.money -= 200;
		}
		if(name == "Luxury Tax"){
		    player.money -= 100;
		}
		if(name == "Go to Jail"){
		    player.in_jail = true;
		    //10 is where Jail is
		    player.location = 10
		}
		
	    }
	    


	    //if run out of money, lose
	    if(player.money <= 0){
		player.alive = false;
	    }

	    //if double roll, roll again
	    if (d0 == d1){
		go(player, turn+1);
	    }
	}
    }
};

var go_all = function(){
    var i = 0;
    while (i < players.length){
	if (players[i].alive){
	    console.log(players[i]);
	    go(players[i]);
	    i+=1;
	}
    }
};
