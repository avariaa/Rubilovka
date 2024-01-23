import tkinter

from Player.PlayerModel import *
from Player.PlayerView import *
from Asteroid.AsteroidModel import *
class OldController:
    def __init__(self, model, view, controllers):
        self.model = model
        self.view = view
        self.controllers = controllers

        self.view.OnKeyPressed(self.EventListener)
        self.view.OnUpdate(self.Update)

        self.view.get_view(PlayerView).h = self.model.get_model(PlayerModel).radius

        self.view.Start()

    def CheckCollision(self):
        pass

    def Update(self, delta_time):
        for controller in self.controllers:
            self.controllers[controller].Update(delta_time)

        self.view.get_view(PlayerView).ShowPos(self.model.get_model(PlayerModel).position,
                                               self.model.get_model(PlayerModel).angle)




    def EventListener(self, event: tkinter.Event):
        delta_time = 0.1
        print(event.x_root, event.y_root, event.x, event.y)
        if event.keysym == 'Up':
            self.model.get_model(PlayerModel).Move(delta_time, event.keysym)
        if event.keysym == 'Down':
            self.model.get_model(PlayerModel).Move(delta_time, event.keysym)
        if event.keysym == 's':
            self.model.get_model(PlayerModel).Shoot()
        if event.keysym == 'Left':
            self.model.get_model(PlayerModel).TurnLeft(delta_time)
        if event.keysym == 'Right':
            self.model.get_model(PlayerModel).TurnRight(delta_time)
