# from turtle import Turtle, Screen
import random
import turtle as t
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


# tim.color("red", "green")
# for a in range(0, 4):
#     tim.forward(100)
#     tim.right(90)
# for a in range(0,5):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# triangle
# number_of_sides = 3
# while number_of_sides <= 10:
#     for a in range(number_of_sides):
#         angle = 360 /number_of_sides
#         tim.forward(100)
#         tim.right(angle)
#     number_of_sides += 1
color = random_color()

def draw_shape(number_sides):
    angle = 360 / number_sides
    for a in range(number_sides):
        tim.color(random_color())
        tim.forward(100)
        tim.right(angle)


#
# movement = [0, 90, 180, 270]
# n =1
# tim.pensize(10)
# tim.speed("fastest")
# while n < 200:
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(movement))
#     n+=1
def draw_spirograph(gap_between_circles):
    number_of_circles = int(360/gap_between_circles)
    for a in range(number_of_circles):
        tim.color(random_color())
        tim.circle(100)
        # current_title = tim.heading()
        # tim.setheading(current_title + 10)
        tim.left(gap_between_circles)

draw_spirograph(5)
# I tried to deploy the tilt function, didnt work out. can also deploy heading function here.






screen = t.Screen()
screen.exitonclick()
