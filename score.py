from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())


        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 380)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
