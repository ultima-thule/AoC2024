from sympy import symbols, Eq, solve
from sympy.core.numbers import Integer

def simulate(a_x: int, a_y: int, b_x: int, b_y: int, p_x: int, p_y: int, is_part_two: bool) -> int:
    '''Use numpy to solve two equations with two unknows'''
    a, b = symbols('a b')

    eq1 = Eq((a * a_x) + (b * b_x), p_x if not is_part_two else p_x + 10000000000000)
    eq2 = Eq((a * a_y) + (b * b_y), p_y if not is_part_two else p_y + 10000000000000)

    result = solve((eq1,eq2), (a, b))

    # no solution
    if result[a] < 0 or result[b] < 0:
        return 0
    
    # only integer solutions
    if isinstance(result[a], Integer) and isinstance(result[b], Integer):
        return (result[a] * 3) + result[b]
    
    return 0
