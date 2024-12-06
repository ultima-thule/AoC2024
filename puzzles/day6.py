import re
import sys

def extract_data(input: list[str], start_dir: str):
    '''Extract and transform text data. Map obstacles to dictionary, find starting point and maze boundaries.'''

    start_row, start_col, max_col = -1, -1, -1
    max_row = len(input)
    obstacles = {}

    for row in range(0, len(input)):
        line = input[row].strip()
        max_col = len(line)
        col = line.find(start_dir)

        # starting position found
        if col != -1:
            start_row, start_col = row, col
            line = line.replace(start_dir, ".")

        # obstacle found
        for i in re.finditer("#", line):
            obst_col = i.start()
            obstacles[point(row, obst_col)] = True

    return start_row, start_col, max_row, max_col, obstacles, start_dir

def point(row, col):
    return f"{row},{col}"

def point_with_dir(row, col, direction):
    return f"{point(row, col)},{direction}"

def move(curr_row, curr_col, dir, obstacles, max_row, max_col):
    '''Execute one step in given direction'''
    next_row, next_col = curr_row, curr_col

    # calculate new position
    vectors = {"^": [-1, 0], "v": [1, 0], "<": [0, -1], ">": [0, 1]}
    next_row += vectors[dir][0]
    next_col += vectors[dir][1]

    # out of maze
    if next_row < 0 or next_row >= max_row or next_col < 0 or next_col >= max_col:
        return -1, -1, dir, True
    
    # still in maze
    next_point = point(next_row, next_col)
    next_dir = dir

    # obstacle found, change the direction
    if next_point in obstacles:
        # change direction
        dir_changes = {"^": ">", "v": "<", "<": "^", ">": "v"}
        next_dir = dir_changes[dir]

        # revoke latest move to stay in place
        next_row, next_col = curr_row, curr_col

    return next_row, next_col, next_dir, False


def execute_part_one(input: list[str]) -> None:
    start_row, start_col, max_row, max_col, obstacles, direction = extract_data(input, "^")

    visited = {}
    # mark starting point as visited
    visited[point(start_row, start_col)] = True

    # do first move
    next_row, next_col, next_dir, stop = move(start_row, start_col, direction, obstacles, max_row, max_col)
    # if not out of maze
    while not stop:
        # mark point as visited
        visited[point(next_row, next_col)] = True
        # do next move
        next_row, next_col, next_dir, stop = move(next_row, next_col, next_dir, obstacles, max_row, max_col)

    print(f"Solved 1: {len(visited)}")


def execute_part_two(input: list[str]) -> None:
    start_row, start_col, max_row, max_col, obstacles, direction = extract_data(input, "^")

    count = 0

    # brute force all scenarios :) 
    for i in range (0, max_row):
        for j in range (0, max_col):
            sys.stdout.write("\rScenario {} of {}".format(i * max_row + j+1, max_row * max_col))
            sys.stdout.flush()

            # add new point to obstacles dictionary
            new_obstacles = obstacles.copy()
            new_obstacles[point(i, j)] = True

            visited = {}
            # mark starting point as visited with specific move direction
            visited[point_with_dir(i, j, direction)] = True

            # do first move
            next_row, next_col, next_dir, stop = move(start_row, start_col, direction, new_obstacles, max_row, max_col)
            # if not out of maze
            while not stop:
                # mark point as visited with specific move direction
                p = point_with_dir(next_row, next_col, next_dir)
                if p in visited:
                    # crossed already visited point
                    count += 1
                    break
                visited[p] = True
                # do next move
                next_row, next_col, next_dir, stop = move(next_row, next_col, next_dir, new_obstacles, max_row, max_col)

    print(f"\nSolved 2: {count}")
