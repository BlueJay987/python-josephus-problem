# This program solves The Josephus Problem using a formulaic solution.
import math
# Variables
circleSize = 243

# This is needed to make the next function work
def Log2(x):
    if x == 0:
        return False
    return (math.log10(x) / math.log10(2))

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def nearestPowOf2(n):
    i = 1
    while math.pow(2, i) < n:
        i += 1
    return int(math.pow(2, i-1))

def calcSurvivingPos(n):
    if (isPowerOfTwo(n)):
        return 1
    y = n - nearestPowOf2(n) + 1
    return (y*2) - 1

survivor = calcSurvivingPos(circleSize)
print("To survive, stand in position", str(survivor) + ".")