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
		}
		else {
			int where = lower_bound(lis.begin(), lis.end(), v[i])-lis.begin();
			lis[where] = v[i];
		}
	}
	cout << lis.size() << "\n";
	return 0;
}