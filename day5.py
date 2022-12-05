import re

def constructCrateStacks(stackDescription: str) -> list:
    crateStacks = []
    stackIndexDescLine = stackDescription.pop()
    for i in range(int(stackIndexDescLine[len(stackIndexDescLine) - 2])):
        crateStacks.append([])

    for line in reversed(stackDescription):
        columnIndex = 0
        for i in range(1, len(line), 4):
            if line[i].isalpha():
                crateStacks[columnIndex].append(line[i])
            columnIndex += 1
    return crateStacks

buffer = []
with open('input/day5.txt', 'r') as f:
    buffer = f.read().split('\n\n')

##################
# PART ONE
##################

crateStacks = constructCrateStacks(buffer[0].split('\n'))
for line in buffer[1].split('\n'):
    move = list(map(int, filter(None, re.split("move|from|to", line.strip()))))
    if move == []:
        break

    for _ in range(move[0]):
        crate = crateStacks[move[1] - 1].pop()
        crateStacks[move[2] - 1].append(crate)

result = ''
for stack in crateStacks:
    result += stack[len(stack) - 1]
print(result)

##################
# PART TWO
##################

crateStacks = constructCrateStacks(buffer[0].split('\n'))
for line in buffer[1].split('\n'):
    move = list(map(int, filter(None, re.split("move|from|to", line.strip()))))
    if move == []:
        break

    for i in reversed(range(move[0])):
        fromStack = crateStacks[move[1] - 1]
        crate = fromStack.pop(len(fromStack) - i - 1)
        crateStacks[move[2] - 1].append(crate)

result = ''
for stack in crateStacks:
    result += stack[len(stack) - 1]
print(result)
