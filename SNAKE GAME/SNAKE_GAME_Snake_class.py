# Writing program to create the snake class to import in snake game

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake (self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle('circle')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            for segment_number in range(len(self.segments)-1, 0, -1):   # loop to make remaining part take place of front part and follow head
                new_x = self.segments[segment_number - 1].xcor()
                new_y = self.segments[segment_number - 1].ycor() 
                self.segments[segment_number].goto(new_x, new_y)
            self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  #if snake is going down it can't go up
                self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:   # if snake is going up it can't go down
                self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:   #set heading and heading are two different things
                self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)
