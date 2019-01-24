"""
María Mercedes Retolaza Reyna, 16339
Gráficas por Computadora  
""" 
#import libs 
import struct
from libs import Bitmap
from libs import word
from libs import getColor


#Objet to draw 
img = None

#Constructor 
def glInit():
    return None

#Init FrameBuffer
def glCreateWindow(width, height):
    global img 
    img = Bitmap(width,height)
    return img 

#Delete actual image 
def glClear(): 
    img.clear()

#Image area can draw
def glViewPort(x,y,widht, height):
    img.viewPort(x,y,widht, height)

#Get Color 
def glColor(r,g,b):
    getColor(0,1,0)

#Init canvas with new color 
def glClearColor(r,g,b):
    img.clearColor(0,0,0) 

#Get new x,y points 
def glVertex(x,y):
    img.vertex(x,y)

#Show new image 
def glFinish():
    img.writeFile("popo.bmp")

glCreateWindow(600,400)
glClearColor(0,0,0)
glClear()
glViewPort(0,0,599,399)
glColor(1,1,1)
glVertex(0,1)
glFinish()