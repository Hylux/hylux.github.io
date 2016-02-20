var canvas = document.getElementById("bong"),
	ctx = canvas.getContext("2d"),
	l_p = {x:10,y:canvas.height/2,width:20,height:100},
	r_p = {x:canvas.width-l_p.x-l_p.width,y:l_p.y,width:l_p.width,height:l_p.height},
	ball = {x:canvas.width/2,y:canvas.height/2,radius:10},
	speed=16,step=1.5,leeway=3,y_bound=canvas.height-l_p.height,
	ball_speed=16,ball_step=1,ball_dir=-1,moving=true,
	map = [], 
	m=1,c=-100,
	refresh_rate=10,
	p1=0,p2=0,
	insane=false; 

function displayResult() {							//ADDITION
    document.getElementById("p1").innerHTML = p1;
	document.getElementById("p2").innerHTML = p2;
}
	
function updateView(){
	ball_speed=document.getElementById("ball_speed").value;
	if (ball_speed>32) ball_step=ball_speed/32;
	else if (insane) ball_step=3;
	else ball_step=1;
	speed=document.getElementById("p_speed").value;
	if (speed>32) step=speed/32*1.5;
	else if (insane) step=4.5;
	else step=1.5;
	//ctx.clearRect(0, 0, canvas.width,canvas.height);
	ctx.fillStyle= "skyblue";
	ctx.fillRect(0,0,canvas.width,canvas.height);

	ctx.beginPath();
	ctx.arc(ball.x,ball.y,ball.radius,0,2*Math.PI);
	ctx.fillStyle = "white";
	ctx.fill();

	ctx.font = "60px Times";
	ctx.textAlign = "center";
	ctx.fillStyle = "black";
	//ctx.fillText(p1+" - P O N G - "+p2,canvas.width/2,75); REMOVAL
	
	displayResult();	//ADDITION
	
	ctx.fillRect(l_p.x,l_p.y,l_p.width,l_p.height);
	ctx.fillRect(r_p.x,r_p.y,r_p.width,r_p.height);
	//setTimeout(updateView,1000/60);
	requestAnimationFrame(updateView);
}

//paddle 1 - left paddle, paddle 2 - right paddle
//up - 1, down - -1
function movePaddle(paddle,direction){
	if (direction==-1){
			if (paddle==1) l_p.y+=step;
			else if (paddle==2) r_p.y+=step;
	}
	else if (direction==1){
			if (paddle==1) l_p.y-=step;
			else if (paddle==2) r_p.y-=step;
	}
}

function moveoldBall(x,y){
	var m=(y-ball.y)/(x-ball.x);
	var c=ball.y-m*ball.x;
	for (var i=ball.x;i<=$("canvas").width()&&i>=0;(x>ball.x?i+=step:i-=step)){
		//console.log(ball);
		ball.x=i;
		ball.y=m*ball.x+c;
	}
}

function updateBall(){
	if (moving){
	change=ball_dir==1?ball_step:-ball_step;
	ball.x+=change;
	ball.y=m*ball.x+c;
	}
	var next_loc={x:ball.x+change,y:m*(ball.x+change)+c};
	//console.log(next_loc,l_p.y,l_p.y+l_p.height);
	if ((next_loc.x<l_p.x+l_p.width+ball.radius-leeway&&next_loc.x>l_p.x+l_p.width-leeway&&next_loc.y>l_p.y&&next_loc.y<l_p.y+l_p.height) || 
		(next_loc.x+change>r_p.x-ball.radius+leeway&&next_loc.x<r_p.x+leeway&&next_loc.y>r_p.y&&next_loc.y<r_p.y+r_p.height))
		{ball_dir*=-1; m*=-1; c=ball.y-m*ball.x;}
	else if (next_loc.y<ball.radius || next_loc.y>canvas.height-ball.radius) {m=-m; c=ball.y-m*ball.x;}
	else if (next_loc.x<-50||next_loc.x>canvas.width+50) {
		moving=false;
		if (next_loc.x<0) p1++;
		else if (next_loc.x>canvas.width) p2++;
		ball_dir*=-1;
		ball.x=canvas.width/2;
		ball.y=canvas.height/2;
		c=ball.y-m*ball.x;
		setTimeout(function(){
		moving=true;
		},1500);
	}
	setTimeout(updateBall,32/Math.min(ball_speed,32));
}

function updateP(){
	if(map[81] && l_p.y-step>=0) movePaddle(1,1);
	if (map[65] && l_p.y+step<=y_bound) movePaddle(1,-1);
	if (map[80] && r_p.y-step>=0) movePaddle(2,1);
	if (map[76] && r_p.y+step<=y_bound) movePaddle (2,-1)
	setTimeout(updateP,32/Math.min(speed,32));
}

function setD(x,y){
	d_x=x;
	d_y=y;
	m=(d_y-ball.y)/(d_x-ball.x);
	c=ball.y-m*ball.x;
}

$(document).ready(function(){
	requestAnimationFrame(updateView);
	updateBall();
	updateP();
	/*$(document).keydown(function(e) {
		if(e.which == 87 && l_p.y-speed*step>=0) movePaddle(1,1);
		else if (e.which==83 && l_p.y+speed*step<=y_bound) movePaddle(1,-1);
		else if (e.which==38 && r_p.y-speed*step>=0) movePaddle(2,1);
		else if (e.which==40 && r_p.y+speed*step<=y_bound) movePaddle (2,-1);
	});*/
	
	onkeydown = onkeyup = function(e){
    map[e.keyCode] = e.type == 'keydown';
	/*if(map[87] && l_p.y-speed*step>=0) movePaddle(1,1);
	if (map[83] && l_p.y+speed*step<=y_bound) movePaddle(1,-1);
	if (map[38] && r_p.y-speed*step>=0) movePaddle(2,1);
	if (map[40] && r_p.y+speed*step<=y_bound) movePaddle (2,-1);*/
	}
});