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
#se carga textura y modelo obj con la textura
##para cargar pelota de basketball
t = Texture('./models/ball.bmp')
r.loadModel('./models/earth.obj', (500,500,0), (1,1,1), t)

#para cargar ejemplo OBJ de Carlos
"""t = Texture('./models/model.bmp')
r.loadModel('./models/model.obj', (500,500,0), (300,300,300), t)"""



r.glFinish('output.bmp')





