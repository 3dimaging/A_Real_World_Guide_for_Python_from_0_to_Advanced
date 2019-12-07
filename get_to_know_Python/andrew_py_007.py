import turtle
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange','pink','gold','silver']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(-1)
for x in range(100000000000):
    t.pencolor(colors[x%9])
    t.width(x/100+1)
    t.forward(x)
    t.left(30)
    
