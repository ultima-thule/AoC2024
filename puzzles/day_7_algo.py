from typing import Any

def calculate(a: str | int, b: str | int, operation: str) -> int:
    '''Calculate result of operation'''
    if operation == "+":
        return int(a) + int(b)
    if operation == "*":
        return int(a) * int(b)
    if operation == "||":
        return int(str(a) + str(b))
    return 0


def calc_step(expected: int, subtotal: int, numbers_left: list[str], solutions: dict[str, bool], sol_key: str, with_concat: bool) -> None:
    '''Executes single calculations step'''

    # all numbers used in an equation 
    if len(numbers_left) == 0:
        # save result and finish
        solutions[sol_key] |= (subtotal == expected)
        return

    # no valid equation variation found yet
    if not solutions[sol_key]:
        # pick next starting number
        start_num = numbers_left[0]
        # trim leftover numbers
        numbers_left = numbers_left[1:]

        # spawn next variants for +, * and ||
        c1 = calculate(subtotal, start_num, "*")
        calc_step (expected, c1, numbers_left, solutions, sol_key, with_concat) 

        c2 = calculate(subtotal, start_num, "+")
        calc_step (expected, c2, numbers_left, solutions, sol_key, with_concat)

        if with_concat:
            c3 = calculate(subtotal, start_num, "||")
            calc_step (expected, c3, numbers_left, solutions, sol_key, with_concat)


def validate (eq_data: list[Any], sol_key: str, solutions: dict[str, bool], with_concat: bool) -> None:
    '''Validates whether the equation has at least one solution'''
    expected = int(eq_data[0])
    numbers = eq_data[1]

    return calc_step(expected, int(numbers[0]), numbers[1:], solutions, sol_key, with_concat)


def execute(input_data: dict[str, list[Any]], solutions: dict[str, bool], scenario: int, with_concat: bool) -> None:
    count = 0

    #iterate throgh calibration equations, in- or excluding concat operator
    for k in input_data:
        validate(input_data[k], k, solutions, with_concat)

        # equation is valid
        if solutions[k]:
            count += int(input_data[k][0])

    print(f"\nSolved {scenario}: {count} ")