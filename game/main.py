from tkinter import *

from map import *


def game_start():
    draw("levels/level_1.txt", root, game_canvas)

root = Tk()

full_width, full_height = root.winfo_screenwidth(), root.winfo_screenheight()
# root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (full_width, full_height))

game_canvas = Canvas(width = full_height, heigh = full_height, bg = "black")
game_canvas.pack()

game_start()

mainloop()
