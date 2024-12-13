trailGrid = []
with open('input/day10.txt', 'r') as f:
    for line in f:
        trailGrid.append([int(x) for x in line[:-1]])

# PART ONE

def getScore(y, x):
    visitedPoints = set()
    queue = [(y, x)]
    score = 0

    while queue:
        y, x = queue.pop(0)
        if (y, x) in visitedPoints:
            continue

        visitedPoints.add((y, x))
        currentHeight = trailGrid[y][x]

        if currentHeight == 9:
            score += 1
            continue

        if y > 0 and trailGrid[y - 1][x] == currentHeight + 1:
            queue.append((y - 1, x))

        if y < len(trailGrid) - 1 and trailGrid[y + 1][x] == currentHeight + 1:
            queue.append((y + 1, x))

        if x > 0 and trailGrid[y][x - 1] == currentHeight + 1:
            queue.append((y, x - 1))

        if x < len(trailGrid[y]) - 1 and trailGrid[y][x + 1] == currentHeight + 1:
            queue.append((y, x + 1))

    return score

totalScore = 0
for y in range(len(trailGrid)):
    for x in range(len(trailGrid[y])):
        if trailGrid[y][x] == 0:
            totalScore += getScore(y, x)

print('PART 1: %d' % totalScore)

# PART TWO

def getScore(y, x):
    queue = [(y, x)]
    score = 0

    while queue:
        y, x = queue.pop(0)
        currentHeight = trailGrid[y][x]

        if currentHeight == 9:
            score += 1
            continue

        if y > 0 and trailGrid[y - 1][x] == currentHeight + 1:
            queue.append((y - 1, x))

        if y < len(trailGrid) - 1 and trailGrid[y + 1][x] == currentHeight + 1:
            queue.append((y + 1, x))

        if x > 0 and trailGrid[y][x - 1] == currentHeight + 1:
            queue.append((y, x - 1))

        if x < len(trailGrid[y]) - 1 and trailGrid[y][x + 1] == currentHeight + 1:
            queue.append((y, x + 1))

    return score

totalScore = 0
for y in range(len(trailGrid)):
    for x in range(len(trailGrid[y])):
        if trailGrid[y][x] == 0:
            totalScore += getScore(y, x)

print('PART 1: %d' % totalScore)
