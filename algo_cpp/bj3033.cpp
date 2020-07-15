#include<iostream>
#include<cstring>
#include<algorithm>
#define MAX 200003

using namespace std;

char s[MAX];
int lcp[MAX], arr[MAX], pos[MAX], d, sl;

bool cmp(int i, int j) {
	if (pos[i] != pos[j])
		return pos[i] < pos[j];
	i += d;
	j += d;
	return (i < sl&& j < sl) ? (pos[i] < pos[j]) : (i > j);
}

void la() {
	for (int i = 0, k = 0; i < sl; i++, k = max(k - 1, 0)) {
		if (pos[i] == sl - 1)
			continue;
		for (int j = arr[pos[i] + 1]; s[i + k] == s[j + k]; k++);
		lcp[pos[i]] = k;
	}
}

void sa() {
	for (int i = 0; i < sl; i++) {
		arr[i] = i;
		pos[i] = s[i];
	}
	for (d = 1; ; d *= 2) {
		sort(arr, arr + sl, cmp);
		int tmp[MAX] = { 0 };
		for (int i = 0; i < sl - 1; i++)
			tmp[i + 1] = tmp[i] + cmp(arr[i], arr[i + 1]);
		for (int i = 0; i < sl; i++)
			pos[arr[i]] = tmp[i];
		if (tmp[sl - 1] == sl - 1)
			break;
	}
}

int main(void)
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >>  sl >> s;
	sa();
	la();
	int res = 0;
	for (int i = 0; i < sl - 1; i++) {
		res = res < lcp[i] ? lcp[i] : res;
	}
	cout<< res;
	return 0;
}