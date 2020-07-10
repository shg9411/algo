#include<cstdio>
#include<vector>
#define MAX 501
using namespace std;

int stone[MAX];
bool check[MAX];
vector<int> person[MAX];

bool dfs(int i) {
	for (auto w : person[i]) {
		if (check[w])
			continue;
		check[w] = 1;
		if (stone[w] == 0 || dfs(stone[w])) {
			stone[w] = i;
			return true;
		}
	}
	return false;
}

int main(void)
{
	int n, m, res = 0;
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= m; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		person[a].push_back(b);
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			check[j] = 0;
		if (dfs(i))
			res++;
	}
	printf("%d", res);
	return 0;
}