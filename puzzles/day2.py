def extract_data(input: list[str]):
    '''Extract and transform text data'''
    for line in input:
        lst = [int(x) for x in line.split()]
        yield lst


def sign_of(number: int):
    '''Calculate mathematical sign of number'''
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def is_diff_allowed(diff: int) -> bool:
    '''Determine if the difference is allowed'''
    return (abs(diff) >= 1 and abs(diff) <= 3)


def are_all_same_dir(sum_of_dirs: int, report: list[int]) -> bool:
    ''' abs of summed up direction signs should be equal to length of report - 1'''
    return (abs(sum_of_dirs) == len(report)-1)


def is_safe_report(report: list[int]) -> bool:
    '''Determine whether a single report is safe'''
    ret = True
    sum_of_vectors = 0

    for i in range(0, len(report)-1):
        # compare pairs of numbers
        diff = report[i] - report[i+1]
        # determine whether direction is decreasing or increasing
        vector = sign_of(diff)
        # check if difference is allowed and direction is either increasing or decreasing
        ret &= is_diff_allowed(diff) & (dir != 0)
        # sum direction signs
        sum_of_vectors += vector

    # check if all directions were increasing or all were decreasing
    return ret & are_all_same_dir(sum_of_vectors, report)


def altered_reports(report: list[int]):
    '''Generate all variant of given list with one element removed'''
    for i in range(len(report)):
        yield report[:i] + report[i+1:]


def execute_part_one(input: list[str]) -> None:
    count = 0

    for line in extract_data(input):
        if is_safe_report(line):
            count += 1

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    for line in extract_data(input):
        safe = is_safe_report(line)
        if not safe:
            for a in altered_reports(line):
                if is_safe_report(a):
                    safe = True
                    break
        if safe:
            count += 1

    print(f"Solved 2: {count}")
