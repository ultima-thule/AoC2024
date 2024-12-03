import re

def extractData(input: list[str]):
    '''Extract and transform text data'''
    
    pattern = r'mul\(([\d]+),([\d]+)\)'

    for l in input:
        # print (f"=> line: {l}")
        mul = re.findall(pattern, l)
        for m in mul:
            # print(f"found: {m} {m[0]}*{m[1]}")
            yield m
            

def sliceData(input: list[str]):

    pattern1 = r'do\(\)(.+?)don\'t\(\)'

    for l in input:
        print (f"=> line: {l}")
        l = "do()" + l.strip() + "don't()"
        print (f"==> line: {l}")
        match = re.findall(pattern1, l)
        print(match)

        for t in match:
            print (f"=> match: {t}")
            pattern2 = r'mul\(([\d]+),([\d]+)\)'
            mul = re.findall(pattern2, t)
            for m in mul:
                print(f"found: {m} {m[0]}*{m[1]}")
                yield m


def executePartOne(input: list[str]) -> None:
    count = 0

    for m in extractData(input):
        count += int(m[0]) * int(m[1])
        pass   

    print(f"Solved 1: {count}")


def executePartTwo(input: list[str]) -> None:
    count = 0

    for m in sliceData(input):
        count += int(m[0]) * int(m[1])
        pass   

    print(f"Solved 2: {count}")
