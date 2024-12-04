def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []
    for i in range (0, len(input)):
        data.append([*input[i].strip()])

    # print(data)
    return data

def validate_position(data, y, vector_y_left, vector_y_right, x, vector_x_left, vector_x_right) -> bool:
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    if  y + vector_y_left < min_y or y + vector_y_right >= max_y:
        return False
    if x + vector_x_left < min_x or x + vector_x_right >= max_x:
        return False
    
    return True


def check_right(data, y: int, x: int) -> int:
    if not validate_position(data, y, 0, 0, x, 0, 3):
        return 0
   
    row = data[y]
    if row[x] == 'X' and row[x+1] == 'M' and row[x+2] == 'A' and row[x+3] == 'S':
        return 1
    
    return 0

def check_left(data, y: int, x: int) -> int:
    if not validate_position(data, y, 0, 0, x, -3, 0):
        return 0
    
    row = data[y]
    if row[x] == 'X' and row[x-1] == 'M' and row[x-2] == 'A' and row[x-3] == 'S':
        return 1
    
    return 0

def check_top(data, y: int, x: int) -> int:
    if not validate_position(data, y, -3, 0, x, 0, 0):
        return 0
   
    if data[y][x] == 'X' and data[y-1][x] == 'M' and data[y-2][x] == 'A' and data[y-3][x] == 'S':
        return 1
    
    return 0

def check_down(data, y: int, x: int) -> int:
    if not validate_position(data, y, 0, 3, x, 0, 0):
        return 0
    
    if data[y][x] == 'X' and data[y+1][x] == 'M' and data[y+2][x] == 'A' and data[y+3][x] == 'S':
        return 1
    
    return 0

def check_diag_down_right(data, y: int, x: int) -> int:
    if not validate_position(data, y, 0, 3, x, 0, 3):
        return 0
    
    if data[y][x] == 'X' and data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S':
        return 1
    
    return 0

def check_diag_down_left(data, y: int, x: int) -> int:
    if not validate_position(data, y, 0, 3, x, -3, 0):
        return 0    
    
    if data[y][x] == 'X' and data[y+1][x-1] == 'M' and data[y+2][x-2] == 'A' and data[y+3][x-3] == 'S':
        return 1
    
    return 0

def check_diag_up_right(data, y: int, x: int) -> int:
    if not validate_position(data, y, -3, 0, x, 0, 3):
        return 0       
    
    if data[y][x] == 'X' and data[y-1][x+1] == 'M' and data[y-2][x+2] == 'A' and data[y-3][x+3] == 'S':
        return 1
    
    return 0

def check_diag_up_left(data, y: int, x: int) -> int:
    if not validate_position(data, y, -3, 0, x, -3, 0):
        return 0         
    
    if data[y][x] == 'X' and data[y-1][x-1] == 'M' and data[y-2][x-2] == 'A' and data[y-3][x-3] == 'S':
        return 1
    
    return 0

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
    data = extract_data(input)

    for i in range (0, len(data)):
        for j in range (0, len(data[i])):
            count += check_xmas(data, i, j)     

    print(f"Solved 2: {count}")
