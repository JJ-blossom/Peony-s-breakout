from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.title("Peony's Breakout")
screen.tracer(0)

ball = Ball()
paddle = Paddle()
brick = Brick()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_on = True
while game_on:
    screen.update()
    ball.move()
#     detect ball collision with side walls
    if ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_x()
#     detect ball collision with top wall
    if ball.ycor() > 200:
        ball.bounce_y()
#     detect ball collision with paddle
    if ball.distance(paddle) < 50 and -210 > ball.ycor() > -220:
        ball_x = ball.xcor()
        paddle_x = paddle.xcor()
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.reverse()
            else:
                ball.bounce_y()
        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.reverse()
            else:
                ball.bounce_y()
        else:
            if ball_x > paddle_x:
                ball.reverse()
            elif ball_x < paddle_x:
                ball.reverse()
            else:
                ball.bounce_y()
#     detect collision with bricks
    for b in brick.all_bricks:
        if ball.distance(b) < 25:
            scoreboard.increase_points()
            ball_x = ball.xcor()
            ball_y = ball.ycor()
            brick_x = b.xcor()
            brick_y = b.ycor()
            if ball_x < brick_x and ball_y < brick_y:
                b.clear()
                b.hideturtle()
                brick.all_bricks.remove(b)
                ball.reverse()
            elif ball_x > brick_x and ball_y < brick_y:
                b.clear()
                b.hideturtle()
                brick.all_bricks.remove(b)
                ball.bounce_x()
            elif ball_x < brick_x and ball_y > brick_y:
                b.clear()
                b.hideturtle()
                brick.all_bricks.remove(b)
                ball.bounce_y()
            elif ball_x > brick_x and ball_y > brick_y:
                b.clear()
                b.hideturtle()
                brick.all_bricks.remove(b)
                ball.reverse()
            else:
                b.clear()
                b.hideturtle()
                brick.all_bricks.remove(b)
                ball.bounce_x()
    if len(brick.all_bricks) == 0:
        scoreboard.increase_level()
        brick.increase_level()
        ball.increase_level()
        ball.reset_ball()
#     detect collision with bottom wall
    if ball.ycor() < -235 and scoreboard.lives_remaining > 0:
        time.sleep(0.2)
        scoreboard.decrease_lives()
        scoreboard.update_score()
        ball.reset_ball()
#     detect when ball past paddle and run end game
    if ball.ycor() < -235 and scoreboard.lives_remaining == 0:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
