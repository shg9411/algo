#include<cstdio>
#include<vector>
using namespace std;

int house[201];
bool check[201];
vector<int> cow[201];

bool dfs(int i) {
	for (auto w : cow[i]) {
		if (check[w])
			continue;
		check[w] = 1;
		if (house[w] == 0 || dfs(house[w])) {
			house[w] = i;
			return true;
		}
	}
	return false;
}

int main(void)
{
	int n, m, res = 0;
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) {
		int s, tmp;
		scanf("%d", &s);
        cow[i].resize(s);
		for (int j = 0; j < s; j++) {
			scanf("%d", &cow[i][j]);
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int i = 1; i <= m; i++)
			check[i] = 0;
		if (dfs(i))
			res += 1;
	}
	printf("%d", res);
	return 0;
}