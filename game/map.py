from random import *
from tkinter import *

from movement import *
from shirt import *

def draw(level, root, game_canvas):
    level_file = open(level)
    level_map = level_file.readlines()

    box_side = root.winfo_screenheight() // len(level_map[0].strip().split(" "))

    # print(len(level_map))

    for y in range(len(level_map)):
        level_map[y] = level_map[y].strip().split(" ")
        # print(level_map[y], len(level_map[y]))
        for x in range(len(level_map[y])):
            if level_map[y][x] == "0":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, fill = "black")
            elif level_map[y][x] == "1":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "white", fill = "white")
            elif level_map[y][x] == "2":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "blue", fill = "blue")
            elif level_map[y][x] == "3":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "red", fill = "red")
            elif level_map[y][x] == "p1":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "blue", fill = "blue")
                # player_one = Label(root, height = box_side, width = int(0.8 * box_side), anchor = NW, fg = "black")
                # player_one.place(x = (x * box_side + box_side // 10),y = (y * box_side))
                player_one = game_canvas.create_rectangle(x * box_side + box_side // 10, y * box_side, (x + 1) * box_side - box_side // 10, (y + 1) * box_side, fill = "black")
            elif level_map[y][x] == "p2":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "red", fill = "red")
                player_two = game_canvas.create_rectangle(x * box_side + box_side // 10, y * box_side, (x + 1) * box_side - box_side // 10, (y + 1) * box_side, fill = "black")

    bind_p1(game_canvas, level_map, player_one, player_two, box_side)
    # movement_p2 = movement_class_p2(player_two)
    print(game_canvas.coords(player_one))
    for _ in range(10):
        shirt(root, box_side, level_map, game_canvas)
