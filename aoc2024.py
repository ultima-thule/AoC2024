import sys
from puzzles import day1, day2

def readInput(day):
    with open(f"puzzles/data/day{day}.txt", "r+") as dataFile:
        print(f"--- DAY {day} --- ")
        print("Reading data from a file")
        return dataFile.readlines()

def runPart(day, part, input):
    print(f"Executing part {part}")

    match day:
        case "1": 
           day1.executePartOne(input) if part == 1 else day1.executePartTwo(input)
        case "2": 
           day2.executePartOne(input) if part == 1 else day2.executePartTwo(input)



def main(argv):
    input = readInput(argv[0])
    # print(data)
    
    runPart(argv[0], 1, input)
    runPart(argv[0], 2, input)

if __name__ == "__main__":
    main(sys.argv[1:])