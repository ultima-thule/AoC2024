def extractData(input):
    # print(input)
    # extract and transform data
    data1 = []
    data2 = []
    for l in input:
        x = l.split()
        data1.append(int(x[0]))
        data2.append(int(x[1]))

    return [data1, data2]

def executePartOne(input):
    data = extractData(input)

    # sort both lists asc
    data[0].sort()
    data[1].sort()

    # calculate absolute distance and add to sum
    sum = 0
    for i in range(0, len(data[0])):
        sum += abs(data[1][i] - data[0][i])

    print(f"Solved 1: {sum}")


def executePartTwo(input):
    data = extractData(input)

    # calculate no of occurences in second list
    dict = {}
    for i in data[1]:
        dict[i] = dict[i] + 1 if i in dict else 1
    # print(dict)

    #calculate score for first list based on occurrences in second list
    sum = 0
    for i in data[0]:
        sum += (i * dict[i] if i in dict else 0)

    print(f"Solved 2: {sum}")
