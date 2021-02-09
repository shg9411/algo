300001#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int K, V, E, u, v, check[300001];
vector<int> adj[300001];

void dfs(int n, int g) {
	check[n] = g;
	for (int j : adj[n]) {
		if (check[j] == -1) {
			dfs(j, !g);
		}
	}
}

void solve() {
	cin >> V >> E;
	for (int i = 1; i <= V; i++) {
		check[i] = -1;
		adj[i].clear();
	}
	for (int i = 0; i < E; i++) {
		cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	for (int i = 1; i <= V; i++) {
		if (check[i] == -1) {
			dfs(i, 1);
		}
	}
	for (int i = 1; i <= V; i++) {
		for (int j : adj[i]) {
			if (check[i] == check[j]) {
				cout << "NO\n";
				return;
			}
		}
	}
	cout << "YES\n";
}

int main(void) {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> K;
	for (int i = 0; i < K; i++)
		solve();
	return 0;
}