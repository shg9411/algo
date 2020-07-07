#include <bits/stdc++.h>
using namespace std;

int main(void) {
    cin.tie(0); ios_base::sync_with_stdio(0);
    int n;
    vector<int> v{ 0,1 };
    cin >> n;
    for (int i = 2; i < n + 1; i++) {
        v.push_back(i);
        swap(v[i], v[i - 1]);
        int j = i - 1;
        while (j != 1) {
            swap(v[j], v[j / 2]);
            j /= 2;
        }
    }
    vector<int>::iterator iter;
    for (iter = v.begin() + 1; iter != v.end(); iter++)
        cout << *iter << ' ';

    return 0;
}