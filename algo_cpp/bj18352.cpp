#include<cstdio>
#include<vector>
#include<queue>
#ifdef WIN32
inline int getchar_unlocked() { return _getchar_nolock(); }
#endif

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

vector<int> v[300001];
queue<int> pq;
int dist[300001];

int main(void)
{
	int n, m, k, x, d;
	scan(n); scan(m); scan(k); scan(x);

	for (int i = 0; i < m; i++) {
		int a, b;
		scan(a); scan(b);
		v[a].push_back(b);
	}
	for (int i = 1; i <= n; i++)
		dist[i] = 987654321;
	dist[x] = 0;
	pq.push(x);
	while (!pq.empty()) {
		d = pq.front(); pq.pop();
		if (dist[d] == k)
			break;
		for (auto vertex : v[d]) {
			if (dist[vertex] == 987654321) {
				dist[vertex] = dist[d] + 1;
				pq.push(vertex);
			}
		}
	}
	vector<int> ans;
	for (int i = 1; i <= n; i++) {
		if (dist[i] == k) {
			ans.push_back(i);
		}
	}
	if (ans.empty())
		printf("-1\n");
	else
		for (auto i : ans)
			printf("%d\n", i);
	return 0;
}