def get_program(file_name):
    with open(file_name) as f:
        program = [int(i) for i in f.readline().rstrip().split(",")]
    return program

def fetch_opcode(pointer):
    opcode = program[pointer]
    return opcode

def run_opcode(opcode, pointer):
    opcode = str(opcode)
    paramodes = ["0", "0", "0"]
    pointer += 1
    if len(opcode) > 2:
        paramodes = [i for i in opcode[:-2]]
        paramodes.reverse()
        while len(paramodes) < 3:
            paramodes.append("0")
    if opcode[-1] == "1":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer += 1
        operand_2 = fetch_value(program[pointer], paramodes[1])
        pointer += 1
        pointer = add(operand_1, operand_2, pointer)
    if opcode[-1] == "2":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer += 1
        operand_2 = fetch_value(program[pointer], paramodes[1])
        pointer += 1
        pointer = multiply(operand_1, operand_2, pointer)
    if opcode[-1] == "3":
        pointer = write_input(pointer)
    if opcode[-1] == "4":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer = output(operand_1, pointer)
    if opcode[-1] == "5":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer += 1
        operand_2 = fetch_value(program[pointer], paramodes[1])
        pointer = jump_if_true(operand_1, operand_2, pointer)
    if opcode[-1] == "6":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer += 1
        operand_2 = fetch_value(program[pointer], paramodes[1])
        pointer = jump_if_false(operand_1, operand_2, pointer)
    if opcode[-1] == "7":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer += 1
        operand_2 = fetch_value(program[pointer], paramodes[1])
        pointer += 1
        pointer = less_than(operand_1, operand_2, pointer)
    if opcode[-1] == "8":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer += 1
        operand_2 = fetch_value(program[pointer], paramodes[1])
        pointer += 1
        pointer = equals(operand_1, operand_2, pointer)
    if opcode == "99":
        return ""
    return pointer

def fetch_value(address, paramode):
    if paramode == "0":
        value = program[address]
    if paramode == "1":
        value = address
    return value

def add(operand_1, operand_2, pointer):
    address = program[pointer]
    program[address] = operand_1 + operand_2
    pointer += 1
    return pointer

def multiply(operand_1, operand_2, pointer):
    address = program[pointer]
    program[address] = operand_1 * operand_2
    pointer += 1
    return pointer

def write_input(pointer):
    address = program[pointer]
    program[address] = int(input())
    pointer += 1
    return pointer

def output(operand_1, pointer):
    print(operand_1)
    pointer += 1
    return pointer

def jump_if_true(operand_1, operand_2, pointer):
    if operand_1 != 0:
        pointer = operand_2
    else:
        pointer += 1
    return pointer

def jump_if_false(operand_1, operand_2, pointer):
    if operand_1 == 0:
        pointer = operand_2
    else:
        pointer += 1
    return pointer

def less_than(operand_1, operand_2, pointer):
    address = program[pointer]
    if operand_1 < operand_2:
        program[address] = 1
    else:
        program[address] = 0
    pointer += 1
    return pointer

def equals(operand_1, operand_2, pointer):
    address = program[pointer]
    if operand_1 == operand_2:
        program[address] = 1
    else:
        program[address] = 0
    pointer += 1
    return pointer

def main():
    pointer = 0
    while pointer != "":
        opcode = fetch_opcode(pointer)
        pointer = run_opcode(opcode, pointer)

phase_sequence = [int(phase) for phase in str(i).zfill(5)]


    

