import re

def extract_data(input: list[str]) -> tuple[int, int, dict[str,list[str]]]:
    '''Extract and transform text data. Map antennas to dictionary.'''

    size_x = len(input)
    size_y = len(input[0].strip())
    antennas_sorted = {}

    p = re.compile(r"\w")

    for x in range(0, size_x):
        line = input[x].strip()

        for y in range(0, size_y):
            c = input[x][y]

            # antenna found
            if p.match(c):
                if c not in antennas_sorted:
                    antennas_sorted[c] = []
                antennas_sorted[c].append(point_to_str(x, y))

    return size_x, size_y, antennas_sorted

def point_to_str(x, y):
    return f"{x},{y}"

def point_from_str(point_string: str) -> tuple[int, int]:
    p = point_string.split(",")
    x = int(p[0])
    y = int(p[1])

    return x, y

def generate_all_antennas(antennas: list[str]) -> set:
    '''Generates all possible antennas to check for a given list of antennas'''
    all_antennas = set()

    for i in range (0, len(antennas)):
        for j in range (i+1, len(antennas)):
            all_antennas.add(antennas[i] + "+" + antennas[j])

    return all_antennas

def is_in_range(x: int, y: int, size_x: int, size_y: int) -> bool:
    if x < 0 or x >= size_x or y < 0 or y >= size_y:
        return False
    return True

def is_valid(x: int, y: int, size_x: int, size_y: int, antenna: str, check_overlap: bool):
    # check if is within grid range
    if not is_in_range(x, y, size_x, size_y):
        print(f"* Point {x}, {y} out of range!")
        return None

    print(f"* Point {x}, {y} in range")
    antinode = point_to_str(x, y)
   
    # return antinode if is not overlapping
    if check_overlap:
        print(f"- checking overlap {antinode} with {antenna}: {antinode == antenna}")
        return antinode if antinode != antenna else None
    
    return antinode


def possible_antinodes(x: int, y: int, dist_x: int, dist_y: int, antenna: str, size_x: int, size_y: int, repeat: bool):
    if not repeat:
        return [[x + dist_x, y + dist_y, antenna], 
        [x - dist_x, y - dist_y, antenna]]

    result = []

    counter = 0
    while True:
        counter += 1
        next_x = x + counter * dist_x
        next_y = y + counter * dist_y
        print(f"+ Point {x}, {y} => next point: {next_x}, {next_y}")
        if is_in_range(next_x, next_y, size_x, size_y):
            result += [[next_x, next_y, antenna]]
        else:
            break

    counter = 0
    while True:
        counter += 1
        next_x = x - counter * dist_x
        next_y = y - counter * dist_y
        print(f"- Point {x}, {y} => next point: {next_x}, {next_y}")
        if is_in_range(next_x, next_y, size_x, size_y):
            result += [[next_x, next_y, antenna]]
        else:
            break

    return result

def calculate_antinodes(point_1, point_2, size_x, size_y, repeat: bool):
    result = set() 

    # print(f"Point 1: {point_1}, point 2: {point_2}")

    x_1, y_1 = point_from_str(point_1)
    x_2, y_2 = point_from_str(point_2)

    dist_x = x_2 - x_1
    dist_y = y_2 - y_1

    # print (f"Point: {x_1},{y_1} and {x_2},{y_2} in distance [{dist_x},{dist_y}]")

    nodes_to_check = possible_antinodes(x_1, y_1, dist_x, dist_y, point_2, size_x, size_y, repeat)
    nodes_to_check += possible_antinodes(x_2, y_2, dist_x, dist_y, point_1, size_x, size_y, repeat)
   
    for n in nodes_to_check:
        antinode = is_valid(n[0], n[1], size_x, size_y, n[2], not repeat)    
        if antinode is not None:
            result.add(antinode)

    print(f"Antinodes found: {result}")

    return result

def find_antinodes(points: list[str], size_x: int, size_y: int, repeat: bool) -> None:
    '''Find all positions of antinodes for given set of antennas, within boudaries of max_x and max_y'''
    
    all_antennas = generate_all_antennas(points)
    result = set()

    print(f"All antenas: {all_antennas}")

    for i in all_antennas:
        pp = i.split("+")
        res = calculate_antinodes(pp[0], pp[1], size_x, size_y, repeat)
        result = result.union(res)

    print(f"All antinodes found: {result}")

    return result

def execute(input: list[str], repeat: bool) -> dict[str, str]:
    '''Execute single scenario'''
    size_x, size_y, antennas_sorted = extract_data(input)

    antinodes = set()

    for k,v in antennas_sorted.items():
        print(f"\nChecking antinodes for {k}")
        antinodes = antinodes.union(find_antinodes(v, size_x, size_y, repeat))


    print_grid(size_x, size_y, antinodes)

    return antinodes

def execute_part_one(input: list[str]) -> None:

    antinodes = execute(input, False)

    print(f"Antinodes: {antinodes} of len {len(antinodes)}")
    print(f"==> Solution 1: {len(antinodes)}")


def execute_part_two(input: list[str]) -> None:
    antinodes = execute(input, True)

    print(f"Antinodes: {antinodes} of len {len(antinodes)}")
    print(f"==> Solution 2: {len(antinodes)}")

def print_grid(size_x, size_y, antinodes):
    for i in range(0, size_x):
        for j in range(0, size_y):
            if point_to_str(i,j) in antinodes:
                print("#", end="")
            else:
                print(".", end="")
        print("")