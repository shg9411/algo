#include<iostream>
#include<algorithm>
#include<cmath>
#include<climits>
using namespace std;

int n, m, arr[1000000];
int tree[2100000];

void init(int node, int s, int e) {
	if (s == e) {
		tree[node] = arr[s];
		return;
	}
	int mid = (s + e) / 2;
	init(node * 2, s, mid);
	init(node * 2 + 1, mid + 1, e);
	tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
	return;
}

int getValue(int node, int s, int e, int l, int r) {
	if (l > e || r < s)
		return INT_MAX;
	if (l<=s && e <= r)
		return tree[node];
	int mid = (s + e) / 2;
	return min(getValue(node * 2, s, mid, l, r), getValue(node * 2 + 1, mid + 1, e, l, r));
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
		cout << getValue(1, 0, n - 1, a - 1, b - 1) << '\n';
	}
	return 0;
}