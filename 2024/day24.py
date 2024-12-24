from collections import deque

wires = {}
wireOperations = deque()

with open('input/day24.txt', 'r') as f:
    input = f.read().split('\n\n')

    for line in input[0].split('\n'):
        line = line.split(': ')
        wires[line[0]] = bool(int(line[1]))

    for line in input[1].split('\n')[:-1]:
        line = line.strip().split(' ')
        wireOperations.append((line[0], line[2], line[1], line[4]))

while wireOperations:
    wireOperation = wireOperations.popleft()
    wireA, wireB, operation, wireC = wireOperation

    if wireA not in wires or wireB not in wires:
        wireOperations.append(wireOperation)
        continue

    if operation == 'AND':
        wires[wireC] = wires[wireA] and wires[wireB]
    elif operation == 'OR':
        wires[wireC] = wires[wireA] or wires[wireB]
    elif operation == 'XOR':
        wires[wireC] = wires[wireA] != wires[wireB]

output = 0
for wire, val in wires.items():
    if wire[0] == 'z':
        output += val * 2 ** int(wire[1:])

print('PART ONE %d' % output)

