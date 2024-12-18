from collections import deque

mazeGrid = []
snakes = deque()

with open('input/day16.txt', 'r') as f:
    for (y, line) in enumerate(f):
        mazeRow = []
        line = line.strip()
        for x in range(len(line)):
            if line[x] == 'S':
                # position, last movement (starts facing east), score
                snakes.append(((y, x), (0, 1), 0))
        mazeGrid.append(line)

finalScore = float('inf')
intersections = {} # min score at various intersections
directions = {
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
}
while snakes:
    (y, x), direction, score = snakes.popleft()


    if mazeGrid[y][x] == 'E':
        finalScore = min(finalScore, score)
        continue

    if (y, x, direction) in intersections and intersections[(y, x, direction)] < score:
        continue

    numMovementsFromPos = 0
    for newDirection in directions:
        if newDirection[0] == -direction[0] and newDirection[1] == -direction[1]:
            continue

        newY = y + newDirection[0]
        newX = x + newDirection[1]
        if mazeGrid[newY][newX] != '#':
            numMovementsFromPos += 1
            if newDirection == direction:
                snakes.append(((newY, newX), newDirection, score + 1))
            else:
                snakes.append(((y, x), newDirection, score + 1000))

    if numMovementsFromPos > 1:
        intersections[(y, x, direction)] = score

print('PART ONE: %d' % finalScore)

