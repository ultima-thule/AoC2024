from typing import Any
from puzzles.day_7_algo import *

def extract_data(input: list[str]) -> tuple[dict[str, list[Any]], dict[str, bool]]:
    input_data = {}
    solutions = {}

    for line in input:
        # use whole equation as key in equations dictionary
        eq = line.strip()

        temp = eq.split(":")
        numbers = temp[1].strip().split()
        input_data[eq] = [temp[0], numbers]
        # set initial validity of found solutions
        solutions[eq] = False

    return input_data, solutions

def execute_part_one(input: list[str]) -> None:
    input_data, solutions = extract_data(input)
    execute (input_data, solutions, 1, False)

def execute_part_two(input: list[str]) -> None:
    input_data, solutions = extract_data(input)
    execute (input_data, solutions, 2, True)
