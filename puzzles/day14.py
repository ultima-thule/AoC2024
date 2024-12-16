import re
from collections import defaultdict

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []

    for line in input:
        line = line.strip()
        p_x, p_y, v_x, v_y = parse_line(line)
        data.append([(p_x, p_y), (v_x, v_y)])

    return data

def parse_line(line):
    pattern = r'p=(\d+),(\d+) v=([-]?\d+),([-]?\d+)'
    result = re.search(pattern, line)

    return int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4))

def next_position(position, vector, max_x, max_y):
    x = position[0] + vector[0]
    y = position[1] + vector[1]

    if x < 0:
        x = max_x + x
    if x >= max_x:
        x = x - max_x
    if y < 0:
        y = max_y + y
    if y >= max_y:
        y = y - max_y

    return (x, y)

def simulate(robot, repeat, max_x, max_y):
    (x, y) = robot[0]
    for i in range(0, repeat):
        (x, y) = next_position((x, y), robot[1], max_x, max_y)

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
    
    return q_1 * q_2 * q_3 * q_4    

def plot_robots(positions, max_x, max_y):
    for x in range(0, max_x):
        for y in range(0, max_y):
            print("X" if (x, y) in positions else ".", end="")
        print()

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

    max_x = 101
    max_y = 103

    robots = extract_data(input)

    while True:
        ending_positions = defaultdict(int)
        count += 1
        new_robots = []
        for r in robots: 
            (x, y) = next_position(r[0], r[1], max_x, max_y)
            ending_positions[(x,y)] += 1
            new_robots.append([(x, y), r[1]])

        robots = new_robots

        # assume that picture is drawn when there is no overlap in robots
        if len(ending_positions) == len(robots):
            break;

    plot_robots (ending_positions, max_x, max_y)

    print(f"Solved 2: {count}")
