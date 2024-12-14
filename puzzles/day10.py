from collections import defaultdict
from puzzles.day_10_algo import *

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    trailheads_set, trailheads_count = {}, {}
    
    max_x = len(input)
    for i in range(0, len(input)):
        line = input[i].strip()
        max_y = len(line)
        data.append([])
        for c in list(line):
            data[i].append(int(c))
        
        s, c = init_trailheads(line, i)
        trailheads_set = trailheads_set | s
        trailheads_count = trailheads_count | c

    return data, trailheads_set, trailheads_count, max_x, max_y

def init_trailheads(line, row):
    data_set, data_count = {}, {}
    for i in range(0, len(line)):
        if line[i] == "0":
            data_set[(row, i)] = set()
            data_count[(row, i)] = 0

    return data_set, data_count

def execute_part_one(input: list[str]) -> None:
    count = 0

    data, heads_set, heads_count, max_x, max_y = extract_data(input)

    for item in heads_set.items():
        find_all_trails(item[0][0], item[0][1], max_x, max_y, data, heads_set, heads_count, item[0])

    for k, v in heads_set.items():
        count += len(v)

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    data, heads_set, heads_count, max_x, max_y = extract_data(input)

    for item in heads_count.items():
        find_all_trails(item[0][0], item[0][1], max_x, max_y, data, heads_set, heads_count, item[0])

    for k, v in heads_count.items():
        count += v

    print(f"Solved 2: {count}")
