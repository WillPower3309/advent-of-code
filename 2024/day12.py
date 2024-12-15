farmGrid = []
visitedRegions = set()

with open('input/day12.txt', 'r') as f:
    for line in f:
        line = line.strip()
        farmRow = []
        for char in line:
            farmRow.append(char)
        farmGrid.append(farmRow)

def findRegionCost(y: int, x: int) -> int:
    currVisited = {(y, x)}
    currVal = farmGrid[y][x]
    area = 1
    perimeter = 0

    regions = [(y, x)]
    while regions:
        y, x = regions.pop()

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if (ny, nx) in currVisited:
                continue 

            if 0 <= ny < len(farmGrid) and 0 <= nx < len(farmGrid[0]) and farmGrid[ny][nx] == currVal:
                regions.append((ny, nx))
                area += 1
                currVisited.add((ny, nx))

            else:
                perimeter += 1

    visitedRegions.update(currVisited)
    return area * perimeter

def partOne(farmGrid: list[str]) -> int:
    cost = 0
    for y in range(len(farmGrid)):
        for x in range(len(farmGrid[0])):
            if (y, x) in visitedRegions:
                continue
            cost += findRegionCost(y, x)
    return cost

def partTwo():
    return 0

print('PART ONE: %d' % partOne(farmGrid))
print('PART TWO: %d' % partTwo())

