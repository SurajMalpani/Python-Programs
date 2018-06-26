import turtle

def draw_square(turtle):
    for i in range(0,4):
        turtle.forward(100)
        turtle.left(90)

def draw_triangle(turtle):
    for i in range(0,3):
        turtle.forward(100)
        turtle.left(120)

def draw_hex(turtle):
    for i in range(0,6):
        turtle.forward(50)
        turtle.left(60)

def draw_oct(turtle):
    for i in range(0,8):
        turtle.forward(50)
        turtle.left(45)
        
def drawing():
    window = turtle.Screen()
    window.bgcolor("cyan")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("Purple")
    brad.speed("4")

    #draw_oct(brad)
    
    for i in range(0,72):
        draw_oct(brad)
        brad.left(5)

    brad.right(90)
    brad.forward(200)
    
    window.exitonclick()

drawing()
