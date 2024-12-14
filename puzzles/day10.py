from collections import defaultdict

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    heads = {}
    max_x = len(input)
    for i in range(0, len(input)):
        line = input[i].strip()
        max_y = len(line)
        data.append([])
        for c in list(line):
            data[i].append(int(c))
        heads = heads | find_heads(line, i)

    print(f"Data: {data}\nHeads: {heads}\nmax_x: {max_x}, max_y: {max_y}")
    return data, heads, max_x, max_y

def find_heads(line, row):
    data = {}
    for i in range(0, len(line)):
        if line[i] == "0":
            data[(row, i)] = set()

    return data

def is_valid(x, y, max_x, max_y, data, expected):
    # print(f"Checking point {x},{y} of expected {expected}")
    if x >= 0 and x < max_x and y >= 0 and y < max_y:
        return data[x][y] == expected
    return False

def get_valid_points(x, y, max_x, max_y, data):
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
    
    # print(f"Valid points: {valid_points}")

    return valid_points

def find_all_trails(x, y, max_x, max_y, data, heads, head_key):
    # print(f"Checking point {x},{y} starting from {head_key}")

    # current point is ending point
    if data[x][y] == 9:
        # print(f"=> End point {x},{y} found for {head_key}")
        # save position to list
        heads[head_key].add((x, y))
        return
    
    # search for all possible valid poinst
    valid_points = get_valid_points(x, y, max_x, max_y, data)
    if len(valid_points) == 0:
        return

    for i in valid_points:
        find_all_trails(i[0], i[1], max_x, max_y, data, heads, head_key)


def execute_part_one(input: list[str]) -> None:
    count = 0

    data, heads, max_x, max_y = extract_data(input)

    for item in heads.items():
        # print(item)
        # print(f"\nSearching for trails from point {item[0][0]},{item[0][1]}")
        find_all_trails(item[0][0], item[0][1], max_x, max_y, data, heads, item[0])

    print(f"Heads: {heads}")
    for k, v in heads.items():
        # print(f"Head: {k}, score: {len(v)}")
        count += len(v)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    data, heads, max_x, max_y = extract_data(input)

    print(f"Solved 2: {count}")
