import turtle
  
t = turtle.Turtle()
t.circle(50)


def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("green") #background color
    tom = turtle.Turtle()
    tom.forward(100) 
    tom.left(120)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    window.exitonclick() #to exit 
draw_triangle()