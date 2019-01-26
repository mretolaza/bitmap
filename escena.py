"""
María Mercedes Retolaza Reyna, 16339
Gráficas por Computadora  
""" 
import libsEsc 
import struct
import os 
from libsEsc import Bitmap
from libsEsc import word
from libsEsc import getColor

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
    img.setColor(r,g,b)

#Init canvas with new color 
def glClearColor(r,g,b):
    img.clearColor(0,0,0) 

#Get new x,y points 
def glVertex(x,y):
    img.vertex(x,y)

def createImage(): 
    img.stars(40)
    img.drawLeftLine(10)
    img.drawRightLine(10)
    img.drawTopLine(10)
    img.drawBottonLine(10)
    img.nave()

#Show new image 
def glFinish():
    img.writeFile("atari.bmp")

def menu(): 
    os.system('cls')
    print ('0. Salir')
    print('1. Escena de Atari')

glCreateWindow(160,192)

option = True 
while option: 
    menu()
    menuOption = input("Ingresa una opción del menú  >> ")

    if menuOption == "1":
        print("----")
        input ("Escena de Atari...\npulsa una tecla para continuar")
        glClearColor(0,0,0)
        glClear()
        glViewPort(0,0,140,170)
        glColor(255,255,255)
        createImage()
        glFinish()

    elif menuOption == "0":
        break 
    else: 
        print("")
        input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")