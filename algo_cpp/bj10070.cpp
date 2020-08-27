#include<iostream>
using namespace std;
const int MAXN = 2000000, MAXH = 1e6;

int n, k;
pair<int, int> tree[2 << 21];
int base[MAXN];

void u_rage(int node, int op, int h) {
	if (op == 1)
		tree[node] = { max(tree[node].first,h),max(tree[node].second,h) };
	else
		tree[node] = { min(tree[node].first,h),min(tree[node].second,h) };
}

void update(int node, int s, int e, int l, int r, int op, int h) {
	if (e<l || s>r)
		return;
	if (l <= s && e <= r) {
		u_rage(node, op, h);
		base[l] = tree[node].first;
		return;
	}
	int mid = (s + e)>>1;
	u_rage(node<<1, 1, tree[node].first);u_rage(node<<1, 2, tree[node].second);
    u_rage(node<<1|1, 1, tree[node].first);u_rage(node<<1|1, 2, tree[node].second);
	tree[node] = { 0,MAXH };
	update(node<<1, s, mid, l, r, op, h);
	update(node<<1|1, mid + 1, e, l, r, op, h);
    return;
}

int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	cin >> n >> k;
	for (int i = 0; i < k; i++) {
		int op, l, r, h;
		cin >> op >> l >> r >> h;
		update(1, 0, n - 1, l, r, op, h);
	}
	for (int i = 0; i < n; i++) {
		update(1, 0, n - 1, i, i, 1, 0);
		cout << base[i] << '\n';
	}
    return 0;
}