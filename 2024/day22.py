secretNumbers = []
with open('input/day21.txt', 'r') as f:
    for line in f:
        line = line.strip()
        secretNumbers.append(int(line))

finalSecretNumberSum = 0
for number in secretNumbers:
    for _ in range(2000):
        number = ((number * 64) ^ number) % 16777216
        number = ((number // 32) ^ number) % 16777216
        number = ((number * 2048) ^ number) % 16777216
    finalSecretNumberSum += number

print(finalSecretNumberSum)

