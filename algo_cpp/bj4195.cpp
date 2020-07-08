#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

int parents[200000];
int s[200000];

int find(int i) {
	if (parents[i] == i)
		return i;
	return parents[i] = find(parents[i]);
}

int uni(int i, int j) {
	i = find(i);
	j = find(j);
	if (i != j) {
		parents[i] = j;
		s[j] += s[i];
		s[i] = 1;
	}
	return s[j];
}

int main(void) {
	cin.tie(0); ios_base::sync_with_stdio(0);
	int tc;
	cin >> tc;
	while (tc--) {
		int n;
		cin >> n;
		string a, b;
		unordered_map<string, int> um;
		int idx = 1;
		while (n--) {
			cin >> a >> b;
			int i, j;
			i = um[a];
			if(i==0){
				i = idx;
				parents[i] = idx;
				s[i] = 1;
				um[a] = idx++;
			}
			j = um[b];
			if(j==0){
				j = idx;
				parents[j] = idx;
				s[j] = 1;
				um[b] = idx++;
			}
			cout << uni(i, j) << '\n';
		}
		fill(parents, parents+idx, 0);
		fill(s, s+idx, 0);
	}
	return 0;
}