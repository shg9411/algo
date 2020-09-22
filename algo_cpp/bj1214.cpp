#include<cstdio>
#include<algorithm>
using namespace std;


int main(void) {
	int d, p, q;
	scanf("%d %d %d", &d, &p, &q);
	if (d % p == 0 || d % q == 0) {
		printf("%d", d);
		return 0;
	}
	if (p < q) {
		int t = p;
		p = q;
		q = t;
	}
	int r = 2e9;
	for (int i = 0; i < min(q,d / p + 2); i++) {
		int tq = (d - p * i) / q;
		for (int j = max(0, tq - 2); j < tq + 2; j++) {
			int tr = p * i + q * j;
			if (tr < d)
				continue;
			r = min(r, tr);
		}
	}
	printf("%d", r);
	return 0;
}