import numpy as np

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    maze_walls = {}
    maze_nodes = {}
    maze_start = (-1, -1)
    maze_end = (-1, -1)
    max_row = len(input)
    max_col = -1

    for i in range(0, len(input)):
        line = input[i].strip()

        max_col = len(line)
        for j, e in enumerate(list(line)):
            if e == "#":
                maze_walls[(i, j)] = True
            elif e == "E":
                maze_end = (i, j)
            elif e == "S":
                maze_start = (i, j)
            else:
                maze_nodes[(i, j)] = True

    # plot_data(maze_walls, maze_start, maze_end, max_row, max_col)

    return maze_walls, maze_nodes, maze_start, maze_end, max_row, max_col

def plot_data(maze_walls, maze_start, maze_end, max_row, max_col):
    for x in range(0, max_row):
        for y in range(0, max_col):
            c = "."
            if (x, y) in maze_walls:
                c = "#"
            elif (x, y) == maze_start:
                c = "S"
            elif (x, y) == maze_end:
                c = "E"
            print(c, end="")
        print()

# def build_graph(maze_walls, maze_nodes, max_row, max_col):
#     for x in range(0, max_row):
#         for y in range(0, max_col):
#             c = "."
#             if (x, y) in maze_walls:s
#                 c = "#"
#             elif (x, y) == maze_start:
#                 c = "S"
#             elif (x, y) == maze_end:
#                 c = "E"
#             print(c, end="")


def find_all_paths(point, max_row, max_col, maze_walls, maze_end, visited, sum_up_to, result_set, result_key):
    sum_up_to += point[2]
    visited_key = f"{point[0]},{point[1]},{point[3]}"
    visited[visited_key] = True
    print(f"Visiting {point} sum {sum_up_to}")

    # reached end
    if (point[0], point[1]) == maze_end:
        # save ending point to the list
        print(f"Found end of maze with result: {sum_up_to}!")
        result_set[result_key].add(sum_up_to)
        return

    moves = get_possible_moves(point, maze_walls, max_row, max_col)
    # no further path found
    if len(moves) == 0:
        return
    # explore all possibilities
    for m in moves:
        # already visited this point with this direction
        # not visited yet
        m_key = f"{point[0]},{point[1]},{point[3]},{m[0]},{m[1]},{m[3]}"
        if m_key not in visited:
            find_all_paths(m, max_row, max_col, maze_walls, maze_end, visited, sum_up_to, result_set, result_key)

def is_valid_move(point, maze_walls, max_row, max_col):
    if point[0] >= 0 and point[0] < max_row and point[1] >= 0 and point[1] < max_col:
        return (point[0], point[1]) not in maze_walls
    return False

def get_possible_moves(point, maze_walls, max_row, max_col):
    possible_moves = []
    result = []
    direction = point[3]

    if direction == ">":
        possible_moves = [(-1, 0, 1000, "^"), (0, 1, 1, ">"), (1, 0, 1000, "v")]
    elif direction == "<":
        possible_moves = [(-1, 0, 1000, "^"), (0, -1, 1, "<"), (1, 0, 1000, "v")]
    elif direction == "^":
        possible_moves = [(0, -1, 1000, "<"), (-1, 0, 1, "^"), (0, 1, 1000, ">")]
    elif direction == "v":
        possible_moves = [(0, 1, 1000, ">"), (1, 0, 1, "v"), (0, -1, 1000, "<")]

    for p in possible_moves:
        m = (point[0] + p[0], point[1] + p[1], p[2], p[3])
        if is_valid_move(m, maze_walls, max_row, max_col):
            result.append(m)

    # print(f"All possible moves for {point} direction {direction}: {result}")

    return result

def get_node_cost(node):
    return node[2]

def init_nodes(maze_nodes, max_row, max_col):
    distances = {}
    for k, v in maze_nodes:
        distances[(k[0],k[1])] = np.inf
    return distances

def dijkstra():


def execute_part_one(input: list[str]) -> None:
    count = 0

    maze_walls, maze_nodes, maze_start, maze_end, max_row, max_col = extract_data(input)

    # get_possible_moves(maze_start, ">", maze_walls, max_row, max_col)
    # get_possible_moves(maze_start, "<", maze_walls, max_row, max_col)
    
    # start_point = (maze_start[0], maze_start[1], 0, ">")
    # print(f"Starting point: {start_point}")

    # set_key = f"{start_point[0]},{start_point[1]},{start_point[3]}"
    # set_results = {}
    # set_results[set_key] = set()
    # visited = {}

    # find_all_paths(start_point, max_row, max_col, maze_walls, maze_end, visited, 0, set_results, set_key)

    # print(f"Set results: {set_results}")

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    maze_walls, maze_nodes, maze_start, maze_end, max_row, max_col = extract_data(input)

    print(f"Solved 2: {count}")
