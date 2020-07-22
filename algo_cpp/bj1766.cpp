#include<iostream>
#include<queue>
#include<vector>
using namespace std;

priority_queue<int,vector<int>> pq;
vector<int> pro[32001];
int num[32001];


int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n, m, a, b,tmp;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		num[b]++;
		pro[a].push_back(b);
	}
	for (int i = 1; i <= n; i++) {
		if (!num[i])
			pq.push(-i);
	}
	while (!pq.empty()) {
		tmp = -pq.top();pq.pop();
		cout << tmp << " ";
		for (auto i : pro[tmp]) {
			if (!--num[i])
				pq.push(-i);
		}
	}
	return 0;
}