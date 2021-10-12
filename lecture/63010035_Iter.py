import time  # import time functions

# -----------------------------------------
# function used to test if queen can be placed at location
def placable(row, col):
    # Check if other queen in same column
    # if another queen, return false
    for prevCol in sol:
        if col == prevCol:
            return False
    # Check for other queen in diagonals
    # if there is queen, return false
    for prevRow, prevCol in enumerate(sol):
        if abs(row - prevRow) == abs(col - prevCol):
            return False
    # if no issues queen can be placed, return true
    return True

startFrom = int(input("Please enter the number for starting point : "))
end = int(input('Please enter the number for ending point : '))
print("N-Queen Solver Iterative Solution")
# create stack to store solutions
sol = []
# create row,column and count, set to 0
row = 0
col = 0
count = 0
# set flag used to check for first result to True
first = True
# record time program started
# loop
print("%12s%10s%16s" % ("N Size", "numSol", "Seconds"))
for i in range(startFrom, end+1):
    n = i
    startTime = time.time()
    # create stack to store solutions
    sol = []
    # create row,column and count, set to 0
    row = 0
    col = 0
    count = 0
    # set flag used to check for first result to True
    first = True
    while True:
        # Each Q must be placed in unique column
        # Checks if there is remaining space where Q can be placed
        while col < n:
            # Checks if Q can be placed in next row
            if placable(row, col):
                # place queen in column
                # set column to 0, increase row by 1
                sol.append(col)
                col = 0
                row += 1
                # exit loop break
            else:  # otherwise move to next position in row
                col += 1
        # if cant place
        if row == n or col == n:
            # backtrack
            if col == n and row != 0:
                # find column of last queen in stack and add 1
                # used for next iteration
                col = sol[-1] + 1
                # remove last queen placed
                sol.pop()
                # go to previous row
                row -= 1
            # if already backtracked to first row, no solution
            if row == 0 and col == n:
                # exit loop
                break
            # board complete if n - 1 rows have queens filled (index starts at 0)
            # Found Solution
            if row == n - 1:
                # if first solution found, record time in variable
                if first:
                    first = False
                    firstTime = time.time()

                # increase counter and backtrack
                # count = count + 1
                sol.append(col - 1)
                count += 1

                sol.pop()
    # output results
    elapsedTime = time.time() - startTime
    print("%12d%10d%20.8f" % (n, count, elapsedTime))