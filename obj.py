"""
Maria Ines Vasquez Figueroa
18250
Gráficas
SR5 Textures
Carga OBJ
"""
#Carga de archivo OBJ
import struct

def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Obj(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines=file.read().splitlines()
        #clasificaciones de datos dentro de archivo OBJ
        self.vertices=[]
        self.normals=[]
        self.texcoords=[]
        self.faces=[]

        self.read()
        #print(self.vertices)
        #print("-----------------------------------------------------------------------")

    def read(self):#funcion para leer lineas de archivo OBJ y asi clasificarlo
        for line in self.lines:
            #print(line.split(' ',1))
            if line: #clasificacion de lineas en txt entre vertices, normales, textcoords y cara de modelo 3D
                prefix,value=line.split(' ',1)
                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                elif prefix == 'vn': #normales
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'vt': #textcoords
                    self.texcoords.append(list(map(float,value.split(' '))))
                elif prefix == 'f': #faces XX/YY/ZZ
                    self.faces.append([list(map(int,vert.split('/'))) for vert in value.split(' ')])


#new code Carlos
class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()
        
    def read(self):
        image = open(self.path, 'rb')
        image.seek(10)
        headerSize = struct.unpack('=l', image.read(4))[0]

        image.seek(14 + 4)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]
        image.seek(headerSize)

        self.pixels = []

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1)) / 255
                g = ord(image.read(1)) / 255
                r = ord(image.read(1)) / 255
                self.pixels[y].append(color(r,g,b))

        image.close()

    def getColor(self, tx, ty):
        if tx >= 0 and tx <= 1 and ty >= 0 and ty <= 1:
            x = int(tx * self.width)
            y = int(ty * self.height)

            return self.pixels[y][x]
        else:
            return color(0,0,0)
        

