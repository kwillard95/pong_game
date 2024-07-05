import turtle as t
from constants import HEADING_VALUES, NUM_OF_STEPS

class Paddle(t.Turtle):
    def __init__(self, screen, screen_width, screen_height, is_computer):
        super().__init__()
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        if is_computer:
            self.is_computer = True
            self.setx(screen_width)
        else:
            self.is_computer = False
            self.setx((screen_width + 10) * -1)

        self.penup()
        self.speed("fastest")
        self.setheading(HEADING_VALUES["up"])
        self.color("white")
        self.shape("square")
        self.shapesize(1, 3)

    def move_computer_paddle(self):
        pass

    def move_down(self):
        self.setheading(HEADING_VALUES['down'])
        self.forward(NUM_OF_STEPS)

    def move_up(self):
        self.setheading(HEADING_VALUES['up'])
        self.forward(NUM_OF_STEPS)

    def move_user_paddle(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_down, 'Down')
        self.screen.onkeypress(self.move_up, 'Up')

    def move_paddle(self):
        if self.is_computer:
            self.move_computer_paddle()
        else:
            self.move_user_paddle()
