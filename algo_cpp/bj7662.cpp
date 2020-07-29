#include <cstdio>
#include <map>
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

map<int, int> q;
char cmd;
int n;
int main(void) {
	int t;
	scan(t);
	for (int i = 0; i < t; i++) {
		q.clear();
		int k;
		scan(k);
		for (int i = 0; i < k; i++) {
			cmd=(char)getchar();scan(n);
			if (cmd == 'I')
				q[n]++;
			else if(!q.empty()){
				if (n == 1) {
					q.rbegin()->second--;
					if (q.rbegin()->second == 0)
						q.erase(q.rbegin()->first);
				}
				else {
					q.begin()->second--;
					if (q.begin()->second == 0)
						q.erase(q.begin()->first);
				}
			}
		}
		if (q.empty())
			printf("EMPTY\n");
		else
			printf("%d %d\n",q.rbegin()->first,q.begin()->first);
	}
	return 0;
}