secretNumbers = []
with open('input/day22.txt', 'r') as f:
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

print('PART ONE: %d' % finalSecretNumberSum)

prices = []
for number in secretNumbers:
    monkeyPrices = []
    for _ in range(2000):
        number = ((number * 64) ^ number) % 16777216
        number = ((number // 32) ^ number) % 16777216
        number = ((number * 2048) ^ number) % 16777216
        monkeyPrices.append(number % 10)
    prices.append(monkeyPrices)

changePrices = {}
maxMoney = 0
for monkeyPrices in prices:
    changeSequences = set() # only buy on first sequence per monkey
    for i in range(4, len(monkeyPrices)):
        changeSequenceArr = []
        for j in range(i - 4, i):
            changeSequenceArr.append(monkeyPrices[j + 1] - monkeyPrices[j])

        changeSequence = tuple(changeSequenceArr)
        if changeSequence in changeSequences:
            continue
        changeSequences.add(changeSequence)
        changePrices[changeSequence] = changePrices.get(changeSequence, 0) + monkeyPrices[i]
        maxMoney = max(maxMoney, changePrices[changeSequence])

print('PART TWO: %d' % maxMoney)

