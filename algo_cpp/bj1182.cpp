#include <iostream>
using namespace std;

int n, s, arr[20];
int res = 0;

void dfs(int idx, int val) {
	if (val + arr[idx] == s)
		res++;
	if (idx + 1 == n)
		return;
	dfs(idx + 1, val);
	dfs(idx + 1, val + arr[idx]);
}

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(NULL);
	cin >> n >> s;
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	dfs(0, 0);

	cout << res;

	return 0;
}