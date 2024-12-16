warehouseGrid = []
movements = ""
robotPos = (0, 0)

with open('input/day15.txt', 'r') as f:
    buffer = f.read().split('\n\n')

    wareHouseRows = buffer[0].split('\n')
    for y in range(len(wareHouseRows)):
        row = []
        for x in range(len(wareHouseRows[0])):
            if wareHouseRows[y][x] == '@':
                robotPos = (y, x)
            row.append(wareHouseRows[y][x])
        warehouseGrid.append(row)

    for line in buffer[1].split('\n'):
        movements += line

dirMap = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}
for movement in movements:
    deltaY = dirMap[movement][0]
    deltaX = dirMap[movement][1]
    newY = robotPos[0] + deltaY
    newX = robotPos[1] + deltaX

    if warehouseGrid[newY][newX] == '#':
        continue

    if warehouseGrid[newY][newX] == 'O':
        # find space for rock to move to, if any
        openY = newY + deltaY
        openX = newX + deltaX
        while warehouseGrid[openY][openX] == 'O':
            openY += deltaY
            openX += deltaX

        if warehouseGrid[openY][openX] == '#':
            continue

        # move rocks to open space
        while openY != newY or openX != newX:
            warehouseGrid[openY][openX] = 'O'
            openY -= deltaY
            openX -= deltaX

        warehouseGrid[newY][newX] = '.'
        robotPos = (newY, newX)

    else:
        robotPos = (newY, newX)

gpsCoordinateSum = 0
for y in range(len(warehouseGrid)):
    for x in range(len(warehouseGrid[0])):
        if warehouseGrid[y][x] != 'O':
            continue

        gpsCoordinateSum += 100 * y + x

print('PART ONE: %d' % gpsCoordinateSum)

