buffer = []

pos = (0, 0)
with open('input/day20.txt', 'r') as f:
    for (y, line) in enumerate(f):
        for (x, char) in enumerate(line):
            if char == 'S':
                pos = (y, x)
        buffer.append(line)

trackTimeDict = { pos: 0 }
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
currentTime = 0
while True:
    for direction in directions:
        newY = pos[0] + direction[0]
        newX = pos[1] + direction[1]
        if buffer[newY][newX] != '#' and (newY, newX) not in trackTimeDict:
            pos = (newY, newX)
            break

    currentTime += 1
    trackTimeDict[pos] = currentTime

    if buffer[pos[0]][pos[1]] == 'E':
        break

numCheatsOver100 = 0
for position in trackTimeDict:
    y, x = position
    for direction in directions:
        for i in range(1, 3):
            ny = y + (direction[0] * i)
            nx = x + (direction[1] * i)
            if (ny, nx) in trackTimeDict and trackTimeDict[(ny, nx)] - trackTimeDict[position] - i >= 100:
                numCheatsOver100 += 1

print('PART ONE: %d' % numCheatsOver100)

numCheatsOver100 = 0
for position in trackTimeDict:
    y, x = position

    numCheatsOver100ForPos = set()
    for dy in range(-20, 21):
        ny = y + dy
        for dx in range(-20, 21):
            if abs(dy) + abs(dx) > 20: # TODO: incorporate me into for loop
                continue
            if dy == 0 and dx == 0:
                continue
            nx = x + dx
            if (ny, nx) in trackTimeDict and trackTimeDict[(ny, nx)] - trackTimeDict[position] - abs(dy) - abs(dx) >= 100:
                numCheatsOver100ForPos.add((ny, nx))

    numCheatsOver100 += len(numCheatsOver100ForPos)

print('PART TWO: %d' % numCheatsOver100)

