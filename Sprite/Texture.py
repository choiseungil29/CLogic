# draw to drawPixels
# if calls two over, modifying uses for quad
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image

import numpy


class Texture(object):
    def __init__(self):
        self.texId = 0
        self.image = 0

    def LoadTexture(self, filename):
        self.texId = glGenTextures(1)
        self.image = Image.open(filename)
        Image_Data = numpy.array(list(self.image.getdata()), numpy.int8)
        xsize, ysize, imageData = self.image.size[0], self.image.size[1], self.image.tostring("raw", "RGBA", 0, -1)

        glBindTexture(GL_TEXTURE_2D, self.texId)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        result = glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.image.size[0], self.image.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE,
                     imageData)
        if result == GLU_INVALID_VALUE:
            print 'GLU INVALID VALUE => Cngine: 27'
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)


    def RemoveTexture(self, filename):
        pass