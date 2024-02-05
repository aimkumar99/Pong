from turtle import Turtle, Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Player1_Score:{self.l_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(150, 250)
        self.write(f"Player2_Score: {self.r_score}", align="center", font=("Courier", 20, "normal"))
    def increase_score_left(self):
        self.l_score += 1
        self.update_scoreboard()
    def increase_score_right(self):
        self.r_score += 1
        self.update_scoreboard()
    def game_over(self):
        Screen().clear()
        Screen().bgcolor("grey")
        self.update_scoreboard()
        self.goto(0,0)
        if self.l_score > self.r_score:
            self.write("GAME OVER.", align="center", font=("Courier", 30, "normal"))
            self.goto(0,-35)
            self.write("Player1 won the game.", align="center", font=("Courier", 30, "normal"))
        else:
            self.write("GAME OVER.", align="center", font=("Courier", 30, "normal"))
            self.goto(0,-35)
            self.write("Player2 won the game.", align="center", font=("Courier", 30, "normal"))


       