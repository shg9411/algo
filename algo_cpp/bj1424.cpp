#include <iostream>
using namespace std;


int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n, l, c,tmp,res;
	cin >> n >> l >> c;
	tmp = (c + 1) / (l + 1);
	if (tmp % 13 == 0)
		tmp--;
	if (n % tmp == 0)
		res = n / tmp;
	else if ((n % tmp) % 13 == 0) {
		if (n % tmp >= 1 && tmp > n % tmp + 1)
			res = n / tmp + 1;
		else
			res = n / tmp + 2;
	}
	else
		res = n / tmp + 1;
	cout << res;
	return 0;
}