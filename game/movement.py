from threading import *

def bind_p1(game_canvas, level_map, player_one, box_side):
    movement_p1 = movement_class_p1()
    for i in ["w", "s", "a", "d", "W", "S", "A", "D"]:
        pass
    game_canvas.bind("<Key>", lambda: movement_p1.start())
    game_canvas.bind_all("<Key>", lambda event, level_map = level_map, game_canvas = game_canvas, player_one = player_one, box_side = box_side: run(event, level_map, game_canvas, player_one, box_side))


def bind_p2():
    for i in ["<Up>", "<Down>", "<Left>", "<Right>"]:
        game_canvas.bind(i, lambda: movement_p2.start())

class movement_class_p1(Thread):
    pass
def run(event, level_map, game_canvas, player_one, box_side):
    print("bežím")
    if (event.keysym == "S" or event.keysym == "s") and level_map[int(game_canvas.coords(player_one)[0] // box_side)][int(game_canvas.coords(player_one)[1] // box_side + 1)] != "0":
        game_canvas.move(player_one, 0, 1)
