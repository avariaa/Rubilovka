import tkinter as tk


CENTER_X, CENTER_Y = 450, 250

class AsteroidView:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas):
        self.root = root
        self.canvas = canvas

    def Start(self, number_of_asteroids):
        self.number_of_asteroids = number_of_asteroids
        self.asteroids = [self.CreateAsteroid(-300, -300) for i in range(number_of_asteroids)]
        for ast in self.asteroids:
            #self.canvas.pack(ast)
            pass

    def CreateAsteroid(self, x, y, radius=30):
        return self.canvas.create_oval(x + radius, y + radius,
                                       x - radius, y - radius,
                                       fill = '#50026E', outline='#000000')

    def ShowPos(self, asteroids_data):
        for i in range(self.number_of_asteroids):
            radius = asteroids_data[i].radius
            x = asteroids_data[i].position.x + CENTER_X
            y = asteroids_data[i].position.y + CENTER_Y
            ''' Раньше было вот так, а мы X и Y не меняли
            x = asteroids_data[i].x
            y = asteroids_data[i].y
            '''
            print(i, x, y)
            self.canvas.coords(self.asteroids[i], x + radius, y + radius,
                                            x - radius, y - radius)
