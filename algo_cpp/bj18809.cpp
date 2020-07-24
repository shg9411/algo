#include <cstdio>
#include <queue>
#include <vector>
using namespace std;
int n, m, g, r, res,big,garden[50][50], tmp[50][50],check[10];
vector<pair<int, int>> spoil;
void bfs() {
	int val = 2, ans = 0;
	queue<pair<int, int>> rq, gq;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			tmp[i][j] = garden[i][j];
	for (int i = 0; i < big; i++) {
		if (check[i] == 1) {
			gq.push(spoil[i]);
			tmp[spoil[i].first][spoil[i].second] = 0;
		}
		else if (check[i] == 2) {
			rq.push(spoil[i]);
			tmp[spoil[i].first][spoil[i].second] = 0;
		}
	}
	while (!gq.empty() && !rq.empty()) {
		int size = gq.size();
		int x, y;
		for (int i = 0; i < size; i++) {
			x = gq.front().first;
			y = gq.front().second;
			gq.pop();
			if (tmp[x][y] < 0)
				continue;
			if (x > 0 && tmp[x - 1][y] == 1) {
				tmp[x - 1][y] = val;
				gq.push({ x - 1,y });
			}
			if (y > 0 && tmp[x][y - 1] == 1) {
				tmp[x][y - 1] = val;
				gq.push({ x,y - 1 });
			}
			if (x < n - 1 && tmp[x + 1][y] == 1) {
				tmp[x + 1][y] = val;
				gq.push({ x + 1,y });
			}
			if (y < m - 1 && tmp[x][y + 1] == 1) {
				tmp[x][y + 1] = val;
				gq.push({ x,y + 1 });
			}
		}
		size = rq.size();
		for (int i = 0; i < size; i++) {
			x = rq.front().first;
			y = rq.front().second;
			rq.pop();
			if (x > 0) {
				if (tmp[x - 1][y] == 1) {
					tmp[x - 1][y] = -val;
					rq.push({ x - 1,y });
				}
				else if (tmp[x - 1][y] == val) {
					tmp[x - 1][y] = -val;
					ans++;
				}
			}
			if (y > 0) {
				if (tmp[x][y - 1] == 1) {
					tmp[x][y - 1] = -val;
					rq.push({ x,y - 1 });
				}
				else if (tmp[x][y - 1] == val) {
					tmp[x][y - 1] = -val;
					ans++;
				}
			}
			if (x < n - 1) {
				if (tmp[x + 1][y] == 1) {
					tmp[x + 1][y] = -val;
					rq.push({ x + 1,y });
				}
				else if (tmp[x + 1][y] == val) {
					tmp[x + 1][y] = -val;
					ans++;
				}
			}
			if (y < m - 1) {
				if (tmp[x][y + 1] == 1) {
					tmp[x][y + 1] = -val;
					rq.push({ x,y + 1 });
				}
				else if (tmp[x][y + 1] == val) {
					tmp[x][y + 1] = -val;
					ans++;
				}
			}
		}
		val++;
	}
	if (ans > res)res = ans;
}
void getR(int idx, int cnt) {
	if (cnt == r) {
		bfs();
		return;
	}
	for (int i = idx; i < big; i++) {
		if (check[i] == 0) {
			check[i] = 2;
			getR(i + 1, cnt + 1);
			check[i] = 0;
		}
	}
}
void getG(int idx, int cnt) {
	if (cnt == g) {
		getR(0, 0);
		return;
	}
	for (int i = idx; i < big; i++) {
		if (check[i] == 0) {
			check[i] = 1;
			getG(i + 1, cnt + 1);
			check[i] = 0;
		}
	}
}
int main(void) {
	scanf("%d%d%d%d", &n, &m, &g, &r);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &garden[i][j]);
			if (garden[i][j] == 2) {
				spoil.push_back({ i,j });
				garden[i][j] = 1;
			}
		}
	}
    big = spoil.size();
	getG(0, 0);
	printf("%d", res);
	return 0;
}