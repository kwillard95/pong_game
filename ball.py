import turtle as t
import random as r
from constants import HEADING_VALUES, COLLISION_BUFFER


class Ball(t.Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.vertical_direction = "down"
        self.horizontal_direction = "left"
        self.color("green")
        self.penup()
        self.shape("circle")

    def serve_ball(self, l_paddle_serve):
        y_cor_choices = [self.screen_height + 50, (self.screen_height + 50) * -1]
        y_cor = y_cor_choices[r.randint(0, 1)]
        if l_paddle_serve:
            x_cor = r.uniform(0, self.screen_width * -1)
            self.horizontal_direction = "right"
        else:
            x_cor = r.uniform(0, self.screen_width)
            self.horizontal_direction = "left"
        if y_cor > 0:
            self.vertical_direction = "down"
        else:
            self.vertical_direction = "up"

        self.setpos(x_cor, y_cor)

    def redirect_ball_direction(self):
        if self.heading() == HEADING_VALUES["left"]:
            self.setheading(HEADING_VALUES["right"])
        elif self.heading() == HEADING_VALUES["right"]:
            self.setheading(HEADING_VALUES["left"])

    def move_ball(self):
        # Increase coordinates gradually
        x_position = self.xcor()
        y_position = self.ycor()
        if self.vertical_direction == "up":
            y_position += 10
        elif self.vertical_direction == "down":
            y_position -= 10

        if self.horizontal_direction == "left":
            x_position -= 10
        elif self.horizontal_direction == "right":
            x_position += 10

        self.goto(x_position, y_position)

    def is_ball_missing(self):
        if self.screen_width - abs(self.xcor()) <= COLLISION_BUFFER:
            return True
        return False

    def is_l_paddle_win(self):
        return self.xcor() > 0

    def detect_wall_collision(self):
        # If the ball hits upper wall, redirect ball down in the same direction
        # If ball hits lower wall, redirect ball up in the same direction
        if self.screen_height - abs(self.ycor()) <= COLLISION_BUFFER:
            if self.ycor() >= 0:
                self.vertical_direction = "down"
                return True
            else:
                self.vertical_direction = "up"
                return False

    def detect_paddle_collision(self, l_paddle, r_paddle):
        # If the ball hits the paddle above (0,0), move ball up
        # If the ball hits the paddle below (0,0), move ball down
        if (abs(self.xcor() - l_paddle.xcor()) < COLLISION_BUFFER and abs(self.ycor() - l_paddle.ycor())
                < COLLISION_BUFFER + 40):
            self.horizontal_direction = "right"
            return True
        if (abs(self.xcor() - r_paddle.xcor()) < COLLISION_BUFFER  and
                abs(self.ycor() - r_paddle.ycor()) < COLLISION_BUFFER + 40):
            self.horizontal_direction = "left"
            return True
        else:
            return False
