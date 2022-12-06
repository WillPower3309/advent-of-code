datastream = ''
with open('input/day6.txt', 'r') as f:
    datastream = f.read().strip()

def findMarkerInBuffer(numDistinct, buffer):
    markers = {}
    numNotMarker = 0
    for i in range(len(buffer)):
        marker = buffer[i]
        lastMarkerIndex = markers.get(marker, -1)
        if lastMarkerIndex < i - (numDistinct - 1) and numNotMarker == 0:
            return i + 1
        elif lastMarkerIndex >= 0:
            numNotMarker = max(numNotMarker - 1,  (numDistinct - 1) - (i - lastMarkerIndex))
        elif numNotMarker > 0:
            numNotMarker -= 1
        markers[marker] = i

# PART ONE
print(findMarkerInBuffer(4, datastream))
# PART TWO
print(findMarkerInBuffer(14, datastream))
