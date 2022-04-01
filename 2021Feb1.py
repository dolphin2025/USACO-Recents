
# Increase recursion limit
import sys
sys.setrecursionlimit(10000000)

# Check if a cow is comfortable. If there are 3 cows adjacent to it and it's comfortable, return the cow that needs to be added
def iscomfortable(grid, u, v):
    numadj = 0
    for (xdif, ydif) in adj:
        if grid[u + xdif + 500][v + ydif + 500] == 1: numadj += 1
        else: missingCow = (u + xdif, v + ydif)
    if numadj == 3: return missingCow
    return 'not comfortable'

# Function to add a cow at a given location. If the added cow and adjacent cows are comfortable, recursively add cows accordingly
def addcow(grid, numcows, u, v):
    if grid[u + 500][v + 500]: return numcows - 1
    grid[u + 500][v + 500] = 1
    cow = iscomfortable(grid, u, v)
    if cow != 'not comfortable': numcows = addcow(grid, numcows, cow[0], cow[1]) + 1
    for (xdif, ydif) in adj:
        if grid[u + xdif + 500][v + ydif + 500]:
            cow = iscomfortable(grid, u + xdif, v + ydif)
            if cow != 'not comfortable': numcows = addcow(grid, numcows, cow[0], cow[1]) + 1
    return numcows

# We keep track of the positions of the cows with a 2D boolean grid (starts empty)
n = int(input())
grid = [[0] * 2000 for i in range(2000)]
adj = ((0, 1), (0, -1), (-1, 0), (1, 0))

# Go through through the input cows, adding them and keeping track of the number of cows as we go
numcows = 0
for (x, y) in [[int(i) for i in input().split()] for line in range(n)]:
    numcows = addcow(grid, numcows, x, y)
    print(numcows)
