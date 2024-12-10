from collections import defaultdict

buffer = []
with open('input/day8.txt', 'r') as f:
    buffer = f.read().split('\n')[:-1]

antennaCoordinateMap = defaultdict(list)

for y in range(len(buffer)):
    for x in range(len(buffer[y])):
        char = buffer[y][x]
        if char != '.' and char != '\n':
            antennaCoordinateMap[char].append([y, x])

# PART ONE

antiNodeCoordinates = set()

for antennaCoordList in antennaCoordinateMap.values():
    for coordOne in antennaCoordList:
        for coordTwo in antennaCoordList:
            if coordOne == coordTwo:
                continue

            antiNodeY = 2 * coordOne[0] - coordTwo[0]
            if antiNodeY < len(buffer) and antiNodeY >= 0:
                antiNodeX = 2 * coordOne[1] - coordTwo[1]
                if antiNodeX < len(buffer[0]) and antiNodeX >= 0:
                    antiNodeCoordinates.add((antiNodeY, antiNodeX))

print('PART 1: %d' % len(antiNodeCoordinates))


# PART TWO

antiNodeCoordinates = set()

for antennaCoordList in antennaCoordinateMap.values():
    for coordOne in antennaCoordList:
        for coordTwo in antennaCoordList:
            if coordOne == coordTwo:
                continue

            antiNodeCoordinates.add((coordOne[0], coordOne[1]))

            antiNodeY = 2 * coordOne[0] - coordTwo[0]
            antiNodeX = 2 * coordOne[1] - coordTwo[1]
            while antiNodeY < len(buffer) and antiNodeY >= 0 and antiNodeX < len(buffer[0]) and antiNodeX >= 0:
                antiNodeCoordinates.add((antiNodeY, antiNodeX))
                antiNodeY -= coordTwo[0] - coordOne[0]
                antiNodeX -= coordTwo[1] - coordOne[1]

print('PART 2: %d' % len(antiNodeCoordinates))

