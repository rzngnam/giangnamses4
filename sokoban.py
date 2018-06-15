
map = {
    "size_x": 10,
    "size_y": 10
}
player = {
    "x": 4,
    "y": 4
}
boxes = [
    {"x": 7, "y": 2},
    {"x": 2, "y": 5},
    {"x": 6, "y": 3}
]
destination = [
    {"x": 2, "y": 8},
    {"x": 7, "y": 4},
    {"x": 1, "y": 3}
]
walls = [
    {"x": 3, "y": 5},
    {"x": 6, "y": 6},
    {"x": 6, "y": 5},
    {"x": 6, "y": 4},
    {"x": 5, "y": 2},
    {"x": 3, "y": 2},
    {"x": 4, "y": 2},
    {"x": 3, "y": 1},

]
recent_x = 0
recent_y = 0
recent_box_x = 0
recent_box_y = 0
box_old_pos_x = 0
box_old_pos_y = 0

by = 0
bx = 0
undo_limit = 1

while True:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            box_is_here = False
            player_is_here = False
            des_is_here = False
            wall_is_here = False

            for w in walls:
                if (x == w["x"]) and (y == w["y"]):
                    wall_is_here = True
                    break

            for box in boxes:
                if (x == box["x"]) and (y == box["y"]):
                    box_is_here = True
                    break

            for des in destination:
                if (x == des["x"]) and (y == des["y"]):
                    des_is_here = True
                    break

            if (x == player["x"]) and (y == player["y"]):
                player_is_here = True

            if player_is_here:
                print("P  ", end='')

            elif box_is_here:
                print("B  ", end='')
            elif des_is_here:
                print("D  ", end='')
            elif wall_is_here:
                print("W  ", end='')
            else:
                print("-  ", end='')
        print()

    win = True
    for box in boxes:
        if box not in destination:
            win = False

    if win:
        print("you win ")
        break
    dy = 0
    dx = 0
    while True:
        move = input(" move or undo: ").lower()
        if move == "w":
            dy = -1
            recent_y = -1
            recent_x = 0
            break
        elif move == "a":
            dx = -1
            recent_x = -1
            recent_y = 0
            break
        elif move == "s":
            dy = 1
            recent_y = 1
            recent_x = 0
            break
        elif move == "d":
            dx = 1
            recent_x = 1
            recent_y = 0
            break
        elif (move == "undo") and (undo_limit > 1):
            print("bạn đã undo 1 lần, không được undo nữa")
            recent_x = 0
            recent_y = 0
            recent_box_x = 0
            recent_box_y = 0
            break
        elif move == "undo":
            print("undo")
            undo_limit += 1
            break
        else:
            print("nhập thế đéo ai chơi được, nhập lại")
            break
    if (0 <= player['x'] + dx <= map['size_x']-1) and (0 <= player['y']+dy <= map["size_y"]-1):
        player['x'] += dx
        player['y'] += dy

    for wall in walls:
        if (player['x'] == wall['x']) and (player['y'] == wall['y']):
            player['x'] -= dx
            player['y'] -= dy
            break
    for box in boxes:
        if (player["x"] == box['x']) and (player["y"] == box["y"]) and \
                (0 <= box['x'] + dx <= map['size_x'] - 1) and (0 <= box['y'] + dy <= map["size_y"] - 1):
            bx = dx
            by = dy
            for box_x in boxes:
                for box_y in boxes:
                    if (box_x['x'] == box_y['x'] + dx) and (box_x['y'] == box_y['y'] + dy):
                        player['x'] -= dx
                        player['y'] -= dy
                        recent_y = 0
                        recent_x = 0
                        bx = 0
                        by = 0
            for wall in walls:
                if (wall['x'] - dx == box['x']) and (wall['y'] - dy == box['y']):
                    bx = 0
                    by = 0
                    player['x'] -= dx
                    player['y'] -= dy
                    recent_y = 0
                    recent_x = 0
            recent_box_x = bx
            recent_box_y = by
            box_old_pos_x = box['x']
            box_old_pos_y = box['y']
            box['x'] += bx
            box['y'] += by
    if move == "undo":
        for box in boxes:
            if (box['x'] - recent_box_x == box_old_pos_x) and (box['y'] - recent_box_y == box_old_pos_y):
                box['x'] = box_old_pos_x
                box['y'] = box_old_pos_y
                break
    if move == "undo":
        player['x'] -= recent_x
        player['y'] -= recent_y
