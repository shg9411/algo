#include <iostream>
#include <algorithm>
using namespace std;

string s[20000];

bool cmp(string& a, string& b) {
	if (a.size() == b.size())
		return a < b;
	return a.size() < b.size();
}

int main(void) {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> s[i];
	sort(s, s + n, cmp);
	cout << s[0] << '\n';
	for (int i = 1; i < n; i++)
		if (s[i] != s[i - 1])
			cout << s[i] << '\n';

	return 0;
}