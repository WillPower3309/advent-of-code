input = ''
with open('input/day9.txt', 'r') as f:
    input = f.read()[:-1]

if len(input) % 2 != 1:
    input = input[:-1]

# PART ONE

leftId = 0
leftIndex = 0
rightId = (len(input) - 1) // 2
rightIndex = len(input) - 1

numRemainingRight = int(input[rightIndex])
blockIndex = 0

checkSum = 0

while leftIndex < rightIndex:
    for i in range(int(input[leftIndex])):
        checkSum += blockIndex * leftId
        blockIndex += 1

    leftIndex += 1

    for i in range(int(input[leftIndex])):
        while numRemainingRight == 0:
            rightId -= 1
            rightIndex -= 2
            numRemainingRight = int(input[rightIndex])

        checkSum += blockIndex * rightId
        blockIndex += 1
        numRemainingRight -= 1

    leftIndex += 1
    leftId += 1

if leftIndex == rightIndex:
    checkSum += blockIndex * leftId

print('PART 1: %d' % checkSum)

