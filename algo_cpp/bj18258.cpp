#include <iostream>
#include <queue>
#include <string>
using namespace std;

queue<int> q;
int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int n, tmp;
	string cmd;
	cin >> n;
	while (n--) {
		cin >> cmd;
		if (cmd=="push") {
			cin >> tmp;
			q.push(tmp);
		}
		else if (cmd == "front") {
			if (!q.empty())
				cout << q.front() << "\n";
			else
				cout << "-1\n";
		}
		else if (cmd == "back") {
			if (!q.empty())
				cout << q.back() << "\n";
			else
				cout << "-1\n";
		}
		else if (cmd == "size") {
			cout << q.size() << "\n";
		}
		else if (cmd == "empty") {
			if (!q.empty()) {
				cout << "0\n";
			}
			else
				cout << "1\n";
		}
		else if (cmd == "pop") {
			if (!q.empty()) {
				cout << q.front() << "\n";
				q.pop();
			}
			else
				cout << "-1\n";
		}
	}
	return 0;
}