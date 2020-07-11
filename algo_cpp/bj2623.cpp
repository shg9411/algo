#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

queue<int> q;
vector<int> singer[1001],res;
int n, m, cnt[1001];

bool topology() {
    for (int i = 1; i <= n; i++) {
        if (cnt[i] == 0) {
            q.push(i);
            res.push_back(i);
        }
    }
    int tmp;
    for (int i = 0; i < n; i++) {
        if (q.empty()) {
            return false;
        }
        tmp = q.front(); q.pop();
        for (auto next : singer[tmp]) {
            if (--cnt[next] == 0) {
                q.push(next);
                res.push_back(next);
            }
        }
    }
    return true;
}

int main(void) {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++) {
        int x, before, after;
        scanf("%d%d", &x, &before);
        for (int i = 0; i < x - 1; i++) {
            scanf("%d", &after);
            singer[before].push_back(after);
            cnt[after]++;
            before = after;
        }
    }
    if (topology()) {
        for (int i : res)
            printf("%d\n", i);
    }
    else {
        printf("0\n");
    }
    return 0;
}
