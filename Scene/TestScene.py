from Scene import Scene
from Utils.Log import Logger
from Sprite.Texture import Texture
from Sprite.Sprite import Sprite


class TestScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.sprite = Sprite("test1.png")
        self.sprite.position = 100, 100
    def update(self):
        Scene.update(self)

    def draw(self):
        Scene.draw(self)
        self.sprite.draw()