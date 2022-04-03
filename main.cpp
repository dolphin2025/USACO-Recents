#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for (int i=0; i<n; ++i)
#define mn(v, x) (v = min(v, x));

vector<int> in[200000];
long long ans = 0, n, a, b, nxt[200000], v[200000], seen[200000];

int main() {
    cin >> n; FOR(i, n) (cin >> a >> b), nxt[i] = a - 1, v[i] = b, ans += b, in[a - 1].push_back(i);
    FOR(i, n) {
        vector<int> cycle = {}; for (; !seen[i]; i = nxt[i]) cycle.push_back(i), seen[i] = 1;
        long long start = 0, minedge = 1e9;
        for (auto u: cycle) start += u == nxt[cycle.back()], start and mn(minedge, v[u]);
        if (start) ans -= minedge;
    }
    cout << ans;
}
