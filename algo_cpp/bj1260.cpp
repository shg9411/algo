#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, M, V;
vector<vector<int>> adj(1001);
queue<int> q;
bool visited[1001];
void dfs(int u) {
	cout << u << ' ';
	for (int v : adj[u]) {
		if (visited[v])
			continue;
		visited[v] = true;
		dfs(v);
	}
}

void bfs() {
	while (!q.empty()) {
		int tmp = q.front();
		q.pop();
		cout << tmp << ' ';
		for (int v : adj[tmp]) {
			if (visited[v])
				continue;
			visited[v] = 1;
			q.push(v);
		}
	}
}

int main(void) {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	cin >> N >> M >> V;
	for (int i = 0; i < M; i++) {
		int u, v;
		cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	for (auto& list : adj)
		sort(list.begin(), list.end());
	visited[V] = 1;
	dfs(V);
	cout << '\n';
	memset(visited, 0, sizeof(visited));
	q.push(V);
	visited[V] = 1;
	bfs();

	return 0;
}