from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Utils.Singleton import Singleton
from .Texture import Texture

@Singleton
class TextureManager(object):

	def __init__(self):
		self.textureTable = {}

	def addTexture(self, textureName):
		texture = Texture()
		texture.LoadTexture(textureName)
		self.textureTable[textureName] = texture

	def existTexture(self, textureName):
		if self.textureTable.has_key(textureName):
			return True
		return False

	def getTexture(self, textureName):
		return self.textureTable[textureName]