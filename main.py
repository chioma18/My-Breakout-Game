from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from bricks import Brick

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0, 0)

paddle = Paddle((0, -200))
ball = Ball()
scoreboard = ScoreBoard()

brick_x = -570
brick_y = 150
bricks = []
for _ in range(10):
    for i in range(30):
        brick = Brick((brick_x, brick_y))
        bricks.append(brick)
        brick_x += 45
    brick_x = -570
    brick_y -= 10

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkeypress(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkeypress(paddle.go_right, "Right")

game_on = True
while game_on:
    sleep(ball.speed)
    screen.update()
    ball.move()

    #Detect collision w top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision w paddle
    if ball.distance(paddle) < 45 or ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()

    #Detect collision w side walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    #Detect collision w bricks
    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            x_diff = ball.distance(brick)
            y_diff = ball.distance(brick)
            if x_diff > y_diff:
                #If the ball touches the side of the brick
                ball.bounce_x()
            else:
                #If the ball touches the top or bottom of the brick
                ball.bounce_x()
                ball.bounce_y()
            bricks.remove(brick)
            scoreboard.point()

    #Detect if paddle miss
    if ball.ycor() < -280:
        game_on = False

    if not bricks:
        game_on = False

screen.exitonclick()