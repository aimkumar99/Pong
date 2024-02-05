from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.sleep_time = 0.05
    def move(self):
        new_xcor = self.xcor()+self.xmove
        new_ycor = self.ycor()+self.ymove
        self.goto(new_xcor, new_ycor)
    def ybounce(self):
        self.ymove *= -1
        self.sleep_time *= 0.95
    def xbounce(self):
        self.xmove *= -1
    def reset_position(self):
        self.goto(0,0)
        self.xbounce()
        self.sleep_time = 0.05
