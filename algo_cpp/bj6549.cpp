#include <vector>
#include <iostream>
using namespace std;

int main(void) {
    cin.tie(0); ios_base::sync_with_stdio(0);
    int n;
    while (true) {
        cin >> n;
        if (!n)
            break;
        long long res = 0;
        int tmp;
        vector<int> v = { 0 };
        vector<int> stack = { 0 };
        //v.push_back(0);
        //stack.push_back(0);
        for (int i = 0; i < n; i++) {
            cin >> tmp;
            v.push_back(tmp);
        }
        v.push_back(0);
        int sz = v.size();
        for (int i = 1; i < sz; i++) {
            while (!stack.empty() && v[stack.back()] > v[i]) {
                long long height = stack.back(); stack.pop_back();
                long long x = i - 1 - stack.back();
                res = res > x * v[height] ? res : x * v[height];
            }
            stack.push_back(i);
        }
        cout << res << "\n";
    }
    return 0;
}