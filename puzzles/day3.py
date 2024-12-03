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

def scanLine (s: str):
    started = False
    match = ""
    temp = ""

    s = "do()" + s.strip()
    print(f"========\nline: {s}\n")

    for i in range(0, len(s)):
        if s[i:].startswith("do()"):
            if not started:
                if temp != "":
                    match += temp
            if started:
                match = ""
            started = True
            print(f"\n==> found {s[i:]}")
            match += s[i]
        elif s[i:].startswith("don't()"):
            started = False
            temp += s[i]
        else:
            if started:
               match += s[i] 
            else:
                temp += s[i]



def sliceData(input: list[str]):

    # print(input)

    pattern1 = r'do\(\)(.+?)don\'t\(\)'

    joinedString = ""

    for l in input:
        joinedString += l.strip()

    # print (f"====> line: {l}")
    joinedString = "do()" + joinedString.strip() + "don't()"
    print (f"====> joined: {joinedString}")
    match = re.findall(pattern1, joinedString)
    print(match)

    for t in match:
        t = "do()" + t + "do()"
        print (f"\n\n==> match: {t}")

        # pattern2 = r'.*do\(\)(.+?)do\(\)$'
        # dos = re.findall(pattern2, t)
        # for d in dos:
        #     print(f"\n=> found: {d}")

        pattern3 = r'mul\(([\d]+),([\d]+)\)'
        mul = re.findall(pattern3, t)
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

    # sliceData(input)
    # scanLine(input[0])

    for m in sliceData(input):
        count += int(m[0]) * int(m[1])
        pass   

    print(f"Solved 2: {count}")
