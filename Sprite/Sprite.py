from OpenGL.GL import *
from .Texture import Texture
from .TextureManager import TextureManager

class Sprite(object):
    def __init__(self, textureName):

        textureManager = TextureManager()
        if not textureManager.existTexture(textureName):
            textureManager.addTexture(textureName)

        self.texture = textureManager.getTexture(textureName)
        self.rotation = 0
        self.position = 0, 0
        self.anchor = 0.5, 0.5
        self.scale = 1.0, 1.0
        self.width = self.texture.image.size[0]
        self.height = self.texture.image.size[1]
        self.visible = True
        self.enable = True

    def setPosition(self, x, y):
        self.position = x, y

    def setAnchorPoint(self, x, y):
        self.anchor = x, y

    def setScale(self, x, y):
        self.scale = x, y

    def setVisible(self, visible):
        self.visible = visible

    def setEnable(self, enable):
        self.enable = enable;

    def update(self):
        pass

    def draw(self):
        glTranslatef(self.position[0], self.position[1], 0.0)
        glRotatef(self.rotation, 0, 0, 1)
        glScalef(self.scale[0], self.scale[1], 0.0)

        glBegin(GL_QUADS)

        glTexCoord2d(0, 0) # self.texture.image.size[1] -> height
        glVertex2d(0 - self.width * self.anchor[0], 0 - self.height * self.anchor[1])

        glTexCoord2d(1, 0)
        glVertex2d(self.width - self.width * self.anchor[0], 0 - self.height * self.anchor[1])

        glTexCoord2d(1, 1)
        glVertex2d(self.width - self.width * self.anchor[0], self.height - self.height * self.anchor[1])

        glTexCoord2d(0, 1)
        glVertex2d(0 - self.width * self.anchor[0], self.height - self.height * self.anchor[1])

        glEnd()