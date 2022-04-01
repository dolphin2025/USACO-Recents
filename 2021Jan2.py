
def st(s):
    for o in range (60,100):
        

n,q = [int(i) for i in input().split()]
s = [ord(i) for i in input().split()]
for i in range (q):
    u,v=[int(x) for x in input().split()]
    print(st(s[:u-1]),st(s[v-1:]))