#include <iostream>
using namespace std;

int p[1001];

int find(int i) {
	if (p[i] == i)
		return i;
	return p[i] = find(p[i]);
}

bool uni(int i, int j) {
	i = find(i);
	j = find(j);
	if (i == j)
		return true;
	p[j] = i;
	return false;
}

int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n, m;
	cin >> n >> m;
	int ans = n;
	for (int i = 1; i <= n; i++)
		p[i] = i;
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		if (!uni(u, v))
			ans--;
	}
	cout << ans;
	return 0;
}