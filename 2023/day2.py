##################
# PART ONE
##################

with open('input/day2.txt', 'r') as f:
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    totalGameSum = 0
    gameId = 0

    for line in f:
        gameId = gameId + 1
        validGame = True

        gameData = line.strip().split(': ')[1].split('; ')
        for gameRound in gameData:
            colorList = gameRound.split(', ')
            for color in colorList:
                colorData = color.split(' ')
                if colorData[1] == 'red' and int(colorData[0]) > MAX_RED:
                    validGame = False
                    break
                elif colorData[1] == 'green' and int(colorData[0]) > MAX_GREEN:
                    validGame = False
                    break
                elif colorData[1] == 'blue' and int(colorData[0]) > MAX_BLUE:
                    validGame = False
                    break
            if not validGame:
                break

        if validGame:
            totalGameSum = totalGameSum + gameId

    print("PART 1: %d" % totalGameSum)

##################
# PART TWO
##################

with open('input/day2.txt', 'r') as f:
    totalPower = 0

    for line in f:
        minRed = 0
        minGreen = 0
        minBlue = 0

        gameData = line.strip().split(': ')[1].split('; ')
        for gameRound in gameData:
            colorList = gameRound.split(', ')
            for color in colorList:
                colorData = color.split(' ')
                if colorData[1] == 'red':
                    minRed = max(minRed, int(colorData[0]))
                elif colorData[1] == 'green':
                    minGreen = max(minGreen, int(colorData[0]))
                elif colorData[1] == 'blue':
                    minBlue = max(minBlue, int(colorData[0]))

        totalPower = totalPower + (minRed * minGreen * minBlue)

    print("PART 2: %d" % totalPower)
