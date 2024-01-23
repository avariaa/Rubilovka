import random
import time
from Player.Position import *
from Utility import *
import Utility
seed_a = time.time()
print(seed_a)


class Asteroid:
    a = ['small', 'medium', 'big']

    def __str__(self):
        return f"{self.position.x} {self.position.y}"

    def __init__(self, speed=100,
                       x_start=-510,
                       y_start=-250, radius=0, damage=0):
        self.x_start = x_start
        self.y_start = y_start
        global seed_a
        random.seed(seed_a)
        self.size = self.a[random.randint(0, len(self.a)-1)]
        if self.size == self.a[0]:
            self.radius = radius + 10
            self.speed = speed
            self.damage = damage + 10
        elif self.size == self.a[1]:
            self.radius = radius + 25
            self.speed = speed + 20
            self.damage = damage + 15
        else:
            self.radius = radius + 40
            self.speed = speed + 40
            self.damage = damage + 25
        seed_a += 1000
        self.position = self.RandomPosition()
        print(self.size, self.position.y)


    def IsOutOfBounds(self):
        return self.position.x >= 110


    def RandomPosition(self):
        return Position(random.randint(self.x_start-WIDTH, self.x_start),
                        random.randint(self.y_start, -self.y_start))




    def ToStart(self):
        self.position = self.RandomPosition()
        self.position.x = self.x_start
        self.position.y = random.randint(self.y_start, -self.y_start)

    def CheckBounds(self):
        if self.IsOutOfBounds():
            self.ToStart()


    def Move(self, delta_time):
        print(self.position.x)
        self.position.x += self.speed * delta_time
        self.CheckBounds()
