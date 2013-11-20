from Scene.Scene import Scene
from Utils.Singleton import Singleton


@Singleton
class SceneManager(object):
    def __init__(self):

        self.SceneMap = {}
        self.NowScene = None

    def AddScene(self, sceneName, scene):
        if type(sceneName) == str:
            for base in scene.__class__.__bases__:
                if Scene == base: # type check (parent)
                    self.SceneMap[sceneName] = scene

                    if self.NowScene == None:
                        self.NowScene = scene

    def RemoveScene(self, sceneName, scene):
        pass

    def ReplaceScene(self, sceneName): # if match is found, the name is replaced by scene else return None
        pass

    def Update(self):
        if self.NowScene.enabled is True:
            self.NowScene.Update()

    def Draw(self):
        if self.NowScene.enabled is True:
            self.NowScene.Draw()

    def Event(self): # later
        pass