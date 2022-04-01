
import time


n=int(input())

points=[]
for i in range (n):
    points.append([int(i) for i in input().split()])

grid = [[0]*(n+1) for i in range (n+1)]
points.sort()
for i in range (n): points[i][0] = i+1
points.sort(key= lambda x: x[1])
for i in range (n): points[i][1] = i+1
for (x,y) in points:
    grid[x][y] = 1
s=time.clock()
for i in range (1,n+1):
    for j in range (1,n+1):
        grid[i][j]+=grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
ans=1
def rect(l,r,u,d):
    return grid[r][u]-grid[l-1][u]-grid[r][d-1]+grid[l-1][d-1]
print(time.clock()-s)
for a in points:
    for b in points:
        if a[1]<=b[1]:
            ans+=rect(1,min(a[0],b[0]),b[1],a[1])*rect(max(a[0],b[0]),n,b[1],a[1])
print(ans)
print(time.clock()-s)