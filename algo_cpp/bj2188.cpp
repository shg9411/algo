#include<cstdio>
#include<vector>
#include<cstring>
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
		for (int j = 0; j < s; j++) {
			scanf("%d", &tmp);
			cow[i].push_back(tmp);
		}
	}
	for (int i = 1; i <= n; i++) {
		memset(check, 0, sizeof(check));
		if (dfs(i))
			res += 1;
	}
	printf("%d", res);
	return 0;
}