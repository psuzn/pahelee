from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from constants import *

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