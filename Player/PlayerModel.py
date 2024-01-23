from math import *
from Player.Position import *

HEIGHT = 500
WIDTH = 500


class PlayerModel:
    def __init__(self, angle=pi, x=0, y=0, speed=100, hit_point=50, speed_turning=0.5, radius=25, y_bound=250):
        self.radius = radius
        self.angle = angle
        self.position = Position(x, y)
        self.y_bound = y_bound
        self.speed = speed
        self.hit_point = hit_point
        self.speed_turning = speed_turning

    def Shoot(self):
        print('Пиу пиу пиу')

    def Turn(self, delta_time, direction_of_rotation: str):
        if direction_of_rotation.lower() == 'right':
            self.angle = self.angle + self.speed_turning * delta_time
        elif direction_of_rotation.lower() == 'left':
            self.angle = self.angle - self.speed_turning * delta_time

    def TurnRight(self, delta_time):
        self.Turn(delta_time, 'right')

    def TurnLeft(self, delta_time):
        self.Turn(delta_time, 'left')

    def Move(self, delta_time, direction):
        if direction == 'Up':
            self.position.y -= self.speed * delta_time
        if direction == 'Down':
            self.position.y += self.speed * delta_time
        self.CheckBounds()


    def IsOutOfBoundTop(self):
        return self.position.y < -290


    def IsOutOfBoundBottom(self):
        return self.position.y > 290


    def ToBottom(self):
        self.position.y = self.y_bound + self.radius


    def ToTop(self):
        self.position.y = -(self.y_bound + self.radius)


    def CheckBounds(self):
        if self.IsOutOfBoundTop():
            self.ToBottom()
        elif self.IsOutOfBoundBottom():
            self.ToTop()


    def IsAlive(self):
        if self.hit_point <= 0:
            return False
        else:
            return True
