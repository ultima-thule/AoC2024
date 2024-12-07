import sys

def extract_data(input: list[str]):
    input_data = {}
    equations = {}

    for line in input:
        key = line.strip()
        fl = key.split(":")
        sl = fl[1].strip().split()
        input_data[key] = [fl[0], sl]
        equations[key] = False

    return input_data, equations

def calculate(a, b, operation) -> int:
    '''Calculate result of operation'''
    if operation == "+":
        return int(a) + int(b)
    if operation == "*":
        return int(a) * int(b)
    if operation == "||":
        return int(str(a) + str(b))


def calc_step(expected, subtotal, numbers_left, equations, key, with_concat):
    '''Executes single calculations step'''

    # all numbers used in an equation 
    if len(numbers_left) == 0:
        # OR result to previously saved equation variations results
        equations[key] |= (subtotal == expected)
        return

    # no valid equation variation found yet
    if not equations[key]:
        # pick next starting number
        start_num = numbers_left[0]
        # trim leftover numbers
        left_numbers = numbers_left[1:]

        # spawn next variants
        c1 = calculate(subtotal, start_num, "*")
        calc_step (expected, c1, left_numbers, equations, key, with_concat) 

        c2 = calculate(subtotal, start_num, "+")
        calc_step (expected, c2, left_numbers, equations, key, with_concat)

        if with_concat:
            c3 = calculate(subtotal, start_num, "||")
            calc_step (expected, c3, left_numbers, equations, key, with_concat)


def validate (eq_data, eq_key, equations, with_concat):
    '''Validates whether the equation has at least one solution'''
    expected = int(eq_data[0])
    numbers = eq_data[1]

    start_num = numbers[0]
    numbers_left = numbers[1:]

    return calc_step(expected, start_num, numbers_left, equations, eq_key, with_concat)


def execute_part_one(input: list[str]) -> None:
    count = 0

    input_data, equations = extract_data(input)

    #iterate throgh calibration equations, excluding concat operator
    for k in input_data:
        validate(input_data[k], k, equations, False)

        # equation is valid
        if equations[k]:
            count += int(input_data[k][0])

    print(f"\nSolved 1: {count} ")


def execute_part_two(input: list[str]) -> None:
    count = 0

    input_data, equations = extract_data(input)

    #iterate throgh calibration equations, including concat operator
    for k in input_data:
        validate(input_data[k], k, equations, True)

        # equation is valid
        if equations[k]:
            count += int(input_data[k][0])

    print(f"Solved 2: {count}")
