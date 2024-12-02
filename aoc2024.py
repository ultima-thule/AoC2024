import sys

def readInput(day):
    with open(f"puzzles/data/day{day}.txt", "r+") as dataFile:
        print(f"--- DAY {day} --- ")
        print("Reading data from a file")
        return dataFile.readlines()

def runPart(day, part, input):
    print(f"Executing part {part}")

    fncPartOne = 'executePartOne'
    fncPartTwo = 'executePartTwo'
    importlib = __import__('importlib')
    mod = importlib.import_module(f"puzzles.day{day}")

    funcOne = getattr(mod, fncPartOne)
    funcTwo = getattr(mod, fncPartTwo)

    funcOne(input) if part == 1 else funcTwo(input)

def main(argv):
    input = readInput(argv[0])
    
    runPart(argv[0], 1, input)
    runPart(argv[0], 2, input)

if __name__ == "__main__":
    main(sys.argv[1:])