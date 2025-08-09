from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("violet")
        self.speed("fastest")
        self.random_location()

    def random_location(self):
        self.goto(random.randint(-380,380),random.randint(-380,380))


