#include <cstdio>
#include <unordered_map>

using namespace std;

unordered_map<int, int> a;
int A[1000], B[1000];
inline void scan(int& x)
{
	int c = getchar_unlocked();
	x = 0;
	int neg = 0;
	for (; ((c < 48 || c>57) && c != '-'); c = getchar_unlocked());
	if (c == '-') {
		neg = 1;
		c = getchar_unlocked();
	}
	for (; c > 47 && c < 58; c = getchar_unlocked()) {
		x = (x << 1) + (x << 3) + c - 48;
	}
	if (neg)
		x = -x;
}

int main(void) {
	int t, n, m, tmp;
	long long res = 0;
	scan(t);
	scan(n);
	for (int i = 0; i < n; i++)
		scan(A[i]);
	scan(m);
	for (int i = 0; i < m; i++)
		scan(B[i]);
	for (int i = 0; i < n; i++) {
		tmp = 0;
		for (int j = i; j < n; j++) {
			tmp += A[j];
			a[tmp]++;
		}
	}
	for (int i = 0; i < m; i++) {
		tmp = 0;
		for (int j = i; j < m; j++) {
			tmp += B[j];
			if (a.find(t - tmp) != a.end())
				res += a[t - tmp];
		}
	}
	printf("%lli", res);
	return 0;
}