input = []
with open('input/day19.txt', 'r') as f:
    input = f.readlines()

towelPatterns = {}
for colors in input[0].strip().split(', '):
    existingTowelPatterns = towelPatterns.get(colors[0], [])
    existingTowelPatterns.append(colors)
    towelPatterns[colors[0]] = existingTowelPatterns

def isDesignPossible(colorCombination: list[str]) -> bool:
    currentIndices = [ 0 ]
    visitedIndices = set()

    while currentIndices:
        currentIndex = currentIndices.pop()
        if currentIndex == len(colorCombination) - 1:
            return True

        if currentIndex in visitedIndices:
            continue
        visitedIndices.add(currentIndex)

        for colors in towelPatterns.get(colorCombination[currentIndex], []):
            for i in range(len(colors)):
                nextIndex = currentIndex + i
                if nextIndex >= len(colorCombination) or colors[i] != colorCombination[nextIndex]:
                    break
                if i == len(colors) - 1:
                    currentIndices.append(nextIndex + 1)

    return False

numPossiblePatterns = 0
for colorCombination in input[2:]:
    numPossiblePatterns += isDesignPossible(colorCombination)

print('PART ONE: %d' % numPossiblePatterns)

def numWaysToMakeDesign(colorCombination: list[str]) -> int:
    indiceNumMatchesMap = {}

    def numWaysToMakeDesignRec(index: int) -> int:
        if index in indiceNumMatchesMap:
            return indiceNumMatchesMap[index]
        if index == len(colorCombination) - 1:
            return 1

        numMatches = 0
        for colors in towelPatterns.get(colorCombination[index], []):
            for i in range(len(colors)):
                nextIndex = index + i
                if nextIndex >= len(colorCombination) or colors[i] != colorCombination[nextIndex]:
                    break
                if i == len(colors) - 1:
                    numMatches += numWaysToMakeDesignRec(nextIndex + 1)
        indiceNumMatchesMap[index] = numMatches
        return numMatches

    return numWaysToMakeDesignRec(0)

totalWaysToMakeDesign = 0
for colorCombination in input[2:]:
    totalWaysToMakeDesign += numWaysToMakeDesign(colorCombination)

print('PART TWO: %d' % totalWaysToMakeDesign)

