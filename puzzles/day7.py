import sys

def extract_data(input: list[str]):
    data = {}
    results = {}

    for line in input:
        fl = line.strip().split(":")
        sl = fl[1].strip().split()
        key = get_key(fl[0], sl)
        data[key] = [fl[0], sl]
        results[key] = False

    # print(data)
    # print(results)
    return data, results

def get_key(total, numbers):
    res = f"{total}"
    for n in numbers:
        res += f",{n}"
    return res

def calculate(a, b, operation):
    if operation == "+":
        return int(a) + int(b)
    if operation == "*":
        return int(a) * int(b)

def calc_step(total, subtotal, numbers_to_do, results, key, oper_string):
    # print(f"Calculating step, subtotal {subtotal}, steps to do {numbers_to_do}, res {results}, key {key}")

    if len(numbers_to_do) == 0:
        results[key] = results[key] or (subtotal == total)
        # print (f"=> {total}: {oper_string} = {subtotal}.\n")

        if subtotal != total:
            pass
            # print (f"=> Subtotal {subtotal} of {total}. Solution found {subtotal == total}, {oper_string}.\n")
        return

    start_num = numbers_to_do[0]
    left_numbers = numbers_to_do[1:]

    c1 = calculate(subtotal, start_num, "*")
    c2 = calculate(subtotal, start_num, "+")

    # print (f"Oper *: {c1}, oper +: {c2}")

    calc_step (total, c1, left_numbers, results, key, oper_string + " * " + start_num) 
    calc_step (total, c2, left_numbers, results, key, oper_string + " + " + start_num)


def validate (total, numbers, results):

    start_num = numbers[0]
    left_numbers = numbers[1:]

    return calc_step(total, start_num, left_numbers, results, get_key(total, numbers), str(start_num))


def execute_part_one(input: list[str]) -> None:
    count = 0

    data, results = extract_data(input)

    #iterate throgh calibration equations
    for k in data:
        # equation is valid
        total = data[k][0]
        numbers = data[k][1]
        validate(int(total), numbers, results)
        is_valid = results[k]
        # print(f"\n===> Checked line: {numbers}, expected result: {total}. Found: {is_valid}")

        if is_valid:
            count += int(total)
        # else:
            # print(f"\n===> Checking line: {data[k]}, expected result: {k}. Solution found: {is_valid}")
    
    # print(f"results len: {len(results)}")
    # print(f"results: {results}")

    print(f"\nSolved 1: {count} ")


def execute_part_two(input: list[str]) -> None:
    count = 0

    # for l in extract_data(input):
    #     pass

    print(f"Solved 2: {count}")
