from random import *
from tkinter import *

from movement import *
from shirt import *


def draw(level, root):
    global game_canvas
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

    shirt_list = [0] * 10
    print(shirt_list)

    shirt_yellow = PhotoImage(file = "../img/tricko_yellow.gif")
    shirt_yellow_2 = PhotoImage(file = "../img/tricko_yellow.gif")

    id_1 = game_canvas.create_image(100, 100, image = shirt_yellow, anchor = NW)
    id_2 = game_canvas.create_image(300, 300, image = shirt_yellow_2, anchor = NW)

    game_canvas.move(id_1, 10, 0)

    def shirt(p_box_side, p_root, p_level_map, p_game_canvas, p_shirt_yellow, p_shirt_list):
        x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        while level_map[y_sur // box_side][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or (level_map[y_sur // box_side][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]) or level_map[y_sur // box_side + 1][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or level_map[y_sur // box_side + 1][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]:
            x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
            y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        game_canvas.create_rectangle(x_sur, y_sur, x_sur + box_side, y_sur + box_side, fill = "yellow")
        p_shirt_list[shirt_count] = game_canvas.create_image(x_sur, y_sur, image = shirt_yellow, anchor = NW)

        print(shirt_list[shirt_count], x_sur, y_sur)
        game_canvas.tag_raise(shirt_list[shirt_count])
        level_map[y_sur // box_side][x_sur // box_side] = "t"


    print(game_canvas.coords(player_one))
    for shirt_count in range(10):
        print("kreslim")
        shirt(box_side, root)
