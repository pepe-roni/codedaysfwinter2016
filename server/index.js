var express = require('express')
var bodyParser = require('body-parser')
var app = express()
var player1 = {"health": 100, "phone": ""}
var player2 = {"health": 100, "phone": ""}

app.use(bodyParser.json())

app.post('/post', function(req, res){
	console.log(req.body())
	if(req.body().part == 'limb'){
		if(req.body().player == 1){
			player1.health = player1.health - 30
		} else if(req.body().player == 2){
			player2.health = player2.health - 30
		}
	} else if(req.body().part == 'body'){
		if(req.body().player == 1){
			player1.health = player1.health - 80
		} else if(req.body().player == 2){
			player2.health = player2.health - 80
		}
	} else if(req.body().part == 'head'){
		if(req.body().player == 1){
			player1.health = player1.health - 100
		} else if(req.body().player == 2){
			player2.health = player2.health - 100
		}
	}
	if(player1.health <= 0){
		res.json("PLAYER 2 WON")
	} else if(player2.health <= 0){
		res.json("PLAYER 1 WON")
	} else {
		// nothing happens
		res.json("keep going")
	}
})

app.listen(3000, function(){
	console.log("running on port 3000")
})