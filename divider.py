from turtle import Turtle
class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.color("black")
        self.setheading(-90)
        for step in range(0,16):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        


