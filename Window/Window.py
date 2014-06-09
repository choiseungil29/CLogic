from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Event.Event import KeyboardEvent, MouseEvent

from Scene.TestScene import TestScene
from SceneManager.SceneManager import SceneManager

# from Game.Scene.GameScene import GameScene

from Utils.Log import Logger


#noinspection PyUnresolvedReferences
class Window(object):
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height

    def createWindow(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        glutInitWindowPosition(50, 100)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Cngine")
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        gluOrtho2D(0.0, self.width / 2, 0.0, self.height / 2)

        scene = TestScene()
        # Init Scene

        sceneManager = SceneManager()
        sceneManager.AddScene("TestScene", scene)

        keyboardEvent = KeyboardEvent()
        mouseEvent = MouseEvent()

        # Init Manager

        glutDisplayFunc(sceneManager.draw)
        glutIdleFunc(sceneManager.update)
        glutKeyboardFunc(keyboardEvent.KeyboardDownEvent)
        glutKeyboardUpFunc(keyboardEvent.KeyboardUpEvent)
        glutMotionFunc(mouseEvent.onMouseMove)
        glutMouseFunc(mouseEvent.onMouseButton)
        glutMainLoop()