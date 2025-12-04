# PART ONE
numZero = 0
with open('input/day1.txt', 'r') as f:
    dialPos = 50
    for line in f:
        if line[0] == 'R':
            dialPos += int(line[1:])
        else:
            dialPos -= int(line[1:])
        dialPos = dialPos % 100

        if dialPos == 0:
            numZero += 1

print('PART 1: %d' % numZero)

# PART TWO
numZero = 0
with open('input/day1.txt', 'r') as f:
    dialPos = 50
    for line in f:
        isZeroStart = dialPos == 0

        if line[0] == 'R':
            dialPos += int(line[1:])
        else:
            dialPos -= int(line[1:])

        numFullRotations = abs(dialPos // 100)
        if numFullRotations:
            numZero += numFullRotations - isZeroStart

        if dialPos == 0:
            numZero += 1

        dialPos = dialPos % 100

print('PART 2: %d' % numZero)

