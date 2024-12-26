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

def find_shortest_path_bfs(walls, maze_start, maze_end, size_x, size_y):
    q = deque()
    q.append((maze_start[0], maze_start[1], maze_start[2], maze_start[3], 0))

    visited = set()

    distance = defaultdict(lambda: sys.maxsize)
    distance[(maze_start[0], maze_start[1], maze_start[3])] = 0

    scores = [[sys.maxsize]*size_y for i in range(size_x)]
    scores[maze_start[0]][maze_start[1]] = 0

    while q:
        x, y, cost, direct, length = q.popleft()

        # get all valid neighbours (within range)
        moves = get_possible_moves((x, y, cost, direct, length), walls, size_x, size_y, True)
        for n_x, n_y, n_c, n_d, n_l in moves:
            # check if visited from this direction
            if (n_x, n_y, n_d) not in visited:
                new_score = length + n_c
                if scores[n_x][n_y] > new_score:
                    scores[n_x][n_y] = new_score
                    q.append((n_x, n_y, n_c, n_d, new_score))

    return scores

def find_shortest_path_bfs_backtrack(walls, maze_start, maze_end, size_x, size_y, scores):
    q = deque()
    count = 1

    # two possible starting directions from end to start
    q.append((maze_end[0], maze_end[1], 0, "<", scores[maze_end[0]][maze_end[1]]))
    q.append((maze_end[0], maze_end[1], 0, "v", scores[maze_end[0]][maze_end[1]]))

    visited = set()

    while q:
        x, y, cost, direct, length = q.popleft()

        # get possible moves with SUBtracking cost
        moves = get_possible_moves((x, y, cost, direct, length), walls, size_x, size_y, False)
        for n_x, n_y, n_c, n_d, n_l in moves:
            new_score = length + n_c
            # check if was already visited and if score for the candidate is same or different by 1000
            if (n_x, n_y) not in visited and scores[n_x][n_y] in [new_score, new_score - 1000]:
                count += 1
                visited.add((n_x, n_y))
                q.append((n_x, n_y, n_c, n_d, new_score))
    
    return count

def is_valid_move(point, maze_walls, size_x, size_y):
    if point[0] >= 0 and point[0] < size_x and point[1] >= 0 and point[1] < size_y:
        return (point[0], point[1]) not in maze_walls
    return False

def get_possible_moves(point, maze_walls, size_x, size_y, add=True):
    possible_moves = []
    result = []
    direction = point[3]
    length = point[4]

    # add for BFS, subtract fro backwards BFS
    if direction == ">":
        possible_moves = [(0, 1, 1 if add else -1, ">", length), (-1, 0, 1 if add else -1, "^", length), (1, 0, 1 if add else -1, "v", length)]
    elif direction == "<":
        possible_moves = [(0, -1, 1 if add else -1, "<", length), (-1, 0, 1 if add else -1, "^", length), (1, 0, 1 if add else -1, "v", length)]
    elif direction == "^":
        possible_moves = [(-1, 0, 1 if add else -1, "^", length), (0, -1, 1 if add else -1, "<", length), (0, 1, 1 if add else -1, ">", length)]
    elif direction == "v":
        possible_moves = [(1, 0, 1 if add else -1, "v", length), (0, -1, 1 if add else -1, "<", length), (0, 1, 1 if add else -1, ">", length)]

    for p in possible_moves:
        m = (point[0] + p[0], point[1] + p[1], p[2], p[3], p[4])
        if is_valid_move(m, maze_walls, size_x, size_y):
            result.append(m)

    return result

def execute_part_one(input: list[str]) -> None:
    maze_walls, maze_nodes, maze_start, maze_end, size_x, size_y = extract_data(input)

    scores = []

    start_point = (maze_start[0], maze_start[1], 0, ">", 0)
    scores = find_shortest_path_bfs(maze_walls, start_point, maze_end, size_x, size_y)

    normal = scores[maze_end[0]][maze_end[1]]
    time_savings = defaultdict(int)

    for x, y in maze_walls:
        # do not simulate removing external walls
        if x != 0 and y != 0 and x != size_x - 1 and y != size_y - 1:
            temp_walls = maze_walls.copy()
            del temp_walls[(x, y)]
            temp_scores = find_shortest_path_bfs(temp_walls, start_point, maze_end, size_x, size_y)
            temp_result = temp_scores[maze_end[0]][maze_end[1]]
            # print(f"({x},{y}) => time is {temp_result} (saving {normal - temp_result})")
            time_savings[normal - temp_result] += 1

    print(time_savings)

    count = 0

    for k, v in time_savings.items():
        if k > 100:
            count += v

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    maze_walls, maze_nodes, maze_start, maze_end, size_x, size_y = extract_data(input)

    # start_point = (maze_start[0], maze_start[1], 0, ">", 0)
    # # find shortest path using BFS/dijkstra
    # scores = find_shortest_path_bfs(maze_walls, start_point, maze_end, size_x, size_y)
    # # backtrack from end to start
    # count = find_shortest_path_bfs_backtrack(maze_walls, start_point, maze_end, size_x, size_y, scores)

    # print(f"Solved 2: {count}")
