import time
import tkinter as tk
from math import *
from View import *

class PlayerView:
    center_x, center_y = 450, 250

    def __init__(self, root: tk.Tk, canvas: tk.Canvas):
        self.root = root
        self.canvas = canvas
        self.h = 25
        self.player = self.CreatePlayer(self.center_x, self.center_y, pi)



    def CreatePlayer(self, x, y, angle):
        return self.canvas.create_polygon(x + self.h * cos(angle), y + self.h * sin(angle),
                                            x + 2 * self.h * cos(angle+2*pi/3), y + 2 * self.h * sin(angle+2*pi/3),
                                            x + 2 * self.h * cos(angle-2*pi/3), y + 2 * self.h * sin(angle-2*pi/3), fill = '#50026E', outline='#000000')

    def ShowPos(self, position, angle):
        x = position.x + self.center_x
        y = position.y + self.center_y
        pos = [x + self.h * cos(angle), y + self.h * sin(angle),
        x + 2 * self.h * cos(angle+2*pi/3), y + 2 * self.h * sin(angle+2*pi/3),
        x + 2 * self.h * cos(angle-2*pi/3), y + 2 * self.h * sin(angle-2*pi/3)]
        self.canvas.coords(self.player, *pos)
        '''self.canvas.coords(self.player, position.x - offset + 250, 250 - position.y - offset, position.x + offset + 250,
                           250 - position.y + offset)'''
        print(f'Игрок находится на x({position.x}) и y({position.y})')
