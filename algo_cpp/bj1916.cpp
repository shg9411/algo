#include <iostream>
#include <queue>
#define INF 987654321
using namespace std;

vector<pair<int, int>> adj[1001];
int dist[1001];

void dijkstra(int s, int e) {
	priority_queue<pair<int, int>> pq;
	dist[s] = 0;
	pq.push({ 0,s });
	while (!pq.empty()) {
		int cost, cur;
		cost = -pq.top().first;
		cur = pq.top().second;
		pq.pop();
		if (dist[cur] < cost)
			continue;
		for (auto& n : adj[cur]) {
			int tmpCost = cost + n.second;
			if (tmpCost < dist[n.first]) {
				dist[n.first] = tmpCost;
				pq.push({ -tmpCost ,n.first });
			}
		}

	}
	cout << dist[e];
}

int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n, m,s,e;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int u, v, c;
		cin >> u >> v >> c;
		adj[u].push_back({ v,c });
	}
	cin >> s >> e;
	for (int i = 1; i <= n; i++)
		dist[i] = INF;
	dijkstra(s, e);
	return 0;
}