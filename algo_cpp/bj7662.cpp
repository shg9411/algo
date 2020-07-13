#include <iostream>
#include <map>
using namespace std;

map<int, int> q;
char cmd[2];
int n;
int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		q.clear();
		int k;
		cin >> k;
		for (int i = 0; i < k; i++) {
			cin >> cmd >> n;
			if (cmd[0] == 'I')
				q[n]++;
			else if(!q.empty()){
				if (n == 1) {
					q.rbegin()->second--;
					if (q.rbegin()->second == 0)
						q.erase(q.rbegin()->first);
				}
				else {
					q.begin()->second--;
					if (q.begin()->second == 0)
						q.erase(q.begin()->first);
				}
			}
		}
		if (q.empty())
			cout << "EMPTY\n";
		else
			cout << q.rbegin()->first << " " << q.begin()->first << "\n";
	}
	return 0;
}