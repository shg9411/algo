#include <queue>
#include <vector>
#include <cstdio>
using namespace std;
#define MAX 200001

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

int n, m, res[MAX], rumor[MAX];
vector<int> v[MAX];
queue<int> q;

int main(void) {
	int t, p;
    scan(n);
	for (int i = 1; i <= n; i++) {
		res[i] = -1;
		while (true) {
			scan(t);
			if (t) {
				v[i].push_back(t);
			}
			else
				break;
		}
	}
	scan(m);
	for (int i = 0; i < m; i++) {
		scan(t);
		q.push(t);
		res[t] = 0;
	}
	while (!q.empty()) {
		p = q.front(); q.pop();
		for (int x : v[p]) {
			if (res[x] == -1) {
				rumor[x]++;
				if (v[x].size() <= rumor[x] * 2) {
					q.push(x);
					res[x] = res[p] + 1;
				}
			}
		}
	}
	for (int i = 1; i <= n; i++)
		printf("%d ",res[i]);
	return 0;
}