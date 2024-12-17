import re

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    registers = {}
    registers["pointer"] = 0
    registers["output"] = ""
    registers["program"] = ""
    data = []

    for line in input:
        if line.startswith("Register A: "):
            registers["A"] = int(extract_numbers(line, False))
        elif line.startswith("Register B: ",):
            registers["B"] = int(extract_numbers(line, False))
        elif line.startswith("Register C: "):
            registers["C"] = int(extract_numbers(line, False))
        elif line.startswith("Program: "):
            registers["program"] = extract_numbers(line, True)
            program = [int(x) for x in registers["program"].split(",")]

    # print(f"Reg A: {reg_a}, Reg B: {reg_b}, Reg C: {reg_c}, Data: {data}")

    return registers, program

def extract_numbers(line: str, is_program: bool) -> tuple[int, int]:
    '''Extract numeric data from single line of text'''
    spl = line.strip()
    # line contains button definitions
    if not is_program:
        pattern = r'Register [ABC]: ([\d]+)'
    # line contains prize definitions
    else:
        pattern = r'Program: ([\d,]*)'
    result = re.search(pattern, line)

    return result.group(1)

def combo_value(operand, registers):
    if operand == 0 or operand == 1 or operand == 2 or operand == 3:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]

def adv(registers, combo):
    numerator = registers["A"]
    denominator = 2**combo_value(combo, registers)

    result = int(numerator / denominator)
    # print(f"adv {numerator} / {denominator} = {result}")
    registers["A"] = result
    registers["pointer"] += 2

def bxl(registers, literal):
    result = registers["B"] ^ literal
    # print(f"bxl {registers['B']} ^ {literal} = {result}")
    registers["B"] = result
    registers["pointer"] += 2

def bst(registers, combo):
    result = combo % 8
    # print(f"bst {combo} % 8 = {result}")
    registers["B"] = result
    registers["pointer"] += 2

def jnz(registers, literal):
    if registers["A"] == 0:
        registers["pointer"] += 2
        return
    # print(f"jnz to {literal}")
    registers["pointer"] = literal

def bxc(registers, literal):
    result = registers["B"] ^ registers["C"]
    # print(f"bxc {registers['B']} ^ {registers['C']} = {result}")
    registers["B"] = result
    registers["pointer"] += 2

def out(registers, combo):
    result = combo % 8
    # print(f"out {combo} % 8 = {result}")
    registers["output"] += f"{result},"
    registers["pointer"] += 2

def bdv(registers, combo):
    numerator = registers["A"]
    denominator = 2**combo_value(combo, registers)

    result = int(numerator / denominator)
    # print(f"bdv {numerator} / {denominator} = {result}")
    registers["B"] = result
    registers["pointer"] += 2

def cdv(registers, combo):
    numerator = registers["A"]
    denominator = 2**combo_value(combo, registers)

    result = int(numerator / denominator)
    # print(f"cdv {numerator} / {denominator} = {result}")
    registers["C"] = result
    registers["pointer"] += 2

def run_op(opcode, operand, registers):
    combo = combo_value(operand, registers)
    match opcode:
        case 0:
            adv(registers, combo)
        case 1:
            bxl(registers, operand)
        case 2:
            bst(registers, combo)
        case 3:
            jnz(registers, operand)
        case 4:
            bxc(registers, operand)
        case 5:
            out(registers, combo)
        case 6:
            bdv(registers, operand)
        case 7:
            cdv(registers, operand)                                                                        

    # print(f"Registers: {registers}")

def execute_part_one(input: list[str]) -> None:
    count = 0

    registers, program = extract_data(input)
    pointer = registers["pointer"]
    while pointer < len(program):
        # print(f"Pointer {pointer}/{len(program)}: opcode: {program[pointer]}: operand: {program[pointer+1]}")
        run_op(program[pointer], program[pointer+1], registers)
        pointer = registers["pointer"]

    print(f"Solved 1: {registers['output']}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    registers, program = extract_data(input)
    for i in range(100001, 2000001):
        registers["A"] = i
        registers["pointer"] = 0
        registers["output"] = ""
        pointer = registers["pointer"]
        while pointer < len(program):
            # print(f"Pointer {pointer}/{len(program)}: opcode: {program[pointer]}: operand: {program[pointer+1]}")
            run_op(program[pointer], program[pointer+1], registers)
            pointer = registers["pointer"]
        if registers["output"][:-1] == registers["program"]:
            print("Found!")
            print(f"Registers: {registers['output'][:-1]}{registers['program']}")            

    print(f"Solved 2: {count}")
