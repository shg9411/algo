#include<cstdio>
#include <vector>
inline int g_u() { return _getchar_nolock(); }

int dp[1001], time[1001];
std::vector<int> adj[1001];

inline void scan(int& x)
{
	int c = g_u();
	x = 0;
	int neg = 0;
	for (; ((c < 48 || c>57) && c != '-'); c = g_u());
	if (c == '-') {
		neg = 1;
		c = g_u();
	}
	for (; c > 47 && c < 58; c = g_u()) {
		x = (x << 1) + (x << 3) + c - 48;
	}
	if (neg)
		x = -x;
}


int dfs(int u) {
	if (dp[u] != -1)
		return dp[u];
	int m = 0;
	for (int v : adj[u]) {
		int tmp = dp[v] == -1 ? dfs(v) : dp[v];
		if (tmp > m)
			m = tmp;
	}
	dp[u] = m + time[u];
	return dp[u];
}

void solve() {
	int N, K;
	scan(N); scan(K);
	for (int i = 1; i <= N; i++) {
		scan(time[i]);
		adj[i].clear();
		dp[i] = -1;
	}
	for (int i = 0; i < K; i++) {
		int x, y;
		scan(x); scan(y);
		adj[y].push_back(x);
	}
	int target;
	scan(target);
	printf("%d\n", dfs(target));
}

int main(void) {
	int T;
	scan(T);
	for (int i = 0; i < T; i++)
		solve();
	return 0;
}