from OpenGL.raw.GLUT import GLUT_DOWN
from Utils.Singleton import Singleton

@Singleton
class KeyboardEvent():
    def __init__(self):
        self.keys = {}
        self.beforeKeys = {}

    def KeyboardDownEvent(self, key, x, y):
        """ glutKeyboardFunc(KeyboardEvent.KeyboardDownEvent) """

        if self.keys.has_key(key) is True:
            self.beforeKeys[key] = self.keys[key]
        self.keys[key] = True

    def KeyboardUpEvent(self, key, x, y):
        """ glutKeyboardUpFunc(KeyboardEvent.KeyboardUpEvent) """

        if self.keys.has_key(key) is True:
            self.beforeKeys[key] = self.keys[key]
        self.keys[key] = False

    def getKeyDown(self, key):
        if self.beforeKeys[key] is False and self.keys[key] is True:
            return True
        return False

    def getKeyUp(self, key):
        if self.beforeKeys[key] is True and self.keys[key] is False:
            return True
        return False

    def getIsKeyDown(self, key):
        if not self.keys.has_key(key) or not self.keys[key]:
            return False
        return True

    def getIsKeyUp(self, key):
        if not self.keys.has_key(key) or self.keys[key]:
            return False
        return True


@Singleton
class MouseEvent():
    def __init__(self):
        """ Init MouseEvent """

        self.x = 0
        self.y = 0
        self.beforMouseButtonState = {}
        self.mouseButtonState = {}

    def onMouseMove(self, x, y):
        """ glutMotionFunc(MouseEvent.onMouseMove) """

        self.x = x
        self.y = y

    def onMouseButton(self, button, state, x, y):
        """ glutMouseFunc(MouseEvent.onMouseButton) """

        """if not hasattr(self.mouseButtonState, button):
            setattr(self.mouseButtonState, button, False)"""

        if state is GLUT_DOWN:
            self.mouseButtonState[button] = True
        else:
            self.mouseButtonState[button] = False

    def getMouseDown(self, key):
        if self.beforMouseButtonState[key] is False and self.mouseButtonState[key] is True:
            return True
        return False

    def getMouseUp(self, key):
        if self.beforMouseButtonState[key] is True and self.mouseButtonState[key] is False:
            return True
        return False

    def getIsKeyDown(self, key):
        if not hasattr(self.mouseButtonState, key) or not self.mouseButtonState[key]:
            return False
        return True

    def getIsKeyUp(self, key):
        if not hasattr(self.mouseButtonState, key) or self.mouseButtonState[key]:
            return False
        return True










