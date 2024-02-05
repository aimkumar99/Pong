from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("Blue")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_ycor = self.ycor() + 40
        self.goto(self.xcor(), new_ycor)
    def go_down(self):
        new_ycor = self.ycor() - 40
        self.goto(self.xcor(), new_ycor)

