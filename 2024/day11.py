import math

stones = None
with open('input/day11.txt', 'r') as f:
    buffer = f.read()[:-1]
    stones = [int(x) for x in buffer.split(' ')]

cache = {}
def getNumStones(stone, numIterations):
    if numIterations == 0:
        return 1

    if (stone, numIterations) in cache:
        return cache[(stone, numIterations)]

    size = 0
    if stone == 0:
        size = getNumStones(1, numIterations - 1)
    elif (int(math.log10(stone)) + 1) % 2 == 0:
        dataStr = str(stone)
        size = getNumStones(int(dataStr[:len(dataStr) // 2]), numIterations - 1) + getNumStones(int(dataStr[len(dataStr) // 2:]), numIterations - 1)
    else:
        size = getNumStones(stone * 2024, numIterations - 1)

    if (stone, numIterations) not in cache:
        cache[(stone, numIterations)] = size

    return size

print('PART 1: %d' % sum(getNumStones(stone, 25) for stone in stones))
print('PART 2: %d' % sum(getNumStones(stone, 75) for stone in stones))

