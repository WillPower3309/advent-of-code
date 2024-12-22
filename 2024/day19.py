input = []
with open('input/day19.txt', 'r') as f:
    input = f.readlines()

towelColors = {}
for colors in input[0].strip().split(', '):
    existingTowelColors = towelColors.get(colors[0], [])
    existingTowelColors.append(colors)
    towelColors[colors[0]] = existingTowelColors

def isColorPossible(colorCombination: list[str]):
    currentIndices = [ 0 ]
    visitedIndices = set()

    while currentIndices:
        currentIndex = currentIndices.pop()
        if currentIndex == len(colorCombination) - 1:
            return True

        if currentIndex in visitedIndices:
            continue
        visitedIndices.add(currentIndex)

        for colors in towelColors.get(colorCombination[currentIndex], []):
            for i in range(len(colors)):
                if colors[i] != colorCombination[currentIndex + i]:
                    break
                if i == len(colors) - 1:
                    currentIndices.append(currentIndex + i + 1)

    return False

numPossiblePatterns = 0
for colorCombination in input[2:]:
    numPossiblePatterns += isColorPossible(colorCombination)

print(numPossiblePatterns)

