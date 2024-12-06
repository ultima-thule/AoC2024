import sys
import time

def read_input(day):
    with open(f"puzzles/data/day{day}.txt", "r+") as dataFile:
        print(f"--- DAY {day} --- ")
        print("Reading data from a file")
        return dataFile.readlines()

def run_part(day, part, input):
    print(f"Executing part {part}")

    fnc_part_one = 'execute_part_one'
    fnc_part_two = 'execute_part_two'
    importlib = __import__('importlib')
    mod = importlib.import_module(f"puzzles.day{day}")

    func_one = getattr(mod, fnc_part_one)
    func_two = getattr(mod, fnc_part_two)

    func_one(input) if part == 1 else func_two(input)

def main(argv):
    input = read_input(argv[0])
    
    start_time = time.time()
    run_part(argv[0], 1, input)
    print("--- %s seconds ---\n" % (time.time() - start_time))
    start_time = time.time()
    run_part(argv[0], 2, input)
    print("--- %s seconds ---\n" % (time.time() - start_time))

if __name__ == "__main__":
    main(sys.argv[1:])