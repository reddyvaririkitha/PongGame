import turtle as t
from Ball import Ball
from Paddle import Paddle
from display_and_score import Scoreboard, Border
import time


#TODO-1: Screen seting
screen = t.Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game 📲🥎📲")
screen.tracer(0)

# TODO-2: Boundary line between 2 players
border = Border()

#TODO-3: Paddle initialisation
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#TODO-5: Ball Call
ball = Ball()
score_board = Scoreboard()


is_game_on = True

#TODO-4: Paddle controls
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

while is_game_on:
    time.sleep(ball.move_speed) #0.02
    screen.update()
    ball.move()

    #TODO-6: Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    #TODO-7: Detect paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() >=340) or (ball.distance(l_paddle) < 50 and ball.xcor() <=-340):
        ball.paddle_bounce()
    #TODO-8: Detect r_paddle miss
    if ball.xcor() >=360:
        ball.reset_position()
        score_board.l_score_increment()

    # TODO-8: Detect l_paddle miss
    if ball.xcor() <= -360:
        ball.reset_position()
        score_board.r_score_increment()

screen.exitonclick()