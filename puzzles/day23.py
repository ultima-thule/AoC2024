from collections import defaultdict
from itertools import chain, combinations

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    pairs = set()
    vertices = set()
    adjacent = {}

    for line in input:
        tmp = line.strip().split("-")
        pairs.add((tmp[0], tmp[1]))
        vertices.add(tmp[1])
        vertices.add(tmp[0])
    
    for v in vertices:
        adjacent[v] = []

    for p in pairs:
        adjacent[p[0]].append(p[1])
        adjacent[p[1]].append(p[0])

    # print(f"Pairs: {pairs}")
    # print(f"vertices: {vertices}")
    # print(f"adjacent: {adjacent}")

    return pairs, vertices, adjacent

def execute_part_one(input: list[str]) -> None:
    count = 0

    pairs, vertices, adjacent = extract_data(input)

    found = set()

    for k, v in adjacent.items():
        # print(f"Adj: {k}, {v}")
        for i in range(0, len(v)):
            item_b = v[i]
            # print(f"{k} {item_b}")
            for j in range (i + +1, len(v)):
                item_c = v[j]
                if (item_b, item_c) in pairs or (item_c, item_b) in pairs:
                    # print(f"Found! {k}, {item_b}, {item_c}")
                    lst = []
                    lst.append(k)
                    lst.append(item_b)
                    lst.append(item_c)
                    lst.sort()
                    res = ','.join(lst)
                    if k.startswith("t") or item_b.startswith("t") or item_c.startswith("t"):
                        found.add(res)

    # print(f"\nTotal: {len(found)}")
   
    print(f"Solved 1: {len(found)}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    pairs, vertices, adjacent = extract_data(input)

    lens = list()

    for k,v in adjacent.items():
        s = set(v)
        s.add(k)
        lens.append(s)

    inter = defaultdict(int)

    for i in range(0, len(lens)):
        item_a = lens[i]
        for j in range (i+1, len(lens)):
            item_b = lens[j]
            tmp = item_a & item_b
            inter[",".join(sorted(tmp))] += 1

    inv_map = defaultdict(list)
    for k, v in inter.items():
        inv_map[v].append(k)

    # print(f"\nLens: {lens}")
    # print(f"\nInter: {inter}")
    # print(f"\ninv_map: {inv_map}")

    print(f"Solved 2: {inv_map[list(inv_map)[-1]]}")
