import re
from collections import namedtuple
from puzzles.day_13_algo import *

Machine = namedtuple('Machine', ['a_x', 'a_y', 'b_x', 'b_y', 'p_x', 'p_y'])

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    a_x, a_y, b_x, b_y, p_x, p_y = -1, -1, -1, -1, -1, -1

    for line in input:
        if line.startswith("Button A: "):
            a_x, a_y = extract_numbers(line, True)
        elif line.startswith("Button B: "):
            b_x, b_y = extract_numbers(line, True)
        elif  line.startswith("Prize"):
            p_x, p_y = extract_numbers(line, False)
        else:
            data.append(Machine(a_x, a_y, b_x, b_y, p_x, p_y))
            a_x, a_y, b_x, b_y, p_x, p_y = -1, -1, -1, -1, -1, -1
    
    data.append(Machine(a_x, a_y, b_x, b_y, p_x, p_y))

    return data

def extract_numbers(line: str, is_button: bool) -> tuple[int, int]:
    '''Extract numeric data from single line of text'''
    spl = line.split()
    # line contains button definitions
    if is_button:
        pattern = r'Button [AB]: X\+([\d]+), Y\+([\d]+)'
    # line contains prize definitions
    else:
        pattern = r'Prize: X=([\d]+), Y=([\d]+)'
    result = re.search(pattern, line)

    return int(result.group(1)), int(result.group(2))

def execute_part_one(input: list[str]) -> None:
    count = 0

    machine_data = extract_data(input)
    for m in machine_data:
        count += simulate(m.a_x, m.a_y, m.b_x, m.b_y, m.p_x, m.p_y, False)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    machine_data = extract_data(input)
    for m in machine_data:
        count += simulate(m.a_x, m.a_y, m.b_x, m.b_y, m.p_x, m.p_y, True)

    print(f"Solved 2: {count}")
