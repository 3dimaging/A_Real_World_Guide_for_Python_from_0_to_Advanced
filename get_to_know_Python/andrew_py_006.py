import turtle
loadWindow = turtle.Screen()
turtle.speed(-100)

turtle.colormode(255)

sides=3

def shape(size,sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(36)
        


for i in range(100):
    shape(5*i,sides)
    turtle.left(i)
    turtle.color(i+100, i+150, 2*i+50)
turtle.exitonclick()
