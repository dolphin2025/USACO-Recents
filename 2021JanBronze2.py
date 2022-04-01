
input()
# get each cow mod 2 in the input
cows = [int(i)%2 for i in input().split()]
# we can use the mod 2 values to get counts of even and odd cows
e, o = cows.count(0), cows.count(1)
# if there are too many odd cows
while o > e:
    # then we can combine them in to an even cow because the sum of 2 odd numbers is even
    o -= 2
    e += 1
# if there are too many even cows
if e > o + 1:
    # then we can just group the extras with the previous even groups, so we don't really have to worry about them
    e = o + 1
# now each cow is it's own group, so the total number of groups is the total number of cows
print(e+o)