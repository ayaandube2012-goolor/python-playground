import turtle
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.next_direction = UP
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_seg(position)

    def game_over(self):
        for seg in self.segments:
            seg.hideturtle()

        self.segments.clear()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.next_direction = UP

    def add_seg(self, position):
        seg = Turtle(shape="square")
        seg.penup()
        seg.goto(position)
        seg.color("white")
        self.segments.append(seg)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        # Apply next direction only if it's valid
        if self.next_direction == UP and self.head.heading() != DOWN:
            self.head.setheading(UP)
        elif self.next_direction == DOWN and self.head.heading() != UP:
            self.head.setheading(DOWN)
        elif self.next_direction == LEFT and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        elif self.next_direction == RIGHT and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        for seg_num in range(len(self.segments) - 1, 0, -1):
            prev_seg = self.segments[seg_num - 1]
            self.segments[seg_num].goto(prev_seg.xcor(), prev_seg.ycor())
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        self.next_direction = UP

    def down(self):
        self.next_direction = DOWN

    def left(self):
        self.next_direction = LEFT

    def right(self):
        self.next_direction = RIGHT
