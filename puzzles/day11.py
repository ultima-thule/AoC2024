import sys
from collections import defaultdict

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for line in input:
        spl = line.split()
        data += [int(x) for x in spl]

    return data

def transform(stone, count, blink_freq):
    # stone with num 0
    if stone == 0:
        blink_freq[0] -= count
        blink_freq[1] += count
        return
    
    stone_str = str(stone)
    digits_num = len(stone_str)

    # even number of digits
    if digits_num % 2 == 0:
        mid = int(digits_num / 2)
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        blink_freq[stone] -= count
        blink_freq[left] += count
        blink_freq[right] += count
        return

    # other case - multiply by 2024
    blink_freq[stone] -= count
    blink_freq[stone * 2024] += count
    return
    
def init_freq(stones):
    freq = defaultdict(int)
    for s in stones:
        freq[s] = 1

    return freq

def count_freq(freq):
    count = 0
    for k,v in freq.items():
        count += v

    return count

def blink(stones, blinks_number):

    blink_freq = init_freq(stones)

    for b in range(0, blinks_number):
        iter_dict = blink_freq.copy()
        for k, v in iter_dict.items():
            if v != 0:
                transform(k, v, blink_freq)

    return count_freq(blink_freq)


def execute_part_one(input: list[str]) -> None:
    count = 0

    data = extract_data(input)
    count = blink(data, 25)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    data = extract_data(input)
    count = blink(data, 75)

    print(f"Solved 2: {count}")
