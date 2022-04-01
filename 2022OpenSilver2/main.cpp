#include <bits/stdc++.h>
using namespace std;
#define REP(i, a, b) for (int i=a; i<b; ++i)
#define FOR(i, n) REP(i, 0, n)

const int maxn = 2e5;
vector<int> in[maxn];
long long ans = 0, a, b, nxt[maxn], weight[maxn], seen[maxn];

int main() {
    int n; cin >> n;
    FOR(i, n) {
        cin >> a >> b;
        nxt[i] = a - 1;
        weight[i] = b;
        ans += b;
        in[a - 1].push_back(i);
    }
    FOR(i, n) if (!seen[i]) {
        vector<int> cycle = {};
        for (; !seen[i]; i = nxt[i]) cycle.push_back(i), seen[i] = 1;
        if (count(cycle.begin(), cycle.end(), nxt[cycle.back()])) {
            long long minedge = 1e9;
            REP(u, *find(cycle.begin(), cycle.end(), nxt[cycle.back()]), cycle.size()) minedge = min(minedge, weight[cycle[u]]);
            ans -= minedge;
        }
    }
    cout << ans;
}
