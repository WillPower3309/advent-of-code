responseScoreDict = { 'X': 1, 'Y': 2, 'Z': 3 }

##################
# PART ONE
##################

outcomeDict = {
    'A': { 'X': 3, 'Y': 6, 'Z': 0 },
    'B': { 'X': 0, 'Y': 3, 'Z': 6 },
    'C': { 'X': 6, 'Y': 0, 'Z': 3 },
}

f = open('input/day2.txt', 'r')

totalScore = 0
buffer = f.readline()
while buffer:
    challenge = buffer[0]
    response = buffer[2]
    totalScore += responseScoreDict[response] + outcomeDict[challenge][response]
    buffer = f.readline()

print("the score according to the strategy guide would be %d" % totalScore)

##################
# PART TWO
##################

f = open('input/day2.txt', 'r')

responseDict = {
    'A': { 'X': 'Z', 'Y': 'X', 'Z': 'Y' },
    'B': { 'X': 'X', 'Y': 'Y', 'Z': 'Z' },
    'C': { 'X': 'Y', 'Y': 'Z', 'Z': 'X' },
}
outcomeDict = { 'X': 0, 'Y': 3, 'Z': 6 }

totalScore = 0
buffer = f.readline()
while buffer:
    challenge = buffer[0]
    outcome = buffer[2]
    response = responseDict[challenge][outcome]
    totalScore += responseScoreDict[response] + outcomeDict[outcome]
    buffer = f.readline()

print("the score according to the strategy guide would be %d" % totalScore)
