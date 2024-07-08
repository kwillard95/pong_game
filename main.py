import turtle as t
from constants import WINDOW_PADDING
from paddle import Paddle
from ball import Ball

screen = t.Screen()
screen.bgcolor("black")
screen_height = (screen.window_height() / 2)
screen_width = (screen.window_width() / 2)


def set_up_game():
    user = Paddle(screen, screen_width, screen_height, False)
    computer = Paddle(screen, screen_width, screen_height, True)
    ball = Ball(screen_width, screen_height)
    user.move_user_paddle()
    def play_game():
        computer.move_computer_paddle()
        ball.is_wall_collision()
        ball.detect_paddle_collision(user, computer)
        ball.move_ball()
        screen.ontimer(play_game, 5)

    play_game()










set_up_game()

screen.exitonclick()
screen.mainloop()