import turtle as t
from constants import HEADING_VALUES


class Ball(t.Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.top_wall = screen_height
        self.bottom_wall = screen_height * -1
        self.color("green")
        self.shape("circle")
        self.shapesize(.5, .5)
        self.setpos(0,0)

    def redirect_ball(self):
        if self.heading() == HEADING_VALUES["left"]:
            self.setheading(HEADING_VALUES["right"])
        elif self.heading() == HEADING_VALUES["right"]:
            self.setheading(HEADING_VALUES["left"])

    def move_ball(self):
        pass

    def detect_wall_collision(self):
        pass

    def detect_paddle_collision(self, user, computer):
        pass

