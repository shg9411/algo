#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int cnt[32001];
vector<int> v[32001];
int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int n,m;
	cin >> n >> m;
	for(int i = 0; i < m; i++){
		int a,b;
		cin >> a >> b;
		v[a].push_back(b);
		cnt[b]++;
	}
	queue<int> q;
	for(int i = 1; i <= n; i++){
		if(cnt[i]==0)
			q.push(i);
	}
	
	for(int i = 1; i <= n; i++){
		int tmp = q.front();q.pop();
		cout << tmp << ' ';
		for(int n : v[tmp]){
			if(--cnt[n]==0)
				q.push(n);
		}
	}

	return 0;
}