#include <iostream>
using namespace std;

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(NULL);
	int n, tmp, arr[10001] = { 0 };
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		arr[tmp]++;
	}
	for (auto i = 0; i < 10001; i++)
		for (int j = 0; j < arr[i]; j++)
			cout << i << '\n';
	return 0;
}