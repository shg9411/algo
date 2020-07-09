#include <vector>
#include <cstdio>
using namespace std;

vector<pair<int, int>> f;
int cnt, sudoku[9][9];
bool done, status, row[9][9], col[9][9], sqr[9][9];

void dfs(int idx) {
	if (idx == cnt) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				printf("%d", sudoku[i][j]);
			}
			printf("\n");
		}
		done = 1;
		return;
	}
	int x, y;
	x = f[idx].first;
	y = f[idx].second;
	for (int i = 0; i < 9; i++) {
		if (!row[x][i] && !col[y][i] && !sqr[x / 3 * 3 + y / 3][i]) {
			row[x][i] = col[y][i] = sqr[x / 3 * 3 + y / 3][i] = 1;
			sudoku[x][y] = i + 1;
			if (done)
				return;
			dfs(idx + 1);
			sudoku[x][y] = row[x][i] = col[y][i] = sqr[x / 3 * 3 + y / 3][i] = 0;
		}
	}
}

int main(void) {
	int t;
	scanf("%d", &t); getchar();
	while (t--) {
		done = 0;
		status = 1;
		f.clear();
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				row[i][j] = col[i][j] = sqr[i][j] = 0;
			}
		}
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				sudoku[i][j] = getchar() - '0';
				if (!sudoku[i][j])
					f.push_back({ i,j });
				else
				{
					if (row[i][sudoku[i][j] - 1] || col[j][sudoku[i][j] - 1] || sqr[i / 3 * 3 + j / 3][sudoku[i][j] - 1])
						status = 0;
					row[i][sudoku[i][j] - 1] = 1;
					col[j][sudoku[i][j] - 1] = 1;
					sqr[i / 3 * 3 + j / 3][sudoku[i][j] - 1] = 1;
				}
			}
			getchar();
		}
		cnt = f.size();
		if (status)
			dfs(0);
		if (!done)
			printf("Could not complete this grid.\n");
		if (t)
			printf("\n");
	}
	return 0;
}