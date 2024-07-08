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

    def create_redirect_paddle(self, direction):
        def redirect_paddle():
            nonlocal direction
            if self.is_computer and self.is_at_edge():
                self.setheading(HEADING_VALUES[direction])
            elif not self.is_computer:
                opposite_direction = ''
                if direction == 'up':
                    opposite_direction = 'down'
                elif direction == 'down':
                    opposite_direction = 'up'

                if (not self.is_at_edge()) or (
                        not self.is_computer and self.is_at_edge() and self.heading() == HEADING_VALUES[opposite_direction]):
                    self.setheading(HEADING_VALUES[direction])
                    self.forward(NUM_OF_STEPS)
        return redirect_paddle

    def is_at_edge(self):
        if self.screen_height - abs(self.ycor()) <= 30:
            return True
        else:
            return False

    def redirect_paddle(self):
        if self.heading() == HEADING_VALUES['up']:
            self.create_redirect_paddle("down")()
        elif self.heading() == HEADING_VALUES['down']:
            self.create_redirect_paddle("up")()

    def move_computer_paddle(self):
        if self.is_at_edge():
            self.redirect_paddle()
        self.forward(COMPUTER_PACE)

    def move_user_paddle(self):
        self.screen.listen()
        self.screen.onkeypress(self.create_redirect_paddle("down"), 'Down')
        self.screen.onkeypress(self.create_redirect_paddle("up"), 'Up')


