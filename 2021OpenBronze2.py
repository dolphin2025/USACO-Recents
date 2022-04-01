
k, n = [int(i) for i in input().split()]
cows = input().split()
pos = {cow: cows.index(cow) for cow in cows}
ans = [['?' for i in range(n)] for j in range(n)]

for _ in range(k):
    p = input().split()
    for i in range(n - 1):
        if p[i] > p[i + 1]:
            for l in range(i + 1):
                for r in range(i + 1, n):
                    ans[pos[p[l]]][pos[p[r]]] = '0'
                    ans[pos[p[r]]][pos[p[l]]] = '1'

for i in range(n):
    ans[i][i] = 'B'
    print(''.join(ans[i]))
