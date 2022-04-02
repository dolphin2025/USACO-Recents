#include <bits/stdc++.h>

using namespace std;
#define REP(i, a, b) for (int i=a; i<b; ++i)
#define FOR(i, n) REP(i, 0, n)

int n, single[501], edges[501][501], a[501][501], seen[501], reachable[501][501];

void dfs(int u) {
    seen[u] = 1;
    FOR(v, n) if (edges[u][v] and !seen[v]) dfs(v);
}

int main() {
    cin >> n;
    FOR(i, n) FOR(j, n) {
            cin >> a[i][j];
            a[i][j]--;
    }
    FOR(i, n) for (auto j: a[i]) {
            if (i == j) break;
            edges[i][j] = 1;
    }
    FOR(i, n) if (a[i][0] == i) single[i] = 1;
    FOR(cur, n) {
        FOR(i, n) seen[i] = 0;
        dfs(cur);
        FOR(i, n) if (seen[i]) reachable[cur][i] = 1;
    }
    FOR(cur, n) for (auto i: a[cur]) if (i == cur or reachable[i][cur]) {
                cout << i + 1 << endl;
                break;
    }
}
