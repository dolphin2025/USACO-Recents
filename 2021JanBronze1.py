
# the starting index is set to 100 so that the first letter counts as a new starting of the alphabet
cowphabet, index, ans = input(), 100, 0

# loop through the letters that were heard
for i in input():
    # if the current letter is before the previous letter in the cowphabet, then Bessie must have restarted the alphabet
    if cowphabet.index(i) <= index:
        # so we increase the count of the number of times Bessie said the cowphabet
        ans += 1
    index = cowphabet.index(i)
print(ans)