import re
from puzzles.lib.helpers import *
from puzzles.day_8_algo import *

def extract_data(input: list[str]) -> tuple[int, int, dict[str,list[str]]]:
    """Extract and transform text data. 
    Map antennas to dictionary, where antenna type is the key, and list of all locations is the value."""

    size_x, size_y = len(input), len(input[0].strip())
    antennas = {}

    p = re.compile(r"\w")

    for x in range(0, size_x):
        line = input[x].strip()

        for y in range(0, size_y):
            c = input[x][y]

            # antenna found
            if p.match(c):
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append(point_to_str(x, y))

    return size_x, size_y, antennas

def execute_part_one(input: list[str]) -> None:
    size_x, size_y, antennas = extract_data(input)

    antinodes = execute(size_x, size_y, antennas, False)

    print(f"==> Solution 1: {len(antinodes)}")

def execute_part_two(input: list[str]) -> None:
    size_x, size_y, antennas = extract_data(input)

    antinodes = execute(size_x, size_y, antennas, True)

    print(f"==> Solution 2: {len(antinodes)}")
