#include <cstdio>
#include <vector>
using namespace std;


int main(void) {
	int n,arr[10];
	vector<int> res;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	for (int i = n - 1; i >= 0; i--)
		res.insert(res.begin()+arr[i], i + 1);
	for (int i : res)
		printf("%d ", i);
	return 0;
}