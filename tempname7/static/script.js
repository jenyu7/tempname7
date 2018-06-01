//import math

var player = {
    location: 0,
    properties: [],
    money: 1500,
    in_jail: false,
    get_out_jail: 0
};

var go = function(turn, player){
    //rolls die
    var d0 = Math.floor(Math.random() * 6) + 1
    var d1 = Math.floor(Math.random() * 6) + 1
    console.log(d0);
    console.log(d1);

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
	    if (loca > 40){
		loca = loca % 40;
		player.money += 200;
	    }
	    player.location = loca;
	    
	    //see player location and link that with whatevers gonna happen

	    

    

	    //if double roll, roll again
	    if (d0 == d1){
		go(turn+1, player);
	    }
	}
    }
};

