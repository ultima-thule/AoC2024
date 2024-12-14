from collections import defaultdict
from collections import Counter

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    plots_area = defaultdict(int)
    plots = defaultdict(list)
    data = []
    max_x = len(input)
    regions = defaultdict(set)

    for x in range(0, len(input)):
        line = input[x].strip()
        max_y = len(line)
        data.append([])

        for y in range(0, len(line)):
            plots_area[line[y]] += 1
            plots[line[y]].append((x, y))
            data[x].append(line[y])
            regions[(x,y)].add((x,y))

    # print(regions)

    return plots_area, plots, max_x, max_y, data, regions

def identify_regions(data, regions, max_x, max_y):
    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            letter = data[x][y]
            # print(f"Letter: {letter} regions: {regions[(x,y)]}")

            if x - 1 > 0:
                if data[x - 1][y] == letter:
                    # print(f"Same letter {letter} regions {regions[(x - 1, y)]}")
                    reg_2 = regions[(x - 1, y)]
                    regions[(x, y)] |= reg_2
                    for i in regions[(x, y)]:
                        regions[i] = regions[(x, y)]

            if x + 1 < max_x:
                if data[x + 1][y] == letter:
                    # print(f"Same letter {letter} regions {regions[(x + 1, y)]}")
                    reg_2 = regions[(x + 1, y)]
                    regions[(x, y)] |= reg_2
                    for i in regions[(x, y)]:
                        regions[i] = regions[(x, y)]

            if y - 1 > 0:
                if data[x][y - 1] == letter:
                    # print(f"Same letter {letter} regions {regions[(x , y - 1)]}")
                    reg_2 = regions[(x, y - 1)]
                    regions[(x, y)] |= reg_2
                    for i in regions[(x, y)]:
                        regions[i] = regions[(x, y)]

            if y + 1 < max_y:
                if data[x][y + 1] == letter:
                    # print(f"Same letter {letter} regions {regions[(x, y + 1)]}")
                    reg_2 = regions[(x, y + 1)]
                    regions[(x, y)] |= reg_2
                    for i in regions[(x, y)]:
                        regions[i] = regions[(x, y)]


def get_adjacents(point, all_plots):
    p_1 = (point[0] - 1, point[1])
    p_2 = (point[0] + 1, point[1])
    p_3 = (point[0], point[1] - 1)
    p_4 = (point[0], point[1] + 1)

    count = 0

    if p_1 in all_plots:
        count += 1
    if p_2 in all_plots:
        count += 1
    if p_3 in all_plots:
        count += 1
    if p_4 in all_plots:
        count += 1

    return count

def calculate_perimeters(shape):
    total = 0
    for i in shape:
        perim = 4 - get_adjacents(i, shape)
        total += perim

    return total

def execute_part_one(input: list[str]) -> None:
    count = 0

    plots_area, plots, max_x, max_y, data, regions = extract_data(input)

    identify_regions(data, regions, max_x, max_y)

    # res = Counter(regions.values())

    # print(regions)

    res = defaultdict(set)
    for k, v in regions.items():
        if v in res.values():
            continue
        res[f"{data[k[0]][k[1]]}_{k[0]}_{k[1]}"] = v
    # print(f"=> Agregated regions:\n {res}\n")

    for k, v in res.items():
        letter = k[0]
        area = len(v)
        perim = calculate_perimeters(v)
        price = area * perim
        # print(f"Letter {letter}, area {area} * perim {perim} = price {price}")
        count += price


    # for k, v in plots_area.items():
    #     results = calculate_perimeters(k, plots[k])
        # for r in results:
        #     price = r[0] * r[1]
        #     count += price
        #     print(f"Plot {k} - area {v} * perimeter {perim} = price {price}")

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    plots_area, plots, max_x, max_y, data, regions = extract_data(input)

    print(f"Solved 2: {count}")
