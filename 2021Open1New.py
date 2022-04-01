
n = int(input())
grid = [input() for i in range (n)]
grid = [[grid[i][3 * j:3 * (j + 1)] for j in range(n)] for i in range(n)]
s, w = set(), set()

def dfs(i, j, b):
    if 0 <= i < n and 0 <= j < n and grid[i][j] != '###' and (i, j, b) not in s:
        s.add((i, j, b))
        if any([b[l[0]],b[l[1]],b[l[2]]] in [[1,1,2],[2,1,1]] for l in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]): w.add(b)
        else:
            b = list(b)
            if grid[i][j][0] in ['O', 'M']:
                x = 3 * (int(grid[i][j][1]) - 1) + int(grid[i][j][2]) - 1
                if b[x] == 0: b[x] = [0, 'O', 'M'].index(grid[i][j][0])
            for (x, y) in ((0, 1), (1, 0), (-1, 0), (0, -1)): dfs(i + x, j + y, tuple(b))

[dfs(i, j, tuple([0]) * 9) for i in range(n) for j in range(n) if grid[i][j] == 'BBB']
print(len(w))