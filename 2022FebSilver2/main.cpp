#include <bits/stdc++.h>
using namespace std;

array<int,2> a[50]; long long ans[50];

map<array<int,2>,map<int,int>> comp(int i) {
    if (i == -1) return {{{0,0},{{0,1}}}};
    map<array<int, 2>, map<int, int>> s = comp(i-1);
    auto scopy = s;
    for (auto[coords, mp]: scopy) for (auto[moves, cnt]: mp) {
            array<int, 2> newcoords = {coords[0] + a[i][0], coords[1] + a[i][1]};
            if (s.count(newcoords) and s[newcoords].count(moves + 1)) s[newcoords][moves + 1] += cnt;
            else s[newcoords][moves + 1] = cnt;
    }
    return s;
}

int main() {
    int n, xg, yg; cin >> n >> xg >> yg;
    for (int i = 0; i < n / 2; i++) cin >> a[i][0] >> a[i][1];
    map<array<int, 2>, map<int, int>> l = comp(n / 2 - 1);
    for (int i = 0; i < n - n / 2; i++) cin >> a[i][0] >> a[i][1];
    map<array<int, 2>, map<int, int>> r = comp(n - n / 2 - 1);
    for (auto[coords, mp]: l) {
        array<int, 2> newcoords = {xg - coords[0], yg - coords[1]};
        if (r.count(newcoords)) for (auto[moves1, cnt1]: l[coords]) for (auto[moves2, cnt2]: r[newcoords])
            ans[moves1 + moves2] += (long long)cnt1 * (long long)cnt2;
    }
    for (int moves = 1; moves <= n; moves++) cout << ans[moves] << endl;
}