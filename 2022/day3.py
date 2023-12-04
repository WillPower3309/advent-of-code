def getPriority(item: str) -> int:
    asciiVal = ord(item)
    if asciiVal <= 90: # upper case
        return asciiVal - 38
    return asciiVal - 96

##################
# PART ONE
##################

prioritySum = 0
with open('input/day3.txt', 'r') as f:
    for line in f:
        contents = line.strip()
        midpoint = len(contents) // 2
        compartmentA = sorted(contents[:midpoint])
        compartmentB = sorted(contents[midpoint:])

        i = 0
        j = 0
        while i < midpoint and j < midpoint:
            if compartmentA[i] < compartmentB[j]:
                i += 1
            elif compartmentB[j] < compartmentA[i]:
                j += 1
            else:
                prioritySum += getPriority(compartmentA[i])
                while i < midpoint and compartmentA[i] == compartmentB[j]:
                    i += 1
                j += 1

print(prioritySum)

##################
# PART TWO
##################

def getGroupPrioritySum(fileName: str) -> int:
    prioritySum = 0
    with open(fileName, 'r') as f:
        while True:
            contentsA = f.readline().strip()
            if not contentsA: return prioritySum
            contentsB = f.readline().strip()
            if not contentsB: return prioritySum
            contentsC = f.readline().strip()
            if not contentsC: return prioritySum

            # much faster to sort and then iterate as above but this is faster for me to type :p
            commonContents = set(contentsA) & set(contentsB) & set(contentsC)
            prioritySum += getPriority(commonContents.pop())

print(getGroupPrioritySum('input/day3.txt'))
