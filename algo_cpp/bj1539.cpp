#include <iostream>
#include <map>
using namespace std;

map<int, int> bst;
int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int n, tmp;
	cin >> n;
	cin >> tmp;
	bst[tmp] = 1;
	long long res = 1;
	for (int i = 0; i < n - 1; i++) {
		cin >> tmp;
		auto it = bst.lower_bound(tmp);
		int td;
		if (it == bst.begin())
			td = it->second + 1;
		else if (it == bst.end())
			td = (--it)->second+1;
		else {
			td = it->second;
			td = td > (--it)->second ? td + 1 : it->second + 1;
		}
		bst[tmp] = td;
		res += td;
	}
	cout << res;
	return 0;
}