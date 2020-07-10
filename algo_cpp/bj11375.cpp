#include<cstdio>
#include<cstring>
#include<vector>
#define MAX 1001
using namespace std;

int job[MAX];
bool check[MAX];
vector<int> person[MAX];

bool dfs(int i) {
	for (auto w : person[i]) {
		if (check[w])
			continue;
		check[w] = 1;
		if (job[w] == 0 || dfs(job[w])) {
			job[w] = i;
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
			person[i].push_back(tmp);
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