#include <vector>
#include <iostream>
using namespace std;

vector<pair<int, int>> f;
int cnt, row[9], col[9], sqr[9], sudoku[9][9];

void dfs(int idx) {
	if (idx == cnt) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				cout << sudoku[i][j] << ' ';
			}
			cout << '\n';
		}
		exit(0);
	}
	int x, y;
	x = f[idx].first;
	y = f[idx].second;
	for (int i = 1; i <= 9; i++) {
		int tmp = 1 << i;
		if (row[x] & tmp || sqr[x / 3 * 3 + y / 3] & tmp || col[y] & tmp)
			continue;
		row[x] |= tmp; col[y] |= tmp; sqr[x / 3 * 3 + y / 3] |= tmp;
		sudoku[x][y] = i;
		dfs(idx + 1);
		row[x] &= (~tmp); col[y] &= (~tmp); sqr[x / 3 * 3 + y / 3] &= (~tmp);
	}
}

int main(void) {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> sudoku[i][j];
			if (!sudoku[i][j])
				f.push_back({ i,j });
			else
			{
				row[i] |= (1 << sudoku[i][j]);
				col[j] |= (1 << sudoku[i][j]);
				sqr[i / 3 * 3 + j / 3] |= (1 << sudoku[i][j]);
			}
		}
	}
	cnt = f.size();
	dfs(0);
	return 0;
}