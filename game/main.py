from tkinter import *
from threading import *
from random import *
from PIL import Image, ImageTk
#from simpleaudio import *

class Shirt:
    pass

def bind_p1():
    global pressed, game_canvas, level_map, player_one, player_two, box_side
    for char in ["w", "s", "a", "d", "W", "S", "A", "D", "Down", "Up", "Left", "Right","f", "g", "k", "l"]:
        pressed[char] = False
        print(char, pressed[char])
    print(pressed)
    game_canvas.bind("<KeyPress>", _pressed)
    game_canvas.bind("<KeyRelease>", _released)

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

povolenie = 1
neviem = 0 # to iste ako shirt_count iba pre nove tricka
body_p1 = 0
v1_p1 = 0
v2_p1 = 0
v3_p1 = 0
body_p2 = 0
v1_p2 = 0
v2_p2 = 0
v3_p2 = 0
def movement():
    global wait_bool_p1, wait_bool_p2, t_1, t_2, level_map, game_canvas, player_one, player_two, box_side, pressed, povolenie, neviem, body_p1, v1_p1, v2_p1, v3_p1, body_p2, v1_p2, v2_p2, v3_p2
    game_canvas.tag_raise(player_one)
    game_canvas.tag_raise(player_two)
    # print(level_map[int(game_canvas.coords(player_one)[1]) // box_side][int(game_canvas.coords(player_one)[2]) // box_side])
    # print(int(game_canvas.coords(player_one)[2]) // box_side)
    # print(int(game_canvas.coords(player_one)[1]) // box_side)
    if wait_bool_p1:
        if pressed["s"] and level_map[int(game_canvas.coords(player_one)[3] + 4) // box_side][int(game_canvas.coords(player_one)[2]) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[3] + 4) // box_side][int(game_canvas.coords(player_one)[0]) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, 0, 4)
            wait_bool_p1 = False
            game_canvas.after(t_1, wait_p1)
            #print(game_canvas.coords(player_one))
            povolenie = 1
        if pressed["w"] and level_map[int(game_canvas.coords(player_one)[1] - 4) // box_side][int(game_canvas.coords(player_one)[2]) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[1] - 4) // box_side][int(game_canvas.coords(player_one)[0]) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, 0, -4)
            wait_bool_p1 = False
            # print(game_canvas.coords(player_one))
            game_canvas.after(t_1, wait_p1)
            povolenie = 1
        if pressed["a"] and level_map[int(game_canvas.coords(player_one)[1]) // box_side][int(game_canvas.coords(player_one)[0] - 4) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[3]) // box_side][int(game_canvas.coords(player_one)[0] - 4) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, -4, 0)
            wait_bool_p1 = False
            # print(game_canvas.coords(player_one))
            game_canvas.after(t_1, wait_p1)
            povolenie = 1
        if pressed["d"] and level_map[int(game_canvas.coords(player_one)[1]) // box_side][int(game_canvas.coords(player_one)[2] + 4) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[3]) // box_side][int(game_canvas.coords(player_one)[2] + 4) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, 4, 0)
            wait_bool_p1 = False
            # print(game_canvas.coords(player_one))
            game_canvas.after(t_1, wait_p1)
            povolenie = 1
        if pressed["f"]:
            for i in range(16):
                if shirt_positions[i].color == "pyimage3": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.2 #cervene tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[3])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[3])):
                        if v3_p1 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v3_p1 = 1 #oblecie si velkost 3
                            t_1 += 10
                            print(t_1)
                if shirt_positions[i].color == "pyimage2": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 # modre tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[3])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[3])):
                        if v2_p1 == 0 and v3_p1 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v2_p1 = 1 #oblecie si velkost 2
                            t_1 += 8
                            print(t_1)
                if shirt_positions[i].color == "pyimage1": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 0.8 #zlte tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[3])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[3])):
                        if v1_p1 == 0 and v2_p1 == 0 and v3_p1 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v1_p1 = 1 # oblecie si velkost 1
                            t_1 += 6
                            print(t_1)
            if level_map[int(game_canvas.coords(player_one)[0]) // box_side][int(game_canvas.coords(player_one)[3]) // box_side] == "3":
                body_p1+=(v1_p1 + v2_p1 + v3_p1)
                print("ulozene hrac 1   :)))")
                v1_p1 = 0
                v2_p1 = 0
                v3_p1 = 0
                print(t_1)
                t_1 = 12
        if pressed["g"]:
            print("body hrac 1 ----->", body_p1)
#===============================================================
#hrac 2====================================================================================================
#==============================================================
    if wait_bool_p2:
        if pressed["Down"] and level_map[int(game_canvas.coords(player_two)[3] + 4) // box_side][int(game_canvas.coords(player_two)[2]) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[3] + 4) // box_side][int(game_canvas.coords(player_two)[0]) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, 0, 4)
            # print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t_2, wait_p2)
            povolenie = 1
        if pressed["Up"] and level_map[int(game_canvas.coords(player_two)[1] - 4) // box_side][int(game_canvas.coords(player_two)[2]) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[1] - 4) // box_side][int(game_canvas.coords(player_two)[0]) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, 0, -4)
            # print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t_2, wait_p2)
            povolenie = 1
        if pressed["Left"] and level_map[int(game_canvas.coords(player_two)[1]) // box_side][int(game_canvas.coords(player_two)[0] - 4) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[3]) // box_side][int(game_canvas.coords(player_two)[0] - 4) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, -4, 0)
            # print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t_2, wait_p2)
            povolenie = 1
        if pressed["Right"] and level_map[int(game_canvas.coords(player_two)[1]) // box_side][int(game_canvas.coords(player_two)[2] + 4) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[3]) // box_side][int(game_canvas.coords(player_two)[2] + 4) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, 4, 0)
            # print(game_canvas.coords(player_two))
            wait_bool_p2 = False
            game_canvas.after(t_2, wait_p2)
            povolenie = 1
        if pressed["k"]:
            for i in range(16):
                if shirt_positions[i].color == "pyimage3": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.2 #cervene tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[3])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[3])):
                        if v3_p2 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v3_p2 = 1 #oblecie si velkost 3
                            t_2 += 10
                if shirt_positions[i].color == "pyimage2": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 # modre tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[3])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[3])):
                        if v2_p2 == 0 and v3_p2 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v2_p2 = 1 #oblecie si velkost 2
                            t_2 += 8
                if shirt_positions[i].color == "pyimage1": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 0.8 #zlte tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[3])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[2]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[2]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[3]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[3])):
                        if v1_p2 == 0 and v2_p2 == 0 and v3_p2 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v1_p2 = 1 # oblecie si velkost 1
                            t_2 += 6
            if level_map[int(game_canvas.coords(player_two)[2]) // box_side][int(game_canvas.coords(player_two)[1]) // box_side] == "2":
                body_p2+=(v1_p2 + v2_p2 + v3_p2)
                print("ulozene hrac 2 :)))")
                v1_p2 = 0
                v2_p2 = 0
                v3_p2 = 0
                t_2 = 12
        if pressed["l"]:
            print("body hrac 2 ----->", body_p2)

    game_canvas.after(10, movement)

wait_bool_p1 = True
wait_bool_p2 = True
t_1 = 12
t_2 = 12
pressed = {}
#==========================================================================================
def shirt_new():
    global box_side, root, level_map, game_start, shirt_yellow, shirt_list, povolenie, neviem
    if povolenie == 1: #toto je asi zatial zbytocne, chcel som aby si nemohol drzat "j" a zbierat tricka :((((
        #print(shirt_positions[neviem].id)
        #print('po spusteni shirt_new number ---> ', shirt_positions[neviem].number)
        game_canvas.delete(shirt_positions[neviem].id)
        x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        while level_map[y_sur // box_side][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or (level_map[y_sur // box_side][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]) or level_map[y_sur // box_side + 1][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or level_map[y_sur // box_side + 1][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]:
            x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
            y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)

        shirt_random = choice([shirt_yellow, shirt_blue, shirt_red])

        shirt_list[shirt_positions[neviem].number] = game_canvas.create_image(x_sur, y_sur, image = shirt_random, anchor = NW, tags = "shirts")

        game_canvas.tag_raise(shirt_list[neviem])

        shirt_positions[neviem].x_sur = x_sur
        shirt_positions[neviem].y_sur = y_sur
        shirt_positions[neviem].id = shirt_list[neviem]
        shirt_positions[neviem].number = neviem
        shirt_positions[neviem].color = str(shirt_random)

        #print(shirt_list)
        # print(shirt_list[shirt_count], x_sur, y_sur)
        game_canvas.tag_raise(shirt_list[shirt_count])
        level_map[y_sur // box_side][x_sur // box_side] = "t"
#=======================================================================================
def shirt_init():
    global box_side, root, level_map, game_start, shirt_yellow, shirt_list
    x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    while level_map[y_sur // box_side][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or (level_map[y_sur // box_side][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]) or level_map[y_sur // box_side + 1][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or level_map[y_sur // box_side + 1][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]:
        x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)

    shirt_random = choice([shirt_yellow, shirt_blue, shirt_red])

    shirt_list[shirt_count] = game_canvas.create_image(x_sur, y_sur, image = shirt_random, anchor = NW, tags = "shirts")

    game_canvas.tag_raise(shirt_list[shirt_count])

    shirt_positions[shirt_count].x_sur = x_sur
    shirt_positions[shirt_count].y_sur = y_sur
    shirt_positions[shirt_count].id = shirt_list[shirt_count]
    shirt_positions[shirt_count].number = shirt_count
    shirt_positions[shirt_count].color = str(shirt_random)

    print(shirt_positions[shirt_count].number)
    # print(shirt_list[shirt_count], x_sur, y_sur)
    game_canvas.tag_raise(shirt_list[shirt_count])
    level_map[y_sur // box_side][x_sur // box_side] = "t"


def draw(level, root):
    global game_canvas, box_side, level_map, shirt_yellow, shirt_red, shirt_blue, shirt_list, shirt_count, player_one, player_two
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
    game_canvas.focus_set()

    shirt_list = [0] * 16
    print(shirt_list)

    shirt_yellow_ = Image.open("../img/tricko_yellow.gif").resize((int(0.8 * box_side), int(0.8 * box_side)), Image.ANTIALIAS)
    shirt_blue_ = Image.open("../img/tricko_blue.gif").resize((int(1.0 * box_side), int(1.0 * box_side)), Image.ANTIALIAS)
    shirt_red_ = Image.open("../img/tricko_red.gif").resize((int(1.2 * box_side), int(1.2 * box_side)), Image.ANTIALIAS)

    shirt_yellow = ImageTk.PhotoImage(shirt_yellow_)
    shirt_blue = ImageTk.PhotoImage(shirt_blue_)
    shirt_red = ImageTk.PhotoImage(shirt_red_)

    # shirt_yellow = PhotoImage(file = "../img/tricko_yellow.gif")
    # shirt_blue = PhotoImage(file = "../img/tricko_blue.gif")
    # shirt_red = PhotoImage(file = "../img/tricko_red.gif")

    print(game_canvas.coords(player_one))
    for shirt_count in range(16):
        print("kreslim")
        shirt_init()
        print(shirt_positions[shirt_count].id)
        print(shirt_list)
def game_start():
    draw("levels/level_1.txt", root)

root = Tk()
full_width, full_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (full_width, full_height))
# root.wm_attributes('-fullscreen', 1)

game_canvas = Canvas(width = full_height, heigh = full_height, bg = "black")
game_canvas.pack()

shirt_positions = list()

for i in range(16):
    shirt_positions.append(Shirt())

game_start()

mainloop()
