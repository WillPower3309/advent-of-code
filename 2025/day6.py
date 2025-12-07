input = []

with open('input/day6.txt', 'r') as f:
    for line in f.read().splitlines():
        row = []
        for val in line.split(' '):
            if val != '':
                row.append(val)
        input.append(row)

# PART ONE
total = 0
for i, operation in enumerate(input[-1]):
    val = int(input[0][i])
    for j in range(1, len(input) - 1):
        num = int(input[j][i])
        if operation == '+':
            val += num
        else:
            val *= num
    total += val

print('PART 1: %d' % total)

