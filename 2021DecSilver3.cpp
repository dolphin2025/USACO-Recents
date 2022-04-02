#include <bits/stdc++.h>
using namespace std;
#define f0r(i, n) for(int i = 0; i < n; i++)

long long n, m, a, b, ans, asum[111111], bsum[111111], cnta[111111], cntb[111111];

int main() {
    cin >> n >> m;
    f0r(i, n) cin >> a >> b, cnta[a]++, cntb[b]++;
    f0r(i, m + 1) f0r(j, m + 1) asum[i + j] += cnta[i] * cnta[j], bsum[i + j] += cntb[i] * cntb[j];
    f0r(k, 2 * m + 1) ans += asum[k] - (k > 0) * bsum[k - 1], cout << ans << endl;
}
