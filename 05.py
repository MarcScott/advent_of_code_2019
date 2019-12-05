program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,78,40,225,1102,52,43,224,1001,224,-2236,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1,191,61,224,1001,224,-131,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,86,74,225,1102,14,76,225,1101,73,83,224,101,-156,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,43,82,225,2,196,13,224,101,-6162,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,161,51,224,101,-70,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,102,52,187,224,1001,224,-832,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1102,19,79,225,101,65,92,224,1001,224,-147,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1102,16,90,225,1102,45,44,225,1102,92,79,225,1002,65,34,224,101,-476,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,344,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,359,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,419,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,449,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,464,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,494,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,569,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,644,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,659,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]

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

main()
