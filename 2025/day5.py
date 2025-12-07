ranges = ''
ids = ''
with open('input/day5.txt', 'r') as f:
    ranges, ids = f.read()[:-1].split('\n\n')
    ranges = [ tuple(map(int, x.split('-'))) for x in ranges.splitlines() ]

# PART ONE

numFresh = 0
for id in ids.splitlines():
    for low, high in ranges:
        if low <= int(id) <= high:
            numFresh += 1
            break

print('PART 1: %d' % numFresh)

# PART TWO
import bisect

minimizedRanges = []
for low, high in ranges:
    i = bisect.bisect_left(minimizedRanges, (low, )) # search using low value

    # check right
    while i < len(minimizedRanges):
        if minimizedRanges[i][0] > high + 1:
            break
        high = max(high, minimizedRanges[i][1])
        minimizedRanges.pop(i)

    # check left
    if i > 0 and low - 1 <= minimizedRanges[i - 1][1]:
        minimizedRanges[i - 1] = (min(low, minimizedRanges[i - 1][0]), max(high, minimizedRanges[i - 1][1]))
    else:
        minimizedRanges.insert(i, (low, high))

numFresh = 0
for low, high in minimizedRanges:
    numFresh += high - low + 1

print('PART 2: %d' % numFresh)

