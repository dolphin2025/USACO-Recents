#include <bits/stdc++.h>
using namespace std;
#define REP(i, a, b) for (long long i=a; i<b; ++i)
#define FOR(i, n) REP(i, 0, n)

string s, t;
const int maxn = 2e5;
int prefixs[20][maxn], prefixt[20][maxn], bad[20][20];
set<int> rem, noonecares;

int main() {
    cin >> s >> t;
    FOR(i, 18) {
        if (count(s.begin(),s.end(),'a'+i)!=count(t.begin(),t.end(),'a'+i)) {
            s.erase(remove(s.begin(),s.end(),'a'+i), s.end());
            t.erase(remove(t.begin(),t.end(),'a'+i), t.end());
            rem.insert(i);
        }
        if (count(s.begin(),s.end(),'a'+i)==0) noonecares.insert('a'+i);
    }
    int n = s.size();
    vector<vector<int>> occs(20, {-1}), occt(20, {-1});
    FOR(i, n) occs[s[i]-'a'].push_back(i), occt[t[i]-'a'].push_back(i);
    FOR(c, 18) FOR(i, n) prefixs[c][i+1] = prefixs[c][i]+(s[i]==('a'+c)), prefixt[c][i+1] = prefixt[c][i]+(t[i]==('a'+c));
    FOR(c1, 18) FOR(c2, 18) if (c1!=c2) FOR(i, occs[c1].size()-1) {
            if (prefixs[c2][occs[c1][i + 1]] - prefixs[c2][occs[c1][i]+1] !=
                prefixt[c2][occt[c1][i + 1]] - prefixt[c2][occt[c1][i]+1])
                bad[c1][c2] = 1;
    }
    vector<vector<int>> subsets = {{}};
    FOR(c2, 18) if (!rem.count(c2)) {
        vector<vector<int>> newsubsets;
        for (auto subset: subsets) {
            int good = 1;
            for (auto c1: subset) if (bad[c1][c2]) good = 0;
            if (good) {
                vector<int> newsubset;
                for (auto i: subset) newsubset.push_back(i);
                newsubset.push_back(c2);
                newsubsets.push_back(newsubset);
            }
        }
        for (auto i: newsubsets) subsets.push_back(i);
    }
    set<vector<int>> setofsubsets;
    for (auto i: subsets) setofsubsets.insert(i);
    int q; cin >> q; FOR(i, q) {
        string test; cin >> test;
        vector<int> inttest;
        for (auto c: test) if (!noonecares.count(c)) inttest.push_back(c-'a');
        cout<<((setofsubsets.count(inttest)) ? 'Y' : 'N');
    }
}
