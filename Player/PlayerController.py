import tkinter

from Player.PlayerModel import *
from Player.PlayerView import *

class PlayerController:
    def __init__(self, model: PlayerModel, view: PlayerView):
        self.model = model
        self.view = view

    def Move(self, event: tkinter.Event):
        delta_time = 0.1
        self.model.Move(delta_time, event.keysym)
        self.view.ShowPos(self.model.position)

    def Shoot(self, event: tkinter.Event):
        self.model.Shoot()

    def Update(self, delta_time):
        self.view.ShowPos(self.model.position, self.model.angle)

    def Accelerate(self):
        self.model.Accelerate(1)
