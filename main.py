import time
from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #     Detecting food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.current_score += 1
        score.update()

    #    Detecting wall collision
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    #    Detecting collision with itself
    for check in snake.segments[1:]:
        if snake.head.distance(check)<10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
