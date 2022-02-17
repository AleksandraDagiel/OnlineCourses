from turtle import Turtle

FONT = ("Courier", 18, "bold")
ALIGN = 'center'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score_points = 0
        self.score()

    def score(self):
        self.write(arg=f"Score: {self.score_points}", font=FONT, align=ALIGN)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGN)

    def point_up(self):
        self.clear()
        self.score_points += 1
        self.score()


