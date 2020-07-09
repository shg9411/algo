#include <vector>
#include <cstdlib>
#include <cstdio>
using namespace std;

vector<pair<int, int>> f;
int cnt;
bool row[9][9];
bool col[9][9];
bool sqr[9][9];
int sudoku[9][9];

void dfs(int idx) {
	if (idx == cnt) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				printf("%d",sudoku[i][j]);
			}
			printf("\n");
		}
		exit(0);
	}
	int x, y;
	x = f[idx].first;
	y = f[idx].second;
	for (int i = 0; i < 9; i++) {
		if (!row[x][i] && !col[y][i] && !sqr[x / 3 * 3 + y / 3][i]) {
			row[x][i] = col[y][i] = sqr[x / 3 * 3 + y / 3][i] = 1;
			sudoku[x][y] = i + 1;
			dfs(idx + 1);
			sudoku[x][y] = row[x][i] = col[y][i] = sqr[x / 3 * 3 + y / 3][i] = 0;
		}
	}
}

int main(void) {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			sudoku[i][j] = getchar()-'0';
			if (!sudoku[i][j])
				f.push_back({ i,j });
			else
			{
				row[i][sudoku[i][j] - 1] = 1;
				col[j][sudoku[i][j] - 1] = 1;
				sqr[i/3*3+j/3][sudoku[i][j] - 1] = 1;
			}
		}
		getchar();
	}

	cnt = f.size();
	dfs(0);
	return 0;
}