from collections import defaultdict
from itertools import chain, combinations

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    pairs = set()
    adjacent = defaultdict(list)

    for line in input:
        tmp = line.strip().split("-")
        pairs.add((tmp[0], tmp[1]))

    for p in pairs:
        adjacent[p[0]].append(p[1])
        adjacent[p[1]].append(p[0])

    return pairs, adjacent

def execute_part_one(input: list[str]) -> None:
    pairs, adjacent = extract_data(input)

    found = set()

    for item_a, v in adjacent.items():
        for i in range(0, len(v)):
            item_b = v[i]
            for j in range (i + 1, len(v)):
                item_c = v[j]
                if (item_b, item_c) in pairs or (item_c, item_b) in pairs:
                    if item_a.startswith("t") or item_b.startswith("t") or item_c.startswith("t"):
                        found.add(','.join(sorted([item_a, item_b, item_c])))
   
    print(f"Solved 1: {len(found)}")


def execute_part_two(input: list[str]) -> None:
    _, adjacent = extract_data(input)

    vertices_collections = list()

    # make unified vertices set
    for k,v in adjacent.items():
        s = set(v)
        s.add(k)
        vertices_collections.append(s)

    intersections = defaultdict(int)

    # compare all vertices collections with each other
    for i in range(0, len(vertices_collections)):
        item_a = vertices_collections[i]
        for j in range (i+1, len(vertices_collections)):
            item_b = vertices_collections[j]
            # get intersection
            tmp = item_a & item_b
            # increase counter for the non-empty intersection result
            if len(tmp) > 0:
                intersections[",".join(sorted(tmp))] += 1

    # select intersection with highest count
    sorted_intersections = {k: v for k, v in sorted(intersections.items(), key=lambda item: item[1])}

    print (f"Solved 2: {list(sorted_intersections)[-1]}")