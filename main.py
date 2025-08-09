from turtle import Screen, Turtle
import time
import score
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake  = Snake()
food = Food()
score_board = score.Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()

    if snake.head.distance(food) < 17:

        food.random_location()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() < -380 or snake.head.xcor() > 380 or snake.head.ycor() < -380 or snake.head.ycor() > 380:
        score_board.reset_score()
        snake.reset_snake()


    for segment in snake.segments[1:]:
        # if segment in snake.segments:
        #     pass
        if snake.head.distance(segment) < 10:
            score_board.reset_score()
            snake.reset_snake()


screen.exitonclick()
