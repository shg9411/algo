#include <vector>
#include <cstdio>
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
using namespace std;

vector<int> lis;

int main(void) {
	int n, tmp;
	scan(n);
	scan(tmp);
	lis.push_back(tmp);
	for (int i = 0; i < n - 1; i++) {
		scan(tmp);
		auto it = lower_bound(lis.begin(), lis.end(), tmp);
		if (it == lis.end())
			lis.push_back(tmp);
		else
			*it = tmp;
	}
	printf("%d\n", lis.size());
	return 0;
}