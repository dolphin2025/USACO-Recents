from math import *
# print(ceil(log2(2)))
deg, ans, n = [0] * 200000, 0, int(input())

for _ in range(n - 1):
    u, v = [int(i)-1 for i in input().split()]
    deg[u] += 1
    deg[v] += 1

print(sum(ceil(log2(i)) for i in deg[1:n] if i > 1) + ceil(log2(deg[0]+1)) + n - 1)