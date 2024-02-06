import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Plisken Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.move_up ,"Up")
screen.onkey(snake.move_down ,"Down")
screen.onkey(snake.move_left ,"Left")
screen.onkey(snake.move_right ,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()