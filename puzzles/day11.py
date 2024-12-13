def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for line in input:
        spl = line.split()
        data += [int(x) for x in spl]

    print(f"Data: {data}")

    return data

def transform(stone) -> list[int]:
    # stone with num 0
    if stone == 0:
        # print(f"Stone: {stone} replaced by [1]")
        return [1]
    
    # even number of digits
    stone_str = str(stone)
    digits_num = len(stone_str)
    mid = int(digits_num / 2)
    if digits_num % 2 == 0:
        # print(f"Digits num {digits_num}, mid: {mid}")
        left = stone_str[:mid]
        right = stone_str[mid:]
        # print(f"Stone: {stone} replaced by [{left}, {right}]")
        return [int(left), int(right)]
    
    # other case - multiply by 2024
    # print(f"Stone: {stone} multiplied by 2024: [{stone*2024}]")
    return [stone * 2024]
    
def blink(stones, blinks_number):
    # print(f"Starting stones {stones}, blinking {blinks_number} times")
    for b in range(0, blinks_number):
        # print(f"=> Blink #{b+1}, stones before {stones}")
        blink_after = []
        for s in stones:
            blink_after += transform(s)
        stones = blink_after
        # print(f"=> Blink #{b+1}, stones after {stones}")

    return len(stones)


def execute_part_one(input: list[str]) -> None:
    count = 0

    data = extract_data(input)

    count = blink(data, 25)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    # for l in extract_data(input):
    #     pass

    print(f"Solved 2: {count}")
