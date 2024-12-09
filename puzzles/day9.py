from typing import Any

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data: list[Any] = []
    empty_indices = []
    index = 0
    
    all_lines = ""
    for line in input:
        all_lines += line.strip()

    for i in range(0, len(all_lines)):
        mod = i % 2
        cnt = int(all_lines[i])
        for _ in range(0, cnt):
            if mod == 0:
               data.append(index)
            else:
                data.append('.')
        if mod == 0:
            index += 1
        else:
            if cnt != 0:
                empty = f"{len(data) - cnt}|{cnt}"
                empty_indices.append(empty)

    return data, empty_indices

def move(input_data):
    
    pointer_start, pointer_end = 0, len(input_data) - 1

    while True:
        # break if passed pointer_end
        if pointer_start > pointer_end:
            break

        # move until an empty slot is reached
        while input_data[pointer_start] != ".":
            pointer_start += 1

        # break if passed pointer_end
        if pointer_start > pointer_end:
            break

        # empty slot reached
        # find first ID to be moved
        while input_data[pointer_end] == ".":
            pointer_end -= 1

        # break if passed pointer_end
        if pointer_start > pointer_end:
            break
        
        # exchange chars
        start = input_data[pointer_start]
        end = input_data[pointer_end]

        input_data[pointer_start] = end
        input_data[pointer_end] = start

        pointer_start += 1
        pointer_end -= 1

    print(f"After running: \n{input_data}")



def compute_checksum(input_data) -> int:
    checksum = 0

    for i in range(0, len(input_data)):
        if input_data[i] == ".":
            break
        checksum += i * input_data[i]

    return checksum


def execute_part_one(input: list[str]) -> None:
    count = 0

    data, empty_indices = extract_data(input)

    print(data)
    print(empty_indices)

    move(data)

    count = compute_checksum(data)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    data, empty_indices = extract_data(input)

    print(f"Solved 2: {count}")
