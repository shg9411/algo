#include <cstdio>
#include <cstring>
#define MAX 246913
using namespace std;

bool sosu[MAX];
int count[MAX];
int main(void) {
	int n;
	memset(sosu, 1, sizeof(sosu));
	sosu[0] = sosu[1] = 0;
	for (int i = 2; i * i < MAX; i++) {
		if (sosu[i]) {
			for (int j = i * i; j < MAX; j += i) {
				sosu[j] = false;
			}
		}
	}
	for (int i = 1; i < MAX; i++) {
		if (sosu[i])
			count[i] = count[i - 1] + 1;
		else
			count[i] = count[i - 1];
	}
	while (true) {
		scanf("%d", &n);
		if (n == 0)
			break;
		printf("%d\n", count[n * 2] - count[n]);
	}
	return 0;
}