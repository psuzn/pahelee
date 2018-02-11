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
from PIL import Image
from pahelee.lib import *
from pahelee.constants import *
import sys,os
from time import gmtime, strftime
import random

# 
GRID_WIDTH=8
GRID_HEIGHT=8
IMAGE_FORMAT="png"
IMAGENAME=strftime("%Y-%m-%d_%H:%M:%S", gmtime())+"pahelee"
DESTINATION=os.path.expanduser("~")
# 

grid=[]
current=None
visitedGrids=[]
def initializeGrid():
    global grid,current
    for i in range(0,GRID_COLUMNS):
        for j in range(0,GRID_ROWS):
            if j is 0:
                grid.append([Cell(i,j)])
            else:
                grid[i].append(Cell(i,j))
    current=grid[random.randint(0,GRID_COLUMNS-1)][random.randint(0,GRID_ROWS-1)]
    current.visited=True

def visit(cel):
    cel.visited=True
    return
def saveImage():
    name="{}.{}".format(IMAGENAME,IMAGE_FORMAT)
    x, y, width, height = glGetIntegerv(GL_VIEWPORT)
    data = ( GLubyte * (3*width*height) )(0)
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    glReadPixels(x, y, width, height, GL_RGB,GL_UNSIGNED_BYTE,data)
    image = Image.frombytes(mode="RGB", size=(width, height), data=data)     
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(os.path.join(DESTINATION,name), format=IMAGE_FORMAT) 
    print("Image saved as {}".format(os.path.join(DESTINATION,name)))

def removeWallBetween(current,nxt):
    if current.x>nxt.x:
        removeWall(current,LEFT)
        removeWall(nxt,RIGHT)

    elif current.x < nxt.x:
        removeWall(current,RIGHT)
        removeWall(nxt,LEFT)

    elif current.y > nxt.y:
        removeWall(current,BOTTOM)
        removeWall(nxt,TOP)
    
    elif current.y < nxt.y:
        removeWall(current,TOP)
        removeWall(nxt,BOTTOM)
    return
        
def removeWall(cel,wall):
    cel.wall[wall]=False
    return

def next(current):
    neighbours=[]
    if current.y+1 <GRID_ROWS:
        if not  grid[current.x][current.y+1].visited : # TOP CELL
            neighbours.append(grid[current.x][current.y+1])

    if current.x+1 < GRID_COLUMNS:
        if not  grid[current.x+1][current.y].visited : #RIGHT
            neighbours.append(grid[current.x+1][current.y])

    if current.y-1 >= 0:
        if not  grid[current.x][current.y-1].visited : # BOTTOM
            neighbours.append(grid[current.x][current.y-1])

    if current.x-1 >= 0:
        if not  grid[current.x-1][current.y].visited :# LEFT
            neighbours.append(grid[current.x-1][current.y])

    neighboursCount=len(neighbours)
    # print("Current ({},{})".format(current.x,current.y))
    # print("neighbourd")
    # for cels in neighbours:
    #     print("{},{}".format(cels.x,cels.y))

    if neighboursCount > 0:
        choosed=neighbours[random.randint(0,neighboursCount-1)]
        #print("choosed ({},{})".format(choosed.x,choosed.y))
        return choosed
    else:
        #print("no naughbour to choose")
        return None


def loop():
    global current,grid
    nxt=next(current)
    if nxt:
        visitedGrids.append(current)
        removeWallBetween(current,nxt)
        current=nxt
        visit(current)
    elif len(visitedGrids)>0:
        current=visitedGrids.pop()
    else:
        showGrid()
        saveImage()
        exit()
    showGrid()
    return

def updateConstants():
    global GRID_WIDTH,GRID_HEIGHT
    GRID_WIDTH=glutGet(GLUT_WINDOW_WIDTH)/GRID_COLUMNS
    GRID_HEIGHT=glutGet(GLUT_WINDOW_HEIGHT)/GRID_ROWS
    Cell.height=GRID_HEIGHT
    Cell.width=GRID_WIDTH

def display(val=None):
    glutTimerFunc(int(1000/FPS), display,1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    loop()
    glutSwapBuffers()
    return

def showGrid():
    global grid
    for rows in grid:
        for cel in rows:
            cel.show()
    setColor(CURRENT_BACKGROUND)
    current.show(backgroundColor=CURRENT_BACKGROUND)

def resize( width, height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    updateConstants()
    gluOrtho2D(0, GLdouble (width), 0, GLdouble (height) )
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def initializeOPENGL():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(GRID_COLUMNS*GRID_WIDTH*5,GRID_ROWS*GRID_HEIGHT*5)
    glutInitWindowPosition(350,120)
    glutCreateWindow(TITLE)
    updateConstants()
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutMainLoop()

def main():
    initializeGrid()
    initializeOPENGL()
    return