from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("貪吃蛇")

screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_os_on = True
while game_os_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.over()
        snake.reset()

    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            score.over()
            snake.reset()

screen.exitonclick()
