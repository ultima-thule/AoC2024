from collections import defaultdict
from collections import Counter

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    max_x = len(input)
    regions = defaultdict(set)

    for x in range(0, len(input)):
        line = input[x].strip()
        max_y = len(line)
        data.append([])

        for y in range(0, len(line)):
            data[x].append(line[y])
            regions[(x,y)].add((x,y))

    return max_x, max_y, data, regions

def merge_sets(regions, point_1, point_2):
    reg_2 = regions[point_2]
    regions[point_1] |= reg_2
    for i in regions[point_1]:
        regions[i] = regions[point_1]

def identify_regions(data, regions, max_x, max_y):
    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            letter = data[x][y]

            if x - 1 > 0:
                if data[x - 1][y] == letter:
                    merge_sets(regions, (x, y), (x - 1, y))

            if x + 1 < max_x:
                if data[x + 1][y] == letter:
                    merge_sets(regions, (x, y), (x + 1, y))

            if y - 1 > 0:
                if data[x][y - 1] == letter:
                    merge_sets(regions, (x, y), (x, y - 1))

            if y + 1 < max_y:
                if data[x][y + 1] == letter:
                    merge_sets(regions, (x, y), (x, y + 1))

def get_cnt(point, all_points):
    if point in all_points:
        return 1
    return 0


def get_adjacents(point, all_plots):
    count = 0

    count += get_cnt((point[0] - 1, point[1]), all_plots)
    count += get_cnt((point[0] + 1, point[1]), all_plots)
    count += get_cnt((point[0], point[1] - 1), all_plots)
    count += get_cnt((point[0], point[1] + 1), all_plots)

    return count

def calculate_perimeters(shape):
    total = 0
    for i in shape:
        perim = 4 - get_adjacents(i, shape)
        total += perim

    return total

def execute_part_one(input: list[str]) -> None:
    count = 0

    max_x, max_y, data, regions = extract_data(input)

    # identify all regions
    identify_regions(data, regions, max_x, max_y)

    # get unique shapes
    res = defaultdict(set)
    for k, v in regions.items():
        if v in res.values():
            continue
        res[f"{data[k[0]][k[1]]}_{k[0]}_{k[1]}"] = v

    for k, v in res.items():
        price = len(v) * calculate_perimeters(v)
        count += price

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    max_x, max_y, data, regions = extract_data(input)

    print(f"Solved 2: {count}")
