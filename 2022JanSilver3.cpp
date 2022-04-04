#include <bits/stdc++.h>

using namespace std;
#define REP(i, a, b) for (int i=a; i<b; ++i)
#define FOR(i, n) REP(i, 0, n)

int n, cnt = 0, m, a, b, vis[200000], vis2[200000], edgevis[200000];
array<int, 2> edge = {-1, -1};
vector<array<int, 3>> edges[200000];
vector<int> eat, hungry;

void dfs(int u, int num) {
    vis[u] = 1;
    for (auto[v, i, d]: edges[u]) if (num != i) {
            if (vis[v]) {
                if (d == 1) edge = {u, i};
                else edge = {v, i};
            } else dfs(v, i);
    }
}

void dfs2(int u) {
    vis2[u] = 1;
    for (auto[v, i, d]: edges[u]) if (i != edge[1] and !edgevis[i]) {
            edgevis[i] = 1;
            if (vis2[v]) hungry.push_back(i);
            else eat.push_back(i), dfs2(v);
    }
}

int main() {
    cin >> n >> m;
    FOR(i, n) (cin >> a >> b), edges[a].push_back({b, i + 1, 1}), edges[b].push_back({a, i + 1, -1});
    FOR(u, m + 1) if (!vis2[u]) {
        edge = {-1, -1}, dfs(u, -1);
        if (edge[0] == -1) dfs2(u);
        else eat.push_back(edge[1]), dfs2(edge[0]);
    }
    cout << hungry.size() << endl;
    for (auto i: eat) cout << i << endl;
    for (auto i: hungry) cout << i << endl;
}
