def extract_data(input: list[str]):
    '''Extract and transform text data'''
    maze_walls = {}
    maze_boxes = {}
    robot_start = (-1, -1)
    moves = []
    read_moves = False
    max_row = -1
    max_col = -1

    row = -1

    for line in input:
        line = line.strip()
        # separator reached
        if line == "":
            read_moves = True        
            continue

        if read_moves:
            moves += list(line)
        else:
            row += 1
            max_col = len(line)
            for i, e in enumerate(list(line)):
                if e == "#":
                    maze_walls[(row, i)] = True
                elif e == "O":
                    maze_boxes[(row, i)] = True
                elif e == "@":
                    robot_start = (row, i)

    max_row = row + 1

    return maze_walls, maze_boxes, robot_start, moves, max_row, max_col

def extract_data_second(input: list[str]):
    '''Extract and transform text data'''
    maze_walls = {}
    maze_boxes_left = {}
    maze_boxes_right = {}
    robot_start = (-1, -1)
    moves = []
    read_moves = False
    max_row = -1
    max_col = -1

    row = -1

    for line in input:
        line = line.strip()
        # separator reached
        if line == "":
            read_moves = True        
            continue

        if read_moves:
            moves += list(line)
        else:
            row += 1
            max_col = 2*len(line)
            i = 0
            for c in list(line):
                if c == "#":
                    maze_walls[(row, i)] = True
                    maze_walls[(row, i + 1)] = True
                elif c == "O":
                    maze_boxes_left[(row, i)] = True
                    maze_boxes_right[(row, i + 1)] = True
                elif c == "@":
                    robot_start = (row, i)
                i += 2

    max_row = row + 1

    plot_data_second(maze_walls, maze_boxes_left, maze_boxes_right, robot_start, max_row, max_col)

    # print(f"Moves: {moves}")
    # print(f"Maze walls: {maze_walls}")
    # print(f"Maze boxes: {maze_boxes}")
    # print(f"Robot start: {robot_start}")
    # print(f"Max row, max col: {max_row},{max_col}")

    return maze_walls, maze_boxes_left, maze_boxes_right, robot_start, moves, max_row, max_col

def plot_data(maze_walls, maze_boxes, robot, max_row, max_col):
    for x in range(0, max_row):
        for y in range(0, max_col):
            c = "."
            if (x, y) in maze_walls:
                c = "#"
            elif (x, y) in maze_boxes and maze_boxes[(x, y)]:
                c = "O"
            elif (x, y) == robot:
                c = "@"
            print(c, end="")
        print()

def plot_data_second(maze_walls, maze_boxes_left, maze_boxes_right, robot, max_row, max_col):
    for x in range(0, max_row):
        for y in range(0, max_col):
            c = "."
            if (x, y) in maze_walls:
                c = "#"
            elif (x, y) in maze_boxes_left and maze_boxes_left[(x, y)]:
                c = "["
            elif (x, y) in maze_boxes_right and maze_boxes_right[(x, y)]:
                c = "]"
            elif (x, y) == robot:
                c = "@"
            print(c, end="")
        print()

def get_next_pos(current_pos, move, max_row, max_col):
    dict_moves = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    v = dict_moves[move]
    row_move = current_pos[0] + v[0]
    col_move = current_pos[1] + v[1]

    return (row_move, col_move)

def get_check(move, i, pos):
    if move == ">" or move == "<":
        return (pos[0], i)
    if move == "^" or move == "v":
        return (i, pos[1])

def move_all_boxes(move, pos, maze_walls, maze_boxes, max_row, max_col):
    ret_vectors = {">": (pos[0], pos[1] - 1), "<": (pos[0], pos[1] + 1), "^": (pos[0] + 1, pos[1]), "v": (pos[0] - 1, pos[1])}
    range_vectors = {">": (pos[1], max_col, 1), "<": (pos[1], -1, -1), "^": (pos[0], -1, -1), "v": (pos[0], max_row, 1)}

    return_pos = pos
    last_box = (pos[0], pos[1])

    ret_v = ret_vectors[move]
    rg_v = range_vectors[move]

    # check how much boxes are to the right
    for i in range (rg_v[0], rg_v[1], rg_v[2]):
        check = get_check(move, i, pos)
        # found next box
        if (check in maze_boxes and maze_boxes[check] == True):
            continue
        # found free space
        if check not in maze_walls:
            last_box = check
            maze_boxes[pos] = False
            maze_boxes[last_box] = True
            return_pos = pos
            break
        # found wall
        else:
            return_pos = (ret_v[0], ret_v[1])
            break

    return return_pos

