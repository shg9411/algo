#include <iostream>
using namespace std;


int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n;
	while (true) {
		cin >> n;
		if (!n)
			break;
		int tmp = n;
		for (int i = 2; i * i <= n; i++) {
			if (n % i == 0)
				tmp = tmp / i * (i - 1);
			while (n % i == 0)
				n /= i;
		}
		if (n != 1)
			tmp = tmp / n * (n - 1);
		cout << tmp << "\n";
	}
	return 0;
}