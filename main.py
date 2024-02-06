import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_SIZE = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Plisken Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.place_food()

    if snake.head.xcor() > SCREEN_SIZE or snake.head.xcor() < -SCREEN_SIZE or snake.head.ycor() > SCREEN_SIZE or snake.head.ycor() < -SCREEN_SIZE:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if snake.head != segment and snake.head.distance(segment) < 10:
          game_is_on = False
          scoreboard.game_over()

screen.exitonclick()