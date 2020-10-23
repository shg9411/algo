#include <cstdio>
#include <queue>

using namespace std;

int N, M;
char miro[1001][1001];
int visited[2][1001][1001];
queue<pair<pair<int, int>, int>> q;
int main(void) {
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++)
		scanf("%s", miro[i]);
	q.push({ { 0,0, }, 0 });
	int res = 1;
	while (!q.empty()) {
		int l = q.size();
		for (int idx = 0; idx < l; idx++) {
			auto pop = q.front(); q.pop();
			int i = pop.first.first, j = pop.first.second, k = pop.second;
			if (i == N - 1 && j == M - 1) {
				printf("%d", res);
				return 0;
			}
			if (i > 0) {
				if (miro[i - 1][j] == '0') {
					if (!visited[k][i - 1][j]) {
						visited[k][i - 1][j] = 1;
						q.push({ {i - 1,j},k });
					}
				}
				else {
					if (!k && !visited[k][i - 1][j]) {
						visited[k][i - 1][j] = 1;
						q.push({ {i - 1,j},1 });
					}
				}
			}

			if (j > 0) {
				if (miro[i][j - 1] == '0') {
					if (!visited[k][i][j - 1]) {
						visited[k][i][j - 1] = 1;
						q.push({ {i,j - 1},k });
					}
				}
				else {
					if (!k && !visited[k][i][j - 1]) {
						visited[k][i][j - 1] = 1;
						q.push({ {i,j - 1},1 });
					}
				}
			}
			if (i + 1 < N) {
				if (miro[i + 1][j] == '0') {
					if (!visited[k][i + 1][j]) {
						visited[k][i + 1][j] = 1;
						q.push({ {i + 1,j},k });
					}
				}
				else {
					if (!k && !visited[k][i + 1][j]) {
						visited[k][i + 1][j] = 1;
						q.push({ {i + 1,j},1 });
					}
				}
			}
			if (j + 1 < M) {
				if (miro[i][j + 1] == '0') {
					if (!visited[k][i][j + 1]) {
						visited[k][i][j + 1] = 1;
						q.push({ {i,j + 1},k });
					}
				}
				else {
					if (!k && !visited[k][i][j + 1]) {
						visited[k][i][j + 1] = 1;
						q.push({ {i,j + 1},1 });
					}
				}
			}
		}
		res++;
	}

	printf("-1");
	return 0;
}