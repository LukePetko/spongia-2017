from tkinter import *
from threading import *
from random import *
from PIL import Image, ImageTk
import simpleaudio

import sys

class Shirt:
    pass

class Music(Thread):
    def run(self):
        while not koniec_bool:
            wave_obj = simpleaudio.WaveObject.from_wave_file("sounds/hudba.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
        root.destroy()
        quit()

hudba = Music()

def koniec():
    global koniec_bool

    koniec_bool = True


def bind_p1():
    global pressed, game_canvas, level_map, player_one, player_two, box_side
    for char in ["w", "s", "a", "d", "W", "S", "A", "D", "Down", "Up", "Left", "Right","f", "k", "Escape"]:
        pressed[char] = False
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
v4_p1 = 0
body_p2 = 0
v1_p2 = 0
v2_p2 = 0
v3_p2 = 0
v4_p2 = 0
rychlost_p1 = 4
rychlost_p2 = 4

def movement():
    global wait_bool_p1, wait_bool_p2, t, level_map, game_canvas, player_one, player_two, box_side, pressed, povolenie, neviem, body_p1, v1_p1, v2_p1, v3_p1, v4_p1, body_p2, v1_p2, v2_p2, v3_p2, v4_p2, stop_bool, p2_skore_desiatky, p2_skore_jednotky, p1_skore_desiatky, p1_skore_jednotky, rychlost_p1, rychlost_p2
    game_canvas.tag_raise(player_one)
    game_canvas.tag_raise(player_two)
    if wait_bool_p1:
        if pressed["s"] and level_map[int(game_canvas.coords(player_one)[1] + 4 + 1.92 * box_side) // box_side][int(game_canvas.coords(player_one)[0] + box_side) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[1] + 1.92 * box_side + 4) // box_side][int(game_canvas.coords(player_one)[0]) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, 0, int(rychlost_p1))
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
            povolenie = 1
        if pressed["w"] and level_map[int(game_canvas.coords(player_one)[1] - 4) // box_side][int(game_canvas.coords(player_one)[0] + box_side) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[1] - 4) // box_side][int(game_canvas.coords(player_one)[0]) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, 0, -int(rychlost_p1))
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
            povolenie = 1
        if pressed["a"] and level_map[int(game_canvas.coords(player_one)[1]) // box_side][int(game_canvas.coords(player_one)[0] - 4) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[1] + 1.92 * box_side) // box_side][int(game_canvas.coords(player_one)[0] - 4) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[1] + 0.96 * box_side) // box_side][int(game_canvas.coords(player_one)[0] - 4) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, -int(rychlost_p1), 0)
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
            povolenie = 1
        if pressed["d"] and level_map[int(game_canvas.coords(player_one)[1]) // box_side][int(game_canvas.coords(player_one)[0] + box_side + 4) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[1] + 1.92 * box_side) // box_side][int(game_canvas.coords(player_one)[0] + box_side + 4) // box_side] in ["1", "2", "t", "p1"] and level_map[int(game_canvas.coords(player_one)[1] + 0.96 * box_side) // box_side][int(game_canvas.coords(player_one)[0] + box_side + 4) // box_side] in ["1", "2", "t", "p1"]:
            game_canvas.move(player_one, int(rychlost_p1), 0)
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
            povolenie = 1
        if pressed["f"]:
            for i in range(16):
                if shirt_positions[i].color == "pyimage9": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.4 #zlte tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 0.96 * box_side)):
                        if v4_p1 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v4_p1 = 1 # oblecie si velkost 4
                            game_canvas.itemconfig(player_one, image = p1_tricko4)
                if shirt_positions[i].color == "pyimage8": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.2 #cervene tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 0.96 * box_side)):
                        if v3_p1 == 0 and v4_p1 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v3_p1 = 1 #oblecie si velkost 3
                            game_canvas.itemconfig(player_one, image = p1_tricko3)
                if shirt_positions[i].color == "pyimage7": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 # modre tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 0.96 * box_side)):
                        if v2_p1 == 0 and v3_p1 == 0 and v4_p1 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v2_p1 = 1 #oblecie si velkost 2
                            game_canvas.itemconfig(player_one, image = p1_tricko2)
                if shirt_positions[i].color == "pyimage6": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 0.8 #zlte tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 0.96 * box_side)):
                        if v1_p1 == 0 and v2_p1 == 0 and v3_p1 == 0 and v4_p1 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v1_p1 = 1 # oblecie si velkost 1
                            game_canvas.itemconfig(player_one, image = p1_tricko1)

                if shirt_positions[i].color == "pyimage14": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 #tenisky
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 0.96 * box_side)):
                        if rychlost_p1 == 4:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            rychlost_p1 = 8 # oblecie si tenisky
                if shirt_positions[i].color == "pyimage15": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 #topanky

                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_one)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_one)[1] + 0.96 * box_side)):
                        if rychlost_p2 == 4 or rychlost_p2 == 8:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            rychlost_p2 = 2 # oblecie si velkost nohy


            if level_map[int(game_canvas.coords(player_one)[0]) // box_side][int(game_canvas.coords(player_one)[1] + 1.92 * box_side) // box_side] == "3":
                body_p1+=(v1_p1 + v2_p1 + v3_p1 + v4_p1)

                game_canvas.itemconfig(p1_skore_jednotky, image = cisla_skore[body_p1 % 10])
                game_canvas.itemconfig(p1_skore_desiatky, image = cisla_skore[body_p1 // 10])

                v1_p1 = 0
                v2_p1 = 0
                v3_p1 = 0
                v4_p1 = 0
                rychlost_p1 = 4
                game_canvas.itemconfig(player_one, image = character_1)
#===============================================================
#hrac 2====================================================================================================
#==============================================================
    if wait_bool_p2:
        if pressed["Down"] and level_map[int(game_canvas.coords(player_two)[1] + 1.92 * box_side + 4) // box_side][int(game_canvas.coords(player_two)[0] + box_side) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[1] + 1.92 * box_side + 4) // box_side][int(game_canvas.coords(player_two)[0]) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, 0, int(rychlost_p2))
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
            povolenie = 1
        if pressed["Up"] and level_map[int(game_canvas.coords(player_two)[1] - 4) // box_side][int(game_canvas.coords(player_two)[0] + box_side) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[1] - 4) // box_side][int(game_canvas.coords(player_two)[0]) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, 0, -int(rychlost_p2))
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
            povolenie = 1
        if pressed["Left"] and level_map[int(game_canvas.coords(player_two)[1]) // box_side][int(game_canvas.coords(player_two)[0] - 4) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[1] + 1.92 * box_side) // box_side][int(game_canvas.coords(player_two)[0] - 4) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[1] + 0.96 * box_side) // box_side][int(game_canvas.coords(player_two)[0] - 4) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, -int(rychlost_p2), 0)
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
            povolenie = 1
        if pressed["Right"] and level_map[int(game_canvas.coords(player_two)[1]) // box_side][int(game_canvas.coords(player_two)[0] + box_side + 4) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[1] + 1.92 * box_side) // box_side][int(game_canvas.coords(player_two)[0] + box_side + 4) // box_side] in ["1", "3", "t", "p2"] and level_map[int(game_canvas.coords(player_two)[1] + 0.96 * box_side) // box_side][int(game_canvas.coords(player_two)[0] + box_side + 4) // box_side] in ["1", "3", "t", "p2"]:
            game_canvas.move(player_two, int(rychlost_p2), 0)
            wait_bool_p2 = False
            game_canvas.after(t, wait_p2)
            povolenie = 1
        if pressed["k"]:
            for i in range(16):
                if shirt_positions[i].color == "pyimage9": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.4 #zlte tricko

                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 0.96 * box_side)):
                        if v4_p2 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v4_p2 = 1 # oblecie si velkost 4
                            game_canvas.itemconfig(player_two, image = p2_tricko4)
                if shirt_positions[i].color == "pyimage8": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.2 #cervene tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 0.96 * box_side)):
                        if v3_p2 == 0 and v4_p2 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v3_p2 = 1 #oblecie si velkost 3
                            game_canvas.itemconfig(player_two, image = p2_tricko3)
                if shirt_positions[i].color == "pyimage7": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 # modre tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 0.96 * box_side)):
                        if v2_p2 == 0 and v3_p2 == 0 and v4_p2 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v2_p2 = 1 #oblecie si velkost 2
                            game_canvas.itemconfig(player_two, image = p2_tricko2)
                if shirt_positions[i].color == "pyimage6": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 0.8 #zlte tricko
                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 0.96 * box_side)):
                        if v1_p2 == 0 and v2_p2 == 0 and v3_p2 == 0 and v4_p2 == 0:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            v1_p2 = 1 # oblecie si velkost 1
                            game_canvas.itemconfig(player_two, image = p2_tricko1)

                #======rychlost hraca=================================================================
                if shirt_positions[i].color == "pyimage14": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 #tenisky

                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 0.96 * box_side)):
                        if rychlost_p2 == 4:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            rychlost_p2 = 8 # oblecie si velkost nohy
                if shirt_positions[i].color == "pyimage15": #podla farby vyberie velkost okolo tricka ktoru pripocita..
                    velkost = 1.0 #topanky

                    if (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1]) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1])) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0]) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0]) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 1.92 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 1.92 * box_side)) or (shirt_positions[i].x_sur < int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].x_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[0] + 0.5 * box_side) and shirt_positions[i].y_sur < int(game_canvas.coords(player_two)[1] + 0.96 * box_side) and shirt_positions[i].y_sur + int(velkost * box_side) > int(game_canvas.coords(player_two)[1] + 0.96 * box_side)):
                        if rychlost_p1 == 4 or rychlost_p1 == 8:
                            neviem = i
                            shirt_new()
                            povolenie = 0
                            rychlost_p1 = 2 # oblecie si velkost nohy



            if level_map[int(game_canvas.coords(player_two)[0] + box_side) // box_side][int(game_canvas.coords(player_two)[1]) // box_side] == "2":
                body_p2+=(v1_p2 + v2_p2 + v3_p2 + v4_p2)

                game_canvas.itemconfig(p2_skore_jednotky, image = cisla_skore[body_p2 % 10])
                game_canvas.itemconfig(p2_skore_desiatky, image = cisla_skore[body_p2 // 10])

                v1_p2 = 0
                v2_p2 = 0
                v3_p2 = 0
                v4_p2 = 0
                rychlost_p2 = 4
                game_canvas.itemconfig(player_two, image = character_2)
    if pressed["Escape"]:
        quit()
    if not stop_bool:
        game_canvas.after(10, movement)

wait_bool_p1 = True
wait_bool_p2 = True
t = 12
pressed = {}
#==========================================================================================
def shirt_new():
    global box_side, full_height, root, level_map, game_start, shirt_yellow, shirt_list, povolenie, neviem, tenisky_, topanky_
    if povolenie == 1: #toto je asi zatial zbytocne, chcel som aby si nemohol drzat "j" a zbierat tricka :((((
        game_canvas.delete(shirt_positions[neviem].id)
        x_sur = randint(2 * box_side, full_height - 2 * box_side)
        y_sur = randint(2 * box_side, full_height - 2 * box_side)
        while level_map[y_sur // box_side][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or (level_map[y_sur // box_side][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]) or level_map[y_sur // box_side + 1][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or level_map[y_sur // box_side + 1][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]:
            x_sur = randint(2 * box_side, full_height - 2 * box_side)
            y_sur = randint(2 * box_side, full_height - 2 * box_side)

        shirt_random = choice([shirt_yellow, shirt_blue, shirt_red, shirt_white, tenisky_, topanky_])

        shirt_list[shirt_positions[neviem].number] = game_canvas.create_image(x_sur, y_sur, image = shirt_random, anchor = NW, tags = "shirts")

        game_canvas.tag_raise(shirt_list[neviem])

        shirt_positions[neviem].x_sur = x_sur
        shirt_positions[neviem].y_sur = y_sur
        shirt_positions[neviem].id = shirt_list[neviem]
        shirt_positions[neviem].number = neviem
        shirt_positions[neviem].color = str(shirt_random)

        game_canvas.tag_raise(shirt_list[shirt_count])
        level_map[y_sur // box_side][x_sur // box_side] = "t"
#=======================================================================================
def shirt_init():
    global box_side, root, level_map, game_start, shirt_yellow, shirt_list, tenisky_, topanky_
    x_sur = randint(2 * box_side, full_height - 2 * box_side)
    y_sur = randint(2 * box_side, full_height - 2 * box_side)
    while level_map[y_sur // box_side][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or (level_map[y_sur // box_side][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]) or level_map[y_sur // box_side + 1][x_sur // box_side] in ["0", "2", "3", "p1", "p2", "t"] or level_map[y_sur // box_side + 1][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2", "t"]:
        x_sur = randint(2 * box_side, full_height - 2 * box_side)
        y_sur = randint(2 * box_side, full_height - 2 * box_side)

    shirt_random = choice([shirt_yellow, shirt_blue, shirt_red, shirt_white, tenisky_, topanky_])

    shirt_list[shirt_count] = game_canvas.create_image(x_sur, y_sur, image = shirt_random, anchor = NW, tags = "shirts")

    game_canvas.tag_raise(shirt_list[shirt_count])

    shirt_positions[shirt_count].x_sur = x_sur
    shirt_positions[shirt_count].y_sur = y_sur
    shirt_positions[shirt_count].id = shirt_list[shirt_count]
    shirt_positions[shirt_count].number = shirt_count
    shirt_positions[shirt_count].color = str(shirt_random)

    game_canvas.tag_raise(shirt_list[shirt_count])
    level_map[y_sur // box_side][x_sur // box_side] = "t"


def draw(level, root):
    global game_canvas, full_height, box_side, level_map, shirt_yellow, shirt_red, shirt_blue, shirt_list, shirt_count, player_one, player_two, shirt_white, floor, character_1, character_2, p1_tricko1, p1_tricko2, p1_tricko3, p1_tricko4, p2_tricko1, p2_tricko2, p2_tricko3, p2_tricko4, p2_skore_desiatky, p2_skore_jednotky, p1_skore_desiatky, p1_skore_jednotky, cisla_skore, wall, vyhra_p1, vyhra_p2, remiza, tenisky_, topanky_
    level_file = open(level)
    level_map = level_file.readlines()
    box_side = full_height // len(level_map[0].strip().split(" "))


    shirt_yellow_ = Image.open("img/tricko_yellow.gif").resize((int(0.8 * box_side), int(0.8 * box_side)), Image.ANTIALIAS)
    shirt_blue_ = Image.open("img/tricko_blue.gif").resize((int(1.0 * box_side), int(1.0 * box_side)), Image.ANTIALIAS)
    shirt_red_ = Image.open("img/tricko_red.gif").resize((int(1.2 * box_side), int(1.2 * box_side)), Image.ANTIALIAS)
    shirt_white_ = Image.open("img/tricko_white.gif").resize((int(1.4 * box_side), int(1.4 * box_side)), Image.ANTIALIAS)
    floor_ = Image.open("img/podlaha.gif").resize((int(1 * box_side), int(1 * box_side)), Image.ANTIALIAS)
    wall_ = Image.open("img/stena.gif").resize((int(1 * box_side), int(1 * box_side)), Image.ANTIALIAS)
    character_1_ = Image.open("img/postava_1.gif").resize((int(1 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    character_2_ = Image.open("img/postava_2.gif").resize((int(1 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    shoes_ = Image.open("img/tenisky.gif").resize((int(1.0 * box_side), int(1.0 * box_side)), Image.ANTIALIAS)
    boots_ = Image.open("img/topanky.gif").resize((int(1.0 * box_side), int(1.0 * box_side)), Image.ANTIALIAS)

    p1_tricko1_ = Image.open("img/p1_tricka/p1_tricko1.gif").resize((int(1 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    p1_tricko2_ = Image.open("img/p1_tricka/p1_tricko2.gif").resize((int(1 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    p1_tricko3_ = Image.open("img/p1_tricka/p1_tricko3.gif").resize((int(1.2 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    p1_tricko4_ = Image.open("img/p1_tricka/p1_tricko4.gif").resize((int(1.4 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)

    p2_tricko1_ = Image.open("img/p2_tricka/p2_tricko1.gif").resize((int(1 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    p2_tricko2_ = Image.open("img/p2_tricka/p2_tricko2.gif").resize((int(1 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    p2_tricko3_ = Image.open("img/p2_tricka/p2_tricko3.gif").resize((int(1.2 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)
    p2_tricko4_ = Image.open("img/p2_tricka/p2_tricko4.gif").resize((int(1.4 * box_side), int(1.83 * box_side)), Image.ANTIALIAS)

    vyhra_p1_ = Image.open("img/hrac_1_vyhra.gif").resize((int(12 * box_side), int(2 * box_side)), Image.ANTIALIAS)
    vyhra_p2_ = Image.open("img/hrac_2_vyhra.gif").resize((int(12 * box_side), int(2 * box_side)), Image.ANTIALIAS)
    remiza_ = Image.open("img/remiza.gif").resize((int(12 * box_side), int(2 * box_side)), Image.ANTIALIAS)

    shirt_yellow = ImageTk.PhotoImage(shirt_yellow_)
    shirt_blue = ImageTk.PhotoImage(shirt_blue_)
    shirt_red = ImageTk.PhotoImage(shirt_red_)
    shirt_white = ImageTk.PhotoImage(shirt_white_)
    floor = ImageTk.PhotoImage(floor_)
    wall = ImageTk.PhotoImage(wall_)
    character_1 = ImageTk.PhotoImage(character_1_)
    character_2 = ImageTk.PhotoImage(character_2_)
    tenisky_ = ImageTk.PhotoImage(shoes_)
    topanky_ = ImageTk.PhotoImage(boots_)


    p1_tricko1 = ImageTk.PhotoImage(p1_tricko1_)
    p1_tricko2 = ImageTk.PhotoImage(p1_tricko2_)
    p1_tricko3 = ImageTk.PhotoImage(p1_tricko3_)
    p1_tricko4 = ImageTk.PhotoImage(p1_tricko4_)

    p2_tricko1 = ImageTk.PhotoImage(p2_tricko1_)
    p2_tricko2 = ImageTk.PhotoImage(p2_tricko2_)
    p2_tricko3 = ImageTk.PhotoImage(p2_tricko3_)
    p2_tricko4 = ImageTk.PhotoImage(p2_tricko4_)

    vyhra_p1 = ImageTk.PhotoImage(vyhra_p1_)
    vyhra_p2 = ImageTk.PhotoImage(vyhra_p2_)
    remiza = ImageTk.PhotoImage(remiza_)

    cisla_skore = [0] * 10
    cisla_skore_ = [0] * 10

    for i in range(10):
        cisla_skore_[i] = Image.open("img/cisla/cislo_{}.gif".format(i)).resize((int(2 * box_side - 10), int(2.4 * box_side - 12)), Image.ANTIALIAS)
        cisla_skore[i] = ImageTk.PhotoImage(cisla_skore_[i])


    for y in range(len(level_map)):
        level_map[y] = level_map[y].strip().split(" ")
        for x in range(len(level_map[y])):
            if level_map[y][x] == "0":
                game_canvas.create_image(x * box_side, y * box_side, image = wall, anchor = NW)
            elif level_map[y][x] == "1":
                game_canvas.create_image(x * box_side, y * box_side, image = floor, anchor = NW)
            elif level_map[y][x] == "2":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "blue", fill = "blue")
            elif level_map[y][x] == "3":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "red", fill = "red")
            elif level_map[y][x] == "p1":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "blue", fill = "blue")
                player_one = game_canvas.create_image(x * box_side, int(y * box_side + box_side / 4), image = character_1, anchor = NW)
            elif level_map[y][x] == "p2":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "red", fill = "red")
                player_two = game_canvas.create_image(x * box_side, int(y * box_side + box_side / 4), image = character_2, anchor = NW)

    p1_skore_desiatky = game_canvas.create_image(2 * box_side + 5, full_height - 4.8 * box_side, image = cisla_skore[0], anchor = NW)
    p1_skore_jednotky = game_canvas.create_image(4 * box_side + 5, full_height - 4.8 * box_side, image = cisla_skore[0], anchor = NW)

    p2_skore_desiatky = game_canvas.create_image(full_height - 6 * box_side + 5, 2.8 * box_side, image = cisla_skore[0], anchor = NW)
    p2_skore_jednotky = game_canvas.create_image(full_height - 4 * box_side + 5, 2.8 * box_side, image = cisla_skore[0], anchor = NW)

    bind_p1()
    game_canvas.focus_set()

    shirt_list = [0] * 16

    for shirt_count in range(16):
        shirt_init()

def timer_create():
    global game_canvas, full_height, minuty_t, sekundy_t, desiatky_t, dvojbodka_t, dvojbodka, cisla

    cisla_ = [0] * 10
    cisla = [0] * 10

    for i in range(10):
        cisla_[i] = Image.open("img/cisla/cislo_{}.gif".format(i)).resize((int(1 * box_side), int(1.2 * box_side)), Image.ANTIALIAS)
        cisla[i] = ImageTk.PhotoImage(cisla_[i])

    dvojbodka_ = Image.open("img/cisla/dvojbodka.gif").resize((int(0.24 * box_side), int(1.2 * box_side)), Image.ANTIALIAS)
    dvojbodka = ImageTk.PhotoImage(dvojbodka_)

    game_canvas.create_rectangle(full_height // 2 - 2 * box_side - 10, 0, full_height // 2 + 2 * box_side + 10, int(1.2 * box_side) + 10, fill = "white")

    minuty_t = game_canvas.create_image(full_height // 2 - 2 * box_side + 5, 5, image = cisla[minuty], anchor = NW)
    sekundy_t = game_canvas.create_image(full_height // 2 + 1 * box_side + 5, 5, image = cisla[sekundy % 10], anchor = NW)
    desiatky_t = game_canvas.create_image(full_height // 2, 5, image = cisla[sekundy // 10], anchor = NW)
    dvojbodka_t = game_canvas.create_image(full_height // 2 - 1 * box_side + 20, 5, image = dvojbodka, anchor = NW)

    game_canvas.tag_raise(minuty_t)
    timer()

def timer():
    global game_canvas, minuty, sekundy, stop_bool, minuty_t, sekundy_t, desiatky_t, dvojbodka_t, cisla
    if sekundy == 0 and minuty == 0:
        stop_bool = True
        if body_p1 > body_p2:
            game_canvas.create_image(full_height // 2, full_height // 2, image = vyhra_p1)
        elif body_p2 > body_p1:
            game_canvas.create_image(full_height // 2, full_height // 2, image = vyhra_p2)
        else:
            game_canvas.create_image(full_height // 2, full_height // 2, image = remiza)
        game_canvas.after(5000, koniec)
    if minuty == 0:
        game_canvas.itemconfig(minuty_t, image = cisla[minuty])
        game_canvas.itemconfig(sekundy_t, image = cisla[sekundy % 10])
        game_canvas.itemconfig(desiatky_t, image = cisla[sekundy // 10])

    if sekundy != 0:
        sekundy = sekundy - 1
    else:
        if minuty != 0:
            minuty = minuty - 1
            sekundy = sekundy + 59
    game_canvas.after(1000, timer)

def game_start():
    game_canvas.delete("all")
    draw("game/levels/level_3.txt", root)
    timer_create()

def menu_navigation(event):
    global new_game_selected, tutorial_bool, tutorial_screen
    if not tutorial_bool:
        if event.keysym == "Return":
            if new_game_selected:
                game_canvas.unbind_all("<Key>")
                game_start()
            elif not new_game_selected:
                tutorial_bool = True
                tutorial_screen = game_canvas.create_image(0, 0, image = tutorial, anchor = NW)
        if event.keysym == "Down":
            if new_game_selected:
                game_canvas.move(selector, 0, int(full_height / 8.8 + full_height / 17.6))
            new_game_selected = False
        if event.keysym == "Up":
            if not new_game_selected:
                game_canvas.move(selector, 0, - int(full_height / 8.8 + full_height / 17.6))
            new_game_selected = True
    else:
        if event.keysym == "Return":
            game_canvas.delete(tutorial_screen)
            tutorial_bool = False
def menu_start():
    global background, new_game_text, tutorial_text, new_game_selected, arrow, selector, tutorial_bool, tutorial

    new_game_selected = True
    tutorial_bool = False

    background_ = Image.open("img/background.gif").resize((full_height, full_height), Image.ANTIALIAS)
    background = ImageTk.PhotoImage(background_)

    new_game_text_ = Image.open("img/new_game.gif").resize((int(full_height / 2.2), int(full_height / 8.8)), Image.ANTIALIAS)
    new_game_text = ImageTk.PhotoImage(new_game_text_)

    tutorial_text_ = Image.open("img/tutorial.gif").resize((int(full_height / 2.2), int(full_height / 8.8)), Image.ANTIALIAS)
    tutorial_text = ImageTk.PhotoImage(tutorial_text_)

    arrow_ = Image.open("img/arrow.gif").resize((int(full_height / 8.8), int(full_height / 8.8)), Image.ANTIALIAS)
    arrow = ImageTk.PhotoImage(arrow_)

    tutorial_ = Image.open("img/tutorial_screen.gif").resize((int(full_height), int(full_height)), Image.ANTIALIAS)
    tutorial = ImageTk.PhotoImage(tutorial_)

    game_canvas.create_image(0, 0, image = background, anchor = NW)
    game_canvas.create_image(full_height - int(full_height / 21.6) - int(full_height / 2.2), int(5 / 18 * full_height + full_height / 17.6), image = new_game_text, anchor = NW)
    game_canvas.create_image(full_height - int(full_height / 21.6) - int(full_height / 2.2), int(5 / 18 * full_height + full_height / 4.4), image = tutorial_text, anchor = NW)
    selector = game_canvas.create_image(full_height - int(full_height / 21.6) - int(full_height / 2.2) - int(full_height / 8.8) - 10, int(5 / 18 * full_height + full_height / 17.6), image = arrow, anchor = NW)
    game_canvas.bind_all("<Key>", menu_navigation)


root = Tk()
full_height = root.winfo_screenheight() - 100
root.geometry("%dx%d+0-100" % (full_height, full_height))

game_canvas = Canvas(width = full_height, height = full_height, bg = "white")
game_canvas.pack()

cas = 60
minuty = cas // 60
sekundy = cas % 60
stop_bool = False
koniec_bool = False

shirt_positions = list()

for i in range(16):
    shirt_positions.append(Shirt())

hudba.start()

menu_start()

mainloop()
