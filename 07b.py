import itertools

def get_program(file_name):
    with open(file_name) as f:
        program = [int(i) for i in f.readline().rstrip().split(",")]
    return program

def fetch_opcode(pointer):
    opcode = program[pointer]
    return opcode

def run_opcode(opcode, pointer, input_data, index, output_data):
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
        pointer, index = write_input(pointer, input_data, index)
    if opcode[-1] == "4":
        operand_1 = fetch_value(program[pointer], paramodes[0])
        pointer, output_data = output(operand_1, pointer, output_data)
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
        return pointer, output, index, False
    return pointer, output_data, index, True

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

def write_input(pointer, input_data, index):
    address = program[pointer]
    program[address] = input_data[index]
    pointer += 1
    index += 1
    return pointer, index

def output(operand_1, pointer, output_data):
    output_data.append(operand_1)
    pointer += 1
    return pointer, output_data

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

def run_program(program, input_data, output_data):
    pointer = 0
    index = 0
    running = True
    while running == True:
        opcode = fetch_opcode(pointer)
        pointer, output_data, index, running = run_opcode(opcode, pointer, input_data, index, output_data )


phase_sequences = list(itertools.permutations([0 ,1, 2, 3, 4]))
largest_output = 0
for phase_sequence in phase_sequences:
    program = get_program("07.txt")
    output_data = [0]

    for phase in phase_sequence:
        input_data = [phase, output_data[-1]]
        run_program(program, input_data, output_data)
    if output_data[-1] > largest_output:
        largest_output = output_data[-1]
print(largest_output)
        

    

