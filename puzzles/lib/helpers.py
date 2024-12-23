def point_to_str(x, y):
    '''Converts x and y into string point representation'''
    return f"{x},{y}"

def point_from_str(point_string: str) -> tuple[int, int]:
    '''Converts string x,y into separate integers'''
    p = point_string.split(",")
    return int(p[0]), int(p[1])

def is_in_range(x: int, y: int, size_x: int, size_y: int) -> bool:
    '''Validates whether given indices x and y are within grid range of size_x and size_y'''
    if x < 0 or x >= size_x or y < 0 or y >= size_y:
        return False
    return True

def print_grid(size_x, size_y, grid):
    '''Prints grid on the screen'''
    for i in range(0, size_x):
        for j in range(0, size_y):
            if point_to_str(i,j) in grid:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def plot_grid(size_x, size_y, grid):
    '''Prints grid on the screen'''
    for i in range(0, size_x):
        for j in range(0, size_y):
            if (i,j) in grid:
                print("#", end="")
            else:
                print(".", end="")
        print("")

def plot_grid_path(size_x, size_y, grid, visited):
    '''Prints grid on the screen'''
    for i in range(0, size_x):
        for j in range(0, size_y):
            if (i,j) in grid:
                print("#", end="")
            elif (i,j) in visited:
                print("O", end="")
            else:
                print(".", end="")
        print("")