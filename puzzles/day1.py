def extractData(input: list[str]) -> tuple[list[int], list[int]]:
    # print(input)
    # extract and transform data
    data1 = []
    data2 = []
    for l in input:
        x = l.split()
        data1.append(int(x[0]))
        data2.append(int(x[1]))

    return data1, data2

def executePartOne(input: list[str]) -> None:
    data1, data2 = extractData(input)

    # sort both lists asc
    data1.sort()
    data2.sort()

    # calculate absolute distance and add to sum
    sum = 0
    for i in range(0, len(data1)):
        sum += abs(data1[i] - data2[i])

    print(f"Solved 1: {sum}")


def executePartTwo(input: list[str]) -> None:
    data1, data2 = extractData(input)

    # calculate no of occurences in second list
    dict = {}
    for i in data2:
        dict[i] = dict[i] + 1 if i in dict else 1
    # print(dict)

    #calculate score for first list based on occurrences in second list
    sum = 0
    for i in data1:
        sum += (i * dict[i] if i in dict else 0)

    print(f"Solved 2: {sum}")
