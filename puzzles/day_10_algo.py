def is_valid(x, y, max_x, max_y, data, expected):
    '''Check if single move is valid (within boundaries and of expected value)'''
    if x >= 0 and x < max_x and y >= 0 and y < max_y:
        return data[x][y] == expected
    return False

def get_valid_points(x, y, max_x, max_y, data):
    '''Return all possible moves from a given x,y point'''
    current = data[x][y]

    valid_points = []

    if is_valid(x - 1, y, max_x, max_y, data, current + 1):
        valid_points.append((x - 1, y))
    if is_valid(x + 1, y, max_x, max_y, data, current + 1):
        valid_points.append((x + 1, y))
    if is_valid(x, y - 1, max_x, max_y, data, current + 1):
        valid_points.append((x, y - 1))
    if is_valid(x, y + 1, max_x, max_y, data, current + 1):
        valid_points.append((x, y + 1))
    
    return valid_points

def find_all_trails(x, y, max_x, max_y, data, heads_set, heads_count, head_key):
    # current point is ending point
    if data[x][y] == 9:
        # save ending point to list
        heads_set[head_key].add((x, y))
        # increase number of distinct paths found
        heads_count[head_key] += 1
        return
    
    # search for all possible valid points
    valid_points = get_valid_points(x, y, max_x, max_y, data)

    # move to every valid point
    for i in valid_points:
        find_all_trails(i[0], i[1], max_x, max_y, data, heads_set, heads_count, head_key)
