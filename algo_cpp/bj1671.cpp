#include<cstdio>
#include<cstring>
#include<vector>
#define MAX 50
using namespace std;

bool check[MAX];
int eaten[MAX];
vector<pair<pair<int, int>, int>> shark(MAX);
vector<int> can[MAX];


bool dfs(int i) {
	for (auto w : can[i]) {
		if (check[w])
			continue;
		check[w] = 1;
		if (eaten[w] == -1 || dfs(eaten[w])) {
			eaten[w] = i;
			return true;
		}
	}
	return false;
}

int main(void)
{
	int n, res = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &shark[i].first.first, &shark[i].first.second, &shark[i].second);
		eaten[i] = -1;
	}
	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if (shark[i].first.first >= shark[j].first.first && shark[i].first.second >= shark[j].first.second && shark[i].second >= shark[j].second)
				can[i].push_back(j);
			else if (shark[j].first.first >= shark[i].first.first && shark[j].first.second >= shark[i].first.second && shark[j].second >= shark[i].second)
				can[j].push_back(i);
		}
	}
	for (int i = 0; i < n; i++) {
		memset(check, 0, sizeof(check));
		if (dfs(i)) {
			res++;
			memset(check, 0, sizeof(check));
			if (dfs(i))
				res++;
		}
	}
	printf("%d", n - res);
	return 0;

}