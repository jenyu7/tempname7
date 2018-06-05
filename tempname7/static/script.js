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
    player.properties = [];
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

	    //property should be checked last, with updated location
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
	    if(loca_type == 1){
		//go to db, get id of card drawn
		var id = 0;

		//advance to go
		//collect 200
		//pay 50
		//get 50
		//get out of jail free
		//go to jail
		//collect 50 from every player
		//collect 100
		//collect 20
		//collect 10 from every player
		//collect 100
		//pay 100
		//pay 150
		//receive 50
		//pay 40 per property
		//collect 10
		//collect 100
	    }
	    //2: chance
	    if (loca_type == 2){
		//go to db, get id of card drawn
		var id = 0;


		//advance to go
		if(id == 0){
		    player.location = 0;
		    player.money += 200;
		}
		//advance to illinois ave
		if(id == 1){
		    if(player.location >= 24){
			player.money += 200;
		    }
		    player.location = 24;
		}
		//advance to st. charles place
		if(id == 2){
		    if(player.location >= 11){
			player.money += 200;
		    }
		    player.location = 11;
		}
		//=====================================================
		//advance to nearest util
		//if owned, throw dice and pay owner 10x amount
		//if not, you can buy
		if(id == 3){
		    
		}
		//advance to nearest rail
		//pay 2x amount
		if(id == 4){
		    
		}
		//=====================================================
		//bank pays you 50
		if(id == 5){
		    player.money += 50;
		}
		//get out of jail free
		if(id == 6){
		    player.get_out_jail++;
		}
		//=====================================================
		//need to check this space and redo the same process
		//go back 3 spaces
		if(id == 7){
		    player.location -= 3;
		    if (player.location < 0){
			player.location += 40;
		    }
		}
		//go to jail
		if(id == 8){
		    player.in_jail = true;
		    //10 is where Jail is
		    player.location = 10;
		}
		//each property: 25
		if(id == 9){
		    player.money -= 25 * player.properties.length 
		}
		//pay 15
		if(id == 10){
		    player.money -= 15;
		}
		//go to reading rail
		if(id == 11){
		    if(player.location >= 5){
			player.money += 200;
		    }
		    player.location = 5;
		}
		//go to boardwalk
		if(id == 12){
		    if(player.location >= 39){
			player.money += 200;
		    }
		    player.location = 39;
		}
		//=====================================================
		//pay each player 50
		if(id == 13){
		    
		}
		//=====================================================
		//collect 150
		if(id == 14){
		    player.money += 150;
		}
		//collect 100
		if(id == 15){
		    player.money += 100;
		}
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