def move_all_boxes_second(move, pos, maze_walls, maze_boxes_left, maze_boxes_right, max_row, max_col, is_left):
    ret_vectors = {">": (pos[0], pos[1] - 1), "<": (pos[0], pos[1] + 1), "^": (pos[0] + 1, pos[1]), "v": (pos[0] - 1, pos[1])}
    range_vectors = {">": (pos[1], max_col, 1), "<": (pos[1], -1, -1), "^": (pos[0], -1, -1), "v": (pos[0], max_row, 1)}

    return_pos = pos
    last_box = (pos[0], pos[1])

    ret_v = ret_vectors[move]
    rg_v = range_vectors[move]

    print(f"Moving boxes, position: {pos}")

    # check how much boxes are to the right
    for i in range (rg_v[0], rg_v[1], rg_v[2]):
        check = get_check(move, i, pos)
        # found next box
        if (check in maze_boxes_left and maze_boxes_left[check] == True) or (check in maze_boxes_right and maze_boxes_right[check] == True):
            continue
        # found free space
        if check not in maze_walls:
            last_box = check
            print(f"Last box: {last_box}")
            if move == ">":
                l = 1
                maze_boxes_left[(pos[0], pos[1])] = False
                for x in range(pos[1], last_box[1] + 1, 1):
                    maze_boxes_left[(pos[0], x)] = (l % 2 == 0)
                    maze_boxes_right[(pos[0], x)] = (l % 2 != 0)
                    l += 1
            elif move == "<":
                l = 1
                # print(f"Move from {pos[1] - 1} to {last_box[1]}")
                maze_boxes_right[(pos[0], pos[1])] = False
                for x in range(pos[1] - 1, last_box[1]-1, -1):
                    # print(f"Checking position {pos[0]},{x}")
                    maze_boxes_left[(pos[0], x)] = (l % 2 == 0)
                    maze_boxes_right[(pos[0], x)] = (l % 2 != 0)
                    l += 1
            elif move == "^":
                l = 1
                for x in range(pos[0], last_box[0] - 1, -1):
                    maze_boxes_left[(x, pos[1])] = (l % 2 != 0)
                    maze_boxes_right[(x, pos[1])] = (l % 2 == 0)
                    l += 1
            elif move == "v":
                l = 1
                for x in range(pos[0], last_box[0] + 1, 1):
                    maze_boxes_left[(x, pos[1])] = (l % 2 != 0)
                    maze_boxes_right[(x, pos[1])] = (l % 2 == 0)
                    l += 1
            return_pos = pos
            break
        # found wall
        else:
            return_pos = (ret_v[0], ret_v[1])
            break

    return return_pos
        
def move_robot(maze_walls, maze_boxes, robot_start, moves, max_row, max_col):
    pos_curr = robot_start
    pos_prev = robot_start

    for m in moves:
        # print(f"\nNext move: {m}")
        # calculate next position
        p = get_next_pos(pos_curr, m, max_row, max_col)
        
        # next move is into the wall, do nothing
        if p in maze_walls:
            # print(f"No move, wall hit")
            # plot_data(maze_walls, maze_boxes, pos_curr, max_row, max_col)
            continue

        # next move is in free space
        # save current pos as prev_pos
        # save calculated pos as current pos
        if p not in maze_boxes or maze_boxes[p] == False:
            # print(f"Move into empty space")
            pos_prev = pos_curr
            pos_curr = p
            # plot_data(maze_walls, maze_boxes, pos_curr, max_row, max_col)
            continue

        # next move is into a box
        if p in maze_boxes:
            # print(f"Move into box")
            ret_pos = move_all_boxes(m, p, maze_walls, maze_boxes, max_row, max_col)
            pos_prev = pos_curr
            pos_curr = ret_pos
            # print(f"Returned pos: {ret_pos}")
            # plot_data(maze_walls, maze_boxes, pos_curr, max_row, max_col)

def move_robot_second(maze_walls, maze_boxes_left, maze_boxes_right, robot_start, moves, max_row, max_col):
    pos_curr = robot_start
    pos_prev = robot_start

    for m in moves:
        print(f"\nNext move: {m}")
        # calculate next position
        p = get_next_pos(pos_curr, m, max_row, max_col)
        
        # next move is into the wall, do nothing
        if p in maze_walls:
            # print(f"No move, wall hit")
            plot_data_second(maze_walls, maze_boxes_left, maze_boxes_right, pos_curr, max_row, max_col)
            continue

        # next move is in free space
        # save current pos as prev_pos
        # save calculated pos as current pos
        if (p not in maze_boxes_left or maze_boxes_left[p] == False) and (p not in maze_boxes_right or maze_boxes_right[p] == False) :
            # print(f"Move into empty space")
            pos_prev = pos_curr
            pos_curr = p
            plot_data_second(maze_walls, maze_boxes_left, maze_boxes_right, pos_curr, max_row, max_col)
            continue

        # next move is into a box - left part
        if p in maze_boxes_left:
            # print(f"Move into box")
            ret_pos = move_all_boxes_second(m, p, maze_walls, maze_boxes_left, maze_boxes_right, max_row, max_col, True)
            pos_prev = pos_curr
            pos_curr = ret_pos
            # print(f"Returned pos: {ret_pos}")
            plot_data_second(maze_walls, maze_boxes_left, maze_boxes_right, pos_curr, max_row, max_col)

        # next move is into a box - right part
        if  p in maze_boxes_right:
            # print(f"Move into box")
            ret_pos = move_all_boxes_second(m, p, maze_walls, maze_boxes_left, maze_boxes_right, max_row, max_col, False)
            pos_prev = pos_curr
            pos_curr = ret_pos
            # print(f"Returned pos: {ret_pos}")
            plot_data_second(maze_walls, maze_boxes_left, maze_boxes_right, pos_curr, max_row, max_col)


def calculate_distance(maze_boxes):
    distance = 0
    for k, v in maze_boxes.items():
        if v:
            distance += (100*k[0]) + k[1]
    return distance

def execute_part_one(input: list[str]) -> None:
    count = 0

    maze_walls, maze_boxes, robot_start, moves, max_row, max_col = extract_data(input)

    move_robot(maze_walls, maze_boxes, robot_start, moves, max_row, max_col)
    count = calculate_distance(maze_boxes)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    maze_walls, maze_boxes_left, max_boxes_right, robot_start, moves, max_row, max_col = extract_data_second(input)

    move_robot_second(maze_walls, maze_boxes_left, max_boxes_right, robot_start, moves, max_row, max_col)

    print(f"Solved 2: {count}")
