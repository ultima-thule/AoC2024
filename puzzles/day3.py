import re

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    
    pattern = r'mul\(([\d]+),([\d]+)\)'

    for line in input:
        mul = re.findall(pattern, line)
        for m in mul:
            yield m


def slice_data(input: list[str]):
    pattern1 = r'do\(\)(.+?)don\'t\(\)'

    joined_line = "".join([x.strip() for x in input])
    joined_line = "do()" + joined_line.strip() + "don't()"
    
    print (f"====> joined: {joined_line}")
    match = re.findall(pattern1, joined_line)
    print(match)

    for t in match:
        t = "do()" + t + "do()"
        print (f"\n\n==> match: {t}")

        pattern3 = r'mul\(([\d]+),([\d]+)\)'
        mul = re.findall(pattern3, t)
        for m in mul:
            print(f"found: {m} {m[0]}*{m[1]}")
            yield m
    

def execute_part_one(input: list[str]) -> None:
    count = 0

    for m in extract_data(input):
        count += int(m[0]) * int(m[1])

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    for m in slice_data(input):
        count += int(m[0]) * int(m[1])   

    print(f"Solved 2: {count}")
