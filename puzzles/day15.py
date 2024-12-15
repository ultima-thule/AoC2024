def extract_data(input: list[str]):
    '''Extract and transform text data'''
    maze_walls = {}
    maze_boxes = {}
    robot_start = (-1, -1)
    robot_pos = {}
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
                    robot_pos[robot_start] = True

    max_row = row + 1

    plot_data(maze_walls, maze_boxes, robot_start, max_row, max_col)

    # print(f"Moves: {moves}")
    # print(f"Maze walls: {maze_walls}")
    # print(f"Maze boxes: {maze_boxes}")
    # print(f"Robot start: {robot_start}")
    # print(f"Max row, max col: {max_row},{max_col}")

    return maze_walls, maze_boxes, robot_pos, robot_start, moves, max_row, max_col

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

def get_next_pos(current_pos, move, max_row, max_col):
    dict_moves = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    v = dict_moves[move]
    row_move = current_pos[0] + v[0]
    col_move = current_pos[1] + v[1]

    return (row_move, col_move)

def move_all_boxes(move, pos, maze_walls, maze_boxes, robot_pos, max_row, max_col):
    return_pos = pos
    
    # move right
    if move == ">":
        last_box = (pos[0], pos[1])
        can_move = False
        # check how much boxes are to the right
        for i in range (pos[1], max_col):
            check = (pos[0], i)
            # print(f"Checking position {check}")
            if (check in maze_boxes and maze_boxes[check] == True):
                continue
            # found free space
            if check not in maze_walls:
                can_move = True
                last_box = check
                # print(f"Boxes from {pos} to {last_box}, can be moved? {can_move}")
                maze_boxes[pos] = False
                maze_boxes[last_box] = True
                return_pos = pos
                break
            else:
                return_pos = (pos[0], pos[1]-1)
                can_move = False
                break

    # move left
    if move == "<":
        last_box = (pos[0], pos[1])
        can_move = False
        # check how much boxes are to the left
        for i in range (pos[1], -1, -1):
            check = (pos[0], i)
            # print(f"Checking position {check}")
            if (check in maze_boxes and maze_boxes[check] == True):
                # print(f"Check{check} is a box")
                continue
            # found free space
            if check not in maze_walls:
                # print(f"Check{check} is not a wall")
                can_move = True
                last_box = check
                # print(f"Boxes from {pos} to {last_box}, can be moved? {can_move}")
                maze_boxes[pos] = False
                maze_boxes[last_box] = True
                return_pos = pos
                break
            else:
                # print(f"Check{check} is a wall")
                return_pos = (pos[0], pos[1]+1)
                can_move = False
                break
    
    # move top
    if move == "^":
        last_box = (pos[0], pos[1])
        can_move = False
        # check how much boxes are to the top
        for i in range (pos[0], -1, -1):
            check = (i, pos[1])
            # print(f"Checking position {check}")
            if (check in maze_boxes and maze_boxes[check] == True):
                continue
            # found free space
            if check not in maze_walls:
                can_move = True
                last_box = check
                # print(f"Boxes from {pos} to {last_box}, can be moved? {can_move}")
                maze_boxes[pos] = False
                maze_boxes[last_box] = True
                return_pos = pos
                break
            else:
                return_pos = (pos[0]+1, pos[1])
                can_move = False
                break

    # move down
    if move == "v":
        last_box = (pos[0], pos[1])
        can_move = False
        # check how much boxes are to the bottom
        for i in range (pos[0], max_row):
            check = (i, pos[1])
            # print(f"Checking position {check}")
            if (check in maze_boxes and maze_boxes[check] == True):
                continue
            # found free space
            if check not in maze_walls:
                can_move = True
                last_box = check
                # print(f"Boxes from {pos} to {last_box}, can be moved? {can_move}")
                maze_boxes[pos] = False
                maze_boxes[last_box] = True
                return_pos = pos
                break
            else:
                return_pos = (pos[0]-1, pos[1])
                can_move = False
                break

    return return_pos

            

def move_robot(maze_walls, maze_boxes, robot_pos, robot_start, moves, max_row, max_col):
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
            ret_pos = move_all_boxes(m, p, maze_walls, maze_boxes, robot_pos, max_row, max_col)
            pos_prev = pos_curr
            pos_curr = ret_pos
            # print(f"Returned pos: {ret_pos}")
            # plot_data(maze_walls, maze_boxes, pos_curr, max_row, max_col)

def calculate_distance(maze_boxes):
    distance = 0
    for k, v in maze_boxes.items():
        if v:
            # print(f"Key {k} value {v} GPS: {100*k[0] + k[1]}")
            distance += (100*k[0]) + k[1]
    return distance

def execute_part_one(input: list[str]) -> None:
    count = 0

    maze_walls, maze_boxes, robot_pos, robot_start, moves, max_row, max_col = extract_data(input)

    move_robot(maze_walls, maze_boxes, robot_pos, robot_start, moves, max_row, max_col)
    count = calculate_distance(maze_boxes)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    # maze_walls, maze_boxes, robot_pos, robot_start, moves, max_row, max_col = extract_data(input)

    print(f"Solved 2: {count}")
