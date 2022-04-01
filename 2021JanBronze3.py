
n = int(input())
# get the cows from tallest to shortest
cows = sorted([int(i) for i in input().split()],reverse=True)
stalls = [int(i) for i in input().split()]

ans = 1
taken = 0
for i in cows:
    # the number of choices for a given cow is the number of stalls that it fits in minus the taken stalls
    ans *= sum(stall>=i for stall in stalls)-taken
    taken += 1
print(ans)
