# PART ONE

# TODO: https://medium.com/pythoniq/a-crash-course-in-python-comprehensions-and-generators-f069c8f8ca38
def fetchFirstDigit(vals: list) -> int:
    for val in vals:
        if val.isdigit():
            return int(val)
    return 0

calibrationValSum = 0
with open('input/day1.txt', 'r') as f:
    for line in f:
        lineContents = line.strip()
        calibrationVal = 10 * fetchFirstDigit(lineContents)
        calibrationVal += fetchFirstDigit(reversed(lineContents))
        calibrationValSum += calibrationVal

print('PART 1: %d' % calibrationValSum)

# PART TWO

# not pretty but gets the job done, didn't have time for a more elegant solution
def fetchDigitPartTwo(vals: str, shouldFetchLast: bool) -> int:
    digitStrs = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
    digit = 0

    i = 0
    while i < (len(vals)):
        val = vals[i]
        if val.isdigit():
            digit = int(val)
            if not shouldFetchLast:
                break

        else:
            for j in range(len(digitStrs)):
                digitStr = digitStrs[j]
                lenDigit = len(digitStr)
                if digitStr[0] == val and i + lenDigit <= len(vals) and digitStr[lenDigit - 1] == vals[i + lenDigit - 1]:
                    if digitStr == vals[i:i + lenDigit]:
                        digit = j
                        if not shouldFetchLast:
                            return digit

        i = i + 1

    return digit

calibrationValSum = 0
with open('input/day1.txt', 'r') as f:
    for line in f:
        lineContents = line.strip()
        calibrationVal = 10 * fetchDigitPartTwo(lineContents, False)
        calibrationVal += fetchDigitPartTwo(lineContents, True)
        calibrationValSum += calibrationVal

print('PART 2: %d' % calibrationValSum)
