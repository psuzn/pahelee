from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pahelee.constants import *

def setColor(colorList):
    glColor3f(colorList[0],colorList[1],colorList[2])

def line(x1,y1,x2,y2): # draw a line from (x1,y1) to (x2,y2)
    glLineWidth(WALLWIDTH)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2,y2)
    glEnd()

def rectangle(x1,y1,x2,y2): # rectangle from left bottom (x1,y1) to top right (x2,y2)
    glBegin(GL_QUADS)
    glVertex2f(x1,y1)
    glVertex2f(x1,y2)
    glVertex2f(x2,y2)
    glVertex2f(x2,y1)  
    glEnd();


class Cell:
    height=10
    width=10

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.visited=False
        self.wall=[True,True,True,True]
    
    def show(self,wallColor=None,backgroundColor=None):
        x=self.x*self.width
        y=self.y*self.height
        # background
        if backgroundColor:
            setColor(backgroundColor)
        elif self.visited:
            setColor(VISITED_BACKGROUND)
        else:
            setColor(UNVISITED_BACKGROUND)

        rectangle(x,y,x+self.width,y+self.height)

        # walls
        if wallColor:
            setColor(wallColor)
        else:
            setColor(WALLCOLOR)

        if self.wall[TOP]:
            line(x,y+self.height,x+self.width,y+self.height)

        if self.wall[RIGHT]:
            line(x+self.width,y+self.height,x+self.width,y)

        if self.wall[BOTTOM]:
            line(x+self.width,y,x,y)
            
        if self.wall[LEFT]:
            line(x,y,x,y+self.height)