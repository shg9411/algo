#include <cstdio>
using namespace std;

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

int parent[100001];

int find(int u) {
	if (parent[u] == u)
		return u;
	return parent[u] = find(parent[u]);
}

void uni(int a, int b) {
	a = find(a);
	b = find(b);
	parent[a] = b;
}

int main(void){
	int g, p, tmp,can, cnt = 0;
	scan(g); scan(p);
	for (int i = 1; i <= g; i++)
		parent[i] = i;
	for (int i = 0; i < p; i++) {
		scan(tmp);
		can = find(tmp);
		if (can) {
			uni(can, can - 1);
			cnt++;
		}
		else
			break;
	}
	printf("%d", cnt);
	return 0;
}