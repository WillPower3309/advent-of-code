# PART ONE
numSafe = 0
with open('input/day2.txt', 'r') as f:
    for line in f:
        safe = True
        levels = line.split(' ')
        increasing = int(levels[0]) < int(levels[-1])

        for i in range(1, len(levels)):
            numDiff = int(levels[i]) - int(levels[i - 1])
            if (increasing and numDiff <= 0) or (not increasing and numDiff >= 0) or abs(numDiff) > 3:
                safe = False
                break
        numSafe += safe

print('PART 1: %d' % numSafe)

# PART TWO
print('PART 2: %d' % 0)

