from collections import defaultdict

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for line in input:
        data.append(int(line))

    return data

def step(secret):
    tmp = secret << 6
    secret ^= tmp
    secret &= (2 << 23) - 1

    tmp = secret >> 5
    secret ^= tmp
    secret &= (2 << 23) - 1

    tmp = secret * 2048
    secret ^= tmp
    secret &= (2 << 23) - 1

    return secret

def simulate(num, iters_no):
    curr_secret = num

    d_deltas = [0] * iters_no
    for i in range(iters_no):
        next_sec = step(curr_secret)
        d_deltas[i] = next_sec % 10 - curr_secret % 10
        curr_secret = next_sec

    return curr_secret, d_deltas

def execute_part_one(input: list[str]) -> None:
    count = 0

    data = extract_data(input)

    for d in data:
        last_secret, _ = simulate(d, 2000)
        count += last_secret

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    data = extract_data(input)

    price_deltas = []
    loop_len = 2000

    for d in data:
        _, deltas = simulate(d, loop_len)
        price_deltas.append(deltas)

    price_sums = defaultdict(int)
    for start_sec, delta in zip(data, price_deltas):
        cumulative = {}
        d0, d1, d2 = delta[0:3]
        curr_sum = start_sec % 10 + d0 + d1 + d2
        # print(f"Sum: {curr_sum}")
        for d3 in delta[3:loop_len]:
            # save cumulative sum
            curr_sum += d3
            cumulative.setdefault((d0, d1, d2, d3), curr_sum)
            # move deltas window by 1
            d0, d1, d2 = d1, d2, d3

        # add sum to dictonary of sequences, we will be maximizing that
        for k, v in cumulative.items():
            price_sums[k] += v

    # max sum is the solution
    print(f"Solved 2: {max(price_sums.values())}")
