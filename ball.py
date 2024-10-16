from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.5)
        self.penup()
        self.goto(0, 0)
        self.penup()
        self.x_move = 3
        self.y_move = -3


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1


    def bat(self):
        self.x_move *= -1


    def refresh(self):
        self.reset()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.5)
        self.penup()
        self.x_move *= -1
