grid = []

with open('input/day7.txt', 'r') as f:
    grid = f.read().splitlines()

# PART ONE

x = 0
for i in range(len(grid[0])):
    if grid[0][i] == 'S':
        x = i
        break

checkedPositions = set()
positions = [ (0, x) ]
numSplits = 0
while positions:
    y, x = positions.pop()
    y += 1

    if (y, x) in checkedPositions or y >= len(grid) or x < 0 or x >= len(grid[0]):
        continue

    if grid[y][x] == '^':
        numSplits += 1
        positions.append((y, x + 1))
        positions.append((y, x - 1))
    else:
        positions.append((y, x))

    checkedPositions.add((y, x))


print('PART 1: %d' % numSplits)

