from tkinter import *

from map import *


def game_start():
    draw("levels/level_1.txt", root, game_canvas)

root = Tk()
game_canvas = Canvas(width = 400, heigh = 400, bg = "black")
game_canvas.pack()

game_start()

mainloop()
