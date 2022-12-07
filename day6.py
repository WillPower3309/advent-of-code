datastream = ''
with open('input/day6.txt', 'r') as f:
    datastream = f.read().strip()

def findMarkerInBuffer(numDistinct, buffer):
    markers = {}
    numNotMarker = 0
    for i in range(len(buffer)):
        marker = buffer[i]
        prevOccurance = markers.get(marker, -1)
        markerToDistinctDistance = prevOccurance + numDistinct - 1 - i
        if markerToDistinctDistance < 0 and numNotMarker == 0:
            return i + 1
        elif prevOccurance >= 0:
            numNotMarker = max(numNotMarker - 1,  markerToDistinctDistance)
        elif numNotMarker > 0:
            numNotMarker -= 1
        markers[marker] = i

# PART ONE
print(findMarkerInBuffer(4, datastream))
# PART TWO
print(findMarkerInBuffer(14, datastream))
