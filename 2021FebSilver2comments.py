
n, k = [int(i) for i in input().split()]

# Find which 12-year periods of time Bessie needs to visit, including the present
p = [1] + [int((-1) * int(input()) / 12) for i in range(n)]

# Remove duplicates and sort
p = sorted(list(set(p)))

# Bessie needs visit all of these except the present
visited = len(p) - 1

# Find the gaps between ranges consecutive ancestors
gaps = sorted([p[i+1]-p[i]-1 for i in range(len(p)-1) if p[i+1]-p[i]>1])

# If we have enough teleports to visit all of the ranges independently, then we don't need to visit any additional time periods
if k >= len(gaps): print(visited * 12)

# If we don't have enough teleports, we wait through smallest gaps in between the ranges
else:
    for i in gaps[:len(gaps) - k]: visited += i
    print(visited * 12)
