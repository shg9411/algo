#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    long long n,a,b,c,ans,tmp;
    map<long double, long long> inc;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b >> c;
        inc[(-a / (long double)b)]++;
    }
    ans = n * (n - 1) / 2ll;
    for (auto d : inc)
        ans -= d.second * (d.second - 1) / 2ll;
    cout << ans;

    return 0;
}
