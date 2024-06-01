import turtle

tur = turtle.Turtle()

tur.speed(6)

tur.getscreen().bgcolor("black")
tur.color("cyan")

tur.penup()

tur.goto((-200, 50)) #middle of screen

tur.pendown() #introductery functions


def star(turtle, size): #fractal function
    if size <= 10: #initial fractal size, #if fractal size is less than 10 in size re-iterate the pre-existing pattern at its resolution fo size.
        return
    else:
        for i in range(5): 
#if not iterate 5 times around each 5 points of the pentagram, creating branching smaller pentagrams around each point of the pentagram and so on branching out like a tree..
            turtle.forward(size)
            star(turtle, size / 3) 
# The division decides to how many times 5 will go to the power of 5 in this order, 3 is very big 0 is infinite

            turtle.left(72) 
# The degree angle, this will act as our "ratio". This is the most instumental part in creating a fractal (at-least from my knowledge of it) in this case we have 72, which will create a branching pentagram that somehow makes a pentagon, idk why it does that but it works


star(tur, 360) #when done spin 360 degrees
turtle.done()