#include <vector>
#include <algorithm>
int kth(std::vector<int> &a, int k) {
	nth_element(a.begin(),a.begin()+k-1,a.end());
    return a[k-1];
}
