#include <iostream>
using namespace std;

int bit[(1 << 25) / 32];
int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n;
	int mod = (1 << 5) - 1;
	while (cin >> n) {
		int x = n >> 5;
		int y = 1<<(n & mod);
		if (!(bit[x] & y)) {
			cout << n << ' ';
			bit[x] |= y;
		}
	}
	return 0;
}