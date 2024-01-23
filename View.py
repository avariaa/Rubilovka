import time
import tkinter as tk

class View:
    def __init__(self, views):
        self.views = views
        self.root = tk.Tk()
        self.canvas = tk.Canvas(height=500, width=500, background='#7CD0A0')
        self.canvas.pack()

    def get_view(self, view_class):
        return self.views[view_class]

    def OnKeyPressed(self, function):
        self.root.bind('<KeyPress>', function)

    def OnUpdate(self, update_function):
        self.update_function = update_function

    def Update(self, delta_time):
        self.update_function(delta_time)
        self.root.update()

    def Start(self):
        delta_time = 0.02
        while True:
            time.sleep(delta_time)
            self.Update(delta_time)