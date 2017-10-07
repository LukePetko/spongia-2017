from random import *

def shirt(root, box_side, level_map, game_canvas):
    x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    while level_map[y_sur // box_side][x_sur // box_side] in ["0", "2", "3", "p1", "p2"] or (level_map[y_sur // box_side][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2"]) or level_map[y_sur // box_side + 1][x_sur // box_side] in ["0", "2", "3", "p1", "p2"] or level_map[y_sur // box_side + 1][x_sur // box_side + 1] in ["0", "2", "3", "p1", "p2"]:
        print(x_sur, y_sur)
        x_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
        y_sur = randint(2 * box_side, root.winfo_screenheight() - 2 * box_side)
    game_canvas.create_rectangle(x_sur, y_sur, x_sur + box_side, y_sur + box_side, fill = "yellow")
