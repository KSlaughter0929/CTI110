# Creating Turtle Graphic Drawing
# February 29 2020
# CTI-110 P2HW2 - Turtle Graphic
# Kyle Slaughter
# import turtle
# Fill color to tan
# Using (0, 0) grid points
# Create two opposing Quadrilaterals with a fill color
# End_fill


import turtle
turtle.hideturtle()
turtle.fillcolor('tan')
turtle.begin_fill()
turtle.goto(45, -45)
turtle.goto(90, 0)
turtle.goto(45, 45)
turtle.goto(0, 0)
turtle.goto(-45, -45)
turtle.goto(-90, 0)
turtle.goto(-45, 45)
turtle.goto(0, 0)
turtle.end_fill()

