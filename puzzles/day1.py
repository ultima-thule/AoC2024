def extract_data(input: list[str]) -> tuple[list[int], list[int]]:
    # print(input)
    # extract and transform data
    data1 = []
    data2 = []
    for line in input:
        x = line.split()
        data1.append(int(x[0]))
        data2.append(int(x[1]))

    return data1, data2

def execute_part_one(input: list[str]) -> None:
    data_1, data_2 = extract_data(input)

    # sort both lists asc
    data_1.sort()
    data_2.sort()

    # calculate absolute distance and add to sum
    total = 0
    for i in range(0, len(data_1)):
        total += abs(data_1[i] - data_2[i])

    print(f"Solved 1: {total}")


def execute_part_two(input: list[str]) -> None:
    data1, data2 = extract_data(input)

    # calculate no of occurences in second list
    dict = {}
    for i in data2:
        dict[i] = dict[i] + 1 if i in dict else 1
    # print(dict)

    #calculate score for first list based on occurrences in second list
    total = 0
    for i in data1:
        total += (i * dict[i] if i in dict else 0)

    print(f"Solved 2: {total}")
