#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int main(void) {
	int n, m, tmp;
	scanf("%d", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		v[i] = tmp;
	}
	sort(v.begin(), v.end());
	scanf("%d", &m);
	
	for (int i = 0; i < m; i++) {
		scanf("%d", &tmp);
		auto p = equal_range(v.begin(), v.end(), tmp);
		printf("%d ", p.second - p.first);
	}
	return 0;
}