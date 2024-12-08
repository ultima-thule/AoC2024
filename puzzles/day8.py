import re

def extract_data(input: list[str]):
    '''Extract and transform text data. Map antennas to dictionary.'''

    size_row = len(input)
    size_col = len(input[0].strip())
    antennas_raw = set()
    antennas_sorted = {}

    p = re.compile(r"\w")

    for row in range(0, size_row):
        line = input[row].strip()

        # print(f"Analyzing line: {line}")

        for col in range(0, size_col):
            c = input[row][col]
            # antenna found
            if p.match(c):
                # print(f"Match found: {c} at point {row},{col}")
                antennas_raw.add(point(row, col))
                if c not in antennas_sorted:
                    antennas_sorted[c] = []
                antennas_sorted[c].append(point(row, col))

    # print(f"Antennas raw: {antennas_raw}")
    # print(f"Antennas sorted: {antennas_sorted}")
    # print(f"Sizes: {max_row} {max_col}")

    return size_row, size_col, antennas_raw, antennas_sorted

def point(row, col):
    return f"{row},{col}"

def generate_all_antennas(antennas: list[str]) -> set:
    '''Generates all possible antennas to check for a given list of pantennas'''
    all_antennas = set()

    for i in range (0, len(antennas)):
        for j in range (i+1, len(antennas)):
            all_antennas.add(antennas[i] + "+" + antennas[j])

    return all_antennas

def is_valid(row, col, size_row, size_col, antenna):
    if row < 0 or row >= size_row:
        return None
    if col < 0 or col >= size_col:
        return None

    antinode = point(row, col)

    if antinode == antenna:
        return None
    
    return antinode

def calculate_antinodes(point_1, point_2, size_row, size_col):
    result = set() 

    print(f"Point 1: {point_1}, point 2: {point_2}")

    p_1 = point_1.split(",")
    row_1 = int(p_1[0])
    col_1 = int(p_1[1])

    p_2 = point_2.split(",")
    row_2 = int(p_2[0])
    col_2 = int(p_2[1])

    dist_row = row_2 - row_1
    dist_col = col_2 - col_1

    print (f"Point: {row_1},{col_1} and {row_2},{col_2} in distance [{dist_row},{dist_col}]")

    antinode = is_valid(row_1 + dist_row, col_1 + dist_col, size_row, size_col, point_2)
    if antinode is not None:
        result.add(antinode)
    antinode = is_valid(row_1 - dist_row, col_1 - dist_col, size_row, size_col, point_2)
    if antinode is not None:
        result.add(antinode)
    antinode = is_valid(row_2 + dist_row, col_2 + dist_col, size_row, size_col, point_1)
    if antinode is not None:
        result.add(antinode)
    antinode = is_valid(row_2 - dist_row, col_2 - dist_col, size_row, size_col, point_1)
    if antinode is not None:
        result.add(antinode)

    print(f"Antinodes found: {result}")

    return result

def generate_antinodes(points: list[str], size_row: int, size_col: int) -> None:
    
    all_antennas = generate_all_antennas(points)
    result = set()

    print(f"All antenas: {all_antennas}")

    for i in all_antennas:
        pp = i.split("+")
        res = calculate_antinodes(pp[0], pp[1], size_row, size_col)
        result = result.union(res)

    print(f"All antinodes found: {result}")

    return result

def execute_part_one(input: list[str]) -> None:
    size_row, size_col, antennas_raw, antennas_sorted = extract_data(input)

    antinodes = set()

    for k,v in antennas_sorted.items():
        print(f"\nChecking antinodes for {k}")
        antinodes = antinodes.union(generate_antinodes(v, size_row, size_col))

    print(f"Antinodes: {antinodes} of len {len(antinodes)}")


    result = antennas_raw ^ antinodes

    print(f"\nAntennas: {antennas_raw}")
    print(f"Result set: {result}")

    print(f"Solved 1: {len(antinodes)}")


def execute_part_two(input: list[str]) -> None:
    pass
    # max_row, max_col, antennas_raw, antennas_sorted = extract_data(input)

    # print(f"Solved 2: {len(antennas_raw)}")