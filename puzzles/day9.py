from typing import Any

def extract_data(input: list[str]) -> tuple[list[Any], list[Any], int]:
    '''Extract and transform text data'''
    raw_data: list[Any] = []
    aggr_data: list[Any] = []
    index = 0
    
    all_lines = ""
    for line in input:
        all_lines += line.strip()

    for i in range(0, len(all_lines)):
        mod = i % 2
        cnt = int(all_lines[i])
        for _ in range(0, cnt):
            if mod == 0:
               raw_data.append(index)
            else:
                raw_data.append('.')

        if cnt != 0:
            aggr_data.append((len(raw_data) - cnt, cnt, index if mod == 0 else "."))

        # data on disk
        if mod == 0:
            index += 1

    return raw_data, aggr_data, index - 1

def move(raw_data: list[Any]):
    
    pointer_start, pointer_end = 0, len(raw_data) - 1

    while True:
        # break if passed pointer_end
        if pointer_start > pointer_end:
            break

        # move until an empty slot is reached
        while raw_data[pointer_start] != ".":
            pointer_start += 1

        # break if passed pointer_end
        if pointer_start > pointer_end:
            break

        # empty slot reached
        # find first ID to be moved
        while raw_data[pointer_end] == ".":
            pointer_end -= 1

        # break if passed pointer_end
        if pointer_start > pointer_end:
            break
        
        # exchange chars
        start = raw_data[pointer_start]
        end = raw_data[pointer_end]

        raw_data[pointer_start] = end
        raw_data[pointer_end] = start

        # move pointers by one position
        pointer_start += 1
        pointer_end -= 1

def convert_to_raw(aggr_data: list[Any]):
    ret = []
    for item in aggr_data:
        for i in range (0, item[1]):
            ret.append(item[2])
    return ret

def move_full(data: list[Any], file: int) -> None:
    
    for i in range(len(data) - 1, -1, -1):
        item = data[i]
        file_pos = item[0]
        file_len = item[1]
        file_name = item[2]
        is_file = file_name != "."

        if file_name == file:
            if is_file:
                index_found = -1

                for j in range (0, len(data)):
                    gap = data[j]
                    gap_pos = gap[0]
                    gap_len = gap[1]
                    is_gap = (gap[2] == ".")
                    # search for gap no smaller than file and located left to file position
                    if is_gap and gap_len >= file_len and gap_pos < file_pos:
                        index_found = j
                        break

                if index_found != -1:
                    # gap and file are the same length
                    if gap_len == file_len:
                        # move file to gap
                        data[index_found] = (data[index_found][0], data[index_found][1], item[2])
                        # clear file in old position
                        data[i] = (file_pos, file_len, ".")
                    # gap is bigger than a file
                    elif gap_len > file_len:
                        gap_len = data[index_found][1] - file_len
                        gap_start = data[index_found][0] + file_len
                        # move file to gap
                        data[index_found] = (data[index_found][0], file_len, item[2])
                        # clear file in old position
                        data[i] = (file_pos, file_len, ".")
                        # create new gap from leftovers
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

    raw_data, _, _ = extract_data(input)

    move(raw_data)
    count = compute_checksum(raw_data)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    _, aggr_data, max_value = extract_data(input)

    for i in range(max_value, -1, -1):
        move_full(aggr_data, i)

    count = compute_checksum(convert_to_raw(aggr_data))

    print(f"Solved 2: {count}")
