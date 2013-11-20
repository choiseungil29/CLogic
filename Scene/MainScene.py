from OpenGL.raw.GLUT import glutSwapBuffers
from Scene import Scene
from OpenGL.GL import *
from Sprite.Texture import Texture
from Sprite.Sprite import Sprite


class MainScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.texture = Texture()
        self.texture.LoadTexture("test1.png")

        self.sprite = Sprite("test1.png")

    def Update(self):
        Scene.Update(self)

    def Draw(self):
        Scene.Draw(self)

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)

        """glBegin(GL_LINES)
        glVertex2i(180, 15)
        glVertex2i(10, 145)
        glEnd()"""


        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND);
        glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);

        # glBegin(GL_QUADS)

        """glTexCoord2d(0, 0) # self.texture.image.size[1] -> height
        glVertex2d(0, 0)

        glTexCoord2d(1, 0)
        glVertex2d(self.texture.image.size[0], 0)

        glTexCoord2d(1, 1)
        glVertex2d(self.texture.image.size[0], self.texture.image.size[1])

        glTexCoord2d(0, 1)
        glVertex2d(0, self.texture.image.size[1])"""

        self.sprite.draw()

        # glEnd()

        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)

        glutSwapBuffers()