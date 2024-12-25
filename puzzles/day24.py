from collections import deque

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    gates = {}
    conn = {}
    q = deque()

    start_connections = False

    for line in input:
        line = line.strip()
        if line == "":
            start_connections = True
            continue
        if not start_connections:
            tmp = line.split(": ")
            gates[tmp[0]] = tmp[1] == "1"
        else:
            tmp = line.split(" -> ")
            left = tmp[0].split(" ")
            q.append((left[0], left[2], left[1], tmp[1]))

    # print(gates)
    # print(q)

    return gates, q

def calc(oper1, oper2, action):
    if action == "AND":
        return oper1 & oper2    
    if action == "OR":
        return oper1 | oper2
    if action == "XOR":
        return oper1 ^ oper2

def decode_bits(gates, letter):
    new_dict = {k: v for k, v in gates.items() if k.startswith(letter)}
    tmp = dict(sorted(new_dict.items(), reverse = True))

    binary = ""
    for k, v in tmp.items():
        binary += str(int(v))

    # print(f"{letter}: {binary} => {int(binary, 2)}")

    return binary, int(binary, 2)

def simulate(gates, conn):

    while len(conn) > 0:

        elem = conn.popleft()

        oper1 = elem[0]
        oper2 = elem[1]
        # print(f"=> Checking: {oper1} {oper2}")
        if oper1 in gates and oper2 in gates:
            o1 = gates[oper1]
            o2 = gates[oper2]
            action = elem[2]
            save_to = elem[3]
            result = calc(o1, o2, action)
            # print(f"{oper1}={o1} {action} {oper2}={o2} = {result} save to {save_to}")
            gates[save_to] = result
        else:
            conn.append(elem)

    # print(f"Results: {gates}")

    x_bin, x = decode_bits(gates, "x")
    y_bin, y = decode_bits(gates, "y")
    z_bin, z = decode_bits(gates, "z")

    return x, y, z, x_bin, y_bin, z_bin

def execute_part_one(input: list[str]) -> None:

    gates, conn =  extract_data(input)
    x, y, z, _,  _, _ = simulate(gates, conn)

    print(f"Solved 1: {z}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    gates, conn =  extract_data(input)
    x, y, z, x_bin, y_bin, z_bin = simulate(gates, conn)

    expected = x & y
    exp_str = f"{expected:b}"
    print(f"Expected {exp_str}")
    print(f"Current- {z_bin}")

    diff = x + y - z

    print(f"Difference: {diff:b}")
    
    diff_str = f"{diff:b}"
    for i in range(len(diff_str)-1, -1, -1):
        # print(f"{exp_str[i]}-{curr_str[i]}")
        if diff_str[i] != "0":
            print(f"Wrong bit at pos {i}")

    print(f"Solved 2: {count}")
