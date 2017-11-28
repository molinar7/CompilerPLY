
import turtle


def drawCircle (x, y, d): # x position, y position, diameter
    #turtle.speed(10)
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.circle(d)
def drawRectangle(x,y,p):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)

def drawTriangle(v1,v2,v3):
    turtle.penup()
    turtle.setposition(v1,v2)
    turtle.pendown()
    turtle.forward(v3) 
    turtle.left(120)
    turtle.forward(v3)
    turtle.left(120)
    turtle.forward(v3)


def drawLine(x, y, f):
    
    turtle.penup()
    turtle.home() # resetea el angulo y cordenadas anteriores
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(f)
   
    

def drawArc(x, y, f):
    
    turtle.left(y)
    turtle.circle(f,180)
    



