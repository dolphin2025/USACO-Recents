
n, k = [int(i) for i in input().split()]
p = [1] + [int((-1) * int(input()) / 12) for i in range(n)]
p = sorted(list(set(p)))
visited = len(p) - 1
gaps = sorted([p[i+1]-p[i]-1 for i in range(len(p)-1) if p[i+1]-p[i]>1])
if k >= len(gaps): print(visited * 12)
else:
    for i in gaps[:len(gaps) - k]: visited += i
    print(visited * 12)
