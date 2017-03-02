import turtle

#Draw background
window = turtle.Screen()
window.bgcolor("#02b3e4!important")

def draw_square(my_turtle, right, color):
    #create instance of class turtle, called my_turtle, "right" defines degrees to turn right
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    my_turtle.color(color)
    my_turtle.speed(0)
    my_turtle.width(2)
    right = my_turtle.right(right)

    my_turtle.up()
    my_turtle.setposition(-200,200)
    my_turtle.down()
    
    for x in range (0, 4):
        #distance per direction
        my_turtle.forward(75)
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

def draw_flower_using_squares():
    turtle1 = turtle.Turtle()
    
    color = "white"
    y = 1
    for x in range (0, 45):
        draw_square(turtle1, y, color)
        y += 8

    turtle1.up()
    turtle1.setposition(-200,200)
    turtle1.down()

    turtle1.right(90)
    turtle1.color(color)
    turtle1.forward(150)

size = 50
def a(x):
    my_name = turtle.Turtle()
    my_name.color("white")
    my_name.width(2)

    my_name.up()
    my_name.setx(x)
    my_name.down()

    my_name.right(-70)
    my_name.forward(size)

    my_name.right(140)
    my_name.forward(size)

    my_name.right(180)
    my_name.forward(size/2)

    my_name.left(70)
    my_name.forward(size/2)

def n(x):    
    my_name = turtle.Turtle()
    my_name.color("white")
    my_name.width(2)

    my_name.up()
    my_name.setx(x)
    my_name.down()

    my_name.right(-90)
    my_name.forward(size)

    my_name.right(160)
    my_name.forward(size+2)

    my_name.right(-160)
    my_name.forward(size)

def t(x):    
    my_name = turtle.Turtle()
    my_name.color("white")
    my_name.width(2)

    my_name.up()
    my_name.setx(x)
    my_name.down()

    my_name.right(-90)
    my_name.forward(size)

    my_name.right(270)
    my_name.forward(size/2)

    my_name.right(180)
    my_name.forward(size)

def h(x):    
    my_name = turtle.Turtle()
    my_name.color("white")
    my_name.width(2)

    my_name.up()
    my_name.setx(x)
    my_name.down()

    my_name.right(-90)
    my_name.forward(size)

    my_name.right(180)
    my_name.forward(size/2)

    my_name.right(-90)
    my_name.forward(size/2)

    my_name.right(90)
    my_name.forward(size/2)

    my_name.right(180)
    my_name.forward(size)

def o(x):    
    my_name = turtle.Turtle()
    my_name.color("white")
    my_name.width(2)

    my_name.up()
    my_name.setx(x)
    my_name.down()

    my_name.circle(size/2.1)

def y(x):    
    my_name = turtle.Turtle()
    my_name.color("white")
    my_name.width(2)

    my_name.up()
    my_name.setx(x)
    my_name.down()

    my_name.right(-90)
    my_name.forward(size/2)

    my_name.right(-30)
    my_name.forward(size/2)

    my_name.right(180)
    my_name.forward(size/2)

    my_name.right(-120)
    my_name.forward(size/2)
       
#run

#draw name, argument is offset for x axis
a(0)
n(size - 5)
t(size*2)
h(size*3 - 10)
o(size*4 + 10)
n(size*5)
y(size*6 - 5)

#draw_square2()            
#draw_triangle()
#draw_circle()

#Close on click
window.exitonclick()
