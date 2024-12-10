# PART ONE
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

antiNodeCoordinates = set()

for antennaCoordList in antennaCoordinateMap.values():
    for coordOne in antennaCoordList:
        for coordTwo in antennaCoordList:
            if coordOne == coordTwo:
                continue

            antiNodeY = 2 * coordOne[0] - coordTwo[0]
            if antiNodeY < len(buffer) and antiNodeY >= 0:
                antiNodeX = 2 * coordOne[1] - coordTwo[1]
                if (antiNodeX < len(buffer[0]) and antiNodeX >= 0):
                    antiNodeCoordinates.add((antiNodeY, antiNodeX))

print('PART 1: %d' % len(antiNodeCoordinates))

