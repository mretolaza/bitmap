"""
Librerías Internas 
""" 

import struct
from math import sqrt
from math import ceil
from random import randint

def char(c):
    return struct.pack("=c", c.encode('ascii'))

def word(c):
    return struct.pack("=h", c)

def dword(c):
    return struct.pack("=l", c)

def getColor(r, g, b):
    return bytes([b, g, r])

class Bitmap(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []
        self.r = 0
        self.g = 0
        self.b = 0 
        self.vpWidth = 0
        self.vpHeight = 0
        self.vpX = 0 
        self.vpY = 0 
        self.vr = 0
        self.vg = 0
        self.vb = 0
        self.clear()
    
    #structure image file 
    def writeFile(self, filename):
        f = open(filename, "wb")
        # estandar
        f.write(char('B'))
        f.write(char('M'))
        # file size
        f.write(dword(14 + 40 + self.width * self.height * 3))
        # reserved
        f.write(dword(0))
        # data offset
        f.write(dword(54))
        # header size
        f.write(dword(40))
        # width
        f.write(dword(self.width))
        # height
        f.write(dword(self.height))
        # planes
        f.write(word(1))
        # bits per pixel
        f.write(word(24))
        # compression
        f.write(dword(0))
        # image size
        f.write(dword(self.width * self.height * 3))
        # x pixels per meter
        f.write(dword(0))
        # y pixels per meter
        f.write(dword(0))
        # number of colors
        f.write(dword(0))
        # important colors
        f.write(dword(0))
        # image data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        # close file
        f.close()

    # Clear image 
    def clear(self):
        self.framebuffer = [
            [
                #show background color 
                getColor(self.r,self.g,self.b) for x in range(self.width)
            ]
            for y in range(self.height)
        ]

    #clear the canvas with a new color 
    def clearColor(self, newR, newG, newB):
        self.r = ceil(newR*255)
        self.g = ceil(newG*255)
        self.b = ceil(newB*255) 

    # get dimension image (begin of glViewPort)
    def viewPort(self, x, y, width, height):
        if height <= 0 or width <= 0:
            print('Error, el Largo y el Ancho de la imágen deben de ser valores mayores a 0')
        elif x< 0 or y < 0 or x > self.width or y > self.height:
            print('Error, Las coordenadas ingresadas (x,y) deben de ser mayores a 0. Además deben de ser menores al ancho y largo de la imagen')
        else:  
            self.vpWidth = width
            self.vpHeight = height
            self.vpX = x 
            self.vpY = y 
    # create new 
    def vertex(self, x, y): 
        if self.vpHeight !=  0 or self.vpWidth != 0:
            localX = round((x+1)*((self.vpWidth)/2) + self.vpX)  
            localY = round((y+1)* ((self.vpHeight)/2) + self.vpY)
            self.point(localX,localY)
        else: 
            print('Debe de ejecutar glViewPort para obtener un área a gráficar')

    # Create point in framebuffer
    def point(self, x, y):
        self.framebuffer[y][x] = getColor(self.vr, self.vg, self.vb)

    # Set random color 
    def random(self):
        for y in range(self.height):
            for x in range(self.width):
                self.point(x, y)

    # Create lego 
    def lego(self):  
        for x in range(70):
            for y in range(70):
                self.framebuffer[x][y] = getColor(self.vr, self.vg, self.vb)

    #create horizontal line 
    def lineHorizontal(self,x,y,lenght,color): 
        for i in range(lenght):
            self.vertex(x+i,y)

    # create vertical line 
    def lineVertical(self,x,y,lenght,color): 
        for j in range(lenght):
            self.vertex(x,y + j)

    # Create square 
    def square(self, x,y):
        for i in range (x, x+200):
            for j in range (y,y+200):
                self.vertex(x + i ,y + j)
    #