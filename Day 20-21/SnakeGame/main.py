from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scorecard import Scorecard
import time

jim = Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorecard.increase_score()


    if snake.head.xcor() > 200 or snake.head.xcor() < -200 or snake.head.ycor() > 200 or snake.head.ycor() < -200:
        game_is_on = False
        scorecard.game_over()

    # if snake.head.distance(segment) < 10:


screen.exitonclick()