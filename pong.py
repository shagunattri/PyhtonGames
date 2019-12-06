import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong By id10t")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#winscore
scorea = 0
scoreb = 0


#Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()  #stop making lines as the move in the turtle module
paddle1.goto(-350,0)


#Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()  #stop making lines as the move in the turtle module
paddle2.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  #stop making lines as the move in the turtle module
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#pen
pen = turtle.Turtle()
pen.speed(1)
pen.color("white")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("Courier",24,"normal"))



#Function 
def paddle1up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)
    
def paddle1down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)
    
def paddle2down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

#keyboard Bindings
wn.listen()
wn.onkeypress(paddle1up,"w")
wn.onkeypress(paddle1down,"s")
wn.onkeypress(paddle2up,"Up")
wn.onkeypress(paddle2down,"Down")


#Main Game Loop
while True:
    wn.update()
    
    #move the ball
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border checking to bounce back the ball
    
    #top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
        #left and right
    if ball.xcor() > 350:
        ball.goto(0,0)
        ball.dx *= -1
        scorea += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scorea,scoreb),align="center",font=("Courier",24,"normal"))
        
    if ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *= -1
        scoreb += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scorea,scoreb),align="center",font=("Courier",24,"normal"))


    #paddle and ball colllision
    if ball.xcor() < -340 and ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50:
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    elif ball.xcor() > 340 and ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)