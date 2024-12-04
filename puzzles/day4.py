def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for i in range (0, len(input)):
        data.append([*input[i].strip()])

    # print(data)
    return data

def validate_position(data, y, vector_y_left, vector_y_right, x, vector_x_left, vector_x_right) -> bool:
    max_x = len(data[0])
    max_y = len(data)

    if  y + vector_y_left < 0 or y + vector_y_right >= max_y:
        return False
    if x + vector_x_left < 0 or x + vector_x_right >= max_x:
        return False
    
    return True

def check_uni(data, y: int, x: int, incr_y: int, incr_x: int) -> int:
    if data[y][x] == 'X' and data[y+incr_y][x+incr_x] == 'M' and data[y+2*incr_y][x+2*incr_x] == 'A' and data[y+3*incr_y][x+3*incr_x] == 'S':
        return 1

    return 0


def check_all(data, y: int, x: int, incr_y: int, incr_x: int) -> int:
    vector_y_left = 0 if incr_y >= 0 else 3 * incr_y
    vector_y_right = 0 if incr_y <= 0 else 3 * incr_y
    vector_x_left = 0 if incr_x >= 0 else 3 * incr_x
    vector_x_right = 0 if incr_x <= 0 else 3 * incr_x

    if not validate_position(data, y, vector_y_left, vector_y_right, x, vector_x_left, vector_x_right):
        return 0

    return check_uni(data, y, x, incr_y, incr_x) 

def check_xmas(data, y: int, x: int) -> int:
    if not validate_position(data, y, -1, 1, x, -1, 1):
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
            count += check_all(data, i, j, 0, 1)
            count += check_all(data, i, j, 0, -1)
            count += check_all(data, i, j, -1, 0)
            count += check_all(data, i, j, 1, 0)
            count += check_all(data, i, j, 1, 1)
            count += check_all(data, i, j, 1, -1)
            count += check_all(data, i, j, -1, 1)
            count += check_all(data, i, j, -1, -1)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0
    data = extract_data(input)

    for i in range (0, len(data)):
        for j in range (0, len(data[i])):
            count += check_xmas(data, i, j)     

    print(f"Solved 2: {count}")
