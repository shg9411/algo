#include<iostream>
using namespace std;

int n, m, k, arr[1000000];
long long tree[4000001];

long long init(int node, int s, int e) {
	if (s == e)
		return tree[node] = arr[s];
	int mid = (s + e) / 2;
	return tree[node] = init(node * 2, s, mid) + init(node * 2 + 1, mid + 1, e);
}

long long query(int node, int s, int e, int l, int r) {
	if (s > r || e < l)
		return 0;
	if (l <= s && e <= r)
		return tree[node];
	int mid = (s + e) / 2;
	return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r);
}

void update(int node, int s, int e, int idx, int diff) {
	if (idx<s || idx>e)
		return;
	tree[node] += diff;
	if (s != e) {
		int mid = (s + e) / 2;
		update(node * 2, s, mid, idx, diff);
		update(node * 2 + 1, mid + 1, e, idx, diff);
	}
}

int main(void)
{	
	cin.tie(0); ios_base::sync_with_stdio(0);
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	init(1, 0, n - 1);
	for (int i = 0; i < m + k; i++) {
		int q, a, b;
		cin >> q >> a >> b;
		if (q == 1) {
			int diff = b - arr[a - 1];
			arr[a - 1] = b;
			update(1, 0, n - 1, a - 1, diff);
		}
		else
			cout << query(1, 0, n - 1, a - 1, b - 1) << '\n';
	}
	return 0;
}