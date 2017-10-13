from tkinter import *
from threading import *
from random import *

# from map import *
# from movement import *

def bind_p1():
    global pressed, game_canvas, level_map, player_one, player_two, box_side
    for char in ["w", "s", "a", "d", "W", "S", "A", "D", "Down", "Up", "Left", "Right"]:
        pressed[char] = False
        print(char, pressed[char])
    print(pressed)
    game_canvas.bind("<KeyPress>", _pressed)
    game_canvas.bind("<KeyRelease>", _released)

    # game_canvas.bind_all("<Key>", lambda event, level_map = level_map, game_canvas = game_canvas, player_one = player_one, box_side = box_side, player_two = player_two: movement(event, level_map, game_canvas, player_one, player_two, box_side))
    movement()

def _pressed(event):
    global pressed
    pressed[event.keysym] = True

def _released(event):
    global pressed
    pressed[event.keysym] = False

def wait(wait_bool_p1):
    wait_bool_p1 = True
    print(wait_bool, "- wait function")

def wait_p1():
    global wait_bool_p1
    wait_bool_p1 = True

def wait_p2():
    global wait_bool_p2
    wait_bool_p2 = True


def movement():
    global wait_bool_p1, wait_bool_p2, t, level_map, game_canvas, player_one, player_two, box_side, pressed
    game_canvas.tag_raise(player_one)
    game_canvas.tag_raise(player_two)

    if wait_bool_p1:
        if pressed["s"]:
            game_canvas.move(player_one, 0, 4)
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
            print(game_canvas.coords(player_one))
        if pressed["w"]:
            game_canvas.move(player_one, 0, -4)
            wait_bool_p1 = False
            # print(game_canvas.coords(player_one))
            game_canvas.after(t, wait_p1)
        if pressed["a"]:
            game_canvas.move(player_one, -4, 0)
            wait_bool_p1 = False
            # print(game_canvas.coords(player_one))
            game_canvas.after(t, wait_p1)
        if pressed["d"]:
            game_canvas.move(player_one, 4, 0)
            wait_bool_p1 = False
            # print(game_canvas.coords(player_one))
            # print(wait_bool_p1, "- pri d")
            game_canvas.after(t, wait_p1)

    if wait_bool_p2:
        if pressed["Down"]:
            game_canvas.move(player_two, 0, 4)
            print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
        if pressed["Up"]:
            game_canvas.move(player_two, 0, -4)
            print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
        if pressed["Left"]:
            game_canvas.move(player_two, -4, 0)
            print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
        if pressed["Right"]:
            game_canvas.move(player_two, 4, 0)
            print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
    game_canvas.after(10, movement)

wait_bool_p1 = True
wait_bool_p2 = True
t = 12
pressed = {}

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
    global game_canvas, box_side, level_map, shirt_yellow, shirt_list, shirt_count, player_one, player_two
    level_file = open(level)
    print(level_file)
    level_map = level_file.readlines()
    box_side = root.winfo_screenheight() // len(level_map[0].strip().split(" "))


    for y in range(len(level_map)):
        level_map[y] = level_map[y].strip().split(" ")
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
                player_one = game_canvas.create_rectangle(x * box_side + box_side // 10, y * box_side, (x + 1) * box_side - box_side // 10, (y + 1) * box_side, fill = "black", outline = "blue")
            elif level_map[y][x] == "p2":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "red", fill = "red")
                player_two = game_canvas.create_rectangle(x * box_side + box_side // 10, y * box_side, (x + 1) * box_side - box_side // 10, (y + 1) * box_side, fill = "black", outline = "red")

    bind_p1()
    print("bbbb")
    game_canvas.focus_set()
    # movement_p2 = movement_class_p2(player_two)

    shirt_list = [0] * 10
    print(shirt_list)

    shirt_yellow = PhotoImage(file = "../img/tricko_yellow.gif")
    # shirt_blue = PhotoImage(file = "../img/tricko_blue.gif")

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
