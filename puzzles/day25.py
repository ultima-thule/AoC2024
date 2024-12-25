def extract_data(input: list[str]):
    '''Extract and transform text data'''
    keys = []
    locks = []
    start_new = True
    is_lock = True
    curr = []

    for line in input:
        line = line.strip()
        if line == "":
            start_new = True
            continue
        if start_new:
            # save previous and reset
            if is_lock:
                locks.append(curr[:-1])
            else:
                keys.append(curr[:-1])
            curr = []
            if line == "#####":
                is_lock = True
            elif line == ".....":
                is_lock = False
            start_new = False
        else:
            curr.append(line)

    if is_lock:
        locks.append(curr[:-1])
    else:
        keys.append(curr[:-1])

    if len(locks[0]) == 0:
        locks = locks[1:]

    if len(keys[0]) == 0:
        keys = keys[1:]

    return keys, locks

def to_pins(matrix):
    pin_defs = []

    for m in matrix:
        counters = [0] * len(m[0])
        for r in m:
            for j in range(len(r)):
                if r[j] == "#":
                    counters[j] += 1
        pin_defs.append(counters)

    return pin_defs

def execute_part_one(input: list[str]) -> None:
    count = 0

    keys, locks = extract_data(input)

    keys_pins = to_pins(keys)
    locks_pins = to_pins(locks)

    for k in keys_pins:
        for l in locks_pins:
            z = [x + y for x, y in zip(k, l)]
            ok = True
            for i in z:
                if i > 5:
                    ok = False
                    break
            if ok:
                count += 1

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    print(f"Solved 2: {count}")
