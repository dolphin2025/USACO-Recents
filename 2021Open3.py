
n, k, l = [int(i) for i in input().split()]
a = list(reversed(sorted([int(i) for i in input().split()])))

def works(h):
    citationsleft = k * l
    for i in a[:h]:
        if i < h:
            citationsleft -= h-i
            if citationsleft < 0 or h - i > k: return False
    return True

low, high = 0, n
while low != high:
    mid = (low + high + 1) // 2
    if works(mid): low = mid
    else: high = mid -1

print(low)