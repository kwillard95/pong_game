import turtle as t
from constants import WINDOW_PADDING
from paddle import Paddle
from ball import Ball
import time

screen = t.Screen()
screen.bgcolor("black")
screen_height = (screen.window_height() / 2)
screen_width = (screen.window_width() / 2)

screen.tracer(0)

def set_up_game():
    user = Paddle(screen, screen_width, screen_height, False)
    computer = Paddle(screen, screen_width, screen_height, True)
    ball = Ball(screen_width, screen_height)
    user.move_user_paddle()

    def play_game():
        time.sleep(.05)
        computer.move_computer_paddle()
        if ball.is_ball_missing():
            ball.serve_ball(True)
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