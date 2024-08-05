from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=280)
        self.update()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align='center', font=('Arial', 12, 'normal'))

    def update(self):
        self.clear()
        self.write(f"Score:{self.current_score}", align='center', font=('Arial', 12, 'normal'))
