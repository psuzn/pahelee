from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from constants import *

def line(x1,y1,x2,y2,visited=False):
    glLineWidth(WALLWIDTH)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2,y2)
    glEnd()