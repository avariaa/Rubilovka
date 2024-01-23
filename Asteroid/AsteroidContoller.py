from Asteroid.AsteroidModel import *
from Asteroid.AsteroidView import *

class AsteroidController:
    def __init__(self, model: AsteroidModel, view: AsteroidView):
        self.model = model
        self.view = view
        self.view.Start(self.model.number_of_asteroids)


    def Update(self, delta_time):
        self.model.Move(delta_time)
        self.view.ShowPos(self.model.asteroids)