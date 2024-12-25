NUM_PINS = 5
MAX_HEIGHT = 7

locks = []
keys = []
with open('input/day25.txt', 'r') as f:
    buffer = f.read().split('\n\n')
    for block in buffer:
        block = block.split('\n')
        heights = []
        for x in range(NUM_PINS):
            columnHeight = -1
            for y in range(MAX_HEIGHT):
                if block[y][x] == '#':
                    columnHeight += 1
            heights.append(columnHeight)
        if block[0][0] == '#':
            locks.append(heights)
        else:
            keys.append(heights)

numMatches = 0
for lock in locks:
    for key in keys:
        isMatch = True
        for i in range(NUM_PINS):
            if lock[i] + key[i] >= MAX_HEIGHT - 1:
                isMatch = False
                break

        numMatches += isMatch

print('PART ONE %d' % numMatches)

