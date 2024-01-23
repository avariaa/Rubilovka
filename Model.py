from Asteroid.AsteroidModel import *
from Player.PlayerModel import *
from Player.Position import *


def Distance(pos1: Position, pos2: Position):
    return ((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2)**(1/2)


class Model:
    def __init__(self, models):
        self.models = models

    def get_model(self, model_class):
        return self.models[model_class]





