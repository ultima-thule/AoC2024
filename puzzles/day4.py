def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for i in range (0, len(input)):
        data.append([*input[i].strip()])

    print(data)
    return data

def check_right(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr >= max_y or row_nr < min_y:
        return 0
    if x < min_x or x + 3 >= max_x:
        return 0
    
    row = data[row_nr]

    if row[x] == 'X' and row[x+1] == 'M' and row[x+2] == 'A' and row[x+3] == 'S':
        print(f"Found RIGHT: row {row_nr} position {x}")
        return 1
    
    return 0

def check_left(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr >= max_y or row_nr < min_y:
        return 0
    if x - 3 < min_x or x >= max_x:
        return 0
    
    row = data[row_nr]

    if row[x] == 'X' and row[x-1] == 'M' and row[x-2] == 'A' and row[x-3] == 'S':
        print(f"Found LEFT: row {row_nr} position {x}")
        return 1
    
    return 0

def check_top(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr >= max_y or row_nr - 3 < min_y:
        return 0
    if x < min_x or x >= max_x:
        return 0
    
    if data[row_nr][x] == 'X' and data[row_nr-1][x] == 'M' and data[row_nr-2][x] == 'A' and data[row_nr-3][x] == 'S':
        print(f"Found TOP: row {row_nr} position {x}")
        return 1
    
    return 0

def check_down(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr + 3 >= max_y or row_nr < min_y:
        return 0
    if x < min_x or x >= max_x:
        return 0
    
    if data[row_nr][x] == 'X' and data[row_nr+1][x] == 'M' and data[row_nr+2][x] == 'A' and data[row_nr+3][x] == 'S':
        print(f"Found DOWN: row {row_nr} position {x}")
        return 1
    
    return 0

def check_diag_down_right(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr + 3 >= max_y or row_nr < min_y:
        return 0
    if x < min_x or x + 3 >= max_x:
        return 0
    
    if data[row_nr][x] == 'X' and data[row_nr+1][x+1] == 'M' and data[row_nr+2][x+2] == 'A' and data[row_nr+3][x+3] == 'S':
        print(f"Found DIAG DOWN RIGHT: row {row_nr} position {x}")
        return 1
    
    return 0

def check_diag_down_left(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr + 3 >= max_y or row_nr < min_y:
        return 0
    if x - 3 < min_x or x >= max_x:
        return 0
    
    if data[row_nr][x] == 'X' and data[row_nr+1][x-1] == 'M' and data[row_nr+2][x-2] == 'A' and data[row_nr+3][x-3] == 'S':
        print(f"Found DIAG DOWN LEFT: row {row_nr} position {x}")
        return 1
    
    return 0

def check_diag_up_right(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr >= max_y or row_nr - 3 < min_y:
        return 0
    if x < min_x or x + 3 >= max_x:
        return 0
    
    if data[row_nr][x] == 'X' and data[row_nr-1][x+1] == 'M' and data[row_nr-2][x+2] == 'A' and data[row_nr-3][x+3] == 'S':
        print(f"Found DIAG UP RIGHT: row {row_nr} position {x}")
        return 1
    
    return 0

def check_diag_up_left(data, row_nr: int, x: int) -> int:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if row_nr >= max_y or row_nr - 3 < min_y:
        return 0
    if x - 3 < min_x or x >= max_x:
        return 0
    
    if data[row_nr][x] == 'X' and data[row_nr-1][x-1] == 'M' and data[row_nr-2][x-2] == 'A' and data[row_nr-3][x-3] == 'S':
        print(f"Found DIAG UP LEFT: row {row_nr} position {x}")
        return 1
    
    return 0

def execute_part_one(input: list[str]) -> None:
    count = 0

    data = extract_data(input)

    for i in range (0, len(data)):
        for j in range (0, len(data[i])):
            right = check_right(data, i, j)
            count += right
            left = check_left(data, i, j)
            count += left
            top = check_top(data, i, j)
            count += top  
            down = check_down(data, i, j)
            count += down    
            diag_down_right = check_diag_down_right(data, i, j)
            count += diag_down_right     
            diag_down_left = check_diag_down_left(data, i, j)
            count += diag_down_left      
            diag_up_right = check_diag_up_right(data, i, j)
            count += diag_up_right   
            diag_up_left = check_diag_up_left(data, i, j)
            count += diag_up_left                                        
                        

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    # data = extract_data(input)

    print(f"Solved 2: {count}")
