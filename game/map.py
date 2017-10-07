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
                player_one = game_canvas.create_rectangle(x * box_side + box_side // 10, y * box_side, (x + 1) * box_side - box_side // 10, (y + 1) * box_side, fill = "black")
            elif level_map[y][x] == "p2":
                game_canvas.create_rectangle(x * box_side, y * box_side, (x + 1) * box_side, (y + 1) * box_side, outline = "red", fill = "red")
                player_two = game_canvas.create_rectangle(x * box_side + box_side // 10, y * box_side, (x + 1) * box_side - box_side // 10, (y + 1) * box_side, fill = "black")
