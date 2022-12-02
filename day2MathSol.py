# convert A/B/C to 1/2/3
def abcToInt(move):
    return ord(move) - 64

# convert X/Y/Z to 1/2/3
def xyzToInt(move):
    return ord(move) - 87

##################
# PART ONE
##################

def responseToOutcome(challenge, response):
    outcome = (challenge - response) % 3
    if outcome == 0: # tie
        return 3
    elif outcome == 1: # loss
        return 0
    elif outcome == 2: # win
        return 6

f = open('input/day2.txt', 'r')

totalScore = 0
buffer = f.readline()
while buffer:
    challenge = abcToInt(buffer[0])
    response = xyzToInt(buffer[2])
    totalScore += response + responseToOutcome(challenge, response)
    buffer = f.readline()

print("the score according to the strategy guide would be %d" % totalScore)

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

f = open('input/day2.txt', 'r')

totalScore = 0
buffer = f.readline()
while buffer:
    challenge = abcToInt(buffer[0])
    outcome = (xyzToInt(buffer[2]) - 1) * 3
    totalScore += outcome + outcomeToResponse(challenge, outcome)
    buffer = f.readline()

print("the score according to the strategy guide would be %d" % totalScore)
