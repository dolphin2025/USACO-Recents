

def genstates(n):
    if n==0:
        a = [0,0,0,0,0,0,0,0,0]
        b = [0,0,0,0,0,0,0,0,0]
        c = [0,0,0,0,0,0,0,0,0]
        b[0]=1
        c[0]=2
        return [a,b,c]
    l=genstates(n-1)
    nl=[]
    for i in l:
        i1=i[:]
        i2=i[:]
        i1[n]=1
        i2[n]=2
        nl.append(i)
        nl.append(i1)
        nl.append(i2)
    return nl
x=genstates(8)
# print(len(x))
streaks = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
winstates=[]
for i in x:
    c=0
    st=[]
    for s in streaks:
        thing=[i[s[0]],i[s[1]],i[s[2]]]
        if (thing==[1,2,2]) or (thing==[2,2,1]):
            c+=1
            st.append(s[:])
    if c==1:
        winstates.append([i,st[0]])
    if c>1:
        common=st[0][:]
        for j in st[1:]:
            ncommon = common[:]
            for t in common:
                if t not in j:
                    ncommon.remove(t)
            common=ncommon[:]
        # if i == [0, 0, 1, 0, 2, 0, 2, 2, 1]:
            # print(common,st)
        if len(common)==1:
            winstates.append([i,common])
# print(len(winstates))
# print(winstates[782])
n=int(input())
grid=[[0 for i in range(n)] for j in range(n)]
inp=[input() for i in range(n)]
for i in range(n):
    for j in range(n):
        s=inp[i][j*3:(j+1)*3]
        if s=='###':
            grid[i][j]='w'
        elif s=='...':
            grid[i][j]='s'
        elif s=='BBB':
            grid[i][j]='b'
        else:
            grid[i][j]=(3*(int(s[1])-1)+(int(s[2])-1),[0,1][s[0]=='O'])
# for i in grid:
#     print(i)
bessiecarreach = set()
canreach = {(i,j):set() for i in range (9) for j in range (2)}

def dfs(i,j,type,seen):
    if (i, j) not in seen and 0 <= i < n and 0 <= j < n and grid[i][j]!='w':
        seen.add((i,j))
        val=grid[i][j]
        if type=='b' and val not in ['w','s','b']:
            bessiecarreach.add(val)
        elif val not in ['w','s','b']:
            canreach[type].add(val)
        else:
            dfs(i+1,j,type,seen)
            dfs(i,j+1,type,seen)
            dfs(i-1,j,type,seen)
            dfs(i,j-1,type,seen)
        if val==type:
            dfs(i + 1, j, type, seen)
            dfs(i, j + 1, type, seen)
            dfs(i - 1, j, type, seen)
            dfs(i, j - 1, type, seen)


for i in range(n):
    for j in range(n):
        if grid[i][j] not in ['s','w']:
            if grid[i][j]=='b':
                dfs(i,j,'b',set())
            else:
                dfs(i, j, grid[i][j], set())
# print(bessiecarreach)
# print(canreach)

def dfs2(u,allowed,seen):
    if u not in seen:
        seen.add(u)
        for v in canreach[u]:
            if v[0]==u[0] or v in allowed:
                seen = dfs2(v,allowed,seen)
    return seen

# print(dfs2((0,1),[(0,1),(0,0),(2,0),(7,1)],set()))

def canget(allowed):
    seen=set()
    for i in allowed:
        if i in bessiecarreach:
            seen=dfs2(i, allowed, seen)
    for i in allowed:
        if i not in seen:
            return False
    return True

ans=0
for s in winstates:
    allowed=set()
    for i in range(9):
        if s[0][i]!=0:
            allowed.add((i,s[0][i]-1))
    # if s[0]==[0,0,1,0,2,0,2,2,1]:
        # print(canget(na))
    if canget(allowed):
        for k in range (len(s[1])):
            na=[i for i in allowed]
            na.remove((s[1][k],s[0][s[1][k]]-1))
            if canget(na):
                ans+=1
                # print(s[0])
                break
print(ans)