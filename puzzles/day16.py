def extract_data(input: list[str]):
    '''Extract and transform text data'''
    maze_walls = {}
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

    plot_data(maze_walls, maze_start, maze_end, max_row, max_col)

    return maze_walls, maze_start, maze_end, max_row, max_col

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

def find_all_parts(row, col, max_row, max_col, maze_walls, maze_end):
    # reached end
    if (row, col) == maze_end:
        # save ending point to the list
        return

def execute_part_one(input: list[str]) -> None:
    count = 0

    maze_walls, maze_start, maze_end, max_row, max_col = extract_data(input)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    maze_walls, maze_start, maze_end, max_row, max_col = extract_data(input)

    print(f"Solved 2: {count}")
