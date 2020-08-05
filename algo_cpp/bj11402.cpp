#include <cstdio>
#define MAX 2010
using namespace std;

int bino[MAX][MAX];

int main(void) {
	long long n, k, m;
    int res = 1;
	scanf("%lld%lld%lld", &n, &k, &m);
	for (int i = 0; i < m; i++) {
		bino[i][0] = 1;
		for (int j = 1; j <= i; j++)
			bino[i][j] = (bino[i - 1][j - 1] + bino[i - 1][j]) % m;
	}
	while (n || k) {
		res *= bino[n % m][k % m];
		n /= m; k /= m;
		res %= m;
	}
	printf("%d", res);
	return 0;
}