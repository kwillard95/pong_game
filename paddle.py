import turtle as t
from constants import HEADING_VALUES, NUM_OF_STEPS, COMPUTER_PACE


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

    def move(self):
        if self.is_computer:
            self.forward(COMPUTER_PACE)
        else:
            self.forward(NUM_OF_STEPS)

    def face_down(self):
        self.setheading(HEADING_VALUES['down'])
        if not self.is_computer:
            self.forward(NUM_OF_STEPS)

    def face_up(self):
        self.setheading(HEADING_VALUES['up'])
        if not self.is_computer:
            self.forward(NUM_OF_STEPS)

    def is_at_edge(self):
        if (self.distance(self.screen_width, self.screen_height) < 10 or
                self.distance(self.screen_width, self.screen_height * -1) < 10):
            return True
        else:
            return False

    def redirect_paddle(self):
        if self.heading() == HEADING_VALUES['up']:
            self.face_down()
        elif self.heading() == HEADING_VALUES['down']:
            self.face_up()

    def move_computer_paddle(self):
        if self.is_at_edge():
            self.redirect_paddle()
        self.move()


    def move_user_paddle(self):
        self.screen.listen()
        self.screen.onkeypress(self.face_down, 'Down')
        self.screen.onkeypress(self.face_up, 'Up')


