#include <iostream>
using namespace std;

int main() {
	cin.tie(0); ios_base::sync_with_stdio(0);
	long long total = 0, xornum = 0;
	int m, i, j;
	cin >> m;
	while (m--) {
		cin >> i;
		if (i == 3)
			cout << total << '\n';
		else if (i == 4)
			cout << xornum << '\n';
		else {
			cin >> j;
			if (i == 1) 
				total += j;
			else 
				total -= j;
			xornum ^= j;
		}
	}
	return 0;
}