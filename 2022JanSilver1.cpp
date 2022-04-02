#include <bits/stdc++.h>
using namespace std;
#define REP(i, a, b) for (long long i=a; i<b; i++)
#define FOR(i, n) REP(i, 0, n)

long long a[400000];

int main() {
    long long n; cin >> n;
    long long ans = 0;
    FOR(i, n) cin >> a[i];
    FOR(i, n-1) {
        long long mx = 0;
        ans += 2;
        REP(j, i+1, n-1) {
            mx = max(mx, a[j]);
            if (mx<a[i] and mx<a[j+1]) ans += j+1-i+1;
        }
    }
    cout<<ans;
}
