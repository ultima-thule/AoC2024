from typing import Any

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data: list[Any] = []
    empty_indices = {}
    full_indices = {}
    file_number_indices = {}
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
        # data on disk
        if mod == 0:
            if cnt != 0:
                if cnt not in full_indices:
                    full_indices[cnt] = []
                full_indices[cnt].append([len(data) - cnt, index])
                file_number_indices[index] = cnt
            index += 1
        # empty space on disk
        else:
            if cnt != 0:
                if cnt not in empty_indices:
                    empty_indices[cnt] = []
                empty_indices[cnt].append(len(data) - cnt)

    print(f"Data: \n{data}")

    print(f"Full indices: \n{full_indices}")
    print(f"Empty indices: \n{empty_indices}")
    print(f"File number indices: \n{file_number_indices}")

    return data, empty_indices, full_indices, file_number_indices

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

        # move pointers by one position
        pointer_start += 1
        pointer_end -= 1

def get_max_gap(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    last_key = list(sorted_dict) [-1]
    return last_key


def move_full(empty_indices, full_indices, file_number_indices):

    #sort dictionary of files in reversed order
    sorted_dict = dict(sorted(file_number_indices.items(), reverse=True))
    print(f"Sorted dict: \n{sorted_dict}\n")

    # iterate through files
    for k, v in sorted_dict.items():
        # what is the max available free space gap
        max_gap = get_max_gap(empty_indices)
        print(f"==> Looking for space for ID={k} of len {v}. Gap from {v} to {max_gap}.")
        for i in range (v, max_gap + 1):
            if i in empty_indices:
                print(f"{k} => {i}")
                print(f"Possible locations for {v}: {empty_indices[i]}\n")
                break




def compute_checksum(input_data) -> int:
    checksum = 0

    for i in range(0, len(input_data)):
        if input_data[i] == ".":
            break
        checksum += i * input_data[i]

    return checksum

def execute_part_one(input: list[str]) -> None:
    count = 0

    data, empty_indices, full_indices, file_number_indices = extract_data(input)

    print(data)
    print(empty_indices)

    move(data)
    count = compute_checksum(data)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    data, empty_indices, full_indices, file_number_indices = extract_data(input)

    move_full(empty_indices, full_indices, file_number_indices)
    # count = compute_checksum(data)

    print(f"Solved 2: {count}")
