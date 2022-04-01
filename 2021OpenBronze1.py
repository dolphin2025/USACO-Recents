
n, l = [int(i) for i in input().split()]
p = sorted([int(i) for i in input().split()])[::-1]
h = max(i for i in range(len(p) + 1) if p[i - 1] >= i)

for i in range(len(p)):
    if p[i] == h and l > 0:
        p[i] += 1
        l -= 1
print(max(i for i in range(len(p) + 1) if p[i - 1] >= i))
