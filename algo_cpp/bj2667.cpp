#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int MAX = 26;
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,-1,0,1 };
vector<int> res;
char apart[MAX][MAX];
int nowx, nowy, tmpx, tmpy, N;


void bfs(int i, int j) {
	queue<pair<int, int>> q;
	q.push(make_pair(i, j));
	int cnt = 0;
	while (!q.empty()) {
		nowx = q.front().first;
		nowy = q.front().second;
		cnt++;
		q.pop();
		for (int i = 0; i < 4; i++) {
			tmpx = nowx + dx[i];
			tmpy = nowy + dy[i];
			if (0 <= tmpx && tmpx < N && 0 <= tmpy && tmpy < N) {
				if (apart[tmpx][tmpy] != '1')
					continue;
				apart[tmpx][tmpy] = '0';
				q.push(make_pair(tmpx, tmpy));
			}
		}
	}
	res.push_back(cnt);
}

int main(void) {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> apart[i];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (apart[i][j] == '1') {
				apart[i][j] = '0';
				bfs(i, j);
			}
		}
	}
	sort(res.begin(), res.end());
	cout << res.size() << '\n';
	for (int r : res)
		cout << r << '\n';

	return 0;
}