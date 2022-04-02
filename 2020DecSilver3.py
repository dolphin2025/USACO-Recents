
n = int(input())
N,E = [], []
for i in range (n):
    line = input().split()
    if line[0] == 'N': N.append([i,int(line[1]),int(line[2])])
    else: E.append([i,int(line[1]),int(line[2])])

blame = [0]*n
stopped = [10**10]*n
events = [[n[0],e[0],e[2]-n[2],n[1]-e[1]] for n in N for e in E if e[1]<n[1] and n[2]<e[2]]
events.sort(key= lambda x: max(x[2:]))

for ev in events:
    if stopped[ev[0]]>ev[2] and stopped[ev[1]]>ev[3]:
        if ev[2] < ev[3]:
            stopped[ev[1]] = ev[3]
            blame[ev[0]] += blame[ev[1]]+1
        if ev[3] < ev[2]:
            stopped[ev[0]] = ev[2]
            blame[ev[1]] += blame[ev[0]]+1
print('\n'.join(str(i) for i in blame))
