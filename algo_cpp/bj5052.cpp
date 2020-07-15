#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<string> phone(10000);

bool cmp(string a, string b) {
	return a<b;
}

int main(void)
{
	cin.tie(0); ios_base::sync_with_stdio(0);
	int t, n;
	bool res;
	cin >> t;
	while (t--) {
		cin >> n;
		phone.clear();
		res = 1;
		for (int i = 0; i < n; i++)
			cin >> phone[i];
		sort(phone.begin(), phone.begin() + n);
		for (int i = 1; i < n; i++) {
			if (!phone[i].compare(0,phone[i-1].size(),phone[i-1])) {
				res = 0;
				break;
			}
		}
		if (res)
			cout << "YES\n";
		else
			cout<< "NO\n";
	}
	return 0;

}