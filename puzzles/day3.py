import re

def calculate(line: str) -> int:
    '''Extracts all multiplications operations and calculates sum of them'''
    pattern = r'mul\(([\d]+),([\d]+)\)'
    mul = re.findall(pattern, line)
    
    count = 0
    for m in mul:
        count += int(m[0]) * int(m[1])   

    return count

def execute_part_one(input: list[str]) -> None:
    '''Calculates results for all mul(M,N) operations'''
    count = 0

    for line in input:
        count += calculate(line)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:  
    '''Calculates results for all mul(M,N) laying between do() and don't() keywords'''

    #join lines to have a single stream of operations and avoid skipping some mul in line 2+
    joined_line = "do()" + "".join([x.strip() for x in input]) + "don't()"

    #find all matches between first do() and first don't()
    pattern = r'do\(\)(.+?)don\'t\(\)'
    match = re.findall(pattern, joined_line)

    count = 0
    for t in match:
        count += calculate(t)

    print(f"Solved 2: {count}")
