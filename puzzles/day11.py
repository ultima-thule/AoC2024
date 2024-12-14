import sys
from collections import defaultdict

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for line in input:
        spl = line.split()
        data += [int(x) for x in spl]

    print(f"Data: {data}")

    return data


def transform(stone, count, blink_freq):
    # stone with num 0
    if stone == 0:
        # print(f"Stone: {stone} replaced by [1], count: {blink_freq}")
        blink_freq[0] -= 1 * count
        blink_freq[1] += 1 * count
        return
    
    stone_str = str(stone)
    digits_num = len(stone_str)
    # print(f"Stone {stone} digits num {digits_num}, mid: {mid}")

    # even number of digits
    if digits_num % 2 == 0:
        mid = int(digits_num / 2)
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        blink_freq[stone] -= 1 * count
        blink_freq[left] += 1 * count
        blink_freq[right] += 1 * count
        # print(f"Stone: {stone} replaced by [{left}, {right}], count: {blink_freq}")
        return

    # other case - multiply by 2024
    # print(f"Stone: {stone} multiplied by 2024: [{stone*2024}], count: {blink_freq}")
    blink_freq[stone] -= 1 * count
    blink_freq[stone * 2024] += 1 * count
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

    # print(f"Starting stones {stones}, blinking {blinks_number} times")
    for b in range(0, blinks_number):
        # print(f"\n=> Blink #{b+1}, stones before {blink_freq}")
        # sys.stdout.write("\rBlinking {} of {}".format(b+1, blinks_number))
        # sys.stdout.flush()

        iter_dict = blink_freq.copy()
        for k, v in iter_dict.items():
            if v != 0:
                transform(k, v, blink_freq)
        # stones = blink_after
        # freq = [k for k, v in blink_freq.items() if v > 0]

        # print(f"=> Blink #{b+1}, stones after {blink_freq}\n")
        # print(freq)
        # print(count_freq(blink_freq))


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
