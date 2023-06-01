from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "black", "green", "blue", "purple"]
turtles = []

for idx in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[idx])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + idx * 40)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 235:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner.")
            else:
                print(f"You've lost! The {win_color} turtle is the winner.")
        distance = random.randint(0, 10)
        turtle.forward(distance)

print(turtles)

screen.exitonclick()
