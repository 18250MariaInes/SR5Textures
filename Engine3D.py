"""
Maria Ines Vasquez Figueroa
18250
Gráficas
SR5 Textures
Main
"""

from gl import Render
from obj import Obj, Texture

#valores con los que se inicializan la ventana y viewport

width=1000
height=1000

#creacion de Window

r = Render(width,height)
t = Texture('./models/woodObj.bmp')
#r.loadModel('./models/face.obj', (960,300,0), (15,15,15), t)

#r.loadModel('./models/objBarrel.obj', (500,500,0), (300,300,300), t)
r.loadModel('./models/model.obj', (500,500,0), (300,300,300), t)

r.glFinish('output.bmp')
r.glZBuffer('zbuffer.bmp')





