from OpenGL.raw.GLUT import glutSwapBuffers
from Scene import Scene
from OpenGL.GL import *
from Sprite.Texture import Texture
from Sprite.Sprite import Sprite


class TestScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.sprite = Sprite("test1.png")
    def Update(self):
        Scene.Update(self)

    def Draw(self):
        Scene.Draw(self)
        self.sprite.draw()

        