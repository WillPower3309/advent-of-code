from collections import deque

corruptedCoords = []

with open('input/day18.txt', 'r') as f:
    for line in f:
        line = line.strip()
        vals = line.split(',')
        corruptedCoords.append((int(vals[1]), int(vals[0])))
        if len(corruptedCoords) >= 1024:
            break

lim = 70
totalNumSteps = float('inf')
visitedPositions = {}
positions = deque([((0, 0), 0)]) # (y, x), numSteps
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while positions:
    position, numSteps = positions.popleft()

    if position[0] < 0 or position[0] > lim or position[1] < 0 or position[1] > lim:
        continue

    if position in corruptedCoords or (position in visitedPositions and visitedPositions[position] <= numSteps):
        continue

    if position == (lim, lim):
        totalNumSteps = min(totalNumSteps, numSteps)
    
    visitedPositions[position] = numSteps

    for direction in directions:
        newPosition = (position[0] + direction[0], position[1] + direction[1])
        positions.append((newPosition, numSteps + 1))

print(totalNumSteps)

