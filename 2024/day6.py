from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

map = []
posX = 0
posY = 0
dir = Direction.UP

with open('input/day6.txt', 'r') as f:
    i = 0
    for line in f:
        guardIndex = line.find('^')
        if guardIndex > 0:
            posY = i
            posX = guardIndex
        map.append(line[:-1])
        i += 1

numDistinctPos = 0
while posX >= 0 and posX < len(map[0]) and posY >= 0 and posY < len(map):
    if map[posY][posX] == '#':
        if dir == Direction.UP:
            posY += 1
        elif dir == Direction.DOWN:
            posY -= 1
        elif dir == Direction.RIGHT:
            posX -= 1
        elif dir == Direction.LEFT:
            posX += 1
        dir = Direction((dir.value + 1) % 4)
        continue
    elif map[posY][posX] != 'X':
        numDistinctPos += 1

    map[posY] = map[posY][:posX] + 'X' + map[posY][posX + 1:]

    if dir == Direction.UP:
        posY -= 1
    elif dir == Direction.DOWN:
        posY += 1
    elif dir == Direction.RIGHT:
        posX += 1
    elif dir == Direction.LEFT:
        posX -= 1

print('PART 1: %d' % numDistinctPos)

