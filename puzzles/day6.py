import re

def extract_data(input: list[str]):
    '''Extract and transform text data'''

    start_row = -1
    start_col = -1
    max_row = len(input)
    max_col = -1
    obstacles = {}
    direction = "^"

    for row in range(0, len(input)):
        line = input[row].strip()
        max_col = len(line)
        # find starting positions
        col = line.find("^")
        if col != -1:
            start_row = row
            start_col = col
            line = line.replace("^", ".")
            direction = "^"

        #find obstacle
        for i in re.finditer("#", line):
            obst_col = i.start()
            obstacles[point(row, obst_col)] = True


    # print(f"\n\nMaze: \n{maze}\nMax size: {max_row}, {max_col}\nStarting position: {start_row},{start_col}, dir: {dir}")
    # print(f"\nObstacles: {obstacles}")

    return start_row, start_col, max_row, max_col, obstacles, direction

def point(row, col):
    return f"{row},{col}"

def move(curr_row, curr_col, dir, obstacles, max_row, max_col):
    next_row = curr_row
    next_col = curr_col

    match dir:
        case "^":
            next_row -= 1
        case "v":
            next_row += 1
        case "<":
            next_col -= 1
        case ">":
            next_col += 1

    # out of maze
    if next_row < 0 or next_row >= max_row or next_col < 0 or next_col >= max_col:
        # print(f"Out of maze! {next_row}, {next_col}")
        return -1, -1, dir, True
    
    # still in maze
    next_point = point(next_row, next_col)
    # print(f"Next point: {next_point}")
    next_dir = dir

    # no obstacle, keep the direction
    if next_point not in obstacles:
        # print(f"- No obstacle found for {next_point}, continue")
        return next_row, next_col, next_dir, False
    else:
        # change direction
        match dir:
            case "^":
                next_dir = ">"
            case "v":
                next_dir = "<"
            case "<":
                next_dir = "^"            
            case ">":
                next_dir = "v"

        # revoke latest move to stay in place
        next_row = curr_row
        next_col = curr_col

        # print(f"# Obstacle found for {next_point}, change direction from {dir} to {next_dir}, stay at {next_row},{next_col}")

    return next_row, next_col, next_dir, False


def execute_part_one(input: list[str]) -> None:
    start_row, start_col, max_row, max_col, obstacles, direction = extract_data(input)

    visited = {}
    visited[point(start_row, start_col)] = True

    next_row, next_col, next_dir, stop = move(start_row, start_col, direction, obstacles, max_row, max_col)

    while not stop:
        visited[point(next_row, next_col)] = True
        next_row, next_col, next_dir, stop = move(next_row, next_col, next_dir, obstacles, max_row, max_col)

    # print(f"\nVisited: {visited}, count: {len(visited)}")

    print(f"Solved 1: {len(visited)}")


def execute_part_two(input: list[str]) -> None:
    start_row, start_col, max_row, max_col, obstacles, direction = extract_data(input)

    visited = {}
    visited[point(start_row, start_col)] = True

    next_row, next_col, next_dir, stop = move(start_row, start_col, direction, obstacles, max_row, max_col)

    while not stop:
        visited[point(next_row, next_col)] = True
        next_row, next_col, next_dir, stop = move(next_row, next_col, next_dir, obstacles, max_row, max_col)

    # print(f"\nVisited: {visited}, count: {len(visited)}")

    print(f"Solved 2: {len(visited)}")
