from collections import deque

buffer = []
with open('input/day18.txt', 'r') as f:
    for line in f:
        line = line.strip()
        vals = line.split(',')
        buffer.append((int(vals[1]), int(vals[0])))

def findMaxStepsToSolve(corruptedCoords: list[tuple[int]]) -> int:
    lim = 70
    visitedPositions = {}
    positions = deque([((0, 0), 0)]) # (y, x), numSteps
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while positions:
        position, numSteps = positions.popleft()

        if position[0] < 0 or position[0] > lim or position[1] < 0 or position[1] > lim:
            continue
        if position in corruptedCoords or (position in visitedPositions and visitedPositions[position] <= numSteps):
            continue

        visitedPositions[position] = numSteps

        for direction in directions:
            newPosition = (position[0] + direction[0], position[1] + direction[1])
            positions.append((newPosition, numSteps + 1))

    return visitedPositions[(lim, lim)] if (lim, lim) in visitedPositions else -1

print('PART ONE: %d' % findMaxStepsToSolve(buffer[:1024]))

right = 0
with open('input/day18.txt', 'r') as f:
    right = len(f.readlines())
left = 1024
while (left != right):
    mid = (left + right) // 2
    if findMaxStepsToSolve(buffer[:mid + 1]) == -1:
        right = mid - 1
    else:
        left = mid + 1

if findMaxStepsToSolve(buffer[:left + 1]) != -1:
    left += 1

print('PART TWO: %d,%d' % (buffer[left][1], buffer[left][0]))

