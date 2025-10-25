import turtle

turtle.Screen().bgcolor("turquoise")

board = turtle.Turtle()
turtle.title("Let us draw a Star")

# first triangle for star 
board.forward(100) #draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# seccond triangle for the star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()



