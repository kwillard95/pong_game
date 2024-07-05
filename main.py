import turtle as t
from constants import WINDOW_PADDING
from paddle import Paddle

screen = t.Screen()
screen.bgcolor("black")
screen_height = (screen.window_height() / 2) - WINDOW_PADDING
screen_width = (screen.window_width() / 2) - WINDOW_PADDING


def set_up_game():
    user = Paddle(screen, screen_width, screen_height, False)
    computer = Paddle(screen, screen_width, screen_height, True)

    user.move_paddle()
    computer.move_paddle()


set_up_game()

screen.exitonclick()
screen.mainloop()