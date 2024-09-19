# This program solves The Josephus Problem using a formulaic solution.
import math
import argparse

parser = argparse.ArgumentParser()

#args
parser.add_argument(
        'n',
        type=int,
        help="Amount of people in the circle."
)

parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enables verbose mathematical output.'
)

args = parser.parse_args()


def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2

    return True

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

survivor = calcSurvivingPos(args.n)
if args.verbose:
        print("Is power of 2:",isPowerOfTwo(args.n))
        print("Nearest power of 2 is", nearestPowOf2(args.n))
        print("To survive, stand in position", str(survivor) + ".")
else:
    print("To survive, stand in position", str(survivor) + ".")