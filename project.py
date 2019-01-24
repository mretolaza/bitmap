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
    getColor(1,1,1)

#Init canvas with new color 
def glClearColor(r,g,b):
    img.clearColor(0,0,0) 

#Get new x,y points 
def glVertex(x,y):
    img.vertex(x,y)

#Show new image 
def glFinish():
    img.writeFile("popo.bmp")

glCreateWindow(700,500)

"""
option = true 
while option: 
    print('Menú de instrucciones')
    print('1. Por renderizar una imagen negra con un punto blanco en una ubicación random dentro de la imagen.')
    print('2. Por renderizar una imagen negra con un punto blanco en cada esquina')
    print('3. Por renderizar un cubo de 100 pixeles en el centro de su imagen')
    print('4. Por renderizar líneas blancas en toda la orilla de su imagen (4 lineas)')
    print('5. Por renderizar una línea blanca en diagonal por el centro de su imagen.')
    print('6. Por llenar su imagen entera de puntos blancos y negros (las posibilidades de que un punto sea blanco o negro son de 50%)')
    print ('7. Por llenar su imagen entera de puntos de colores random')
    print ('8. Por crear una escena de un cielo con estrellas ')

  """  
#1 

""" 
glClearColor(0,0,0)
glClear()
glViewPort(0,0,699,499)
glColor(1,1,1)
glVertex(0,1)
""" 
#2 
glClearColor(0,0,0)
glClear()
glViewPort(0,0,699,499)
glColor(1,1,1)
glVertex(-1,-1)
glVertex(-1,1)
glVertex(1,-1)
glVertex(1,1)


glFinish()