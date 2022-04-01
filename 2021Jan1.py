
import time
n,k = [int(i) for i in input().split()]
pos = [i for i in range (n)]
beento = [{i} for i in range(n)]
s = time.clock()
for _ in range(k):
    i,j = [int(x)-1 for x in input().split()]
    beento[pos[i]].add(j)
    beento[pos[j]].add(i)
    temp = pos[i]
    pos[i] = pos[j]
    pos[j] = temp
# print(pos,beento)
npos = [pos.index(i) for i in range (n)]
pos=npos[:]
seen=set()
one=0
two=0
print(time.clock()-s)
s = time.clock()
for i in range (n):
    # print(i)
    if not i in seen:
        one+=time.clock()-s
        s = time.clock()
        seen.add(i)
        l=[i]
        while not pos[l[-1]] == l[0]:
            l.append(pos[l[-1]])
            seen.add(pos[l[-1]])
        cyclestart = 0
        cyclesum = set()
        two += time.clock() - s
        s = time.clock()
        for asdf in l[cyclestart:]:
            cyclesum = cyclesum.union(beento[asdf])
        for b in l[cyclestart:]:
            beento[b]=cyclesum
        for b in range(cyclestart-1,-1,-1):
            beento[l[b]] = set(list(beento[l[b]])+list(beento[l[b+1]]))
for i in beento:
    print(len(i))
print(one,two)