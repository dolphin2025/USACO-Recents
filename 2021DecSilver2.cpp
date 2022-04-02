#include <bits/stdc++.h>
using namespace std;
#define f0r(i, n) for (int i=0; i<n; i++)
#define mn(x, v) x = min(x, v)

int t, n, m, a, b, p[111111];
int cc(int x) { return p[x] == x ? x : p[x] = cc(p[x]); }

int main() {
    cin >> t; f0r(tc, t) {
        cin >> n >> m;
        f0r(i, n) p[i] = i;
        f0r(i, m) {
            cin >> a >> b;
            a = cc(a - 1), b = cc(b - 1);
            if (a != b) p[a] = b;
        }
        vector<array<int, 2>> dst(n, {n, n}), ccdst(n, {n, n});
        f0r(i, n) f0r(d, 2) {
            if (i) dst[i][d] = dst[i - 1][d] + 1;
            if (cc(i) == cc(d * (n - 1))) dst[i][d] = 0;
            mn(ccdst[cc(i)][d], dst[i][d]);
        }
        for (int i = n - 1; i; i--) f0r(d, 2) {
            if (i < n - 1) dst[i][d] = dst[i + 1][d] + 1;
            if (cc(i) == cc(d * (n - 1))) dst[i][d] = 0;
            mn(ccdst[cc(i)][d], dst[i][d]);
        }
        long long ans = 1e18;
        f0r(i, n) mn(ans, (long long) (pow(ccdst[cc(i)][0], 2) + pow(ccdst[cc(i)][1], 2)));
        cout << ans << endl;
    }
}