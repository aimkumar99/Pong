from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from divider import Divider
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
left_paddle = Paddle((-385, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
divider = Divider()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "f")
screen.onkey(left_paddle.go_down, "v")
game_on = True
sleep_time = 0.05
while game_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    # detect colision with the upper and lower screen
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.ybounce()
    # detect colision with the paddle
    if ball.xcor() > 350 and ball.distance(right_paddle) < 50 or ball.xcor()<-350 and ball.distance(left_paddle)<50:
        ball.xbounce()
        sleep_time *= 0.95
    # detect game reset and add score
    if ball.xcor()> 400:
        ball.reset_position()
        scoreboard.increase_score_left()
        sleep_time = 0.05   
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.increase_score_right()
        sleep_time = 0.05
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        scoreboard.game_over()
        game_on = False
screen.exitonclick()