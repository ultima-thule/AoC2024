def extractData(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for l in input:
        lst = [int(x) for x in l.split()]
        yield lst


def signOf(number: int):
    '''Calculate mathematical sign of number'''
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def isDiffAllowed(diff: int) -> bool:
    '''Determine if the difference is allowed'''
    return (abs(diff) >= 1 and abs(diff) <= 3)


def areAllSameDir(sumOfDirs: int, report: list[int]) -> bool:
    ''' abs of summed up direction signs should be equal to length of report - 1'''
    return (abs(sumOfDirs) == len(report)-1)


def isSafeReport(report: list[int]) -> bool:
    '''Determine whether a single report is safe'''
    ret = True
    sumOfDirs = 0

    for i in range(0, len(report)-1):
        # compare pairs of numbers
        diff = report[i] - report[i+1]
        # determine whether direction is decreasing or increasing
        dir = signOf(diff)
        # check if difference is allowed and direction is either increasing or decreasing
        ret &= isDiffAllowed(diff) & (dir != 0)
        # sum direction signs
        sumOfDirs += dir

    # check if all directions were increasing or all were decreasing
    return ret & areAllSameDir(sumOfDirs, report)


def alteredReports(report: list[int]):
    '''Generate all variant of given list with one element removed'''
    for i in range(len(report)):
        yield report[:i] + report[i+1:]


def executePartOne(input: list[str]) -> None:
    count = 0

    for l in extractData(input):
        if isSafeReport(l):
            count += 1

    print(f"Solved 1: {count}")


def executePartTwo(input: list[str]) -> None:
    count = 0

    for l in extractData(input):
        safe = isSafeReport(l)
        if not safe:
            for a in alteredReports(l):
                if isSafeReport(a):
                    safe = True
                    break
        if safe:
            count += 1

    print(f"Solved 2: {count}")
