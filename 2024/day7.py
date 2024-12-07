# PART ONE

totalCalibrationResult = 0

with open('input/day7.txt', 'r') as f:
    for line in f:
        nums = line.split(" ")

        target = int(nums[0][:-1])

        currValues = [int(nums[1])]
        for num in nums[2:]:
            newCurrValues = []
            for val in currValues:
                sum = int(num) + val
                if sum <= target:
                    newCurrValues.append(sum)
                product = int(num) * val
                if product <= target:
                    newCurrValues.append(product)

            currValues = newCurrValues

        for val in currValues:
            if val == target:
                totalCalibrationResult += target
                break


print('PART 1: %d' % totalCalibrationResult)

# PART TWO

totalCalibrationResult = 0

with open('input/day7.txt', 'r') as f:
    for line in f:
        nums = line.split(" ")

        target = int(nums[0][:-1])

        currValues = [int(nums[1])]
        for num in nums[2:]:
            newCurrValues = []
            for val in currValues:
                sum = int(num) + val
                if sum <= target:
                    newCurrValues.append(sum)
                product = int(num) * val
                if product <= target:
                    newCurrValues.append(product)
                concat = int(str(val) + num)
                if concat <= target:
                    newCurrValues.append(concat)

            currValues = newCurrValues

        for val in currValues:
            if val == target:
                totalCalibrationResult += target
                break


print('PART 2: %d' % totalCalibrationResult)

