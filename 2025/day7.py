grid = []

with open('input/day7.txt', 'r') as f:
    grid = f.read().splitlines()

startX = 0
for i in range(len(grid[0])):
    if grid[0][i] == 'S':
        startX = i
        break

# PART ONE

checkedPositions = set()
positions = [ (0, startX) ]
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

# PART TWO

cache = dict()
def dfs(y: int, x: int) -> int:
    if x < 0 or x >= len(grid[0]):
        return 0
    if y >= len(grid):
        return 1
    if (y, x) in cache:
        return cache[(y, x)]
    if grid[y][x] == '^':
        cache[(y, x)] = dfs(y + 1, x + 1) + dfs(y + 1, x - 1)
        return cache[(y, x)]

    return dfs(y + 1, x)

print('PART 2: %d' % dfs(0, startX))

