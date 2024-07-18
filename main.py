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
    user_scoreboard = Scoreboard(screen_height, screen_width, True)
    computer_scoreboard = Scoreboard(screen_height, screen_width, False)
    user = Paddle(screen, screen_width, screen_height, False)
    computer = Paddle(screen, screen_width, screen_height, True)
    ball = Ball(screen_width, screen_height)
    user.move_user_paddle()

    def play_game():
        time.sleep(.05)
        computer.move_computer_paddle()
        if ball.is_ball_missing():
            users_win = ball.is_users_win()
            if users_win:
                user_scoreboard.score += 1
                user_scoreboard.write_score()
                ball.serve_ball(users_serve=True)
            else:
                computer_scoreboard.score += 1
                computer_scoreboard.write_score()
                ball.serve_ball(users_serve=False)
        else:
            ball.detect_wall_collision()
            if ball.detect_paddle_collision(user, computer):
                ball.redirect_ball_direction()
        ball.move_ball()
        screen.update()
        screen.ontimer(play_game, 5)

    play_game()


set_up_game()

screen.exitonclick()
screen.mainloop()