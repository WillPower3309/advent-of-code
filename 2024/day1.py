import bisect

# PART ONE
leftList = []
rightList = []

with open('input/day1.txt', 'r') as f:
    for line in f:
        vals = line.split('   ')
        bisect.insort(leftList, int(vals[0]))
        bisect.insort(rightList, int(vals[1]))

totalDistance = 0
for i in range(len(leftList)):
    totalDistance += abs(leftList[i] - rightList[i])
print('PART 1: %d' % totalDistance)

# PART TWO
leftQuantityMap = {}
rightQuantityMap = {}

with open('input/day1.txt', 'r') as f:
    for line in f:
        vals = line.split('   ')
        leftKey = int(vals[0])
        leftQuantityMap[leftKey] = leftQuantityMap.get(leftKey, 0) + 1
        rightKey = int(vals[1])
        rightQuantityMap[rightKey] = rightQuantityMap.get(rightKey, 0) + 1

similarityScore = 0
for num in leftQuantityMap.keys():
    similarityScore += num * leftQuantityMap[num] * rightQuantityMap.get(num, 0)
print('PART 2: %d' % similarityScore)

