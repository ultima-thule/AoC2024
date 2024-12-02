def extractData(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for l in input:
        yield l

def executePartOne(input: list[str]) -> None:
    count = 0

    for l in extractData(input):
        pass   

    print(f"Solved 1: {count}")


def executePartTwo(input: list[str]) -> None:
    count = 0

    for l in extractData(input):
        pass

    print(f"Solved 2: {count}")
