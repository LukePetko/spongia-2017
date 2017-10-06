def draw(level, root, game_canvas):
    level_file = open(level)
    level_map = level_file.readlines()

    for y in range(len(level_map)):
        level_map[y] = level_map[y].strip()
        for x in range(len(level_map[y])):
            if level_map[y][x] == "0":
                game_canvas.create_rectangle(x * 40, y * 40, (x + 1) * 40, (y + 1) * 40, fill = "black")
            elif level_map[y][x] == "1":
                game_canvas.create_rectangle(x * 40, y * 40, (x + 1) * 40, (y + 1) * 40, outline = "white", fill = "white")
            elif level_map[y][x] == "2":
                game_canvas.create_rectangle(x * 40, y * 40, (x + 1) * 40, (y + 1) * 40, outline = "blue", fill = "blue")
            elif level_map[y][x] == "3":
                game_canvas.create_rectangle(x * 40, y * 40, (x + 1) * 40, (y + 1) * 40, outline = "red", fill = "red")
