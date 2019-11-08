import turtle 

window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
#stops window from automatically updating, helps to speed up game
window.tracer(0) 

# score
scoreA = 0
scoreB = 0

# paddle A
paddleA = turtle.Turtle()
paddleA.speed(0) #speed of animation
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup() #avoid drawing lines
paddleA.goto(-350,0)

# paddle B

paddleB = turtle.Turtle()
paddleB.speed(0)  # speed of animation
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()  # avoid drawing lines
paddleB.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape("square")
ball.color("white")
ball.penup()  # avoid drawing lines
ball.goto(0, 0)

# Ball movement
ball.dx = 4
ball.dy = -4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

# functions
def paddleAUp():
    y = paddleA.ycor()
    if y < 250:
        y += 40
        paddleA.sety(y)


def paddleADown():
    y = paddleA.ycor()
    if y > -250:
        y -= 40
        paddleA.sety(y)


def paddleBUp():
    y = paddleB.ycor()
    if y < 250:
        y += 40
        paddleB.sety(y)


def paddleBDown():
    y = paddleB.ycor()
    if y > -250:
        y -= 40
        paddleB.sety(y)

# keyboard binding
window.listen()
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down")

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverse direction

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  PlayerB: {scoreB}", align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  PlayerB: {scoreB}", align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

# window.update()
# finalMessage = turtle.Turtle()
# finalMessage.speed(0)
# finalMessage.goto(0,0)
# if scoreA > scoreB:
#     finalMessage.write("Player A: Won!", align="center",
#         font=("Courier", 50, "normal"))
# else:
#     finalMessage.write("Player A: Won!", align="center",
#                 font=("Courier", 50, "normal"))
