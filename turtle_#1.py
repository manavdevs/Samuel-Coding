import turtle

turtle.Screen().bgcolor("White")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Whiteboard")
board=turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1