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

# def dijkstra(s, walls, max_row, max_col):

#         distance = defaultdict(lambda: sys.maxsize)
#         distance[s] = 0
#         shortest_path = defaultdict(bool)
#         # Create a queue for BFS
#         q = deque()

#         adj = get_neighbours(s, max_row, max_col, walls)

#         for _ in range(0, (max_row+1)*(max_col+1)):

#             # Pick the minimum distance vertex from
#             # the set of vertices not yet processed.
#             # x is always equal to src in first iteration
#             x = min_distance(distance, shortest_path, adj)

#             # Put the minimum distance vertex in the
#             # shortest path tree
#             shortest_path[x] = True

#             # Update dist value of the adjacent vertices
#             # of the picked vertex only if the current
#             # distance is greater than new distance and
#             # the vertex in not in the shortest path tree
#             adj = get_neighbours(x, max_row, max_col, walls)
#             for y in adj:
#                 if shortest_path[y] == False and distance[y] > distance[x] + 1:
#                     distance[y] = distance[x] + 1

#         # print_solution(distance)