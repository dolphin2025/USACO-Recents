
n=int(input())
a=[[int(i) for i in input().split()] for j in range (n)]
h=sum(max(sum([a[i][j] for i in range (n) if i%2]),sum([a[i][j] for i in range (n) if not i%2])) for j in range (n))
v=sum(max(sum([a[i][j] for j in range (n) if j%2]),sum([a[i][j] for j in range (n) if not j%2])) for i in range (n))
print(max(h,v))