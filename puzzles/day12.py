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

    # get unique shapes
    res = defaultdict(set)
    for k, v in regions.items():
        if v in res.values():
            continue
        res[f"{data[k[0]][k[1]]}_{k[0]}_{k[1]}"] = v

    return res

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

def calculate_corners(letter, shape):
    # print(f"Calculaing corners for shape {letter} of {shape}")
    total = 0
    for i in shape:
        is_corner = False        
        # print(f"Corner: {i}")
        x = i[0]
        y = i[1]
        p_top = (x - 1, y)
        p_bottom = (x + 1, y)
        p_left = (x, y - 1)
        p_right = (x, y + 1)
        # external corners
        # print(f"Adjacent points: {p_top} => {p_top not in shape}, {p_bottom} => {p_bottom not in shape}, {p_left} => {p_left not in shape}, {p_right} => {p_right not in shape}")
        if p_top not in shape and p_left not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1
        if p_top not in shape and p_right not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1
        if p_bottom not in shape and p_left not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1
        if p_bottom not in shape and p_right not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1

        # internal corners
        p_top_left = (x - 1, y - 1)
        p_top_right = (x - 1, y + 1)
        p_bottom_left = (x + 1, y - 1)
        p_bottom_right = (x + 1, y + 1)

        if p_top in shape and p_right in shape and p_top_right not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1
        if p_top in shape and p_left in shape and p_top_left not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1
        if p_bottom in shape and p_right in shape and p_bottom_right not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1
        if p_bottom in shape and p_left in shape and p_bottom_left not in shape:
            # print(f"Corner found: {x},{y}")
            total += 1

    # print(f"===> Shape {letter} - total corners found: {total}\n")
    return total

def execute_part_one(input: list[str]) -> None:
    count = 0

    max_x, max_y, data, regions = extract_data(input)

    # identify all regions
    unique_regions = identify_regions(data, regions, max_x, max_y)

    for k, v in unique_regions.items():
        price = len(v) * calculate_perimeters(v)
        count += price

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    max_x, max_y, data, regions = extract_data(input)

    # identify all regions
    unique_regions = identify_regions(data, regions, max_x, max_y)

    for k, v in unique_regions.items():
        # print(f"Checking shape {v}")
        price = len(v) * calculate_corners(k[0], v)
        count += price

    print(f"Solved 2: {count}")
