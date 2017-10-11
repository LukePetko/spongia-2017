from threading import *
import time

def bind_p1(game_canvas, level_map, player_one, player_two, box_side):
    global pressed
    for char in ["w", "s", "a", "d", "W", "S", "A", "D"]:
        game_canvas.bind("<KeyPress-%s>" % char, _pressed)
        game_canvas.bind("<KeyRelease-%s>" % char, _released)
        pressed[char] = False
    print(pressed)
    # game_canvas.bind_all("<Key>", lambda event, level_map = level_map, game_canvas = game_canvas, player_one = player_one, box_side = box_side, player_two = player_two: run(event, level_map, game_canvas, player_one, player_two, box_side))
    run(level_map, game_canvas, player_one, player_two, box_side, pressed)

def _pressed(event):
    global pressed
    print(event.keysym)
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


def run(level_map, game_canvas, player_one, player_two, box_side, pressed):
    global wait_bool_p1, wait_bool_p2, t
    game_canvas.tag_raise(player_one)
    game_canvas.tag_raise(player_two)
    # print(event.keysym)
    # print(wait_bool_p1, "- pred if-mi")
    if wait_bool_p1:
        if pressed["s"]:
            game_canvas.move(player_one, 0, 10)
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
            print(game_canvas.coords(player_one))
        if pressed["w"]:
            game_canvas.move(player_one, 0, -10)
            print(game_canvas.coords(player_one))
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
        if pressed["a"]:
            game_canvas.move(player_one, -10, 0)
            print(game_canvas.coords(player_one))
            wait_bool_p1 = False
            game_canvas.after(t, wait_p1)
        if pressed["d"]:
            game_canvas.move(player_one, 10, 0)
            print(game_canvas.coords(player_one))
            wait_bool_p1 = False
            print(wait_bool_p1, "- pri d")
            game_canvas.after(t, wait_p1)
    # if wait_bool_p2:
    #     if (event.keysym == "Down"):
    #         game_canvas.move(player_two, 0, 10)
    #         print(game_canvas.coords(player_two))
    #         wait_bool_p2 = False
    #         game_canvas.after(t, wait_p2)
    #     if (event.keysym == "Up"):
    #         game_canvas.move(player_two, 0, -10)
    #         print(game_canvas.coords(player_two))
    #         wait_bool_p2 = False
    #         game_canvas.after(t, wait_p2)
    #     if (event.keysym == "Left"):
    #         game_canvas.move(player_two, -10, 0)
    #         print(game_canvas.coords(player_two))
    #         wait_bool_p2 = False
    #         game_canvas.after(t, wait_p2)
    #     if (event.keysym == "Right"):
    #         game_canvas.move(player_two, 10, 0)
    #         print(game_canvas.coords(player_two))
    #         wait_bool_p2 = False
    #         game_canvas.after(t, wait_p2)
    game_canvas.after(10, lambda: run(level_map, game_canvas, player_one, player_two, box_side, pressed))
wait_bool_p1 = True
wait_bool_p2 = True
t = 100
pressed = {}
