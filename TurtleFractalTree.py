##  Author      :   itsMohammedThaier
##  Description :   Fractal tree

import math
import turtle

#Helpers
def FractalLine(x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
def Fractal(x,y,angleBase,length,color,depth,maxDepth):
    #Break
    if depth>maxDepth:
        return

    #Pre-drawing
    turtle.pencolor(color)

    #Left sub-fractal
    angleNew = angleBase-(math.pi/8)
    xEnd = x + math.cos(angleNew)*length
    yEnd = y + math.sin(angleNew)*length
    FractalLine(x,y,xEnd,yEnd)
    Fractal(xEnd,yEnd,angleNew,length*.75,color,depth+1,maxDepth)
    #Right sub-fractal
    angleNew = angleBase+(math.pi/8)
    xEnd = x + math.cos(angleNew)*length
    yEnd = y + math.sin(angleNew)*length
    FractalLine(x,y,xEnd,yEnd)
    Fractal(xEnd,yEnd,angleNew,length*.75,color,depth+1,maxDepth)
    
#Turtle customization
turtle.speed('fastest')
#turtle.tracer(0) uncomment for instant render

#Flow
Fractal(x=0,y=0,angleBase=math.pi/2,length=100,color='black',depth=0,maxDepth=8)

#Done
turtle.done()

