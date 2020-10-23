#include <cstdio>
#include <vector>
#include <queue>
#define MAX 1e9

using namespace std;

inline void scan(int& x)
{
	int c = getchar_unlocked();
	x = 0;
	int neg = 0;
	for (; ((c < 48 || c>57) && c != '-'); c = getchar_unlocked());
	if (c == '-') {
		neg = 1;
		c = getchar_unlocked();
	}
	for (; c > 47 && c < 58; c = getchar_unlocked()) {
		x = (x << 1) + (x << 3) + c - 48;
	}
	if (neg)
		x = -x;
}

int N, M, u, v, w, dist[1001], s, e;
vector<pair<int, int>> adj[1001];
priority_queue<pair<int, int>> pq;

int main(void) {
	scan(N); scan(M);
	for (int i = 0; i < M; i++) {
		scan(u); scan(v); scan(w);
		adj[u].push_back({ v,w });
	}
	scan(s); scan(e);
	for (int i = 1; i <= N; i++)
		dist[i] = MAX;
	dist[s] = 0;
	pq.push({ 0,s });
	while (!pq.empty()) {
		int cost, now;
		cost = -pq.top().first;
		now = pq.top().second;
		pq.pop();
		if (dist[now] < cost)
			continue;
		for (auto it : adj[now]) {
			int tmp = it.second + cost;
			if (dist[it.first] > tmp) {
				dist[it.first] = tmp;
				pq.push({ -tmp,it.first });
			}
		}
	}
	printf("%d", dist[e]);
	return 0;
}