#include <iostream>
#include <sstream>
#include <stack>
#include<vector>
#include<algorithm>

using namespace std;

void solution(int numOfOrder, string* orderArr) {
	for (int i = 0; i < numOfOrder; i++) {
		stack<string> st;
		stack<string> res;
		int idx = 0;
		while (idx < orderArr[i].size()) {
			char c = orderArr[i][idx];
			if (c == ')') {
				string tmp = "";
				string x;
				while (st.top() != "(") {
					x = st.top();
					reverse(x.begin(), x.end());
					tmp += x;
					st.pop();
				}
				st.pop();
				if (isdigit(st.top()[0])) {
					string a = "";
					for (int cnt = 0; cnt < st.top()[0] - '0'; cnt++) {
						a += tmp;
					}
					st.pop();
					reverse(a.begin(), a.end());
					st.push(a);
				}
				else {
					string re = "";
					for (int cnt = 0; cnt < tmp.size(); cnt++) {
						re += tmp[cnt];
						re += st.top();
					}
					st.pop();
					reverse(re.begin(), re.end());
					st.push(re);
				}
			}
			else {
				if (isdigit(c) && isupper(orderArr[i][idx + 1])) {
					string re = "";
					for (int cnt = 0; cnt < c - '0'; cnt++) {
						re += orderArr[i][idx + 1];
					}
					st.push(re);
					idx++;
				}
				else {
					st.push(string(1, c));
				}
			}
			idx++;
		}
		while (!st.empty()) {
			res.push(st.top());
			st.pop();
		}
		while (!res.empty()) {
			cout << res.top();
			res.pop();
		}
		cout << "\n";
	}
}

struct input_data {
	int numOfOrder;
	string* orderArr;
};

void process_stdin(struct input_data& inputData) {
	string line;
	istringstream iss;

	getline(cin, line);
	iss.str(line);
	iss >> inputData.numOfOrder;

	inputData.orderArr = new string[inputData.numOfOrder];
	for (int i = 0; i < inputData.numOfOrder; i++) {
		getline(cin, line);
		iss.clear();
		iss.str(line);
		iss >> inputData.orderArr[i];
	}
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.numOfOrder, inputData.orderArr);
	return 0;
}