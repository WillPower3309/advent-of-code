registers = [ 0, 0, 0 ]
program = []
with open('input/day17.txt', 'r') as f:
    input = f.read().split('\n')
    for i in range(3):
        registers[i] = int(input[i].split(': ')[1])
    program = list(map(int, input[4].split(": ")[1].split(",")))

def getComboOperand(operand: int, registers: list[int]) -> int:
    return operand if operand < 4 else registers[operand - 4]

def executeProgram(registers: list[int]) -> str:
    pc = 0
    outputBuffer = []
    while pc < len(program) - 1:
        opcode = program[pc]
        operand = program[pc + 1]
        pc += 2

        if opcode == 0:
            registers[0] //= (2 ** getComboOperand(operand, registers))
        elif opcode == 1:
            registers[1] ^= operand
        elif opcode == 2:
            registers[1] = getComboOperand(operand, registers) % 8
        elif opcode == 3:
            if registers[0] == 0:
                continue
            pc = operand
        elif opcode == 4:
            registers[1] ^= registers[2]
        elif opcode == 5:
            outputBuffer.append(getComboOperand(operand, registers) % 8)
        elif opcode == 6:
            registers[1] = registers[0] // (2 ** getComboOperand(operand, registers))
        elif opcode == 7:
            registers[2] = registers[0] // (2 ** getComboOperand(operand, registers))

    return outputBuffer

outputBuffer = executeProgram(registers) 
print('PART 1: %s' % ','.join(map(str, outputBuffer)))

# brute forceish because my brain is tired
A = 8 ** (len(program) - 1) # works in base 8
power = len(program) - 3 # adjusting 8 ** power modifies the digit of the power plus the two subsequent digits
output = []
while output != program:
    if len(output) > len(program):
        print('Not possible')
        exit()

    output = executeProgram([A, registers[1], registers[2]])

    # match each digit, right to left
    if power > 0 and output[power + 2] == program[power + 2]:
        power -= 1
    else:
        A += 8 ** power

# fine tune it
while executeProgram([A - 1, registers[1], registers[2]]) == program:
    A -= 1

print('PART 2: %s' % A)

