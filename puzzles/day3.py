import re

def calculate(line: str) -> int:
    pattern = r'mul\(([\d]+),([\d]+)\)'
    mul = re.findall(pattern, line)
    
    count = 0
    for m in mul:
        count += int(m[0]) * int(m[1])   

    return count

def execute_part_one(input: list[str]) -> None:
    count = 0

    for line in input:
        count += calculate(line)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:  

    joined_line = "do()" + "".join([x.strip() for x in input]) + "don't()"

    pattern = r'do\(\)(.+?)don\'t\(\)'
    match = re.findall(pattern, joined_line)

    count = 0
    for t in match:
        t = "do()" + t + "do()"
        count += calculate(t)

    print(f"Solved 2: {count}")
