grid = []

with open('input/day4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        grid.append(line)

directions = ( (-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1) )

# PART ONE
accessibleRolls = 0
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == '@':
            numAdjacentRolls = 0
            for (dirY, dirX) in directions:
                checkY = y + dirY
                if checkY < 0 or checkY >= len(grid):
                    continue
                checkX = x + dirX
                if checkX < 0 or checkX >= len(grid[0]):
                    continue

                if grid[checkY][checkX] == '@':
                    numAdjacentRolls += 1
                    if numAdjacentRolls >= 4:
                        break

            if numAdjacentRolls < 4:
                accessibleRolls += 1

print('PART 1: %d' % accessibleRolls)

# PART ONE
print('PART 2: %d' % 0)

