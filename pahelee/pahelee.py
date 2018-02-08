'''
File: pahelee.py
Created Date: Tuesday February 6th 2018
Author: Sujan Poudel
Github: https://github.com/psuzn
Last Modified:Tuesday, February 6th 2018, 9:38:35 pm
Copyright (c) 2018 https://github.com/psuzn
'''

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from lib import *
from constants import *
import sys
import time 
import random



def loop():
    pass

    
def display(val=None):
    glutTimerFunc(int(1000/FPS), display,1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    loop()
    glutSwapBuffers()
    return

def initializeOPENGL():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(TITLE)
    updateConstants()
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutMainLoop()

def main():
    initializeOPENGL()
    return