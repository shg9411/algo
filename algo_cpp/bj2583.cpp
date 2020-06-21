//#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int M, N;
vector<int> res;
bool paper[101][101];

void bfs(int i, int j) {
	queue<pair<int, int>> q;
	q.push(make_pair(i, j));
	int tmpx, tmpy, cnt=0;
	while (!q.empty()) {
		tmpx = q.front().first;
		tmpy = q.front().second;
		q.pop();
		cnt++;
		if (tmpx > 0) {
			if (paper[tmpx - 1][tmpy] == 0) {
				paper[tmpx - 1][tmpy] = 1;
				q.push(make_pair(tmpx - 1, tmpy));
			}
		}
		if (tmpy > 0) {
			if (paper[tmpx][tmpy-1] == 0) {
				paper[tmpx][tmpy-1] = 1;
				q.push(make_pair(tmpx, tmpy-1));
			}
		}
		if (tmpx < M-1) {
			if (paper[tmpx + 1][tmpy] == 0) {
				paper[tmpx + 1][tmpy] = 1;
				q.push(make_pair(tmpx + 1, tmpy));
			}
		}
		if (tmpy < N-1) {
			if (paper[tmpx][tmpy+1] == 0) {
				paper[tmpx][tmpy+1] = 1;
				q.push(make_pair(tmpx, tmpy+1));
			}
		}
	}
	res.push_back(cnt);
}

int main(void) {
	//cin.tie(0);
	//ios_base::sync_with_stdio(0);
	int K,a,b,c,d;
	scanf("%d %d %d", &M, &N, &K);
	//cin >> M >> N >> K;
	for (int i = 0; i < K; i++) {
		scanf("%d %d %d %d", &a, &b, &c, &d);
		//cin >> a >> b >> c >> d;
		for (int j = b; j < d; j++) {
			for (int k = a; k < c; k++) {
				paper[j][k] = 1;
			}
		}
	}
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (paper[i][j] == 0) {
				paper[i][j] = 1;
				bfs(i, j);
			}
		}
	}
	sort(res.begin(), res.end());
	printf("%d\n", res.size());
	//cout << res.size() << '\n';
	for (int r : res)
		printf("%d ", r);
	//cout << r << ' ';

	return 0;
}