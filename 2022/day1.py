# not perfectly optimal but certainly very pythonic :)

buffer = []
with open('input/day1.txt', 'r') as f:
    buffer = f.read().split('\n\n')

totalCalorieList = []
for elf in buffer:
    calorieList = (list(filter(None, elf.split('\n'))))
    totalCalorieList.append(sum([int(x) for x in calorieList]))
totalCalorieList.sort(reverse=True)

# PART ONE
print('The elf carrying the most calories is carrying %d' % totalCalorieList[0])
# PART TWO
print('The elf carrying the most calories is carrying %d' % sum(totalCalorieList[0:3]))
