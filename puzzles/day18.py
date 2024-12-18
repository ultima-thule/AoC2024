def extract_data(input: list[str]):
    data = {}
    
    for i in range(0, len(input)):
        line = input[i].strip()
        data[(line[0], line[2])] = 1

    print(data)

    return data

def 

def execute_part_one(input: list[str]) -> None:
    count = 0

    data = extract_data(input)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    data = extract_data(input)

    print(f"Solved 2: {count}")
