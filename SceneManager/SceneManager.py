from Scene.Scene import Scene
from Utils.Singleton import Singleton


@Singleton
class SceneManager(object):
    def __init__(self):

        self.SceneMap = {}
        self.NowScene = None

    def AddScene(self, sceneName, scene):
        self.SceneMap[sceneName] = scene
        if self.NowScene == None:
            self.NowScene = scene

    def RemoveScene(self, sceneName, scene):
        pass

    def ReplaceScene(self, sceneName): # if match is found, the name is replaced by scene else return None
        pass

    def update(self):
        if self.NowScene.enabled is True:
            self.NowScene.update()
        # print 'update'
    def draw(self):
        if self.NowScene.enabled is True:
            self.NowScene.drawBegin()
            self.NowScene.draw()
            self.NowScene.drawEnd()
    def Event(self): # later
        pass