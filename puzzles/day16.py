import numpy as np
from collections import deque, defaultdict
import sys

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    maze_walls = {}
    maze_nodes = {}
    maze_start = (-1, -1)
    maze_end = (-1, -1)
    size_x = len(input)
    size_y = -1

    for i in range(0, len(input)):
        line = input[i].strip()

        size_y = len(line)
        for j, e in enumerate(list(line)):
            if e == "#":
                maze_walls[(i, j)] = True
            elif e == "E":
                maze_end = (i, j)
            elif e == "S":
                maze_start = (i, j)
            else:
                maze_nodes[(i, j)] = True

    # plot_data(maze_walls, maze_start, maze_end, size_x, size_y)

    # print(f"{size_x} {size_y}")

    return maze_walls, maze_nodes, maze_start, maze_end, size_x, size_y

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

def is_valid(point, max_x, max_y, walls):
    if point[0] < 0 or point[0] > max_x:
        return False
    if point[1] < 0 or point[1] > max_y:
        return False
    return point not in walls

def get_valid_neighbours(point, size_x, size_y, walls):
    data = {}

    vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for v in vectors:
        new_point = (point[0] + v[0], point[1] + v[1])
        if is_valid (new_point, size_x - 1, size_y - 1, walls):
            data[new_point] = True

    return data

def find_shortest_path_bfs(walls, maze_start, maze_end, size_x, size_y, results):
    q = deque()
    q.append((maze_start[0], maze_start[1], maze_start[2], maze_start[3], 0, []))

    visited = set()

    distance = defaultdict(lambda: sys.maxsize)
    distance[(maze_start[0], maze_start[1], maze_start[3])] = 0

    scores = [[sys.maxsize]*size_y for i in range(size_x)]
    scores[maze_start[0]][maze_start[1]] = 0

    while q:
        x, y, cost, direct, length, prev = q.popleft()
        # print(f"Checking {x},{y} with dir {direct}")
        
        # skip if already visited
        # if (x, y, direct) in visited:
        #     # print(f"  -> already visited")
        #     continue


        # # reached the end point, return length
        # if (x, y) == (maze_end[0], maze_end[1]):
        #     # return length
        #     # print(f"Path found with len {length} => \n{prev} ")
        #     results.append((length, prev))
        #     continue
        
        # mark point as visited
        # visited.add((x, y, direct))

        # get all valid neighbours (within range)
        # moves = get_possible_moves(point, walls, size_x, size_y)
        moves = get_possible_moves((x, y, cost, direct, length), walls, size_x, size_y)
        # print(f"  - checking moves {moves}")
        for n_x, n_y, n_c, n_d, n_l in moves:
            if (n_x, n_y, n_d) not in visited:
                # if (x, y) == (maze_start[0], maze_start[1]):
                #     cost = 1
                prev_nodes = prev.copy()
                prev_nodes.append((n_x, n_y, n_d))
                new_score = length + n_c
                if scores[n_x][n_y] > new_score:
                    scores[n_x][n_y] = new_score
                    q.append((n_x, n_y, n_c, n_d, new_score, prev_nodes))
    
    print(f"Distance: {scores[maze_end[0]][maze_end[1]]}")

    # return -1
    return scores[maze_end[0]][maze_end[1]]

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

def is_valid_move(point, maze_walls, size_x, size_y):
    if point[0] >= 0 and point[0] < size_x and point[1] >= 0 and point[1] < size_y:
        return (point[0], point[1]) not in maze_walls
    return False

def get_possible_moves(point, maze_walls, size_x, size_y):
    possible_moves = []
    result = []
    direction = point[3]
    length = point[4]

    if direction == ">":
        possible_moves = [(0, 1, 1, ">", length), (-1, 0, 1001, "^", length), (1, 0, 1001, "v", length)]
    elif direction == "<":
        possible_moves = [(0, -1, 1, "<", length), (-1, 0, 1001, "^", length), (1, 0, 1001, "v", length)]
    elif direction == "^":
        possible_moves = [(-1, 0, 1, "^", length), (0, -1, 1001, "<", length), (0, 1, 1001, ">", length)]
    elif direction == "v":
        possible_moves = [(1, 0, 1, "v", length), (0, -1, 1001, "<", length), (0, 1, 1001, ">", length)]

    for p in possible_moves:
        m = (point[0] + p[0], point[1] + p[1], p[2], p[3], p[4])
        if is_valid_move(m, maze_walls, size_x, size_y):
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


def execute_part_one(input: list[str]) -> None:
    count = 0

    maze_walls, maze_nodes, maze_start, maze_end, size_x, size_y = extract_data(input)

    results = []

    start_point = (maze_start[0], maze_start[1], 0, ">", 0)
    score = find_shortest_path_bfs(maze_walls, start_point, maze_end, size_x, size_y, results)
    # print(f"Results >: \n{results}")

    # minim = sys.maxsize

    # for length, path in results:
    #     print(f"Len found: {length}")
    #     minim = min(minim, length)

    # print(f"Len: {path_len}")

    # print(f"Starting point: {start_point}")

    # set_key = f"{start_point[0]},{start_point[1]},{start_point[3]}"
    # set_results = {}
    # set_results[set_key] = set()
    # visited = {}

    # find_all_paths(start_point, max_row, max_col, maze_walls, maze_end, visited, 0, set_results, set_key)

    # print(f"Set results: {set_results}")

    print(f"Solved 1: {score}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    maze_walls, maze_nodes, maze_start, maze_end, max_row, max_col = extract_data(input)

    print(f"Solved 2: {count}")
