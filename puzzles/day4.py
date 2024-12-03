def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for l in input:
        yield l

def execute_part_one(input: list[str]) -> None:
    count = 0

    for l in extract_data(input):
        pass   

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    for l in extract_data(input):
        pass

    print(f"Solved 2: {count}")
