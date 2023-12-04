##################
# PART ONE
##################

numContainedPairs = 0
with open('input/day4.txt', 'r') as f:
    for line in f:
        pairs = line.strip().split(',')
        rangeA = list(map(int, pairs[0].split('-')))
        rangeB = list(map(int, pairs[1].split('-')))
        if rangeA[0] < rangeB[0]:
            if rangeA[1] >= rangeB[1]:
                numContainedPairs += 1
        elif rangeB[0] < rangeA[0]:
            if rangeB[1] >= rangeA[1]:
                numContainedPairs += 1
        else:
            numContainedPairs += 1

print(numContainedPairs)

##################
# PART TWO
##################

numOverlappedPairs = 0
with open('input/day4.txt', 'r') as f:
    for line in f:
        pairs = line.strip().split(',')
        rangeA = list(map(int, pairs[0].split('-')))
        rangeB = list(map(int, pairs[1].split('-')))
        if rangeA[0] <= rangeB[1] and rangeA[1] >= rangeB[0]:
            numOverlappedPairs += 1
        elif rangeB[0] <= rangeA[1] and rangeB[1] >= rangeA[0]:
            numOverlappedPairs += 1

print(numOverlappedPairs)
