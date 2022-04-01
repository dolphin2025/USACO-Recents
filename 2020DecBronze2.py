
n,l = int(input()), [int(i) for i in input().split()]
print(sum([sum(l[i:j])/len(l[i:j]) in l[i:j] for i in range (n) for j in range (i+1,n+1)]))