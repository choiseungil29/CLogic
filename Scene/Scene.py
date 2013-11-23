from OpenGL.raw.GLUT import glutSwapBuffers
from OpenGL.GL import *

class Scene(object):
    def __init__(self):
        # Initializing

        self.enabled = True

    def Update(self):
        pass

    def DrawBegin(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND);
        glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);

    def Draw(self):
    	pass

    def DrawEnd(self):
    	glDisable(GL_TEXTURE_2D)
    	glDisable(GL_BLEND)
    	glutSwapBuffers()