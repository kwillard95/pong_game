import turtle as t
from constants import HEADING_VALUES, NUM_OF_STEPS, WINDOW_PADDING


class Paddle(t.Turtle):
    def __init__(self, screen, screen_width, screen_height, is_l_paddle):
        super().__init__()
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        if is_l_paddle:
            self.is_l_paddle = True
            self.setx(screen_width - WINDOW_PADDING)
        else:
            self.is_l_paddle = False
            self.setx((screen_width - WINDOW_PADDING + 10) * -1)

        self.penup()
        self.speed("fastest")
        self.setheading(HEADING_VALUES["up"])
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)

    def redirect_paddle(self, direction):
        def redirect_paddle():
            nonlocal direction
            opposite_direction = ''
            if direction == 'up':
                opposite_direction = 'down'
            elif direction == 'down':
                opposite_direction = 'up'

            if (not self.is_at_edge()) or (self.is_at_edge() and self.heading() == HEADING_VALUES[opposite_direction]):
                self.setheading(HEADING_VALUES[direction])
                self.forward(NUM_OF_STEPS)
        return redirect_paddle

    def is_at_edge(self):
        if self.screen_height - abs(self.ycor()) <= 50:
            return True
        else:
            return False

    def move_paddle(self):
        self.screen.listen()
        if self.is_l_paddle:
            self.screen.onkeypress(self.redirect_paddle("down"), 'Down')
            self.screen.onkeypress(self.redirect_paddle("up"), 'Up')
        else:
            self.screen.onkeypress(self.redirect_paddle("down"), 's')
            self.screen.onkeypress(self.redirect_paddle("up"), 'w')




