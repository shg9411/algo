//#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;


int res, r, c;
bool alpha[26];
char board[21][21];

int ctoi(char c) {
	return c - 'A';
}

void dfs(int i, int j, int cnt) {
	int tmp;
	if (i > 0) {
		tmp = ctoi(board[i - 1][j]);
		if (alpha[tmp] == 0) {
			alpha[tmp] = 1;
			res = res > cnt + 1 ? res : cnt + 1;
			dfs(i - 1, j, cnt + 1);
			alpha[tmp] = 0;
		}
	}
	if (j > 0) {
		tmp = ctoi(board[i][j - 1]);
		if (alpha[tmp] == 0) {
			alpha[tmp] = 1;
			res = res > cnt + 1 ? res : cnt + 1;
			dfs(i, j - 1, cnt + 1);
			alpha[tmp] = 0;
		}
	}
	if (i < r - 1) {
		tmp = ctoi(board[i + 1][j]);
		if (alpha[tmp] == 0) {
			alpha[tmp] = 1;
			res = res > cnt + 1 ? res : cnt + 1;
			dfs(i + 1, j, cnt + 1);
			alpha[tmp] = 0;
		}
	}
	if (j < c - 1) {
		tmp = ctoi(board[i][j + 1]);
		if (alpha[tmp] == 0) {
			alpha[tmp] = 1;
			res = res > cnt + 1 ? res : cnt + 1;
			dfs(i, j + 1, cnt + 1);
			alpha[tmp] = 0;
		}
	}
}

int main(void) {
	//cin.tie(0);
	//ios_base::sync_with_stdio(0);
	scanf("%d %d", &r, &c);
	for (int i = 0; i < r; i++) {
		scanf("%s", board[i]);
	}
	alpha[board[0][0] - 'A'] = 1;
	res = 1;
	dfs(0, 0, 1);
	printf("%d", res);
	return 0;
}