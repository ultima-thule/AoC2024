from collections import defaultdict, deque
from puzzles.lib.helpers import *
import sys

def extract_data(input: list[str]):
    data = []
    
    for i in range(0, len(input)):
        line = input[i].strip()
        tmp = line.split(",")
        data.append((int(tmp[1]), int(tmp[0]))) 

    return data

def is_valid(point, max_x, max_y, walls):
    if point[0] < 0 or point[0] > max_x:
        return False
    if point[1] < 0 or point[1] > max_y:
        return False
    return point not in walls

def get_neighbours(point, max_row, max_col, walls, visited):
    data = {}

    vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for v in vectors:
        new_point = (point[0] + v[0], point[1] + v[1])
        if is_valid (new_point, max_row, max_col, walls) and not visited[new_point[0]][new_point[1]]:
            data[new_point] = True

    # print(f"Neighbours: {data}")

    return data

def get_valid_neighbours(point, size_x, size_y, walls):
    data = {}

    vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for v in vectors:
        new_point = (point[0] + v[0], point[1] + v[1])
        if is_valid (new_point, size_x - 1, size_y - 1, walls):
            data[new_point] = True

    return data

def generate_walls(bytes, iterations):
    walls = {}
    for i in range(iterations):
        walls[bytes[i]] = True

    return walls

def find_shortest_path_dfs(walls, size_x, size_y, point_x, point_y, end_x, end_y, min_dist, dist, visited):
    # reached the end point, set minimum distance
    if end_x == point_x and end_y == point_y:
        min_dist = min(dist, min_dist)
        return min_dist

    # mark point as visited
    visited[point_x][point_y] = True

    # get all valid neighbours
    # neighbours = get_neighbours((point_x, point_y), size_x, size_y, walls, visited)

    if is_valid ((point_x + 1, point_y), size_x, size_y, walls) and (not visited[point_x + 1][point_y]):
        min_dist = find_shortest_path_dfs(walls, size_x, size_y, point_x + 1, point_y, end_x, end_y, min_dist, dist + 1, visited)
    if is_valid ((point_x - 1, point_y), size_x, size_y, walls) and (not visited[point_x - 1][point_y]):
        min_dist = find_shortest_path_dfs(walls, size_x, size_y, point_x - 1, point_y, end_x, end_y, min_dist, dist + 1, visited)
    if is_valid ((point_x, point_y + 1), size_x, size_y, walls) and (not visited[point_x][point_y + 1]):
        min_dist = find_shortest_path_dfs(walls, size_x, size_y, point_x, point_y + 1, end_x, end_y, min_dist, dist + 1, visited)
    if is_valid ((point_x, point_y - 1), size_x, size_y, walls) and (not visited[point_x][point_y - 1]):
        min_dist = find_shortest_path_dfs(walls, size_x, size_y, point_x, point_y - 1, end_x, end_y, min_dist, dist + 1, visited)

    visited[point_x][point_y] = False
    return min_dist

def find_shortest_path_bfs(walls, size_x, size_y):
    q = deque()
    q.append((0, 0, 0))

    visited = set()

    while q:
        x, y, length = q.popleft()
        
        # skip if already visited
        if (x, y) in visited:
            continue

        # mark point as visited
        visited.add((x, y))

        # reached the end point, return length
        if (x, y) == (size_x - 1, size_y - 1):
            return length

        # get all valid neighbours (within range)
        for n_x, n_y in get_valid_neighbours((x, y), size_x, size_y, walls):
            q.append((n_x, n_y, length + 1))
    
    return -1

def execute_part_one(input: list[str]) -> None:
    size_x = 71
    size_y = 71
    bytes_num = 1024

    data = extract_data(input)
    walls = generate_walls(data, bytes_num)
    # plot_grid(size_x, size_y, walls)

    # path_len = find_shortest_path_dfs(walls, size_x, size_y, 0, 0, size_x -1, size_y - 1, sys.maxsize, 0, visited)
    path_len = find_shortest_path_bfs(walls, size_x, size_y)

    print(f"Solved 1: {path_len}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    data = extract_data(input)

    print(f"Solved 2: {count}")
