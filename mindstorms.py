
import turtle

#Draw background
window = turtle.Screen()
window.bgcolor("#3cba54")

def draw_square(my_turtle, right):
    #create instance of class turtle, called my_turtle
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    my_turtle.color("white")
    my_turtle.speed(0)
    my_turtle.width(2)
    right = my_turtle.right(right)

    for x in range (0, 4):
        #distance per direction
        my_turtle.forward(200)
        #number of degrees to turn
        my_turtle.right(90)

#create other instances
def draw_circle():
    circle_turtle = turtle.Turtle()
    circle_turtle.shape("triangle")
    circle_turtle.color("red")
    circle_turtle.speed(10)
    circle_turtle.width(4)
    circle_turtle.circle(100)


def draw_triangle():  
    tri_turtle = turtle.Turtle()
    tri_turtle.shape("triangle")
    tri_turtle.color("blue")
    tri_turtle.speed(3)
    tri_turtle.width(4)

    for x in range (0, 3):
        #distance per direction
        tri_turtle.backward(120)
        #number of degrees to turn
        tri_turtle.right(120)

def draw_square2():

    turtle1 = turtle.Turtle()
    y = 0
    for x in range (0, 45):
        draw_square(turtle1, y)
        y += 8

def bill():
    bill = turtle.Turtle()
    for x in range (0, 4):
        draw_square(bill, 0)

bill()

#draw_square2()            
#draw_triangle()
#draw_circle()

#Close on click
window.exitonclick()
