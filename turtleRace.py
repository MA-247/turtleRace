import turtle
import random


colors = ["red", "blue", "green"]

turtles = []

for x in range(0, 3):
	turtle_obj = turtle.Turtle()
	#turtle_obj.hideturtle()
	turtles.append(turtle_obj)
	color_selected = colors[x]
	turtles[x].color(color_selected)
	turtles[x].penup()
	turtles[x].shape("turtle")


screen = turtle.Screen()


turtles[0].setheading(135)
turtles[0].forward(270)
turtles[0].setheading(270)

turtles[1].setheading(90)
turtles[1].forward(190)
turtles[1].setheading(270)


turtles[2].setheading(45)
turtles[2].forward(270)
turtles[2].setheading(270)


for x in range(0, 3):
	turtles[x].pendown()
	turtles[x].pensize(5)
		


while(True):
	for x in range(0, 3):
		turtles[random.randint(0,2)].forward(10)
		turtles[random.randint(0,2)].speed(random.randint(0,10))

		


