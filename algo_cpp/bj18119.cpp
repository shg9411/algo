#include <string>
#include <iostream>
#include <vector>
using namespace std;

vector<int> words(10000);
int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n, m, cur = (1 << 26) - 1;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		string tmp;
		cin >> tmp;
		for (auto c : tmp)
			words[i] |= (1 << (c - 'a'));
	}
	for (int i = 0; i < m; i++) {
		int q, cnt = 0;
		char alpha;
		cin >> q >> alpha;
		if (q == 1)
			cur &= ~(1 << (alpha - 'a'));
		else
			cur |= 1 << (alpha - 'a');
		for (int i = 0; i < n; i++) {
			if ((cur & words[i]) == words[i])
				cnt++;
		}
		cout << cnt << '\n';
	}
	return 0;
}