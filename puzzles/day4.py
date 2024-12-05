def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for i in range (0, len(input)):
        data.append([*input[i].strip()])

    # print(data)
    return data

def is_in_range(data, y, vector_y_left, vector_y_right, x, vector_x_left, vector_x_right) -> bool:
    max_x = len(data[0])
    max_y = len(data)

    if  y + vector_y_left < 0 or y + vector_y_right >= max_y:
        return False
    if x + vector_x_left < 0 or x + vector_x_right >= max_x:
        return False
    
    return True

def validate_single_word(data, y: int, x: int, incr_y: int, incr_x: int) -> int:
    if data[y][x] == 'X' and data[y+incr_y][x+incr_x] == 'M' and data[y+2*incr_y][x+2*incr_x] == 'A' and data[y+3*incr_y][x+3*incr_x] == 'S':
        return 1

    return 0

def get_vector_right(inc: int) -> int:
    return 0 if inc <= 0 else 3 * inc

def get_vector_left(inc: int) -> int:
    return 0 if inc >= 0 else 3 * inc

def check_word(data, y: int, x: int, incr_y: int, incr_x: int) -> int:
    vector_y_left = get_vector_left(incr_y)
    vector_y_right = get_vector_right(incr_y)
    vector_x_left = get_vector_left(incr_x)
    vector_x_right = get_vector_right(incr_x)

    if not is_in_range(data, y, vector_y_left, vector_y_right, x, vector_x_left, vector_x_right):
        return 0

    return validate_single_word(data, y, x, incr_y, incr_x) 

def check_xmas(data, y: int, x: int) -> int:
    if not is_in_range(data, y, -1, 1, x, -1, 1):
        return 0           
    
    if data[y][x] != 'A':
        return 0

    if (data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S') or (data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M'):
        if (data[y-1][x+1] == 'M' and data[y+1][x-1] == 'S') or (data[y-1][x+1] == 'S' and data[y+1][x-1] == 'M'):
            return 1
    
    return 0

def execute_part_one(input: list[str]) -> None:
    count = 0
    data = extract_data(input)

    for i in range (0, len(data)):
        for j in range (0, len(data[i])):
            count += check_word(data, i, j, 0, 1)
            count += check_word(data, i, j, 0, -1)
            count += check_word(data, i, j, -1, 0)
            count += check_word(data, i, j, 1, 0)
            count += check_word(data, i, j, 1, 1)
            count += check_word(data, i, j, 1, -1)
            count += check_word(data, i, j, -1, 1)
            count += check_word(data, i, j, -1, -1)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0
    data = extract_data(input)

    for i in range (0, len(data)):
        for j in range (0, len(data[i])):
            count += check_xmas(data, i, j)     

    print(f"Solved 2: {count}")
