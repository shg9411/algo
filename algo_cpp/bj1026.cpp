#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(NULL);
	int n, first[50], second[50],res = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> first[i];
	for (int i = 0; i < n; i++)
		cin >> second[i];
	sort(first, first + n);
	sort(second, second + n, greater<int>());
	for (int i = 0; i < n; i++)
		res += first[i] * second[i];
	cout << res;

	return 0;
}