import turtle

x = turtle.Turtle()

for j in range(1,6):
    for i in range(10):
        x.right(i * 36)
        x.forward(j * 50)
        x.right(60)
        x.forward(j * 50)
        x.right(120)
        x.forward(j * 50)
        x.right(60)
        x.forward(j * 50)
        x.home()

turtle.done()
