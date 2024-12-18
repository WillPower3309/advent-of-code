from collections import deque

mazeGrid = []
queue = deque()

with open('input/day16.txt', 'r') as f:
    for (y, line) in enumerate(f):
        mazeRow = []
        line = line.strip()
        for x in range(len(line)):
            if line[x] == 'S':
                # position, last movement (starts facing east), score, tiles in snake
                queue.append(((y, x), (0, 1), 0, {(y, x)}))
        mazeGrid.append(line)

finalScore = float('inf')
tilesInFinalScore = set()
intersections = {} # min score at various intersections
directions = {
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
}
while queue:
    (y, x), direction, score, tiles = queue.popleft()

    if mazeGrid[y][x] == 'E':
        if score < finalScore:
            finalScore = score
            tilesInFinalScore = tiles
        elif score == finalScore:
            tilesInFinalScore = tilesInFinalScore.union(tiles)
        continue

    if (y, x, direction) in intersections and intersections[(y, x, direction)] < score:
        continue

    numMovementsFromPos = 0
    for newDirection in directions:
        newY = y + newDirection[0]
        newX = x + newDirection[1]
        if mazeGrid[newY][newX] != '#' and (newY, newX) not in tiles:
            numMovementsFromPos += 1
            if newDirection == direction:
                queue.append(((newY, newX), newDirection, score + 1, tiles | {(newY, newX)}))
            else:
                queue.append(((y, x), newDirection, score + 1000, tiles))

    if numMovementsFromPos > 1:
        intersections[(y, x, direction)] = score

print('PART ONE: %d' % finalScore)
print('PART TWO: %d' % len(tilesInFinalScore))

