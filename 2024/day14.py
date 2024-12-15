import math
import re

limY = 103
limX = 101

finalRobotPositions = []

with open('input/day14.txt', 'r') as f:
    for line in f:
        values = re.findall(r'-?\d+', line)
        x = int(values[0])
        y = int(values[1])
        velocityX = int(values[2])
        velocityY = int(values[3])

        finalPosX = (x + (100 * velocityX)) % limX
        finalPosY = (y + (100 * velocityY)) % limY

        finalRobotPositions.append((finalPosY, finalPosX))

quadrants = [0, 0, 0, 0]
for (y, x) in finalRobotPositions:
    if y < limY // 2:
        if x < limX // 2:
            quadrants[0] += 1
        elif x > limX // 2:
            quadrants[1] += 1
    elif y > limY // 2:
        if x < limX // 2:
            quadrants[2] += 1
        elif x > limX // 2:
            quadrants[3] += 1

print('PART ONE: %d' % math.prod(quadrants))

