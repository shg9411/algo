#include <cstdio>
#include <cstring>
#include <string>
#include<algorithm>
#define MAX 200005

using namespace std;

char a[MAX], s[MAX * 2], tmp[MAX];
int lcp[MAX], arr[MAX], pos[MAX], d, sl, t, tg[MAX], r[MAX];

bool cmp(int i, int j) {
	if (pos[i] == pos[j])
		return pos[i + t] < pos[j + t];
	return pos[i] < pos[j];
}

void la() {
	for (int i = 0; i < sl; i++)
		r[arr[i]] = i;
	int len = 0;
	for (int i = 0; i < sl; i++) {
		int k = r[i];
		if (k) {
			int j = arr[k - 1];
			while (s[j + len] == s[i + len])
				len++;
			lcp[k] = len;
			if (len)
				len--;
		}
	}

}

void sa() {
	t = 1;
	sl = strlen(s);
	for (int i = 0; i < sl; i++) {
		arr[i] = i;
		pos[i] = s[i] - 'a';
	}
	while (t <= sl) {
		pos[sl] = -1;
		sort(arr, arr + sl, cmp);
		tg[arr[0]] = 0;
		for (int i = 1; i < sl; i++) {
			if (cmp(arr[i - 1], arr[i]))
				tg[arr[i]] = tg[arr[i - 1]] + 1;
			else
				tg[arr[i]] = tg[arr[i - 1]];
		}
		for (int i = 0; i < sl; i++)
			pos[i] = tg[i];
		t <<= 1;
	}
}

int main(void)
{
	scanf("%s%s", s, a);
	int m = strlen(s);
	s[m] = '$';
	strcat(s, a);
	sa();
	la();
	int res = 0;
	for (int i = 1; i < sl; i++) {
		if ((arr[i - 1] > m && arr[i] < m || arr[i - 1]<m && arr[i]>m)) {
			if (res < lcp[i]) {
				res = lcp[i];
				for (int j = 0; j < res; j++)
					tmp[j] = s[j + arr[i]];
			}
		}
	}
	printf("%d\n", res);
	for (int i = 0; i < res; i++)
		printf("%c", tmp[i]);
	return 0;
}