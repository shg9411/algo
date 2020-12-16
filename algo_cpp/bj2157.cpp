#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, k, dp[301][301];
vector<vector<pair<int, int>>> adj;


int main(void) {
	scanf("%d%d%d", &n, &m, &k);
	adj.resize(n + 1);
	for (int i = 0; i < k; ++i) {
		int s, d, w;
		scanf("%d%d%d", &s, &d, &w);
		if (s > d)
			continue;
		adj[s].push_back({ d,w });
	}
	for (int i = 0; i < adj[1].size(); ++i) {
		int next = adj[1][i].first;
		int weight = adj[1][i].second;
		dp[next][2] = max(dp[next][2], weight);
	}
	for (int i = 2; i <= m; ++i) {
		for (int cur = 1; cur <= n; ++cur) {
			if (dp[cur][i] != 0) {
				for (int j = 0; j < adj[cur].size(); ++j) {
					int next = adj[cur][j].first;
					int weight = adj[cur][j].second;
					dp[next][i + 1] = max(dp[next][i + 1], dp[cur][i] + weight);
				}
			}
		}
	}
	int ans = 0;
	for (int i = 2; i <= m; ++i)
		ans = max(ans, dp[n][i]);
	printf("%d", ans);

	return 0;
}