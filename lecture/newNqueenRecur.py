# N Queen Problem
# Recursive solution
import time
numQueens = 0
def isSafe(testRow, testCol):
    # no need to check for row 0
    if testRow == 0:
        return True
    for row in range(0, testRow):
        # check vertical
        if testCol == currentSolution[row]:
            return False
        # diagonal
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False
    # no attack found
    return True

def placeQueen(row):
    global currentSolution, solutions, numQueens
    for col in range(numQueens):
        if not isSafe(row, col):
            continue
        else:
            currentSolution[row] = col
            if row == (numQueens - 1):
                #  last row
                solutions.append(currentSolution.copy())
            else:
                placeQueen(row + 1)

print("%12s%10s%16s" % ("N Size", "numSol", "Seconds"))
startFrom = 4
end = 13
for i in range(startFrom, end+1):
    numQueens = i
    # will hold current testing data
    currentSolution = [0 for x in range(numQueens)]
    solutions = []  # found solutions
    startTime = time.time()
    placeQueen(0)
    elapsedTime = time.time() - startTime
    print("%12d%10d%20.8f" % (numQueens, len(solutions), elapsedTime))