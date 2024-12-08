from puzzles.lib.helpers import *

def generate_antenna_pairs(antennas: list[str]) -> set:
    """ Generates all possible antennas pairs from a given list of antennas of the same type.
        Pair format: x1,y1|x2,y2"""
    all_pairs = set()

    for i in range (0, len(antennas)):
        for j in range (i+1, len(antennas)):
            all_pairs.add(f"{antennas[i]}|{antennas[j]}")

    return all_pairs

def is_valid(antinode, size_x: int, size_y: int, check_overlap: bool):
    '''Validates whether given point is a valid antinode'''
    x, y = antinode[0], antinode[1]
    antenna = antinode[2]

    # check if is within grid range
    if not is_in_range(x, y, size_x, size_y):
        return None

    antinode = point_to_str(x, y)
   
    if check_overlap:
        # return antinode if is not overlapping with given antenna
        return antinode if antinode != antenna else None
    
    return antinode

def get_possible_antinodes(x: int, y: int, dist_x: int, dist_y: int, antenna: str, size_x: int, size_y: int, is_scenario_2: bool):
    '''Gets all possible antinodes within grid range size_x,size_y'''
    result = []

    # for travelling in both directions
    multipliers = [1, -1]

    for m in multipliers:
        counter = 0
        while True:
            counter += m * 1
            # calculate next position
            next_x, next_y = x + counter * dist_x, y + counter * dist_y

            # check if is range
            if is_in_range(next_x, next_y, size_x, size_y):
                result += [[next_x, next_y, antenna]]
            else:
                break
            # break after first loop for scenario 1
            if not is_scenario_2:
                break

    return result

def get_antinodes(antennas_pair, size_x, size_y, is_scenario_2: bool):
    '''Gets valid antinodes for point_1 within grid of size_x, size_y'''
    antinodes = set() 

    # unpack antennas' data
    pp = antennas_pair.split("|")
    antenna_1, antenna_2 = pp[0], pp[1]
    x_1, y_1 = point_from_str(antenna_1)
    x_2, y_2 = point_from_str(antenna_2)

    # calculate distance between antennas
    dist_x, dist_y = x_2 - x_1, y_2 - y_1

    # get possible antinodes in that distance
    possible_antinodes = get_possible_antinodes(x_1, y_1, dist_x, dist_y, antenna_2, size_x, size_y, is_scenario_2)
    possible_antinodes += get_possible_antinodes(x_2, y_2, dist_x, dist_y, antenna_1, size_x, size_y, is_scenario_2)
   
    for pa in possible_antinodes:
        # add to resul only valid antinodes
        item = is_valid(pa, size_x, size_y, not is_scenario_2)    
        if item is not None:
            antinodes.add(item)

    return antinodes

def find_antinodes(points: list[str], size_x: int, size_y: int, is_scenario_2: bool) -> None:
    '''Find all positions of antinodes for given set of antennas, within boudaries of max_x and max_y'''

    #generate all antennas pair for verification    
    all_pairs = generate_antenna_pairs(points)

    # for each antenna pair, find valid antinodes
    antinodes = set()
    for pair in all_pairs:
        antinodes = antinodes | get_antinodes(pair, size_x, size_y, is_scenario_2)

    return antinodes


def execute(size_x, size_y, antennas, is_scenario_2: bool) -> dict[str, str]:
    '''Execute single scenario'''
    antinodes = set()
    # for each antenna type, find antinodes
    for k,v in antennas.items():
        antinodes = antinodes | find_antinodes(v, size_x, size_y, is_scenario_2)

    return antinodes
