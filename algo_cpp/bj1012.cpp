#include <cstdio>
#include <cstring>
#include <queue>
#define MAX 51
using namespace std;

int land[MAX][MAX];
int n, m, k;
int nx[4] = { -1,0,1,0 };
int ny[4] = { 0,-1,0,1 };

void bfs(int x, int y) {
	land[x][y] = 0;
	queue<pair<int, int>> q;
	q.push({ x, y });
	while (!q.empty()) {
		pair<int, int> tmp = q.front(); q.pop(); k--;
		for (int i = 0; i < 4; i++) {
			int tmpx, tmpy;
			tmpx = tmp.first + nx[i];
			tmpy = tmp.second + ny[i];
			if (0 <= tmpx && tmpx < n && 0 <= tmpy && tmpy < m && land[tmpx][tmpy]) {
				q.push({ tmpx,tmpy });
				land[tmpx][tmpy] = 0;
			}
		}
	}
}

int main(void) {
	int t;
	scanf("%d", &t);
	while (t--) {
		int ans = 0;
		scanf("%d%d%d", &m, &n, &k);
		for (int i = 0; i < k; i++) {
			int x, y;
			scanf("%d%d", &y, &x);
			land[x][y] = 1;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (land[i][j]) {
					ans++;
					bfs(i, j);
				}
				if (!k)
					goto ANSWER;
			}
		}
	ANSWER:
		printf("%d\n", ans);
		memset(land, 0, sizeof(land));
	}
	return 0;
}