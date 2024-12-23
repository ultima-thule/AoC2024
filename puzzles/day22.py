import math

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for line in input:
        data.append(int(line))

    # print(f"Data: {data}")

    return data

def mix(num, secret):
    res = num ^ secret
    return res

def prune(secret):
    res = secret % 16777216
    return res

def step_1(secret):
    # print(f"Step 1 Secret: {secret}")
    tmp1 = secret * 64
    tmp2 = mix(tmp1, secret)
    tmp3 = prune(tmp2)

    return tmp3

def step_2(secret):
    # print(f"Step 2 Secret: {secret}")
    tmp1 = secret / 32
    tmp2 = math.floor(tmp1)
    tmp3 = mix(tmp2, secret)
    tmp4 = prune(tmp3)

    return tmp4

def step_3(secret):
    # print(f"Step 3 Secret: {secret}")
    tmp1 = secret * 2048
    tmp2 = mix(tmp1, secret)
    tmp3 = prune(tmp2)

    return tmp3

def simulate(num, iters_no):
    curr_secret = num
    for i in range(0, iters_no):
        curr_secret = step_1(curr_secret)
        curr_secret = step_2(curr_secret)
        curr_secret = step_3(curr_secret)
        # print(f"Iteration {i} result {curr_secret}")
    return curr_secret

def execute_part_one(input: list[str]) -> None:
    count = 0

    data = extract_data(input)
       
    for d in data:
        nr = simulate(d, 2000)
        count += nr

    # print(f"Tests: prune {prune(100000000)}")
    # print(f"Tests: mix {mix(15, 42)}")

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    data = extract_data(input)

    print(f"Solved 2: {count}")
