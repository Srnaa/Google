import turtle
win = turtle.Screen() #background color of the window
win.bgcolor("white")
circle = turtle.Turtle()

#outline of the circle
circle.color("white") #Use to set the color of the turtle 
circle.right(90)
circle.forward(200)
circle.left(90)
circle.color("black")
circle.circle(200)

#Now creating the smaller black circle
circle.color("white")
circle.left(90)
circle.forward(400)
circle.color("black")
circle.fillcolor("black")
circle.begin_fill()
circle.left(90)
circle.circle(100)
circle.end_fill()

#Now black filling color in bigger semicircle
circle.fillcolor("black")
circle.begin_fill()
circle.left(90)
circle.forward(400)
circle.left(90)
circle.circle(200,180)
circle.end_fill()

#Now creating smaller circle
circle.left(90)
circle.forward(200)
circle.color("white")
circle.fillcolor("white")
circle.begin_fill()
circle.right(90)
circle.circle(99)
circle.end_fill()

#Now creating the white eye
circle.color("black")
circle.right(90)
circle.forward(75)
circle.right(90)
circle.fillcolor("white")
circle.begin_fill()
circle.circle(25)
circle.end_fill()

#Now creating the black eye
circle.right(90)
circle.forward(75)
circle.color("white")
circle.forward(75)
circle.right(90)
circle.fillcolor("black")
circle.begin_fill()
circle.circle(25)
circle.end_fill()

turtle.done()