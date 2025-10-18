import turtle

turtle.speed(1)


# dash line
# for i in range(20):
#     turtle.forward(3)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
    
for side_length in range (50,100,10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()