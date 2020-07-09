#include<iostream>
#include<algorithm>
#include<cmath>
#include<climits>
using namespace std;

int n, m, arr[1000000];
int mint[2100000], maxt[2100000];

void init(int node, int s, int e) {
	if (s == e) {
		mint[node] = maxt[node] = arr[s];
		return;
	}
	int mid = (s + e) / 2;
	init(node * 2, s, mid);
	init(node * 2 + 1, mid + 1, e);
	mint[node] = min(mint[node * 2], mint[node * 2 + 1]);
	maxt[node] = max(maxt[node * 2], maxt[node * 2 + 1]);
	return;
}

pair<int, int> getValue(int node, int s, int e, int l, int r) {
	if (l > e || r < s)
		return { INT_MAX,0 };
	if (s <= l && r <= e)
		return { mint[node],maxt[node] };
	int mid = (l + r) / 2;
	pair<int, int> lv = getValue(node * 2, s, e, l, mid);
	pair<int, int> rv = getValue(node * 2 + 1, s, e, mid + 1, r);
	return { min(lv.first,rv.first),max(lv.second,rv.second) };
}


int main(void)
{
	cin.tie(0); ios_base::sync_with_stdio(0);
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	init(1, 0, n - 1);
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		pair<int, int> r = getValue(1, a - 1, b - 1, 0, n - 1);
		cout << r.first << ' ' << r.second << '\n';
	}
	return 0;
}