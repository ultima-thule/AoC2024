import re
from collections import defaultdict

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []

    for line in input:
        line = line.strip()
        p_x, p_y, v_x, v_y = parse_line(line)
        data.append([(p_x, p_y), (v_x, v_y)])

    # print(data)
    return data

def parse_line(line):
    # print(f"Line: {line}")
    pattern = r'p=(\d+),(\d+) v=([-]?\d+),([-]?\d+)'
    result = re.search(pattern, line)

    # print(f"Result: {result}")

    p_x = int(result.group(1))
    p_y = int(result.group(2))
    v_x = int(result.group(3))
    v_y = int(result.group(4))

    # print(f"Robot found at position {p_x}, {p_y} with velocity {v_x}, {v_y}")

    return p_x, p_y, v_x, v_y

def next_position(position, vector, max_x, max_y, move_nr):
    x = position[0] + vector[0]
    y = position[1] + vector[1]

    # print(f"1. Move #{move_nr} from position {position[0]},{position[1]} => {x},{y}")

    if x < 0:
        x = max_x + x
    if x >= max_x:
        x = x - max_x
    if y < 0:
        y = max_y + y
    if y >= max_y:
        y = y - max_y
    # print(f"2. Move #{move_nr} from position {position[0]},{position[1]} => {x},{y}\n")

    return (x, y)

def simulate(robot, repeat, max_x, max_y):
    (x, y) = robot[0]
    for i in range(0, repeat):
        (x, y) = next_position((x, y), robot[1], max_x, max_y, i)

    return (x, y)

def calculate_score(positions, max_x, max_y):
    mid_x = int(max_x / 2)
    mid_y = int(max_y / 2)

    q_1, q_2, q_3, q_4 = 0, 0, 0, 0 

    for k, v in positions.items():
        if k[0] < mid_x:
            if k[1] < mid_y:
                q_1 += v
            elif k[1] > mid_y:
                q_2 += v
        elif k[0] > mid_x:
            if k[1] < mid_y:
                q_3 += v
            elif k[1] > mid_y:
                q_4 += v
    
    print(f"Quadrants {q_1}, {q_2}, {q_3}, {q_4}")

    return q_1 * q_2 * q_3 * q_4    

def execute_part_one(input: list[str]) -> None:
    count = 0

    max_x = 101
    max_y = 103
    repeat = 100

    data = extract_data(input)

    ending_positions = defaultdict(int)

    for i in data:
        (x, y) = simulate(i, repeat, max_x, max_y)
        ending_positions[(x,y)] += 1

    count = calculate_score(ending_positions, max_x, max_y)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    # extract_data(input)

    print(f"Solved 2: {count}")
