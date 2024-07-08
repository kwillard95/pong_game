import turtle as t
from constants import HEADING_VALUES, COLLISION_BUFFER


class Ball(t.Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.vertical_direction = "down"
        self.horizontal_direction = "left"
        self.color("green")
        self.shape("circle")
        self.shapesize(.5, .5)
        self.setpos(0, 0)

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

    def is_wall_collision(self):
        # If the ball hits upper wall, redirect ball down in the same direction
        # If ball hits lower wall, redirect ball up in the same direction
        if self.screen_height - abs(self.ycor()) <= COLLISION_BUFFER:
            if self.ycor() >= 0:
                self.vertical_direction = "down"
                return True
            else:
                self.vertical_direction = "up"
                return False




    def detect_paddle_collision(self, user, computer):
        # If the ball hits the paddle above (0,0), move ball up
        # If the ball hits the paddle below (0,0), move ball down
        if self.distance(user) <= COLLISION_BUFFER:
            self.horizontal_direction = "right"
            return True
        if self.distance(computer) <= COLLISION_BUFFER:
            self.horizontal_direction = "left"
            return True
        else:
            return False





