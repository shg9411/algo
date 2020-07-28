#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define MAX 200001

int n, m, res[MAX], rumor[MAX];
vector<int> v[MAX];
queue<int> q;

int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int t, p;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		res[i] = -1;
		while (true) {
			cin >> t;
			if (t) {
				v[i].push_back(t);
			}
			else
				break;
		}
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> t;
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
		cout << res[i] << ' ';
	return 0;
}