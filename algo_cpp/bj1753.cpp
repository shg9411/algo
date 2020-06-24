#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

vector<pair<int, int>> vec[20001];
vector<int> res;
int V, E;

vector<int> dijkstra(int K) {
	vector<int> dist(V + 1, INT_MAX);
	priority_queue<pair<int, int>> pq;
	int c, p, tc, tp;
	dist[K] = 0;
	pq.push({ 0,K });

	while (!pq.empty()) {
		c = -pq.top().first;
		p = pq.top().second;
		pq.pop();
		if (c > dist[p])
			continue;
		for (auto i = 0; i < vec[p].size(); i++) {
			tp = vec[p][i].first;
			tc = vec[p][i].second + c;
			if (tc < dist[tp]) {
				dist[tp] = tc;
				pq.push({ -tc,tp });
			}
		}
	}
	return dist;
}

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(NULL);

	int K,u, v, w;
	cin >> V >> E >> K;
	for (int i = 0; i < E; i++) {
		cin >> u >> v >> w;
		vec[u].push_back({ v,w });
	}
	res = dijkstra(K);
	for (int i = 1; i <= V; i++) {
		if (res[i] < INT_MAX)
			cout << res[i] << '\n';
		else
			cout << "INF\n";
	}

	return 0;
}