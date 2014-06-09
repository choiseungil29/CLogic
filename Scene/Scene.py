from OpenGL.raw.GLUT import glutSwapBuffers
from OpenGL.GLUT import *
from OpenGL.GL import *

class Scene(object):
    def __init__(self):
        # Initializing

        self.enabled = True

    def update(self):
        pass

    def drawBegin(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND);
        glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    def draw(self):
    	pass

    def drawEnd(self):
    	glDisable(GL_TEXTURE_2D)
    	glDisable(GL_BLEND)
    	glutSwapBuffers()
        glutPostRedisplay()