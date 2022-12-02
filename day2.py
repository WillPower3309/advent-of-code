# convert A/B/C to 1/2/3
def abcToInt(move):
    return ord(move) - 64

# convert X/Y/Z to 1/2/3
def xyzToInt(move):
    return ord(move) - 87

##################
# PART ONE
##################

outcomeArr = [3, 0, 6]

totalScore = 0
with open('input/day2.txt', 'r') as f:
    for line in f:
        challenge = abcToInt(line[0])
        response = xyzToInt(line[2])
        totalScore += response + outcomeArr[(challenge - response) % 3]

print('the score according to the strategy guide would be %d' % totalScore)

##################
# PART TWO
##################

def outcomeToResponse(challenge, outcome):
    if outcome == 3: # tie
        return challenge
    elif outcome == 0: # loss
        return (challenge + 1) % 3 + 1
    elif outcome == 6: # win
        return (challenge) % 3 + 1

totalScore = 0
with open('input/day2.txt', 'r') as f:
    for line in f:
        challenge = abcToInt(line[0])
        outcome = (xyzToInt(line[2]) - 1) * 3
        totalScore += outcome + outcomeToResponse(challenge, outcome)

print('the score according to the strategy guide would be %d' % totalScore)
