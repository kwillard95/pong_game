import turtle as t
from constants import WINDOW_PADDING
from paddle import Paddle
from ball import Ball

screen = t.Screen()
screen.bgcolor("black")
screen_height = (screen.window_height() / 2) - WINDOW_PADDING
screen_width = (screen.window_width() / 2) - WINDOW_PADDING


def set_up_game():
    user = Paddle(screen, screen_width, screen_height, False)
    computer = Paddle(screen, screen_width, screen_height, True)
    ball = Ball(screen_width, screen_height)
    user.move_user_paddle()
    while True:
        computer.move_computer_paddle()
        ball.is_wall_collision()
        ball.detect_paddle_collision(user, computer)
        ball.move_ball()










set_up_game()

screen.exitonclick()
screen.mainloop()