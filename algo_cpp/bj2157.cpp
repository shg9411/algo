#include <cstdio>
#include <cstring>
#include <vector>
#include <unordered_map>

using namespace std;

int n, m, k, a, b, c, dp[301][301];
unordered_map<int, int> v[301];

int solve(int idx, int cnt) {
	if (idx == n)
		return 0;
	if (cnt == m)
		return -1;
	int& res = dp[idx][cnt];
	if (res != -1)
		return res;
	res = -1;
	for (auto it = v[idx].begin(); it != v[idx].end(); it++) {
		if (it->second) {
			res = max(res, it->second + solve(it->first, cnt + 1));
		}
	}
	return res;
}

int main(void) {
	memset(dp, -1, sizeof(dp));
	scanf("%d%d%d", &n, &m, &k);
	for (int i = 0; i < k; i++) {
		scanf("%d%d%d", &a, &b, &c);
		if (b < a)
			continue;
		if (v[a].find(b) != v[a].end()) {
			v[a][b] = max(v[a][b], c);
		}
		else
			v[a][b] = c;
	}
	int r = solve(1, 1);
	printf("%d", r > 0 ? r : 0);
	return 0;
}