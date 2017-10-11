from tkinter import *
from threading import *
from random import *

# from map import *
from movement import *

def shirt():
    global box_side, root, level_map, game_start, shirt_yellow, shirt_list
    x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    while level_map[y_sur // box_side][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or (level_map[y_sur // box_side][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]) or level_map[y_sur // box_side + 1][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or level_map[y_sur // box_side + 1][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]:
        x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    shirt_list[shirt_count] = game_canvas.create_image(x_sur, y_sur, image = shirt_yellow, anchor = NW)

    print(shirt_list[shirt_count], x_sur, y_sur)
    game_canvas.tag_raise(shirt_list[shirt_count])
    level_map[y_sur // box_side][x_sur // box_side] = "t"


def draw(level, root):
    global game_canvas, box_side, level_map, shirt_yellow, shirt_list, shirt_count
    level_file = open(level)
    print(level_file)
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
    # shirt_blue = PhotoImage(file = "../img/tricko_blue.gif")

    id_1 = game_canvas.create_image(100, 100, image = shirt_yellow, anchor = NW)
    id_2 = game_canvas.create_image(300, 300, image = shirt_yellow_2, anchor = NW)

    game_canvas.move(id_1, 10, 0)

    print(game_canvas.coords(player_one))
    for shirt_count in range(10):
        print("kreslim")
        shirt()


def game_start():
    draw("levels/level_1.txt", root)

root = Tk()

full_width, full_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (full_width, full_height))
# root.wm_attributes('-fullscreen', 1)

game_canvas = Canvas(width = full_height, heigh = full_height, bg = "black")
game_canvas.pack()

game_start()

mainloop()
