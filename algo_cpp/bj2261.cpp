#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<algorithm>
#include<cmath>
using namespace std;

struct P {
	int x, y;
	P() {}
	P(int x, int y) :x(x), y(y) {}
	bool operator < (const P& o) const {
		if (y == o.y)
			return x < o.x;
		return y < o.y;
	}
};
bool cmp(const P& u, const P& v) {
	return u.x < v.x;
}
int dist(P p1, P p2) {
	return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

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
	int n;
	scan(n);
	vector<P> v(n);
	for (int i = 0; i < n; i++) {
		scan(v[i].x); scan(v[i].y);
	}
	sort(v.begin(), v.end(),cmp);
	set<P> candi = { v[0],v[1] };
	int res = dist(v[0], v[1]);
	int st = 0;
	for (int i = 2; i < n; i++) {
		P c = v[i];
		while (st < i) {
			auto p = v[st];
			int x = c.x - p.x;
			if (x * x > res) {
				candi.erase(p);
				st++;
				continue;
			}
			break;
		}
		int d = (int)sqrt((double)res) + 1;
		auto L = P(-100000, c.y - d);
		auto R = P(100000, c.y + d);
		auto l = candi.lower_bound(L);
		auto r = candi.upper_bound(R);
		for (auto it = l; it != r; it++) {
			int t = dist(c, *it);
			if (t < res)
				res = t;
		}
		candi.insert(c);
	}
	printf("%d", res);
	return 0;
}