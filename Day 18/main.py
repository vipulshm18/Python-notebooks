import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.color("red")

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#

# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#
#
# for i in range(3, 11):
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)
#
# #Alternate
#
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)
#
#

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple((r, g, b))


directions = [0, 90, 180, 270]


#
# for i in range(200):
#     timmy.speed("fastest")
#     timmy.pensize(15)
#     timmy.color(random_color()  )
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)



draw_spirograph(5)











screen = Screen()
screen.exitonclick()