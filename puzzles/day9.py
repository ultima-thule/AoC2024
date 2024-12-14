from typing import Any

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data: list[Any] = []
    index = 0
    return_data = []
    
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

        if cnt != 0:
            return_data.append((len(data) - cnt, cnt, index if mod == 0 else "."))

        # data on disk
        if mod == 0:
            index += 1

    return data, return_data, index - 1

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

def convert_to_list(data):
    ret = []
    for item in data:
        for i in range (0, item[1]):
            ret.append(item[2])
    return ret

def move_full(data, start_value):
    
    for i in range(len(data) - 1, -1, -1):
        item = data[i]
        file_name = item[2]
        file_len = item[1]
        file_pos = item[0]
        is_file = file_name != "."

        if file_name == start_value:
            if is_file:
                found = False
                item_2 = (-1, -1, -1)
                index_found = -1
                for j in range (0, len(data)):
                    item_2 = data[j]
                    is_gap = (item_2[2] == ".")
                    gap_pos = item_2[0]
                    gap_len = item_2[1]
                    if is_gap and gap_len >= file_len and gap_pos < file_pos:
                        found = True
                        index_found = j
                        break
                if found:
                    # same length
                    if item_2[1] == file_len:
                        data[index_found] = (data[index_found][0], data[index_found][1], item[2])
                        data[i] = (file_pos, file_len, ".")
                    elif item_2[1] > file_len:
                        gap_len = data[index_found][1] - file_len
                        gap_start = data[index_found][0] + file_len
                        data[index_found] = (data[index_found][0], file_len, item[2])
                        data[i] = (file_pos, file_len, ".")
                        data.insert(index_found + 1, (gap_start, gap_len, '.'))
                    break
        else:
            continue

def compute_checksum(input_data) -> int:
    checksum = 0

    for k, v in enumerate(input_data):
        if v == ".":
            continue
        checksum += k * v

    return checksum

def execute_part_one(input: list[str]) -> None:
    count = 0

    data, _, _ = extract_data(input)

    move(data)
    count = compute_checksum(data)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    _, return_data, max_value = extract_data(input)

    for i in range(max_value, -1, -1):
        move_full(return_data, i)

    checksum_data = convert_to_list(return_data)
    count = compute_checksum(checksum_data)

    print(f"Solved 2: {count}")
