#include <iostream>
#include <algorithm>
using namespace std;

int arr[100000];
int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n, m,tmp;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	sort(arr, arr + n);
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> tmp;
		cout << binary_search(arr, arr + n, tmp) << "\n";
	}
	return 0;
}