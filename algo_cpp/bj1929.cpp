#include <iostream>
#include <cstring>
using namespace std;

bool sosu[1000001];
int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int m,n;
	cin >> m >> n;
	memset(sosu, 1, n+1);
	sosu[0] = sosu[1] = 0;
	for (int i = 2; i * i <= n; i++) {
		if (sosu[i]) {
			for (int j = i * i; j <= n; j += i) {
				sosu[j] = false;
			}
		}
	}
	for (int i = m; i <= n; i++)
		if (sosu[i])
			cout << i << "\n";
	return 0;
}