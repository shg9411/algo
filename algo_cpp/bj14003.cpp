#include <vector>
#include <iostream>
using namespace std;

vector<int> v(1000000);
vector<int> lis, res = { 0 };
int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) 
		cin >> v[i];
	lis.push_back(v[0]);
	for (int i = 1; i < n; i++) {
		if (lis.back() < v[i]) {
			lis.push_back(v[i]);
			res.push_back(lis.size() - 1);
		}
		else {
			int where = lower_bound(lis.begin(), lis.end(), v[i])-lis.begin();
			lis[where] = v[i];
			res.push_back(where);
		}
	}
	int len = lis.size();
	cout << len << "\n";
	vector<int> ans;
	for (int i = res.size() - 1; i > -1; i--) {
		if (res[i] == len - 1) {
			ans.push_back(v[i]);
			len--;
		}
	}
	for (int i = ans.size() - 1; i > -1; i--)
		cout << ans[i] << " ";
	return 0;
}