#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(NULL);

	string tmp;
	cin >> tmp;
	sort(tmp.begin(), tmp.end());
	reverse(tmp.begin(), tmp.end());
	cout << tmp;

	return 0;
}