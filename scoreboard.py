import turtle as t
from constants import FONT_STYLE


class Scoreboard(t.Turtle):
    def __init__(self, screen_height, screen_width, user):
        super().__init__()
        self.score = 0
        self.screen_height = screen_height
        self.screen_width = screen_width
        if user:
            x_pos = (self.screen_width / 2) * -1
            y_pos = self.screen_height - 50
            self.scoreboard_position = (x_pos, y_pos)
        else:
            x_pos = (self.screen_width / 2)
            y_pos = self.screen_height - 50
            self.scoreboard_position = (x_pos, y_pos)

        self.color("green")
        self.penup()
        self.hideturtle()

        self.write_score()

    def write_score(self):
        self.clear()
        self.setposition(self.scoreboard_position)
        self.write(self.score, False, 'center', FONT_STYLE)


