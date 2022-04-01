
n,m = [int(i) for i in input().split()]
grid = [input() for i in range (n)]
pairs = set()

for i in range(n):
    for j in range(m):
        if grid[i][j]=='G':
            # Fun fact: if the line below wasn't a one-liner, the code times out on testcase #9!
            adj=[(i+x,j+y) for x,y in ((0,1),(1,0),(-1,0),(0,-1)) if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y]=='C']
            if len(adj)>=2: pairs.add(tuple(adj))
print(len(pairs))