#include <cstdio>
//#include <cstring>
using namespace std;

bool era[10001];

void eratos() {
	for (int i = 2; i <= 10000; i++)
		era[i] = 1;
	for (int i = 2; i * i <= 10000; i++) {
		if (era[i]) {
			for (int j = i * i; j <= 10000; j += i) {
				era[j] = 0;
			}
		}
	}
}
int main(void) {
	int t;
	scanf("%d", &t);
	eratos();
	while (t--) {
		int n;
		scanf("%d", &n);
		for (int i = n / 2; i >= 2; i--) {
			if (era[i] && era[n - i]) {
				printf("%d %d\n", i, n - i);
				break;
			}
		}
	}
	return 0;
}