import math

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def insertNext(self, data):
        newNode = LinkedList(data)
        newNode.prev = self
        newNode.next = self.next

        if self.next:
            self.next.prev = newNode
        self.next = newNode

stonesTail = None

with open('input/day11.txt', 'r') as f:
    buffer = f.read()[:-1]
    vals = buffer.split(' ')
    stones = LinkedList(int(vals[0]))
    currNode = stones
    for i in range(1, len(vals)):
        currNode.insertNext(int(vals[i]))
        currNode = currNode.next

    stonesTail = currNode

# PART ONE
for _ in range(25):
    currNode = stonesTail
    while currNode:
        if currNode.data == 0:
            currNode.data = 1
        elif (int(math.log10(currNode.data)) + 1) % 2 == 0:
            dataStr = str(currNode.data)
            currNode.data = int(dataStr[:len(dataStr) // 2])
            currNode.insertNext(int(dataStr[len(dataStr) // 2:]))
        else:
            currNode.data *= 2024
        currNode = currNode.prev # reverse order to skip newly added stones 

    while stonesTail.next:
        stonesTail = stonesTail.next

stoneCount = 0
currNode = stonesTail
while currNode:
    stoneCount += 1
    currNode = currNode.prev 

print('PART 1: %d' % stoneCount)

