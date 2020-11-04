#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
int s[400004];
int n, m;
vector<int> res;
int u(int idx, int val, int node, int x, int y) {
    if (idx < x || y < idx)
        return s[node];
    if (x == y)
        return s[node] = val;
    int mid = (x + y) >> 1;
    return s[node] = u(idx, val, node * 2, x, mid) + u(idx, val, node * 2 + 1, mid + 1, y);
}
int query(int val, int node, int x, int y) {
    if (x == y)
        return x;
    if (s[node * 2] >= val)
        return query(val, node * 2, x, (x + y) / 2);
    else
        return query(val - s[node * 2], node * 2 + 1, (x + y) / 2 + 1, y);
}
int f(int lo, int hi, int node, int x, int y) {
    if (y < lo || hi < x)
        return 0;
    if (lo <= x && y <= hi)
        return s[node];
    int mid = (x + y) >> 1;
    return f(lo, hi, node * 2, x, mid) + f(lo, hi, node * 2 + 1, mid + 1, y);
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
        u(i, 1, 1, 1, n);
    int mod = n - 1;
    res.push_back(m);
    u(m, 0, 1, 1, n);
    for (int i = 2; i <= n; i++) {
        int x = (f(1, res.back(), 1, 1, n) + m) % mod;
        if (!x)x = mod;
        res.push_back(query(x, 1, 1, n));
        u(res.back(), 0, 1, 1, n);
        mod--;
    }
    printf("<");
    for (int i = 0; i < res.size()-1; i++)
        printf("%d, ", res[i]);
    printf("%d>", res.back());
    return 0;
}