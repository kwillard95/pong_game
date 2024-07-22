import turtle as t
from constants import HEADING_VALUES
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = t.Screen()
screen.bgcolor("black")
screen_height = (screen.window_height() / 2)
screen_width = (screen.window_width() / 2)
screen.tracer(0)


def set_up_screen():
    pen = t.Turtle()
    pen.color('green')
    pen.hideturtle()
    pen.pensize(3)
    pen.penup()
    pen.setposition(0, screen_height)
    pen.setheading(HEADING_VALUES["down"])
    while pen.ycor() > screen_height * -1:
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(20)


def set_up_game():
    set_up_screen()
    l_paddle_scoreboard = Scoreboard(screen_height, screen_width, True)
    r_paddle_scoreboard = Scoreboard(screen_height, screen_width, False)
    l_paddle = Paddle(screen, screen_width, screen_height, False)
    r_paddle = Paddle(screen, screen_width, screen_height, True)
    ball = Ball(screen_width, screen_height)
    l_paddle.move_paddle()
    r_paddle.move_paddle()

    def play_game():
        time.sleep(.05)
        if ball.is_ball_missing():
            l_paddle_win = ball.is_l_paddle_win()
            if l_paddle_win:
                l_paddle_scoreboard.score += 1
                l_paddle_scoreboard.write_score()
                ball.serve_ball(l_paddle_serve=False)
            else:
                r_paddle_scoreboard.score += 1
                r_paddle_scoreboard.write_score()
                ball.serve_ball(l_paddle_serve=True)
        else:
            ball.detect_wall_collision()
            if ball.detect_paddle_collision(l_paddle, r_paddle):
                ball.redirect_ball_direction()
        ball.move_ball()
        screen.update()
        screen.ontimer(play_game, 5)

    play_game()


set_up_game()

screen.exitonclick()
screen.mainloop()