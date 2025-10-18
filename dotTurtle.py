import turtle

height= 5
width =5

turtle.speed(2)

turtle.penup()

for i in range(height):
    for j in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(30*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

for i in range(height):
    for j in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.forward(30*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()