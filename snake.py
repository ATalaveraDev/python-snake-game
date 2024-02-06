from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self) -> None:
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
    self.direction = "east"
  
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def move(self) -> None:
    for seg_num in range(len(self.segments) - 1, 0, -1):
       new_x = self.segments[seg_num - 1].xcor()
       new_y = self.segments[seg_num - 1].ycor()
       self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def move_up(self) -> None:
    if self.head.heading() != DOWN:
      self.head.setheading(90)
      self.direction = "north"
  
  def move_down(self) -> None:
    if self.head.heading() != UP:
      self.head.setheading(270)
      self.direction = "south"

  def move_right(self) -> None:
    if self.head.heading() != LEFT:
      self.head.setheading(360)
      self.direction = "east"

  def move_left(self) -> None:
    if self.head.heading() != RIGHT:
      self.head.setheading(180)
      self.direction = "west"

  def add_segment(self, position):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    self.segments.append(segment)

  def extend(self):
    self.add_segment(self.segments[-1].position())