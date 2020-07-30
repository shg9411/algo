#include<cstdio>
#include<cstring>
#include<algorithm>
#define MAX 100001

using namespace std;

char s[MAX];
int arr[MAX], pos[MAX], d, sl;

bool cmp(int i, int j) {
	if (pos[i] != pos[j])
		return pos[i] < pos[j];
	i += d;
	j += d;
	return (i < sl&& j < sl) ? (pos[i] < pos[j]) : (i > j);
}

void sa() {
	sl = strlen(s);
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
	scanf("%s", s);
	sa();
	for (int i = 0; i < sl; i++)
		printf("%d\n", arr[i]);
	return 0;
}