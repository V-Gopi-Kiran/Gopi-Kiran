# FOOD class for the SNAKE GAME

from turtle import Turtle
import random


class Food(Turtle):  #CLASS INHERITENCE : the food class will behave similarly as the Turtle class but with an extra feature of going to a random location
    def __init__(self):
        super(). __init__()  # initializing from the superclass Turtle
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len = 0.75, stretch_wid = 0.75) # this method allows to change the length and width of shape, so from 20*20 i reduced to 10*10 pixels
        self.color("cyan")
        self.speed(0)
        self.refresh_food()

    def refresh_food (self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-355, 335)
        self.goto(random_x, random_y)
