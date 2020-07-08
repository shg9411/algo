#include <cstdio>
#include <cstring>
#include <queue>
#define MAX 100
using namespace std;

int land[MAX][MAX];
int n;
int nx[4] = { -1,0,1,0 };
int ny[4] = { 0,-1,0,1 };

bool outside(int x, int y) {
	if (x > 0 && land[x - 1][y] == 0)
			return true;
	if (y > 0 && land[x][y - 1] == 0)
			return true;
	if (x < n - 1 && land[x + 1][y] == 0)
			return true;
	if (y < n - 1 && land[x][y + 1] == 0)
			return true;
	return false;
}

int bfs(int x, int y) {
	bool visited[MAX][MAX] = { 0 };
	visited[x][y] = 1;
	int cur = land[x][y];
	int cnt = 0;
	queue<pair<int, int>> q;
	q.push({ x, y });
	while (!q.empty()) {
		int size = q.size();
		for (int i = 0; i < size; i++) {
			pair<int, int> tmp = q.front(); q.pop();
			x = tmp.first; y = tmp.second;
			if (x > 0 && land[x - 1][y] != cur && !visited[x - 1][y]) {
				if (land[x - 1][y])
					return cnt;
				visited[x - 1][y] = 1;
				q.push({ x - 1, y });
			}
			if (y > 0 && land[x][y - 1] != cur && !visited[x][y - 1]) {
				if (land[x][y - 1])
					return cnt;
				visited[x][y - 1] = 1;
				q.push({ x, y - 1 });
			}
			if (x < n - 1 && land[x + 1][y] != cur && !visited[x + 1][y]) {
				if (land[x + 1][y])
					return cnt;
				visited[x + 1][y] = 1;
				q.push({ x + 1, y });
			}
			if (y < n - 1 && land[x][y + 1] != cur && !visited[x][y + 1]) {
				if (land[x][y + 1])
					return cnt;
				visited[x][y + 1] = 1;
				q.push({ x, y + 1 });
			}
		}
		cnt += 1;
	}
	return cnt;
}

void setLand(int x, int y, int num) {
	queue<pair<int, int>> q;
	q.push({ x,y });
	land[x][y] = num;
	while (!q.empty()) {
		pair<int, int> tmp = q.front(); q.pop();
		int tmpx, tmpy;
		for (int i = 0; i < 4; i++) {
			tmpx = tmp.first + nx[i];
			tmpy = tmp.second + ny[i];
			if (0 <= tmpx && tmpx < n && 0 <= tmpy && tmpy < n && land[tmpx][tmpy] == 1) {
				land[tmpx][tmpy] = num;
				q.push({ tmpx,tmpy });
			}
		}
	}
}

int main(void) {
	int res, num = 2;
	scanf("%d", &n);
	res = n * n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &land[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (land[i][j]==1) {
				setLand(i, j, num++);
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (land[i][j] && outside(i, j)) {
				res = min(res, bfs(i, j));
				if (res == 1)
					goto ANSWER;
			}
		}
	}
    ANSWER: {
	    printf("%d", res);
	    return 0;
	    }
	printf("%d", res);
	return 0;
}