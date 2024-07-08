import turtle as t
from constants import HEADING_VALUES, NUM_OF_STEPS, COMPUTER_PACE, WINDOW_PADDING


class Paddle(t.Turtle):
    def __init__(self, screen, screen_width, screen_height, is_computer):
        super().__init__()
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        if is_computer:
            self.is_computer = True
            self.setx(screen_width - WINDOW_PADDING)
        else:
            self.is_computer = False
            self.setx((screen_width - WINDOW_PADDING + 10) * -1)

        self.penup()
        self.speed("fastest")
        self.setheading(HEADING_VALUES["up"])
        self.color("white")
        self.shape("square")
        self.shapesize(1, 3)

    def face_down(self):
        if self.is_computer and self.is_at_edge():
            self.setheading(HEADING_VALUES['down'])
        elif not self.is_computer:
            if (not self.is_at_edge()) or (not self.is_computer and self.is_at_edge() and self.heading() == HEADING_VALUES['up']):
                self.setheading(HEADING_VALUES['down'])
                self.forward(NUM_OF_STEPS)



    def face_up(self):
        if self.is_computer and self.is_at_edge():
            self.setheading(HEADING_VALUES['up'])
        elif not self.is_computer:
            if (not self.is_at_edge()) or (not self.is_computer and self.is_at_edge() and self.heading() == HEADING_VALUES['down']):
                self.setheading(HEADING_VALUES['up'])
                self.forward(NUM_OF_STEPS)


    def is_at_edge(self):
        if self.screen_height - abs(self.ycor()) <= 30:
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
        self.forward(COMPUTER_PACE)


    def move_user_paddle(self):
        self.screen.listen()
        self.screen.onkeypress(self.face_down, 'Down')
        self.screen.onkeypress(self.face_up, 'Up')


